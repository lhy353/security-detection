#!/usr/bin/env python3
"""Summarize SkillDAG ALFWorld graph: actions -> skills and prerequisite chains."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

GRAPH = Path(__file__).resolve().parents[1] / (
    "external/relational-skills/skilldag/data/skilldag_graphs/skillgraph_alfworld.json"
)

# ALFWorld / TextWorld admissible action families
ACTION_KEYWORDS = [
    "heat",
    "cool",
    "clean",
    "put",
    "take",
    "pick up",
    "open",
    "close",
    "go to",
    "look",
    "examine",
    "inventory",
    "toggle",
    "use",
]


def extract_actions(text: str) -> list[str]:
    t = text.lower()
    found: list[str] = []
    for a in ACTION_KEYWORDS:
        if a in t:
            found.append(a)
    return found


def short_id(sid: str) -> str:
    return sid.replace("alfworld-", "")


def main() -> int:
    g = json.loads(GRAPH.read_text(encoding="utf-8"))
    nodes: dict[str, dict] = g["nodes"]
    edges = g["edges"]

    depends: dict[str, set[str]] = defaultdict(set)
    for e in edges:
        if e["type"] == "depends_on":
            depends[e["source"]].add(e["target"])

    def all_prereqs(sid: str) -> set[str]:
        seen: set[str] = set()
        stack = list(depends.get(sid, []))
        while stack:
            p = stack.pop()
            if p in seen:
                continue
            seen.add(p)
            stack.extend(depends.get(p, []))
        return seen

    # Primary action = first keyword hit in description
    by_action: dict[str, list[str]] = defaultdict(list)
    skill_meta: dict[str, dict] = {}
    for sid, n in nodes.items():
        desc = f"{n.get('name', '')} {n.get('description', '')}"
        acts = extract_actions(desc)
        primary = acts[0] if acts else "general"
        by_action[primary].append(sid)
        skill_meta[sid] = {"actions": acts, "description": n.get("description", "")}

    print("SkillDAG ALFWorld: action -> skills (with prerequisite skills)")
    print("=" * 60)
    order = ["go to", "open", "close", "take", "pick up", "put", "heat", "cool", "clean", "look", "examine", "inventory", "toggle", "use", "general"]
    for act in order:
        if act not in by_action:
            continue
        print(f"\n## 动作/能力: {act}")
        for sid in sorted(by_action[act]):
            prereq = sorted(all_prereqs(sid), key=short_id)
            print(f"  - {short_id(sid)}")
            if prereq:
                print(f"      需要先具备 skill: {', '.join(short_id(p) for p in prereq)}")

    print("\n" + "=" * 60)
    print("典型任务链 (depends_on 直接依赖)")
    for sid in sorted(nodes.keys(), key=short_id):
        if depends[sid]:
            need = ", ".join(short_id(x) for x in sorted(depends[sid], key=short_id))
            print(f"  {short_id(sid)} 需要先: {need}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
