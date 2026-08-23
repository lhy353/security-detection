"""Mirror a single skill into datasets/skill_mirror for GitHub-portable sync."""

from __future__ import annotations

import json
from pathlib import Path

from .catalog import (
    MIRROR_DIR,
    format_skill_title,
    parse_skill_md,
    pick_chinese_title,
    safe_id,
)


def mirror_skill_directory(
    skill_id: str,
    source_dir: Path,
    *,
    slug: str = "",
    detection_label: str = "",
    source: str = "upload",
    function_label: str = "",
) -> Path:
    """Copy SKILL.md (+ small sidecars) into skill_mirror and write meta.json."""
    sid = safe_id(skill_id)
    dest = MIRROR_DIR / sid
    dest.mkdir(parents=True, exist_ok=True)

    skill_md = source_dir / "SKILL.md"
    if not skill_md.exists():
        for p in source_dir.rglob("SKILL.md"):
            skill_md = p
            break
    if not skill_md.exists():
        raise FileNotFoundError(f"No SKILL.md in {source_dir}")

    text = skill_md.read_text(encoding="utf-8", errors="replace")
    (dest / "SKILL.md").write_text(text, encoding="utf-8")
    parsed = parse_skill_md(text)
    title = pick_chinese_title(
        heading=parsed.get("heading", ""),
        name=parsed.get("name", ""),
        description=parsed.get("description", ""),
        slug=slug,
        translate=True,
    )
    meta = {
        "id": skill_id,
        "slug": slug,
        "name": parsed.get("name") or slug,
        "title": format_skill_title(title, slug=slug, skill_id=skill_id, max_len=60),
        "description": parsed.get("description") or "",
        "detection_label": detection_label,
        "source": source,
        "function_label": function_label,
    }
    (dest / "meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return dest
