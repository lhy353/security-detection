# 操作手册：Release 说明 + 银标 vs 金标混淆矩阵

对应产出目录：`datasets/gold_security_v1/release/`  
一键生成：`node datasets/gold_security_v1/build_release.mjs`

---

## 一、混淆矩阵是什么？

### 1. 直观理解
混淆矩阵（Confusion Matrix）是一张**对照表**：看「预测标签」和「真实标签」有多少对上了、错到哪里去了。

在本项目里：

| 角色 | 用哪一列 | 含义 |
|------|----------|------|
| 预测（行） | `detection_label` | 银标：自动检测/flash 等机器结果 |
| 真值（列） | `gold_security_label` | 金标：你人工标注的最终答案 |

单元格 `(i, j)` = **银标判成 i、金标其实是 j** 的样本数。

### 2. 怎么读（举例）

假设矩阵片段：

| detection\gold | malicious | BBD | benign |
|---|---:|---:|---:|
| malicious | 99 | 1 | 0 |
| benign | 0 | 29 | 71 |

含义：
- 对角线 `99`、`71`：两边一致（对了）
- `benign → BBD = 29`：机器当良性，你认为是高权限正当（银标**偏松**）
- `malicious → BBD = 1`：机器当恶意，你认为只是危险但正当（银标**偏严/误报**）

### 3. 有什么用？
1. **看总体准不准**：对角线占比 = 一致率（accuracy）
2. **看错在哪类**：是漏检恶意，还是把 BBD 当 benign
3. **指导改检测器**：例如大量 benign→BBD → 要加强「高权限」识别，而不是只抓“恶意关键词”
4. **写论文/组会**：一张表讲清银标偏差，比只报准确率更有信息量

### 4. 和 Precision / Recall 的关系
对某一类（如 `malicious`）把矩阵压成二分类：

- **TP**：预测=malicious 且 金标=malicious  
- **FP**：预测=malicious 但 金标≠malicious  
- **FN**：预测≠malicious 但 金标=malicious  

则：
- Precision = TP / (TP+FP)  （报恶意有多准）
- Recall = TP / (TP+FN)     （真恶意抓回多少）
- F1 = 二者调和平均

`build_release.mjs` 已按每一类算出这些数，见 `confusion_and_metrics.json`。

---

## 二、详细步骤（你要做的事）

### 步骤 0：确认总表已含金标
打开 `datasets/security_merged_v1/manifest.csv`，确认存在且已填：
- `gold_status = human_gold_v1`（约 352 行）
- `gold_security_label`
- `function_label`

### 步骤 1：一键生成 release（推荐）
在 PowerShell：

```powershell
cd E:\security-detection
node datasets\gold_security_v1\build_release.mjs
```

会生成：

```
datasets/gold_security_v1/release/
  ├── gold352.csv
  ├── gold352.jsonl
  ├── confusion_and_metrics.json
  ├── mismatches_detection_vs_gold.csv
  └── RELEASE_NOTES.md
```

### 步骤 2：自己读懂矩阵（必做，5–10 分钟）
1. 打开 `RELEASE_NOTES.md` 里的表格  
2. 圈出最大的非对角线格子（你们主要是 **benign → BBD**）  
3. 打开 `mismatches_detection_vs_gold.csv`，抽读 5–10 条 `gold_review_notes`  
4. 用一句话总结偏差，例如：  
   > 「银标易把高权限正当技能标成 benign；恶意类与金标高度一致。」

### 步骤 3：检查 release 说明是否完整
`RELEASE_NOTES.md` 应包含：
- [x] 样本数与来源  
- [x] 标签定义  
- [x] 金标/功能数量  
- [x] 混淆矩阵与一致率  
- [x] 分标签 P/R/F1  
- [x] 文件清单  

若你要改标注人、抽样说明，直接编辑该 md 补一段「抽样设计」即可。

### 步骤 4：把 release 当“对外版本”
之后评测、给师兄，优先发整个 `release/` 文件夹，而不是整份 8520 总表。

### 步骤 5：（可选）Excel 手做矩阵加深理解
1. 筛选 `gold_status=human_gold_v1`  
2. 插入数据透视表：行=`detection_label`，列=`gold_security_label`，值=计数  
3. 与 `RELEASE_NOTES.md` 中数字核对是否一致  

---

## 三、手写实现逻辑（便于你以后改代码）

伪代码：

```text
对每一条金标样本:
  d = detection_label      # 预测
  g = gold_security_label  # 真值
  matrix[d][g] += 1

accuracy = sum(matrix[i][i]) / N
```

Python 等价：

```python
from collections import Counter
# pairs = [(detection, gold), ...]
labels = ["malicious", "benign_but_dangerous", "benign", "uncertain"]
matrix = {d: {g: 0 for g in labels} for d in labels}
for d, g in pairs:
    matrix[d][g] += 1
```

或用 `sklearn.metrics.confusion_matrix(y_true=gold, y_pred=detection, labels=labels)`  
注意：sklearn 默认 **行=真值、列=预测**，和我们文档里「行=银标预测、列=金标真值」可能行列相反，写论文时要说明。

---

## 四、验收标准
- `gold352.*` 行数 = 352  
- 矩阵各格之和 = 352  
- 一致率与 `agree / 352` 一致  
- 能用中文解释最大错分格的含义  

完成后进入下一任务：用同一套金标跑第二个基线（ClawGuard / flash）并对比 F1。
