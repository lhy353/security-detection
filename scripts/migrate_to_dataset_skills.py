#!/usr/bin/env python3
"""Merge legacy skill_mirror + uploads into datasets/security_merged_v1/skills/."""

from __future__ import annotations

import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "datasets" / "security_merged_v1" / "skills"
LEGACY_MIRROR = REPO_ROOT / "datasets" / "skill_mirror"
LEGACY_UPLOADS = REPO_ROOT / "datasets" / "uploads"


def copy_tree(src: Path, dst: Path) -> None:
    if not src.is_dir():
        return
    dst.mkdir(parents=True, exist_ok=True)
    for item in src.iterdir():
        target = dst / item.name
        if item.is_dir():
            if target.exists():
                copy_tree(item, target)
            else:
                shutil.copytree(item, target)
        else:
            shutil.copy2(item, target)


def main() -> int:
    SKILLS_DIR.mkdir(parents=True, exist_ok=True)
    n_mirror = 0
    n_upload = 0
    if LEGACY_MIRROR.exists():
        for d in LEGACY_MIRROR.iterdir():
            if d.is_dir():
                copy_tree(d, SKILLS_DIR / d.name)
                n_mirror += 1
    if LEGACY_UPLOADS.exists():
        for d in LEGACY_UPLOADS.iterdir():
            if d.is_dir():
                copy_tree(d, SKILLS_DIR / d.name)
                n_upload += 1
    print(f"migrated mirror_dirs={n_mirror} upload_dirs={n_upload} -> {SKILLS_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
