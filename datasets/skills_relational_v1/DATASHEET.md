# skills_relational_v1

SkillDAG **skills_200** 关系型 skill 数据集（200 节点，86 条关系边）。

| 文件 | 说明 |
|------|------|
| `manifest.csv` | 200 条元数据 |
| `skills/<slug>/` | `SKILL.md` + `meta.json` |
| `skillgraph.json` | 类型化边：`specializes`, `similar_to` 等 |

来源：HuggingFace `Eric068/SkillDAG`（`skillgraph_200.json` + `skills_200`）。
