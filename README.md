# security-detection

Agent Skill 数据集仓库，当前门户默认数据集为 **关系型** `skills_relational_v1`（SkillDAG `skills_200`）。

另含安全检测合并集 `security_merged_v1`（8520 条，可选）。

## skills_relational_v1（关系型 · 门户默认）

| 文件 | 说明 |
|---|---|
| `datasets/skills_relational_v1/manifest.csv` | 200 条元数据 |
| `datasets/skills_relational_v1/skills/<slug>/` | `SKILL.md` + `meta.json` |
| `datasets/skills_relational_v1/skillgraph.json` | SkillDAG 关系图（`specializes`、`similar_to` 等边） |

来源：HuggingFace `Eric068/SkillDAG`（`skills_200` + `skillgraph_200.json`）。

构建本机数据集目录：

```bash
python scripts/build_skills_relational_v1.py
```

## security_merged_v1（安全检测合并集）

| `detection_label` | 数量 | 说明 |
|---|---|---|
| `benign` | 5000 | 非恶意负样本 |
| `benign_but_dangerous` | 150 | 功能正当但权限高 / 灰区 |
| `uncertain` | 2 | 证据不足 |
| `malicious` | 3368 | MalSkillBench 恶意样本 |

来源：`clawhub` 5152 条 + `malskillbench` 3368 条。

352 条已有人工金标（`gold_status=human_gold_v1`），字段见 `gold_security_label`、`function_label` 等列。

## CSV 主要字段

| 列 | 含义 |
|---|---|
| `id` | 唯一 ID（如 `clawhub:slug`、`malskillbench:...`） |
| `slug` | skill 短名 |
| `source` | 数据来源 |
| `cohort` | 子集 / 抽样批次 |
| `detection_label` | 安全检测四分类标签 |
| `gold_status` | 金标状态（`human_gold_v1` / `pending_reannotation` / `benchmark_label`） |
| `function_label` | 功能八类（Coding / Research / Browser / …） |
| `gold_security_label` | 人工安全金标（仅金标行有值） |
| `local_path` | 本机 `SKILL.md` 所在目录（clone 后需自行对齐路径） |
| `attack_vector` / `behavior` / `insertion_strategy` | MalSkillBench 恶意元数据 |

## 使用示例

```python
import pandas as pd

df = pd.read_csv("datasets/security_merged_v1/manifest.csv")
malicious = df[df["detection_label"] == "malicious"]
gold = df[df["gold_status"] == "human_gold_v1"]
```

## 同步到 GitHub

默认推送门户数据集 `skills_relational_v1`（可通过 `.env` 中 `PORTAL_DATASET` 切换）。

```bash
# .env：GITHUB_REPO、GITHUB_TOKEN、可选 GITHUB_PROXY
python scripts/sync_to_github.py
```

门户可选自动同步（`.env`）：

- `PORTAL_DATASET=skills_relational_v1`
- `GITHUB_AUTO_PULL=1`：启动后后台 `git pull`，浏览页每 20 秒检测更新并自动刷新
- `GITHUB_AUTO_PUSH=1`：本机上传后自动 commit + push

## 本地门户（可选）

本机可运行 Web 门户浏览 / 筛选 / 上传；默认读取 `datasets/skills_relational_v1/`。

```bash
pip install -r requirements-web.txt
cd web/frontend && npm install && npm run build && cd ../..
python -m web.backend   # http://127.0.0.1:8000
```

恶意样本仅供安全研究，请勿在生产环境执行。
