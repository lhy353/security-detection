#!/usr/bin/env python3
"""Commit and push portal dataset(s) to GitHub."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATASETS = [
    "datasets/skills_relational_v1",
    "datasets/security_merged_v1",
]


def portal_dataset_roots() -> list[str]:
    raw = os.environ.get("PORTAL_DATASET", "all").strip()
    if raw.lower() in ("all", "*"):
        return [r for r in DEFAULT_DATASETS if (REPO_ROOT / r).is_dir()]
    if "," in raw:
        names = [p.strip() for p in raw.split(",") if p.strip()]
    else:
        names = [raw]
    roots: list[str] = []
    for name in names:
        roots.append(name if name.startswith("datasets/") else f"datasets/{name}")
    return roots


def run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    print("+", " ".join(cmd))
    return subprocess.run(
        cmd,
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=check,
    )


def ensure_git_repo() -> None:
    if not (REPO_ROOT / ".git").exists():
        run(["git", "init", "-b", "main"])
        print("Initialized git repository.")


def ensure_remote(repo_url: str) -> None:
    r = run(["git", "remote", "get-url", "origin"], check=False)
    if r.returncode != 0:
        run(["git", "remote", "add", "origin", repo_url])
        print(f"Added remote origin: {repo_url}")
    elif r.stdout.strip() != repo_url:
        print(f"Remote origin already set: {r.stdout.strip()}")


def git_push(repo_url: str | None, branch: str) -> None:
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    proxy = os.environ.get("GITHUB_PROXY", "").strip()
    push_url = repo_url
    if token and repo_url and repo_url.startswith("https://github.com/"):
        push_url = repo_url.replace(
            "https://github.com/",
            f"https://x-access-token:{token}@github.com/",
            1,
        )
    push_cmd = ["git", "-c", "http.version=HTTP/1.1", "-c", "http.postBuffer=524288000"]
    if proxy:
        push_cmd.extend(["-c", f"http.proxy={proxy}", "-c", f"https.proxy={proxy}"])
    push_cmd.extend(["push", "-u"])
    if push_url:
        push_cmd.append(push_url)
    else:
        push_cmd.append("origin")
    push_cmd.append(branch)
    run(push_cmd)


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync skill datasets to GitHub")
    parser.add_argument(
        "--repo",
        default=os.environ.get("GITHUB_REPO", ""),
        help="GitHub repo URL (https://github.com/user/repo.git)",
    )
    parser.add_argument("--branch", default="main")
    parser.add_argument("--message", default="chore: sync skill dataset")
    parser.add_argument("--no-push", action="store_true", help="Commit only, do not push")
    parser.add_argument(
        "--dataset",
        default="",
        help="Single dataset path under datasets/ (default: skills_relational_v1 + security_merged_v1 if present)",
    )
    args = parser.parse_args()

    env_path = REPO_ROOT / ".env"
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            key, val = key.strip(), val.strip().strip('"').strip("'")
            if key and key not in os.environ:
                os.environ[key] = val
    if not args.repo:
        args.repo = os.environ.get("GITHUB_REPO", "")

    ensure_git_repo()

    if args.dataset:
        roots = [args.dataset if args.dataset.startswith("datasets/") else f"datasets/{args.dataset}"]
    else:
        roots = portal_dataset_roots()

    existing_roots = [r for r in roots if (REPO_ROOT / r).is_dir()]
    if not existing_roots:
        print("No dataset directories found to sync.", file=sys.stderr)
        return 1

    for manifest in [f"{r}/manifest.csv" for r in existing_roots]:
        if not (REPO_ROOT / manifest).exists():
            print(f"Missing {manifest}", file=sys.stderr)
            return 1

    run(["git", "add", "-A", "--"] + existing_roots + ["web", "README.md"])

    status = run(["git", "status", "--porcelain"], check=False)
    staged = run(["git", "diff", "--cached", "--quiet"], check=False)
    has_staged = staged.returncode != 0
    unstaged_paths = [line for line in status.stdout.splitlines() if line.strip()]
    if unstaged_paths and not has_staged:
        has_staged = True

    if has_staged or any(line.startswith("A ") or line.startswith("M ") for line in unstaged_paths):
        author_name = os.environ.get("GIT_AUTHOR_NAME", "security-detection")
        author_email = os.environ.get("GIT_AUTHOR_EMAIL", "security-detection@local")
        commit_result = run(
            [
                "git",
                "-c",
                f"user.name={author_name}",
                "-c",
                f"user.email={author_email}",
                "commit",
                "-m",
                args.message,
            ],
            check=False,
        )
        if commit_result.returncode != 0 and "nothing to commit" not in (
            commit_result.stdout + commit_result.stderr
        ):
            raise subprocess.CalledProcessError(
                commit_result.returncode, commit_result.args,
                commit_result.stdout, commit_result.stderr,
            )
    elif unstaged_paths:
        print("No staged changes; pushing existing commits.")
    else:
        print("Nothing to commit.")

    if args.no_push:
        print("Committed locally (--no-push).")
        return 0

    repo_url = args.repo.strip()
    if repo_url:
        ensure_remote(repo_url)

    try:
        git_push(repo_url if repo_url else None, args.branch)
        print("Push succeeded.")
    except subprocess.CalledProcessError as e:
        print(e.stderr or e.stdout or str(e), file=sys.stderr)
        print(
            "\nPush failed. Set GITHUB_REPO and GITHUB_TOKEN (PAT), then retry.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
