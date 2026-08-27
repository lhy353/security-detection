"""Load and query the security_merged_v1 skill catalog."""

from __future__ import annotations

import csv
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]


def _load_portal_env() -> None:
    import os

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


_load_portal_env()

import os  # noqa: E402

_DATASET_NAME = os.environ.get("PORTAL_DATASET", "skills_relational_v1")
DATASET_DIR = REPO_ROOT / "datasets" / _DATASET_NAME
SKILLS_DIR = DATASET_DIR / "skills"
SKILLGRAPH_JSON = DATASET_DIR / "skillgraph.json"
MANIFEST_JSONL = DATASET_DIR / "manifest.jsonl"
MANIFEST_CSV = DATASET_DIR / "manifest.csv"
SUMMARY_JSON = DATASET_DIR / "summary.json"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
CJK_RE = re.compile(r"[\u4e00-\u9fff]")
EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001F9FF"
    "\U00002600-\U000027BF"
    "\U0001FA00-\U0001FAFF"
    "]+",
    flags=re.UNICODE,
)


def safe_id(skill_id: str) -> str:
    return skill_id.replace(":", "__").replace("/", "_").replace("\\", "_")


def format_content_source(source: str) -> str:
    """Map legacy content locations to clawhub for display."""
    if source in ("local", "mirror"):
        return "clawhub"
    return source


def has_cjk(text: str) -> bool:
    return bool(CJK_RE.search(text or ""))


def strip_emoji(text: str) -> str:
    return EMOJI_RE.sub("", text or "").strip()


def humanize_slug(slug: str) -> str:
    s = (slug or "").replace("_", "-").replace(".", " ")
    parts = [p for p in re.split(r"[\s-]+", s) if p]
    return " ".join(parts[:8]).title() if parts else slug


def extract_english_title(
    *,
    heading: str = "",
    name: str = "",
    description: str = "",
    slug: str = "",
) -> str:
    """Best short English title from SKILL.md fields."""
    heading = strip_emoji((heading or "").strip().strip("#").strip())
    name = strip_emoji((name or "").strip().strip("\"'"))
    desc = " ".join((description or "").split())
    slug_l = (slug or "").lower()

    if desc:
        for stop in (
            ". Use when",
            ". Use for",
            ". Trigger",
            ". Use ",
            " — ",
            " - ",
        ):
            if stop in desc:
                desc = desc.split(stop, 1)[0].strip()
        desc = desc.strip(" .")

    candidates: list[str] = []
    if heading and len(heading) > 2 and heading.lower() not in (
        slug_l,
        slug_l.replace("-", " "),
    ):
        candidates.append(heading)
    if name and len(name) > 2:
        display_name = (
            humanize_slug(name) if re.match(r"^[a-z0-9._-]+$", name, re.I) else name
        )
        if display_name.lower() != slug_l or not candidates:
            candidates.append(display_name)
    if desc and len(desc) > 12:
        short = desc.split(",", 1)[0].strip()
        candidates.append(short[:90])
    if slug:
        candidates.append(humanize_slug(slug))

    for c in candidates:
        c = c.strip()
        if c and len(c) >= 2:
            return c[:100]
    return slug or name or "Untitled"


def compact_title(title: str, max_len: int = 48) -> str:
    """Trim to a short display title (sentence end + max length)."""
    t = (title or "").strip()
    if not t:
        return t
    for sep in ("。", "；", "!", "?"):
        if sep in t:
            part = t.split(sep, 1)[0].strip()
            if part:
                t = part
                break
    if len(t) > max_len:
        t = t[: max_len - 1].rstrip() + "…"
    return t


def _cjk_ratio(text: str) -> float:
    if not text:
        return 0.0
    return len(CJK_RE.findall(text)) / len(text)


