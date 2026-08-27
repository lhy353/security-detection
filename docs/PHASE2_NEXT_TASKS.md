# 下一阶段任务（Phase 2）

基于已完成的 `security_merged_v1/manifest.csv`（人工金标 352 + 功能八类）。

## 你已完成（Phase 1 验收）

- 总表 8520 条，均可读 `SKILL.md`
- 人工金标 `human_gold_v1`：**352**
  - malicious 99 · benign_but_dangerous 180 · benign 73
- 功能八类已填满这 352 条
- 银标 `detection_label` 保留未覆盖

---

## Phase 2 目标

把金标从「标完了」推进到「**可评测、可写进组会/支撑师兄论文**」。

### 任务 1：冻结金标发布包（1–2 天）必做

产出目录建议：`datasets/gold_security_v1/release/`

1. 从总表导出仅 `gold_status=human_gold_v1` 的子集 → `gold352.jsonl` / `.csv`
2. 写 `GOLD_RELEASE_NOTES.md`：定义、数量、抽样设计、标注人、已知争议
3. 生成 `gold_vs_detection` 对照表（银标 vs 金标混淆矩阵 + 不一致案例列表）
4. 更新总表说明书 `DATASHEET.md` 中金标章节为「已完成 v1」

**验收：** 别人只拿 release 目录就能复现金标集合。

### 任务 2：搭建最小评测脚本（3–5 天）必做

用金标 352 当测试集，跑至少 **2 个基线**，输出统一指标：

| 指标 | 说明 |
|------|------|
| Accuracy / Macro-F1 | 四分类或三分类（可去掉 uncertain） |
| malicious 的 P/R/F1 | 检测论文最关心 |
| 混淆矩阵 | detection→gold 或 baseline→gold |

建议基线（由易到难）：

1. **银标直接当预测**：`detection_label` vs `gold_security_label`（你已有数据，先出这个数）
2. **规则/现成扫描器**：ClawGuard 或 SkillSpector（若环境还在）
3. **（可选）LLM 裁判**：deepseek-v4-flash，与之前精审 prompt 对齐

产出：`experiments/baseline_v1/results.json` + 一页结果表。

**验收：** 一张表能回答「银标/扫描器相对人工金标差多少」。

### 任务 3：写分析短报（2–3 天）强烈建议

标题可参考：《ClawHub Skill 安全银标与人工金标偏差分析》

至少包含：

1. 金标分布与功能分布
2. 银标→金标主要翻转类型（如 benign→BBD、malicious→BBD）
3. 10–20 个典型案例（附 `gold_review_notes`）
4. 对师兄检测系统的启示（易误报模式 / 易漏报模式）

**验收：** 能在组会讲 10 分钟。

### 任务 4：与师兄对齐接口（半天）必做

当面确认：

1. 他论文评测是否直接用你的 352 金标？要不要再扩到 500+？
2. 他需要的字段格式（csv 列名、正负样本定义）
3. 你是否作为数据/评测共作者或致谢

把结论记进 `docs/alignment_with_senior.md`。

### 任务 5（可选，开题储备）

任选其一深入，不要并行太多：

- **A. 扩金标**：难例再抽 100（BBD 边界、flash 不一致）
- **B. 功能分类器**：用 352 训/提示一个八类功能分类小实验
- **C. MalSkillBench 分层评测**：补 `attack_vector`（CI/PI）后分层报告召回

---

## 本周执行顺序（建议）

```
Day1-2  任务1 冻结 release + 混淆矩阵
Day3-5  任务2 基线1（银标）+ 基线2（扫描器或 flash）
Day6    任务3 短报初稿
Day7    任务4 找师兄对齐
```

## 不要做什么（本阶段）

- 不要急着全量 8520 人工重标
- 不要一上来训练大检测模型抢师兄主线
- 不要改掉总表里的 `detection_label` 银标

---

## 需要我协助时

直接说要做哪一个，例如：

- 「帮我导出 gold352 release」
- 「帮我算银标 vs 金标指标并出表」
- 「帮我起草组会短报大纲」
