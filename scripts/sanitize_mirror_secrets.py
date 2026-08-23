#!/usr/bin/env python3
"""Redact example secrets in skill_mirror SKILL.md for GitHub push protection."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MIRROR = REPO_ROOT / "datasets" / "skill_mirror"

REDACTIONS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"sk-[a-zA-Z0-9]{20,}"), "[REDACTED_API_KEY]"),
    (re.compile(r"https://hooks\.slack\.com/services/[A-Za-z0-9/_-]+"), "[REDACTED_SLACK_WEBHOOK]"),
    (
        re.compile(
            r"https://api\.telegram\.org/bot\d+:[A-Za-z0-9_-]+"
        ),
        "[REDACTED_TELEGRAM_BOT]",
    ),
    (
        re.compile(r"(?i)X-Tos-Credential=[^&\s\"]+"),
        "X-Tos-Credential=[REDACTED]",
    ),
    (
        re.compile(r"(?i)(app_secret|application_secret|lark_secret)\s*[:=]\s*['\"]?[A-Za-z0-9_-]{8,}"),
        "[REDACTED_APP_SECRET]",
    ),
    (
        re.compile(r"(?i)AKLT[A-Za-z0-9]{10,}"),
        "[REDACTED_VOLCENGINE_AK]",
    ),
    (
        re.compile(r"(?i)(api_key|apikey|secret_key)\s*[:=]\s*['\"]?[A-Za-z0-9_-]{16,}"),
        "[REDACTED_SECRET]",
    ),
    (re.compile(r"ghp_[A-Za-z0-9]{20,}"), "[REDACTED_GITHUB_TOKEN]"),
    (re.compile(r"github_pat_[A-Za-z0-9_]{20,}"), "[REDACTED_GITHUB_TOKEN]"),
]


def sanitize_text(text: str) -> str:
    for pattern, repl in REDACTIONS:
        text = pattern.sub(repl, text)
    return text


def main() -> int:
    changed = 0
    for path in MIRROR.rglob("SKILL.md"):
        try:
            raw = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        new = sanitize_text(raw)
        if new != raw:
            path.write_text(new, encoding="utf-8")
            changed += 1
    print(f"sanitized_files={changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
