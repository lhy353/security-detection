# Gold Security v1 Release Notes

## 1. 这是什么
人工金标子集（`gold_status=human_gold_v1`），从 `security_merged_v1` 导出，用于评测安全检测器与分析银标偏差。

- 样本数：**352**
- 标注人：见各行 `gold_reviewer`（主要为 A01）
- 同时含功能八类：`function_label`

## 2. 标签定义（摘要）
| 标签 | 含义 |
|------|------|
| malicious | 明确恶意 |
| benign_but_dangerous | 正当但高权限可滥用 |
| benign | 非恶意且风险较低 |
| uncertain | 证据不足 |

功能八类：Coding / Research / Browser / File-Agent / Communication / Data-Agent / Automation / Other

## 3. 金标数量
| gold_security_label | n |
|---|---:|
| malicious | 99 |
| benign_but_dangerous | 180 |
| benign | 73 |
| uncertain | 0 |

## 4. 功能分布
| function_label | n |
|---|---:|
| Automation | 97 |
| Other | 60 |
| Data-Agent | 48 |
| Coding | 48 |
| File-Agent | 38 |
| Research | 26 |
| Communication | 24 |
| Browser | 11 |

## 5. 银标 vs 金标混淆矩阵

**怎么读：**
- **行（detection_label）** = 银标 / 自动检测结果（当作“预测”）
- **列（gold_security_label）** = 人工金标（当作“真值”）
- **对角线** = 银标与金标一致
- **非对角线** = 不一致（翻转）

一致：**319 / 352 = 0.9063**
不一致：33（详见 `mismatches_detection_vs_gold.csv`）

| detection\\gold | malicious | benign_but_dangerous | benign | uncertain | row sum |
|---|---:|---:|---:|---:|---:|
| **malicious** | 99 | 1 | 0 | 0 | 100 |
| **benign_but_dangerous** | 0 | 149 | 1 | 0 | 150 |
| **benign** | 0 | 29 | 71 | 0 | 100 |
| **uncertain** | 0 | 1 | 1 | 0 | 2 |
| **col sum** | 99 | 180 | 73 | 0 | 352 |

### 分标签指标（把银标当预测，金标当真值；一对多）
| label | precision | recall | F1 |
|---|---:|---:|---:|
| malicious | 0.99 | 1 | 0.995 |
| benign_but_dangerous | 0.9933 | 0.8278 | 0.903 |
| benign | 0.71 | 0.9726 | 0.8208 |
| uncertain | 0 | - | - |

## 6. 主要不一致模式
- 最多见：银标 `benign` → 金标 `benign_but_dangerous`（银标偏松，低估高权限）
- 少见：`malicious` → `benign_but_dangerous`；`benign_but_dangerous` → `benign`

## 7. 文件清单
| 文件 | 说明 |
|------|------|
| gold352.csv / .jsonl | 金标全集 |
| confusion_and_metrics.json | 矩阵与指标机器可读 |
| mismatches_detection_vs_gold.csv | 全部不一致样本 |
| RELEASE_NOTES.md | 本说明 |

## 8. 使用建议
- 评测检测器时：以 `gold_security_label` 为真值
- 不要用银标 `detection_label` 当真值
- 报告时写明：n=352，标注规范见 `../guidelines.md`

## 9. 版本
- release 生成时间：2026-08-17T07:48:31.705Z
- 源表：`security_merged_v1/manifest.csv`
