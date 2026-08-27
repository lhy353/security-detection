"""Run: python -m web.backend"""

from __future__ import annotations

import argparse
import os
import socket

import uvicorn


def _lan_ip() -> str | None:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except OSError:
        return None


def main() -> None:
    parser = argparse.ArgumentParser(description="Skill dataset portal")
    parser.add_argument(
        "--host",
        default=os.environ.get("PORTAL_HOST", "0.0.0.0"),
        help="Bind address (0.0.0.0 = LAN + localhost)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.environ.get("PORTAL_PORT", "8000")),
        help="Listen port",
    )
    args = parser.parse_args()

    lan = _lan_ip()
    print(f"Local:   http://127.0.0.1:{args.port}")
    if lan and args.host in ("0.0.0.0", "::"):
        print(f"LAN:     http://{lan}:{args.port}")
    print("Press Ctrl+C to stop.")

    uvicorn.run(
        "web.backend.app:app",
        host=args.host,
        port=args.port,
        reload=False,
    )


if __name__ == "__main__":
    main()
