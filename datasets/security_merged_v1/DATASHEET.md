# security_merged_v1 数据说明书

| 项 | 内容 |
|---|---|
| 数据集名称 | `security_merged_v1` |
| 版本日期 | 2026-08-05（同日修订：丢弃无 SKILL.md 条目） |
| 用途 | Agent Skill 安全检测的首轮整合集（银标 + 基准正样本）；**人工金标待重标** |
| 主表 | `manifest.jsonl` / `manifest.csv` |
| 工作区 | `E:\security-detection\datasets\security_merged_v1` |

---

## 1. 标签定义

### 1.1 `detection_label`（当前主标签）

本字段表示**当前采用的安全检测标签**（银标或基准标注），用于训练/评测划分前的统一入口。

| 取值 | 含义 | 是否视为“恶意正样本” |
|---|---|---|
| `malicious` | 具有明确恶意意图或已验证的恶意行为（投毒、隐蔽窃密、勿告知用户、恶意驻留等） | 是 |
| `benign` | 非恶意；功能正当且整体风险不高（含原 flash `false_positive` 映射） | 否（负样本） |
| `benign_but_dangerous` | 功能正当，但权限高、可被滥用（shell、云凭证、部署、爬虫、定时任务等） | 否（难负样本 / 灰区） |
| `uncertain` | 证据不足，暂不裁决 | 排除或单独报告 |

**二元检测实验时的建议映射（可改，需在论文中写明）：**

- 正类：`malicious`
- 负类：`benign` +（可选）`benign_but_dangerous`
- 默认先**排除** `uncertain`

### 1.2 与历史标签的关系

| 历史来源 | 如何进入本数据集 |
|---|---|
| ClawGuard `benign` | 抽样进入，`detection_label=benign` |
| llm-deep 曾标 `malicious` 的 672 条 | 经 `deepseek-v4-flash` 复审后写入；其中 flash `false_positive` **映射为** `benign` |
| MalSkillBench malware | 直接作为 `malicious`（基准标签） |

flash 原始四分类与本表映射：

| flash_raw_verdict | detection_label |
|---|---|
| `false_positive` | `benign` |
| `benign_but_dangerous` | `benign_but_dangerous` |
| `malicious` | `malicious` |
| `uncertain` | `uncertain` |

### 1.3 金标与功能标签

| 字段 | 当前状态 | 说明 |
|---|---|---|
| 安全金标 | **已回写 352 条** | 来源 `datasets/gold_security_v1/to_annotate.csv`；主表字段见下 |
| `gold_status` | `human_gold_v1` / `pending_reannotation` / `benchmark_label` | 仅抽样子集为人工金标 |
| `function_status` | `human_gold_v1` / `pending` | 与安全金标同步回写的 352 条有功能八类 |

回写字段（不覆盖 `detection_label`）：`gold_security_label`、`function_label`、`gold_confidence`、`gold_reviewer`、`gold_review_notes`、`gold_sample_id`。
底稿：`datasets/gold_security_v1/to_annotate.csv`；评测筛 `gold_status=human_gold_v1`。

---

## 2. 数据来源

### 2.1 来源概览

