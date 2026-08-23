"""Skill dataset portal API."""

from __future__ import annotations

import io
import os
import re
import subprocess
import sys
import threading
import zipfile
from pathlib import Path
from urllib.parse import unquote

from fastapi import FastAPI, File, Form, HTTPException, Query, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse

from .catalog import (
    DATASET_DIR,
    REPO_ROOT,
    UPLOADS_DIR,
    get_catalog,
    safe_id,
)
from .mirror_skill import mirror_skill_directory

app = FastAPI(title="Skill Dataset Portal", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

SLUG_RE = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9._-]{0,120}$")
FUNCTION_LABELS = {
    "Coding",
    "Research",
    "Browser",
    "File-Agent",
    "Communication",
    "Data-Agent",
    "Automation",
    "Other",
}
DETECTION_LABELS = {
    "benign",
    "benign_but_dangerous",
    "uncertain",
    "malicious",
}


def _load_dotenv() -> None:
    env_path = REPO_ROOT / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key, val = key.strip(), val.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = val


def _auto_push_github(message: str) -> None:
    if os.environ.get("GITHUB_AUTO_PUSH") != "1":
        return
    if not os.environ.get("GITHUB_REPO") and not (REPO_ROOT / ".git").exists():
        return

    def _run() -> None:
        _load_dotenv()
        subprocess.run(
            [
                sys.executable,
                str(REPO_ROOT / "scripts" / "sync_to_github.py"),
                "--message",
                message,
            ],
            cwd=REPO_ROOT,
            capture_output=True,
        )

    threading.Thread(target=_run, daemon=True).start()


def _decode_id(skill_id: str) -> str:
    return unquote(skill_id)


@app.get("/api/stats")
def api_stats():
    return get_catalog().stats()


@app.get("/api/skills")
def api_list_skills(
    q: str = "",
    label: str = "",
    source: str = "",
    function: str = "",
    gold_status: str = "",
    page: int = Query(1, ge=1),
    page_size: int = Query(24, ge=1, le=100),
):
    return get_catalog().list_skills(
        q=q,
        label=label,
        source=source,
        function=function,
        gold_status=gold_status,
        page=page,
        page_size=page_size,
    )


@app.get("/api/dataset/download")
def api_download_dataset():
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for name in (
            "manifest.csv",
            "manifest.jsonl",
            "summary.json",
            "DATASHEET.md",
        ):
            path = DATASET_DIR / name
            if path.exists():
                zf.write(path, f"security_merged_v1/{name}")
        readme = REPO_ROOT / "README.md"
        if readme.exists():
            zf.write(readme, "README.md")
    buf.seek(0)
    return StreamingResponse(
        buf,
        media_type="application/zip",
        headers={
            "Content-Disposition": 'attachment; filename="security_merged_v1-metadata.zip"'
        },
    )


@app.post("/api/skills/upload")
async def api_upload(
    name: str = Form(...),
    slug: str | None = Form(None),
    function_label: str = Form("Other"),
    detection_label: str = Form("benign"),
    tags: str = Form(""),
    description: str = Form(""),
    skill_md: str | None = Form(None),
    file: UploadFile | None = File(None),
):
    cat = get_catalog()
    slug_val = (slug or name).strip().lower().replace(" ", "-")
    if not SLUG_RE.match(slug_val):
        raise HTTPException(400, "Invalid slug; use letters, digits, ._-")
    if detection_label not in DETECTION_LABELS:
        raise HTTPException(400, f"detection_label must be one of {sorted(DETECTION_LABELS)}")
    if function_label and function_label not in FUNCTION_LABELS:
        raise HTTPException(400, f"function_label must be one of {sorted(FUNCTION_LABELS)}")

    skill_id = f"upload:{slug_val}"
    if cat.get(skill_id):
        raise HTTPException(409, f"Skill already exists: {skill_id}")

    sid = safe_id(skill_id)
    dest = UPLOADS_DIR / sid
    dest.mkdir(parents=True, exist_ok=True)

    if file is not None and file.filename:
        raw = await file.read()
        if file.filename.lower().endswith(".zip"):
            with zipfile.ZipFile(io.BytesIO(raw)) as zf:
                for info in zf.infolist():
                    if info.is_dir():
                        continue
                    name_in_zip = Path(info.filename).name
                    if name_in_zip.startswith(".") or ".." in info.filename:
                        continue
                    target = dest / name_in_zip
                    with zf.open(info) as src, target.open("wb") as out:
                        out.write(src.read())
            if not (dest / "SKILL.md").exists():
                for p in dest.rglob("SKILL.md"):
                    text = p.read_text(encoding="utf-8", errors="replace")
                    (dest / "SKILL.md").write_text(text, encoding="utf-8")
                    break
        else:
            (dest / "SKILL.md").write_bytes(raw)
    elif skill_md:
        (dest / "SKILL.md").write_text(skill_md, encoding="utf-8")
    else:
        desc = description or f"{name} skill"
        generated = (
            f"---\nname: {name}\ndescription: {desc}\n---\n\n# {name}\n\n{desc}\n"
        )
        (dest / "SKILL.md").write_text(generated, encoding="utf-8")

    if not (dest / "SKILL.md").exists():
        raise HTTPException(400, "Upload must include SKILL.md (file, zip, or text)")

    tag_list = [t.strip() for t in tags.split(",") if t.strip()]
    row = {
        "id": skill_id,
        "slug": slug_val,
        "source": "upload",
        "cohort": "portal-upload",
        "detection_label": detection_label,
        "attack_vector": "",
        "behavior": "",
        "insertion_strategy": "",
        "gold_status": "pending_reannotation",
        "function_status": "human_gold_v1" if function_label else "pending",
        "gold_security_label": "",
        "function_label": function_label,
        "gold_confidence": "",
        "gold_reviewer": "",
        "gold_review_notes": "",
        "gold_sample_id": "",
        "local_path": str(dest.resolve()),
        "tags": tag_list,
    }
    cat.append_manifest_row(row)
    cat.enrich_from_skill_md(cat.skills[skill_id])
    try:
        mirror_skill_directory(
            skill_id,
            dest,
            slug=slug_val,
            detection_label=detection_label,
            source="upload",
            function_label=function_label,
        )
    except OSError as e:
        raise HTTPException(500, f"Saved skill but mirror failed: {e}")

    _auto_push_github(f"chore: add skill {skill_id}")

    return {"ok": True, "id": skill_id, "item": cat.skills[skill_id].to_list_item()}


