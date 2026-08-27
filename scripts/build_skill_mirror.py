#!/usr/bin/env python3
"""Export SKILL.md files into datasets/security_merged_v1/skills/."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from web.backend.catalog import (  # noqa: E402
    DATASET_DIR,
    MANIFEST_CSV,
    SKILLS_DIR,
    Catalog,
    extract_english_title,
    parse_skill_md,
    pick_chinese_title,
    safe_id,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Export SKILL.md into dataset skills/")
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Max skills to export (0 = all)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing mirror entries",
    )
    args = parser.parse_args()

    if not MANIFEST_CSV.exists():
        print(f"Missing {MANIFEST_CSV}", file=sys.stderr)
        return 1

    cat = Catalog()
    SKILLS_DIR.mkdir(parents=True, exist_ok=True)
    cache_path = DATASET_DIR / "title_translation_cache.json"
    cache: dict[str, str] = {}
    if cache_path.exists():
        try:
            cache = json.loads(cache_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            cache = {}
    index: dict[str, str] = {}
    ok = 0
    missing = 0
    skipped = 0

    ids = cat.order if not args.limit else cat.order[: args.limit]
    for skill_id in ids:
        rec = cat.skills[skill_id]
        sid = safe_id(skill_id)
        dest_dir = SKILLS_DIR / sid
        dest_md = dest_dir / "SKILL.md"

        if dest_md.exists() and not args.force:
            index[skill_id] = f"{sid}/SKILL.md"
            skipped += 1
            continue

        src = Path(rec.local_path) / "SKILL.md" if rec.local_path else None
        if src is None or not src.exists():
            missing += 1
            continue

        try:
            text = src.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            print(f"read fail {skill_id}: {e}", file=sys.stderr)
            missing += 1
            continue

        dest_dir.mkdir(parents=True, exist_ok=True)
        dest_md.write_text(text, encoding="utf-8")
        parsed = parse_skill_md(text)
        title = pick_chinese_title(
            heading=parsed.get("heading", ""),
            name=parsed.get("name") or "",
            description=parsed.get("description") or "",
            slug=rec.slug,
            translate=True,
            cache=cache,
        )
        meta = {
            "id": skill_id,
            "slug": rec.slug,
            "name": parsed.get("name") or rec.slug,
            "title_en": extract_english_title(
                heading=parsed.get("heading", ""),
                name=parsed.get("name") or "",
                description=parsed.get("description") or "",
                slug=rec.slug,
            ),
            "title": title,
            "description": parsed.get("description") or "",
            "detection_label": rec.detection_label,
            "source": rec.source,
        }
        (dest_dir / "meta.json").write_text(
            json.dumps(meta, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        index[skill_id] = f"{sid}/SKILL.md"
        ok += 1
        if ok % 500 == 0:
            print(f"exported {ok}...")
            cache_path.write_text(
                json.dumps(cache, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )

    cache_path.write_text(
        json.dumps(cache, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (DATASET_DIR / "skills_index.json").write_text(
        json.dumps(
            {
                "n": len(index),
                "exported": ok,
                "skipped_existing": skipped,
                "missing": missing,
                "paths": index,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(
        f"Done. exported={ok} skipped_existing={skipped} missing={missing} "
        f"index={len(index)} -> {SKILLS_DIR}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