def clean_display_title(title: str, slug: str = "", skill_id: str = "") -> str:
    """Remove slug / id noise; keep the human-readable title portion."""
    t = (title or "").strip()
    if not t:
        return t

    if skill_id and t.lower().startswith(skill_id.lower()):
        t = t[len(skill_id) :].lstrip(" :|-—")

    t = re.sub(r"^Skill[：:\s]+", "", t, flags=re.IGNORECASE).strip()
    t = re.sub(r"\s*[（(][a-z0-9._-]+[）)]\s*", " ", t, flags=re.IGNORECASE).strip()

    for sep in (" — ", " – ", " - ", " | "):
        if sep in t:
            parts = [p.strip() for p in t.split(sep) if p.strip()]
            if len(parts) >= 2:
                best = max(
                    parts,
                    key=lambda p: (_cjk_ratio(p), 1 if has_cjk(p) else 0, len(p)),
                )
                if has_cjk(best) or _cjk_ratio(best) > _cjk_ratio(parts[0]):
                    t = best
                    break

    if slug:
        sl = slug.lower().replace("_", "-")
        tl = t.lower()
        for prefix in (f"{sl} ", f"{sl}-", sl):
            if tl.startswith(prefix):
                rest = t[len(prefix) :].lstrip(" -—|：:")
                if rest.startswith("集成"):
                    rest = rest[2:].lstrip()
                if rest and (has_cjk(rest) or len(rest) > 2):
                    t = rest
                break

    if has_cjk(t):
        m = re.search(r"[\u4e00-\u9fff]", t)
        if m and m.start() > 0:
            prefix = t[: m.start()].strip(" -—|·")
            suffix = t[m.start() :].strip()
            if suffix and (not has_cjk(prefix) or _cjk_ratio(suffix) > _cjk_ratio(prefix)):
                t = suffix

    t = re.sub(r"\s+Skill\s*$", "", t, flags=re.IGNORECASE).strip()
    return t or (title or "").strip()


def format_skill_title(
    title: str, slug: str = "", skill_id: str = "", max_len: int = 48
) -> str:
    return compact_title(clean_display_title(title, slug, skill_id), max_len)


def translate_to_chinese(text: str, cache: dict[str, str] | None = None) -> str:
    """Translate English title to zh-CN; use cache dict if provided."""
    text = (text or "").strip()
    if not text or has_cjk(text):
        return text
    if cache is not None and text in cache:
        return cache[text]
    try:
        from deep_translator import GoogleTranslator

        zh = GoogleTranslator(source="auto", target="zh-CN").translate(text)
        zh = (zh or text).strip()
    except Exception:
        zh = text
    if cache is not None:
        cache[text] = zh
    return zh


def pick_chinese_title(
    *,
    heading: str = "",
    name: str = "",
    description: str = "",
    slug: str = "",
    translate: bool = True,
    cache: dict[str, str] | None = None,
) -> str:
    """Chinese display title: native Chinese first, else translate extracted English."""
    heading = (heading or "").strip().strip("#").strip()
    name = (name or "").strip().strip("\"'")
    description = (description or "").strip()

    if heading and has_cjk(heading):
        return heading
    if name and has_cjk(name):
        return name
    if description and has_cjk(description):
        for sep in ("。", "；", ";", ".", "\n"):
            if sep in description:
                part = description.split(sep, 1)[0].strip()
                if part and has_cjk(part):
                    return part[:40] + ("…" if len(part) > 40 else "")
        return description[:40] + ("…" if len(description) > 40 else "")

    english = extract_english_title(
        heading=heading, name=name, description=description, slug=slug
    )
    if translate and english and not has_cjk(english):
        return translate_to_chinese(english, cache=cache)
    return english


def parse_skill_md(text: str) -> dict[str, Any]:
    """Extract frontmatter, first H1, and Chinese display title from SKILL.md."""
    name = ""
    description = ""
    body = text
    m = FRONTMATTER_RE.match(text)
    if m:
        body = text[m.end() :]
        try:
            meta = yaml.safe_load(m.group(1)) or {}
            if isinstance(meta, dict):
                name = str(meta.get("name") or "")
                description = str(meta.get("description") or "")
        except yaml.YAMLError:
            pass
    heading = ""
    hm = H1_RE.search(body)
    if hm:
        heading = hm.group(1).strip()
    title = pick_chinese_title(
        heading=heading, name=name, description=description
    )
    return {
        "name": name,
        "description": description,
        "body": body,
        "heading": heading,
        "title": title,
    }