@app.post("/api/reload")
def api_reload():
    get_catalog().reload()
    return {"ok": True, "n": len(get_catalog().order)}


# Sub-routes BEFORE the catch-all detail path
@app.get("/api/skill-download")
def api_download_skill(id: str = Query(...), full: bool = False):
    skill_id = _decode_id(id)
    cat = get_catalog()
    rec = cat.get(skill_id)
    if not rec:
        raise HTTPException(404, f"Skill not found: {skill_id}")

    buf = io.BytesIO()
    sid = safe_id(rec.id)

    if full and rec.local_path:
        root = Path(rec.local_path)
        if root.is_dir() and (root / "SKILL.md").exists():
            with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
                for path in root.rglob("*"):
                    if path.is_file():
                        try:
                            arc = path.relative_to(root).as_posix()
                            zf.write(path, f"{sid}/{arc}")
                        except OSError:
                            continue
            buf.seek(0)
            return StreamingResponse(
                buf,
                media_type="application/zip",
                headers={
                    "Content-Disposition": f'attachment; filename="{sid}-full.zip"',
                    "X-Research-Only": "true",
                },
            )

    directory, source = cat.resolve_content_dir(rec)
    if directory is None:
        raise HTTPException(
            404,
            "Skill content not available. Run scripts/build_skill_mirror.py "
            "or ensure local_path exists.",
        )

    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        skill_md = directory / "SKILL.md"
        if skill_md.exists():
            zf.write(skill_md, f"{sid}/SKILL.md")
        meta = directory / "meta.json"
        if meta.exists():
            zf.write(meta, f"{sid}/meta.json")
        if source in ("mirror", "upload"):
            for path in directory.iterdir():
                if path.is_file() and path.name not in ("SKILL.md", "meta.json"):
                    if path.stat().st_size <= 512_000:
                        zf.write(path, f"{sid}/{path.name}")

    buf.seek(0)
    return StreamingResponse(
        buf,
        media_type="application/zip",
        headers={
            "Content-Disposition": f'attachment; filename="{sid}.zip"',
            "X-Research-Only": "true",
        },
    )


@app.get("/api/skill-related")
def api_related(id: str = Query(...), limit: int = Query(8, ge=1, le=30)):
    skill_id = _decode_id(id)
    cat = get_catalog()
    if not cat.get(skill_id):
        raise HTTPException(404, f"Skill not found: {skill_id}")
    return {"items": cat.related(skill_id, limit=limit)}


@app.get("/api/skill")
def api_skill_detail(id: str = Query(...)):
    skill_id = _decode_id(id)
    cat = get_catalog()
    rec = cat.get(skill_id)
    if not rec:
        raise HTTPException(404, f"Skill not found: {skill_id}")
    cat.enrich_from_skill_md(rec)
    text, source = cat.read_skill_md(rec)
    return rec.to_detail(text, source)


STATIC_DIR = REPO_ROOT / "web" / "frontend" / "dist"


@app.api_route("/{full_path:path}", methods=["GET"])
def spa_fallback(full_path: str):
    """Serve built frontend; SPA routes fall back to index.html."""
    if full_path.startswith("api/") or full_path == "api":
        raise HTTPException(404, "API route not found")
    if not STATIC_DIR.exists():
        raise HTTPException(
            503,
            "Frontend not built. Run: cd web/frontend && npm install && npm run build",
        )
    candidate = (STATIC_DIR / full_path).resolve()
    if (
        full_path
        and candidate.is_file()
        and str(candidate).startswith(str(STATIC_DIR.resolve()))
    ):
        return FileResponse(candidate)
    index = STATIC_DIR / "index.html"
    if index.exists():
        return FileResponse(index)
    raise HTTPException(404, "index.html missing")


def create_app() -> FastAPI:
    return app
