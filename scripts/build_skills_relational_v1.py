#!/usr/bin/env python3
"""Build datasets/skills_relational_v1 from SkillDAG skills_200 + skillgraph_200."""

from __future__ import annotations

import csv
import json
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_SKILLS = REPO_ROOT / "external/relational-skills/skilldag/skills_200"
SRC_GRAPH = (
    REPO_ROOT
    / "external/relational-skills/skilldag/data/skilldag_graphs/skillgraph_200.json"
)
OUT_DIR = REPO_ROOT / "datasets" / "skills_relational_v1"
OUT_SKILLS = OUT_DIR / "skills"
OUT_GRAPH = OUT_DIR / "skillgraph.json"
OUT_MANIFEST = OUT_DIR / "manifest.csv"


def main() -> int:
    if not SRC_SKILLS.is_dir():
        print(f"Missing {SRC_SKILLS}. Run HF download first.", file=sys.stderr)
        return 1
    if not SRC_GRAPH.exists():
        print(f"Missing {SRC_GRAPH}", file=sys.stderr)
        return 1

    graph = json.loads(SRC_GRAPH.read_text(encoding="utf-8"))
    nodes: dict[str, dict] = graph["nodes"]
    edges = graph["edges"]

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_GRAPH.write_text(
        json.dumps(
            {
                "name": "skills_relational_v1",
                "source": "SkillDAG",
                "scale": "skills_200",
                "n_nodes": len(nodes),
                "n_edges": len(edges),
                "edge_types": sorted({e["type"] for e in edges}),
                "nodes": nodes,
                "edges": edges,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    if OUT_SKILLS.exists():
        shutil.rmtree(OUT_SKILLS)
    shutil.copytree(SRC_SKILLS, OUT_SKILLS)

    rows: list[dict[str, str]] = []
    for slug in sorted(nodes.keys()):
        node = nodes[slug]
        skill_dir = OUT_SKILLS / slug
        dest_rel = f"skills/{slug}"
        rows.append(
            {
                "id": f"skilldag:{slug}",
                "slug": slug,
                "source": "skilldag",
                "cohort": "skills_200",
                "detection_label": "benign",
                "attack_vector": "",
                "behavior": "",
                "insertion_strategy": "",
                "gold_status": "benchmark_label",
                "function_status": "auto_labeled_v1",
                "gold_security_label": "",
                "function_label": "Other",
                "gold_confidence": "",
                "gold_reviewer": "",
                "gold_review_notes": "",
                "gold_sample_id": "",
                "local_path": dest_rel,
                "tags": "relational|skilldag",
            }
        )
        meta = {
            "id": f"skilldag:{slug}",
            "slug": slug,
            "name": node.get("name") or slug,
            "title": node.get("name") or slug,
            "description": node.get("description") or "",
            "detection_label": "benign",
            "source": "skilldag",
            "function_label": "Other",
            "status": node.get("status") or "active",
            "tags": node.get("tags") or [],
        }
        (skill_dir / "meta.json").write_text(
            json.dumps(meta, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    fieldnames = list(rows[0].keys())
    with OUT_MANIFEST.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    (OUT_DIR / "DATASHEET.md").write_text(
        f"""# skills_relational_v1

SkillDAG **skills_200** 关系型 skill 数据集（200 节点，{len(edges)} 条关系边）。

| 文件 | 说明 |
|------|------|
| `manifest.csv` | 200 条元数据 |
| `skills/<slug>/` | `SKILL.md` + `meta.json` |
| `skillgraph.json` | 类型化边：`specializes`, `similar_to` 等 |

来源：HuggingFace `Eric068/SkillDAG`（`skillgraph_200.json` + `skills_200`）。
""",
        encoding="utf-8",
    )

    print(f"Built {OUT_DIR}: skills={len(rows)} edges={len(edges)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
