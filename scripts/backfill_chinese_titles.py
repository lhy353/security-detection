#!/usr/bin/env python3
"""Backfill Chinese titles for dataset skills entries that lack CJK in title."""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from web.backend.catalog import (  # noqa: E402
    FRONTMATTER_RE,
    H1_RE,
    SKILLS_DIR,
    compact_title,
    extract_english_title,
    format_skill_title,
    has_cjk,
    translate_to_chinese,
)

CACHE_PATH = DATASET_DIR / "title_translation_cache.json"
FM_NAME_RE = re.compile(r"^name:\s*[\"']?(.+?)[\"']?\s*$", re.MULTILINE)
FM_DESC_RE = re.compile(r"^description:\s*(.+?)(?=^\w|\Z)", re.MULTILINE | re.DOTALL)


def load_cache() -> dict[str, str]:
    if CACHE_PATH.exists():
        try:
            return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            pass
    return {}


def save_cache(cache: dict[str, str]) -> None:
    CACHE_PATH.write_text(
        json.dumps(cache, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def fast_parse_skill_md(text: str) -> tuple[str, str, str]:
    """Lightweight parse for bulk backfill (no YAML loader)."""
    name = ""
    description = ""
    body = text
    m = FRONTMATTER_RE.match(text)
    if m:
        fm = m.group(1)
        body = text[m.end() :]
        nm = FM_NAME_RE.search(fm)
        if nm:
            name = nm.group(1).strip().strip("\"'")
        dm = FM_DESC_RE.search(fm)
        if dm:
            description = " ".join(dm.group(1).strip().split())[:500]
    heading = ""
    hm = H1_RE.search(body)
    if hm:
        heading = hm.group(1).strip()
    return heading, name, description


def main() -> int:
    parser = argparse.ArgumentParser(description="Backfill Chinese titles in dataset skills/")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--sleep", type=float, default=0.008)
    args = parser.parse_args()

    cache = load_cache()
    pending: list[tuple[Path, dict[str, str], str]] = []
    skipped = 0

    print("scanning meta.json...", flush=True)
    for meta_path in sorted(SKILLS_DIR.glob("*/meta.json")):
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        title = str(meta.get("title") or "")
        if has_cjk(title):
            skipped += 1
            continue

        english = str(meta.get("title_en") or "").strip()
        if not english:
            skill_md = meta_path.parent / "SKILL.md"
            if not skill_md.exists():
                continue
            slug = str(meta.get("slug") or meta_path.parent.name)
            heading, name, description = fast_parse_skill_md(
                skill_md.read_text(encoding="utf-8", errors="replace")
            )
            english = extract_english_title(
                heading=heading,
                name=name,
                description=description,
                slug=slug,
            )
        if english:
            pending.append((meta_path, meta, english))

    if args.limit:
        pending = pending[: args.limit]

    print(f"need_update={len(pending)} already_chinese={skipped}", flush=True)

    unique = sorted({e for _, _, e in pending if e and not has_cjk(e)})
    need_translate = [e for e in unique if not has_cjk(cache.get(e, ""))]
    print(f"unique_english={len(unique)} to_translate={len(need_translate)}", flush=True)

    for i, english in enumerate(need_translate, 1):
        cache[english] = translate_to_chinese(english, cache=cache)
        if i % 200 == 0:
            save_cache(cache)
            print(f"translate {i}/{len(need_translate)}", flush=True)
        if args.sleep:
            time.sleep(args.sleep)

    save_cache(cache)

    updated = 0
    for meta_path, meta, english in pending:
        zh = cache.get(english) or english
        if not has_cjk(zh):
            zh = translate_to_chinese(english, cache=cache)
        meta["title_en"] = english
        meta["title"] = format_skill_title(zh, slug=meta.get("slug", ""), skill_id=meta.get("id", ""), max_len=60)
        if not args.dry_run:
            meta_path.write_text(
                json.dumps(meta, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
        updated += 1

    save_cache(cache)
    print(f"done updated={updated} skipped={skipped} cache={len(cache)}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