@dataclass
class SkillRecord:
    id: str
    slug: str
    source: str
    cohort: str
    detection_label: str
    attack_vector: str = ""
    behavior: str = ""
    insertion_strategy: str = ""
    gold_status: str = ""
    function_status: str = ""
    gold_security_label: str = ""
    function_label: str = ""
    gold_confidence: str = ""
    gold_reviewer: str = ""
    gold_review_notes: str = ""
    gold_sample_id: str = ""
    local_path: str = ""
    tags: list[str] = field(default_factory=list)
    # Cached from SKILL.md when available
    display_name: str = ""
    description: str = ""

    @property
    def is_malicious(self) -> bool:
        return self.detection_label == "malicious"

    def tag_list(self) -> list[str]:
        tags: list[str] = []
        for t in (
            self.source,
            self.cohort,
            self.detection_label,
            self.function_label,
            self.gold_status,
        ):
            if t and t not in tags:
                tags.append(t)
        for t in self.tags:
            if t and t not in tags:
                tags.append(t)
        return tags

    def gold_status_display(self) -> str:
        if self.gold_status in ("pending_reannotation", "benchmark_label"):
            return "未标注"
        if self.gold_status == "human_gold_v1":
            return "人工金标"
        return self.gold_status or ""

    def display_tags(self) -> list[str]:
        raw = self.tag_list()
        out: list[str] = []
        for t in raw:
            if t in ("pending_reannotation", "benchmark_label"):
                label = "未标注"
            elif t == "human_gold_v1":
                label = "人工金标"
            else:
                label = t
            if label not in out:
                out.append(label)
        return out

    def to_list_item(self) -> dict[str, Any]:
        function = self.function_label or (
            self.description.split(".")[0].strip() if self.description else ""
        )
        return {
            "id": self.id,
            "slug": self.slug,
            "name": format_skill_title(
                self.display_name or self.slug, self.slug, self.id
            ),
            "function": function,
            "detection_label": self.detection_label,
            "is_malicious": self.is_malicious,
            "source": self.source,
            "cohort": self.cohort,
            "function_label": self.function_label,
            "gold_status": self.gold_status,
            "gold_status_label": self.gold_status_display(),
            "tags": self.display_tags(),
        }

    def to_detail(
        self,
        skill_md: str | None,
        content_source: str,
        relational_edges: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        item = self.to_list_item()
        item.update(
            {
                "attack_vector": self.attack_vector,
                "behavior": self.behavior,
                "insertion_strategy": self.insertion_strategy,
                "function_status": self.function_status,
                "gold_security_label": self.gold_security_label,
                "gold_confidence": self.gold_confidence,
                "gold_reviewer": self.gold_reviewer,
                "gold_review_notes": self.gold_review_notes,
                "gold_sample_id": self.gold_sample_id,
                "local_path": self.local_path,
                "description": self.description,
                "skill_md": skill_md,
                "content_source": format_content_source(content_source),
                "relational_edges": relational_edges or [],
            }
        )
        return item


class Catalog:
    def __init__(self) -> None:
        self.skills: dict[str, SkillRecord] = {}
        self.order: list[str] = []
        self.summary: dict[str, Any] = {}
        self._meta_cache: dict[str, dict[str, str]] = {}
        self._graph_edges: list[dict[str, Any]] = []
        self._slug_to_id: dict[str, str] = {}
        self.reload()

    def _load_skill_graph(self) -> None:
        self._graph_edges = []
        self._slug_to_id = {rec.slug: rec.id for rec in self.skills.values()}
        if not SKILLGRAPH_JSON.exists():
            return
        try:
            data = json.loads(SKILLGRAPH_JSON.read_text(encoding="utf-8"))
            self._graph_edges = list(data.get("edges") or [])
        except (OSError, json.JSONDecodeError):
            self._graph_edges = []

    def reload(self) -> None:
        self.skills.clear()
        self.order.clear()
        self._meta_cache.clear()
        self.summary = {}
        if SUMMARY_JSON.exists():
            self.summary = json.loads(SUMMARY_JSON.read_text(encoding="utf-8"))
        path = MANIFEST_CSV if MANIFEST_CSV.exists() else MANIFEST_JSONL
        if not path.exists():
            return
        if path.suffix == ".jsonl":
            with path.open(encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    row = json.loads(line)
                    self._add_row(row)
        else:
            with path.open(encoding="utf-8-sig", newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self._add_row(row)
        self._load_skill_graph()

    def _add_row(self, row: dict[str, Any]) -> None:
        tags_raw = row.get("tags") or ""
        if isinstance(tags_raw, list):
            tags = [str(t) for t in tags_raw]
        elif isinstance(tags_raw, str) and tags_raw.strip():
            tags = [t.strip() for t in tags_raw.split("|") if t.strip()]
        else:
            tags = []
        rec = SkillRecord(
            id=str(row.get("id") or ""),
            slug=str(row.get("slug") or ""),
            source=str(row.get("source") or ""),
            cohort=str(row.get("cohort") or ""),
            detection_label=str(row.get("detection_label") or ""),
            attack_vector=str(row.get("attack_vector") or ""),
            behavior=str(row.get("behavior") or ""),
            insertion_strategy=str(row.get("insertion_strategy") or ""),
            gold_status=str(row.get("gold_status") or ""),
            function_status=str(row.get("function_status") or ""),
            gold_security_label=str(row.get("gold_security_label") or ""),
            function_label=str(row.get("function_label") or ""),
            gold_confidence=str(row.get("gold_confidence") or ""),
            gold_reviewer=str(row.get("gold_reviewer") or ""),
            gold_review_notes=str(row.get("gold_review_notes") or ""),
            gold_sample_id=str(row.get("gold_sample_id") or ""),
            local_path=str(row.get("local_path") or ""),
            tags=tags,
        )
        if not rec.id:
            return
        # Prefer mirror / uploads for display name without hitting all local paths at boot
        meta = self._peek_meta(rec)
        if meta:
            rec.display_name = format_skill_title(
                meta.get("title") or meta.get("name") or rec.slug,
                rec.slug,
                rec.id,
            )
            rec.description = meta.get("description") or ""
        else:
            rec.display_name = rec.slug
        self.skills[rec.id] = rec
        self.order.append(rec.id)

    def _skill_content_dirs(self, rec: SkillRecord) -> list[Path]:
        dirs: list[Path] = []
        if rec.slug:
            dirs.append(SKILLS_DIR / rec.slug)
        sid_dir = SKILLS_DIR / safe_id(rec.id)
        if sid_dir not in dirs:
            dirs.append(sid_dir)
        return dirs

    def _peek_meta(self, rec: SkillRecord) -> dict[str, str] | None:
        # Boot path: only portable dirs (avoid scanning thousands of local_path files).
        for subdir in self._skill_content_dirs(rec):
            meta_json = subdir / "meta.json"
            if not meta_json.exists():
                continue
            try:
                data = json.loads(meta_json.read_text(encoding="utf-8"))
                title = data.get("title") or pick_chinese_title(
                    name=str(data.get("name") or ""),
                    description=str(data.get("description") or ""),
                    slug=rec.slug,
                    translate=False,
                )
                return {
                    "name": str(data.get("name") or ""),
                    "description": str(data.get("description") or ""),
                    "title": title,
                }
            except (OSError, json.JSONDecodeError):
                continue
        for subdir in self._skill_content_dirs(rec):
            path = subdir / "SKILL.md"
            if path.exists():
                try:
                    text = path.read_text(encoding="utf-8", errors="replace")
                except OSError:
                    continue
                parsed = parse_skill_md(text)
                return {
                    "name": parsed["name"],
                    "description": parsed["description"],
                    "title": pick_chinese_title(
                        heading=parsed.get("heading", ""),
                        name=parsed["name"],
                        description=parsed["description"],
                        slug=rec.slug,
                    ),
                }
        return None

    def _resolve_local_dir(self, rec: SkillRecord) -> Path | None:
        if not rec.local_path:
            return None
        local = Path(rec.local_path)
        if not local.is_absolute():
            local = DATASET_DIR / local
        if (local / "SKILL.md").exists():
            return local
        return None

    def _candidate_skill_md_paths(self, rec: SkillRecord) -> list[Path]:
        paths = [d / "SKILL.md" for d in self._skill_content_dirs(rec)]
        local = self._resolve_local_dir(rec)
        if local:
            paths.append(local / "SKILL.md")
        return paths

    def resolve_content_dir(self, rec: SkillRecord) -> tuple[Path | None, str]:
        """Return (directory containing SKILL.md, source label)."""
        for subdir in self._skill_content_dirs(rec):
            if (subdir / "SKILL.md").exists():
                return subdir, "dataset"
        local = self._resolve_local_dir(rec)
        if local:
            return local, "local"
        return None, "none"

    def read_skill_md(self, rec: SkillRecord) -> tuple[str | None, str]:
        directory, source = self.resolve_content_dir(rec)
        if directory is None:
            return None, source
        path = directory / "SKILL.md"
        try:
            return path.read_text(encoding="utf-8", errors="replace"), source
        except OSError:
            return None, source

    def enrich_from_skill_md(self, rec: SkillRecord) -> None:
        for subdir in self._skill_content_dirs(rec):
            meta_path = subdir / "meta.json"
            if not meta_path.exists():
                continue
            try:
                data = json.loads(meta_path.read_text(encoding="utf-8"))
                title = str(data.get("title") or data.get("name") or "")
                if title:
                    rec.display_name = format_skill_title(title, rec.slug, rec.id)
                    if data.get("description"):
                        rec.description = str(data["description"])
                    return
            except (OSError, json.JSONDecodeError):
                continue
        text, _ = self.read_skill_md(rec)
        if not text:
            return
        parsed = parse_skill_md(text)
        title = pick_chinese_title(
            heading=parsed.get("heading", ""),
            name=parsed.get("name", ""),
            description=parsed.get("description", ""),
            slug=rec.slug,
            translate=False,
        )
        if title:
            rec.display_name = format_skill_title(title, rec.slug, rec.id)
        if parsed["description"]:
            rec.description = parsed["description"]

    def list_skills(
        self,
        q: str = "",
        label: str = "",
        source: str = "",
        function: str = "",
        gold_status: str = "",
        page: int = 1,
        page_size: int = 24,
    ) -> dict[str, Any]:
        q_lower = q.strip().lower()
        results: list[SkillRecord] = []
        for sid in self.order:
            rec = self.skills[sid]
            if label and rec.detection_label != label:
                continue
            if source and rec.source != source:
                continue
            if function and rec.function_label != function:
                continue
            if gold_status == "unlabeled":
                if rec.gold_status not in ("pending_reannotation", "benchmark_label"):
                    continue
            elif gold_status and rec.gold_status != gold_status:
                continue
            if q_lower:
                hay = " ".join(
                    [
                        rec.id,
                        rec.slug,
                        rec.display_name,
                        rec.description,
                        rec.function_label,
                        " ".join(rec.tags),
                    ]
                ).lower()
                if q_lower not in hay:
                    continue
            results.append(rec)

        total = len(results)
        page = max(1, page)
        page_size = min(max(1, page_size), 100)
        start = (page - 1) * page_size
        chunk = results[start : start + page_size]
        return {
            "total": total,
            "page": page,
            "page_size": page_size,
            "items": [r.to_list_item() for r in chunk],
        }

    def get(self, skill_id: str) -> SkillRecord | None:
        return self.skills.get(skill_id)

    def find_clawhub_by_slug(self, slug: str) -> SkillRecord | None:
        return self.skills.get(f"clawhub:{slug}")

    def _manifest_fieldnames(self) -> list[str]:
        default = [
            "id",
            "slug",
            "source",
            "cohort",
            "detection_label",
            "attack_vector",
            "behavior",
            "insertion_strategy",
            "gold_status",
            "function_status",
            "gold_security_label",
            "function_label",
            "gold_confidence",
            "gold_reviewer",
            "gold_review_notes",
            "gold_sample_id",
            "local_path",
            "tags",
        ]
        if not MANIFEST_CSV.exists() or MANIFEST_CSV.stat().st_size == 0:
            return default
        with MANIFEST_CSV.open("r", encoding="utf-8-sig", newline="") as f:
            reader = csv.reader(f)
            header = next(reader, None)
            return header if header else default

    def _row_for_csv(self, row: dict[str, Any], fieldnames: list[str]) -> dict[str, str]:
        out: dict[str, str] = {}
        for key in fieldnames:
            val = row.get(key, "")
            if key == "tags" and isinstance(val, list):
                out[key] = "|".join(val)
            else:
                out[key] = str(val) if val is not None else ""
        return out

    def _write_manifest_rows(self, fieldnames: list[str], rows: list[dict[str, Any]]) -> None:
        with MANIFEST_CSV.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            for row in rows:
                writer.writerow(self._row_for_csv(row, fieldnames))

    def _load_manifest_rows(self) -> tuple[list[str], list[dict[str, str]]]:
        fieldnames = self._manifest_fieldnames()
        if not MANIFEST_CSV.exists():
            return fieldnames, []
        rows: list[dict[str, str]] = []
        with MANIFEST_CSV.open("r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames:
                fieldnames = list(reader.fieldnames)
            for row in reader:
                rows.append(dict(row))
        return fieldnames, rows

    def upsert_manifest_row(self, row: dict[str, Any]) -> str:
        """Insert or update manifest.csv by id. Returns 'inserted' or 'updated'."""
        DATASET_DIR.mkdir(parents=True, exist_ok=True)
        skill_id = str(row.get("id") or "")
        if not skill_id:
            raise ValueError("row.id is required")

        fieldnames, rows = self._load_manifest_rows()
        updated = False
        new_rows: list[dict[str, Any]] = []
        for existing in rows:
            if existing.get("id") == skill_id:
                new_rows.append(row)
                updated = True
            else:
                new_rows.append(existing)
        if not updated:
            new_rows.append(row)

        self._write_manifest_rows(fieldnames, new_rows)
        self.reload()
        return "updated" if updated else "inserted"

    def relational_edges_for(self, skill_id: str) -> list[dict[str, Any]]:
        rec = self.skills.get(skill_id)
        if not rec or not self._graph_edges:
            return []
        slug = rec.slug
        out: list[dict[str, Any]] = []
        for e in self._graph_edges:
            etype = str(e.get("type") or "")
            src = str(e.get("source") or "")
            tgt = str(e.get("target") or "")
            if src == slug:
                other_slug = tgt
                direction = "outgoing"
            elif tgt == slug:
                other_slug = src
                direction = "incoming"
            else:
                continue
            other_id = self._slug_to_id.get(other_slug, f"skilldag:{other_slug}")
            other = self.skills.get(other_id)
            out.append(
                {
                    "type": etype,
                    "direction": direction,
                    "slug": other_slug,
                    "skill_id": other_id,
                    "name": other.display_name if other else other_slug,
                    "reason": str(e.get("reason") or ""),
                }
            )
        return out

    def related(self, skill_id: str, limit: int = 8) -> list[dict[str, Any]]:
        rec = self.skills.get(skill_id)
        if not rec:
            return []
        if self._graph_edges:
            seen: set[str] = set()
            items: list[dict[str, Any]] = []
            for edge in self.relational_edges_for(skill_id):
                oid = edge["skill_id"]
                if oid in seen or oid == skill_id:
                    continue
                seen.add(oid)
                other = self.skills.get(oid)
                if other:
                    item = other.to_list_item()
                    item["relation_type"] = edge["type"]
                    item["relation_direction"] = edge["direction"]
                    items.append(item)
                if len(items) >= limit:
                    break
            if items:
                return items
        scored: list[tuple[int, SkillRecord]] = []
        for sid in self.order:
            if sid == skill_id:
                continue
            other = self.skills[sid]
            score = 0
            if rec.function_label and other.function_label == rec.function_label:
                score += 3
            if other.detection_label == rec.detection_label:
                score += 2
            if other.source == rec.source:
                score += 1
            if rec.cohort and other.cohort == rec.cohort:
                score += 1
            if score > 0:
                scored.append((score, other))
        scored.sort(key=lambda x: (-x[0], x[1].slug))
        return [r.to_list_item() for _, r in scored[:limit]]

    def stats(self) -> dict[str, Any]:
        counts: dict[str, int] = {}
        by_source: dict[str, int] = {}
        for sid in self.order:
            rec = self.skills[sid]
            counts[rec.detection_label] = counts.get(rec.detection_label, 0) + 1
            by_source[rec.source] = by_source.get(rec.source, 0) + 1
        return {
            "n": len(self.order),
            "detection_label_counts": counts,
            "by_source": by_source,
            "summary": self.summary,
        }

    def append_manifest_row(self, row: dict[str, Any]) -> None:
        """Append or update manifest.csv."""
        self.upsert_manifest_row(row)


_catalog: Catalog | None = None


def get_catalog() -> Catalog:
    global _catalog
    if _catalog is None:
        _catalog = Catalog()
    return _catalog
