#!/usr/bin/env python3
"""Auto-label function_label (八类) for skills missing labels."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from web.backend.catalog import (  # noqa: E402
    MIRROR_DIR,
    REPO_ROOT as ROOT,
    parse_skill_md,
    safe_id,
)
from web.backend.function_classifier import FUNCTION_LABELS, classify_function  # noqa: E402

MANIFEST_JSONL = ROOT / "datasets" / "security_merged_v1" / "manifest.jsonl"
MANIFEST_CSV = ROOT / "datasets" / "security_merged_v1" / "manifest.csv"


def read_skill_text(rec: dict) -> str:
    sid = safe_id(rec["id"])
    mirror = MIRROR_DIR / sid / "SKILL.md"
    if mirror.exists():
        return mirror.read_text(encoding="utf-8", errors="replace")
    local = rec.get("local_path")
    if local:
        p = Path(local) / "SKILL.md"
        if p.exists():
            return p.read_text(encoding="utf-8", errors="replace")
    return ""


def skill_blob(rec: dict, text: str) -> str:
    parts = [rec.get("slug", ""), rec.get("description", "")]
    if text:
        parsed = parse_skill_md(text)
        parts.extend(
            [
                parsed.get("name", ""),
                parsed.get("description", ""),
                parsed.get("heading", ""),
                text[:4000],
            ]
        )
    meta = MIRROR_DIR / safe_id(rec["id"]) / "meta.json"
    if meta.exists():
        try:
            m = json.loads(meta.read_text(encoding="utf-8"))
            parts.extend([m.get("title", ""), m.get("description", "")])
        except (OSError, json.JSONDecodeError):
            pass
    return "\n".join(str(p) for p in parts if p)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--overwrite-gold", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    rows: list[dict] = []
    with MANIFEST_JSONL.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))

    counts = Counter()
    updated = 0
    skipped = 0

    for i, rec in enumerate(rows):
        if args.limit and updated >= args.limit:
            break
        existing = (rec.get("function_label") or "").strip()
        status = rec.get("function_status") or ""
        if existing and status == "human_gold_v1" and not args.overwrite_gold:
            skipped += 1
            counts[existing] += 1
            continue
        if existing and not args.overwrite_gold:
            skipped += 1
            counts[existing] += 1
            continue

        text = read_skill_text(rec)
        blob = skill_blob(rec, text)
        pred = classify_function(blob, rec.get("slug", ""))
        label = pred.label
        rec["function_label"] = label
        if status != "human_gold_v1":
            rec["function_status"] = "auto_labeled_v1"
        counts[label] += 1
        updated += 1

        meta_path = MIRROR_DIR / safe_id(rec["id"]) / "meta.json"
        if meta_path.exists() and not args.dry_run:
            try:
                meta = json.loads(meta_path.read_text(encoding="utf-8"))
                meta["function_label"] = label
                meta_path.write_text(
                    json.dumps(meta, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8",
                )
            except (OSError, json.JSONDecodeError):
                pass

        if updated % 1000 == 0:
            print(f"labeled {updated}...", flush=True)

    if args.dry_run:
        print("DRY RUN — manifest not written")
        print(dict(counts))
        return 0

    with MANIFEST_JSONL.open("w", encoding="utf-8") as f:
        for rec in rows:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    fieldnames = list(rows[0].keys()) if rows else []
    if MANIFEST_CSV.exists():
        with MANIFEST_CSV.open("r", encoding="utf-8-sig", newline="") as rf:
            reader = csv.reader(rf)
            existing_header = next(reader, None)
            if existing_header:
                fieldnames = existing_header

    with MANIFEST_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for rec in rows:
            writer.writerow({k: rec.get(k, "") for k in fieldnames})

    print(f"done updated={updated} skipped={skipped}")
    print("distribution", dict(counts))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
