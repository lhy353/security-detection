# security-detection

Agent Skill **安全检测合并数据集** `security_merged_v1`。

GitHub 仓库发布 **CSV 元数据 + `skills/` 正文**（`SKILL.md` + `meta.json`）。

| 文件 | 说明 |
|---|---|
| `datasets/security_merged_v1/manifest.csv` | 主表（8520 条） |
| `datasets/security_merged_v1/skills/<id>/` | 每条 skill 的 `SKILL.md` 与 `meta.json` |

## 规模与标签

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

仓库推送 `manifest.csv` 与 `skills/` 目录。

```bash
# .env 中配置 GITHUB_REPO、GITHUB_TOKEN
python scripts/sync_to_github.py
```

## 本地门户（可选）

本机可运行 Web 门户浏览 / 筛选 / 上传；上传会追加到 `manifest.csv`，正文写入 `datasets/security_merged_v1/skills/`。

```bash
pip install -r requirements-web.txt
cd web/frontend && npm install && npm run build && cd ../..
python -m web.backend   # http://127.0.0.1:8000
```

恶意样本仅供安全研究，请勿在生产环境执行。
