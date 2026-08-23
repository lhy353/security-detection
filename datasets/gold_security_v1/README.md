# gold_security_v1

安全金标抽样底稿（352 条）。人工标注结果已回写主表  
`datasets/security_merged_v1/manifest.*`（`gold_status=human_gold_v1`）。

## 本目录保留

| 文件 | 说明 |
|------|------|
| [`to_annotate.csv`](./to_annotate.csv) | 金标权威底稿（UTF-8 BOM） |
| [`guidelines.md`](./guidelines.md) | 安全 + 功能标注规范 |
| [`function_cheatsheet.md`](./function_cheatsheet.md) | 功能八类速查 |

主表与说明书见 `datasets/security_merged_v1/`（金标已回写，`gold_status=human_gold_v1`）。若再改 `to_annotate.csv`，需手工同步主表对应字段。

## 功能八类

`Coding` · `Research` · `Browser` · `File-Agent` · `Communication` · `Data-Agent` · `Automation` · `Other`  
（恶意样本按**伪装门面**功能标）

## 抽样设计（seed=20260805）

| bucket | 数量 | 说明 |
|--------|------|------|
| malicious | 100 | MalSkillBench |
| benign_hard | 50 | 原 672 flash 复审后的 benign（难负） |
| benign_easy | 50 | ClawGuard benign 抽样 |
| benign_but_dangerous | 150 | 全量 |
| uncertain | 2 | 全量 |
| **合计** | **352** | 已全部人工标注并回写主表 |