| `source` | 数量 | 内容 |
|---|---|---|
| `clawhub` | 5152 | 自建 ClawHub 镜像技能（`E:\clawhub_datasets\<slug>`） |
| `malskillbench` | 3368 | [MalSkillBench](https://github.com/lxyeternal/MalSkillBench) 恶意技能（论文 arXiv:2606.07131）；已剔除无 `SKILL.md` 条目 |

### 2.2 批次（`cohort`）

| `cohort` | 数量 | 说明 |
|---|---|---|
| `llm-deep-malicious-672` | 672 | 原本地 llm-deep 判 malicious → flash 复审（FP→benign） |
| `clawguard-benign-sample` | 4480 | ClawGuard=benign 中确定性抽样，用于把 benign 扩充到 5000 |
| `malware` | 3368 | MalSkillBench `Dataset/Skills/malware`（可读 SKILL.md） |

benign 构成：

- 来自 672 复审且映射为 benign：520  
- 来自 ClawGuard 抽样：4480  
- **合计 benign = 5000**

### 2.3 检测/标注模型信息

| 子集 | `detection_model` | 含义 |
|---|---|---|
| flash 复审 672 | `deepseek-v4-flash` | API 复审银标 |
| ClawGuard 抽样 | `clawguard` | 静态扫描器标签 |
| MalSkillBench | `malskillbench_ground_truth` | 论文基准（生成验证 / wild 核实等） |

---

## 3. 数量统计

**主表总行数：8520**（每条均存在可读 `SKILL.md`）

### 3.1 按 `detection_label`

| 标签 | 数量 | 占比 |
|---|---|---|
| benign | 5000 | 58.7% |
| malicious | 3368 | 39.5% |
| benign_but_dangerous | 150 | 1.8% |
| uncertain | 2 | &lt;0.1% |

### 3.2 按 `source` / `cohort`

见第 2 节。

### 3.3 文件可读性

| 项 | 数量 |
|---|---|
| 主表行且 `SKILL.md` 存在 | **8520 / 8520** |
| 已丢弃（无 `SKILL.md`） | 551（历史清理，未再保留丢弃清单） |

---

## 4. 字段说明（manifest）

| 字段 | 说明 |
|---|---|
| `id` | 全局唯一 ID，形如 `clawhub:<slug>` / `malskillbench:<slug>` |
| `slug` | 技能目录名 |
| `source` | `clawhub` / `malskillbench` |
| `cohort` | 进入数据集的批次（见上） |
| `detection_label` | 当前安全标签 |
| `flash_raw_verdict` | flash 原始标签（仅 672 复审子集有） |
| `detection_model` | 标签来源模型/工具 |
| `detection_reason` | 简短理由 |
| `local_path` | 本地技能根目录（默认**引用**原路径，不复制） |
| `gold_status` | 金标状态（`human_gold_v1` / `pending_reannotation` / `benchmark_label`） |
| `function_status` | 功能标注状态（`human_gold_v1` / `pending`） |
| `gold_security_label` | 人工安全金标（仅 `human_gold_v1` 有值） |
| `function_label` | 功能八类金标（仅 `human_gold_v1` 有值） |
| `gold_confidence` / `gold_reviewer` / `gold_review_notes` / `gold_sample_id` | 金标元数据 |
| `attack_vector` / `behavior` / `insertion_strategy` | MalSkillBench 分类预留 |

---

## 5. 已知缺陷与偏差

1. **不是最终金标**  
   ClawHub 部分为 flash/ClawGuard 银标；旧人工 30 条已降级为历史对照，需重标。

2. **flash 偏宽松**  
   在 30 条人工对照上约 60% 一致；常见错误是把 BBD 判成 FP/benign。全量 672 复审后 **0** 条维持 malicious，可能低估真恶意。

3. **ClawGuard benign 抽样未经人工复核**  
   4480 条仅保证静态扫描为 benign，可能含漏网恶意或高权限技能。

4. **MalSkillBench 不完整**  
   - 论文宣称恶意 **3944**；解压后曾写入 **3919**，因超长路径等导致 **551** 条无 `SKILL.md`，已从主表**丢弃**  
   - 当前主表恶意正样本 **3368**（均有 `SKILL.md`）  
   - 三维分类字段大多为空，需后续从原仓库 sidecar/元数据补齐  

5. **分布偏差**  
   - 正样本几乎全部来自 MalSkillBench（合成+wild），与真实 ClawHub 市场分布不同  
   - MalSkillBench wild 子集论文指出高度集中于特定盗币活动  
   - 负样本含大量“曾被过检”的难例（672 复审）与“易例”（ClawGuard benign）混合  

6. **路径依赖**  
   ClawHub 条目依赖 `E:\clawhub_datasets`；MalSkillBench 依赖 `E:\security-detection\external\MalSkillBench-main\...`。移动磁盘后需改 `local_path`。

7. **功能标签覆盖不全**  
   仅抽样 352 条有 Coding/Research/… 八类功能金标；其余 `function_status=pending`。

---

## 6. 推荐使用方式

1. **做召回/检测主实验**：正样本用 MalSkillBench 中 `SKILL.md` 可读子集；负样本用 `benign`（可再分层：易例 vs 672 难例）。  
2. **做人机金标**：底稿见 `gold_security_v1/to_annotate.csv`；已回写 352 条到主表（`gold_status=human_gold_v1`），**勿用金标覆盖** `detection_label`。评测时可筛 `gold_status=human_gold_v1`。  
3. **报告指标时声明**：银标评测 vs 金标评测；是否包含 BBD；MalSkillBench 可用条数。  
4. **引用**：使用 MalSkillBench 须引用原论文与仓库许可。

---

## 7. 变更记录

| 日期 | 变更 |
|---|---|
| 2026-08-05 | 初版：合并 flash 检测通 + ClawHub benign→5000 + MalSkillBench malware；编写本说明书 |
| 2026-08-05 | 尝试从 zip 补全缺失 SKILL.md 失败；丢弃 551 条；主表降至 8520（malicious 3368） |
| 2026-08-06 | 回写 `gold_security_v1` 人工金标 352 条（`gold_status=human_gold_v1`），不覆盖 detection_label |
| 2026-08-06 | 清理 `datasets/`：仅保留主表、金标底稿与说明文档 |
