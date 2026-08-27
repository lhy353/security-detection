"""Background git pull from GitHub; non-blocking portal startup sync."""

from __future__ import annotations

import os
import subprocess
import threading
import time
from pathlib import Path
from typing import Callable

_lock = threading.Lock()
_state: dict[str, object] = {
    "status": "idle",
    "message": "",
    "last_pull_at": None,
    "data_version": 0,
    "remote_updated": False,
}


def get_sync_status() -> dict[str, object]:
    with _lock:
        return dict(_state)


def _bump_version() -> int:
    with _lock:
        _state["data_version"] = int(_state["data_version"]) + 1
        return int(_state["data_version"])


def _set_state(**kwargs: object) -> None:
    with _lock:
        _state.update(kwargs)


def _git_base_cmd() -> list[str]:
    proxy = os.environ.get("GITHUB_PROXY", "").strip()
    cmd = ["git", "-c", "http.version=HTTP/1.1", "-c", "http.postBuffer=524288000"]
    if proxy:
        cmd.extend(["-c", f"http.proxy={proxy}", "-c", f"https.proxy={proxy}"])
    return cmd


def _run_git(repo_root: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        _git_base_cmd() + args,
        cwd=repo_root,
        text=True,
        capture_output=True,
        check=False,
        env={**os.environ, "GIT_TERMINAL_PROMPT": "0"},
    )


def _remote_url() -> str | None:
    repo = os.environ.get("GITHUB_REPO", "").strip()
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if token and repo.startswith("https://github.com/"):
        return repo.replace(
            "https://github.com/",
            f"https://x-access-token:{token}@github.com/",
            1,
        )
    return repo or None


def _rev_parse(repo_root: Path, ref: str) -> str | None:
    r = _run_git(repo_root, ["rev-parse", ref])
    if r.returncode != 0:
        return None
    return r.stdout.strip()


def pull_from_github(repo_root: Path) -> bool:
    """Fetch and pull if origin/main is ahead. Returns True if local data changed."""
    if not (repo_root / ".git").exists():
        _set_state(status="skipped", message="not a git repository")
        return False

    remote_url = _remote_url()
    branch = os.environ.get("GITHUB_BRANCH", "main").strip() or "main"
    fetch_target = remote_url if remote_url else "origin"
    fetch_ref = f"{fetch_target}:{branch}" if remote_url else f"origin {branch}"

    fetch_args = ["fetch"]
    if remote_url:
        fetch_args.append(remote_url)
        fetch_args.append(branch)
    else:
        fetch_args.extend(["origin", branch])

    fetch = _run_git(repo_root, fetch_args)
    if fetch.returncode != 0:
        raise RuntimeError((fetch.stderr or fetch.stdout or "git fetch failed").strip())

    local = _rev_parse(repo_root, "HEAD")
    remote_ref = "FETCH_HEAD" if remote_url else f"origin/{branch}"
    remote = _rev_parse(repo_root, remote_ref)
    if not local or not remote:
        raise RuntimeError("unable to compare local and remote revisions")

    if local == remote:
        _set_state(status="ok", message="already up to date", remote_updated=False)
        return False

    pull_args = ["pull", "--ff-only"]
    if remote_url:
        pull_args.extend([remote_url, branch])
    else:
        pull_args.extend(["origin", branch])

    pull = _run_git(repo_root, pull_args)
    if pull.returncode != 0:
        raise RuntimeError((pull.stderr or pull.stdout or "git pull failed").strip())

    _set_state(
        status="ok",
        message="pulled remote updates",
        last_pull_at=time.time(),
        remote_updated=True,
    )
    return True


def start_background_pull(repo_root: Path, on_updated: Callable[[], None]) -> None:
    """Spawn daemon thread; does nothing when GITHUB_AUTO_PULL != 1."""

    def _worker() -> None:
        if os.environ.get("GITHUB_AUTO_PULL") != "1":
            _set_state(status="disabled", message="GITHUB_AUTO_PULL is not enabled")
            return
        _set_state(status="pulling", message="fetching from GitHub…")
        try:
            changed = pull_from_github(repo_root)
            if changed:
                on_updated()
                _bump_version()
            elif _state.get("status") == "pulling":
                _set_state(status="ok", message="already up to date")
        except Exception as e:
            _set_state(status="error", message=str(e))

    threading.Thread(target=_worker, daemon=True, name="github-auto-pull").start()


def notify_local_change() -> int:
    """Call after local upload / reload so clients can refresh."""
    return _bump_version()
