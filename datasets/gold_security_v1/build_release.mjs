/**
 * Build gold352 release + silver(detection) vs gold confusion matrix.
 */
import fs from "fs";
import path from "path";

const ROOT = "E:/security-detection/datasets";
const MANIFEST = path.join(ROOT, "security_merged_v1", "manifest.csv");
const OUT = path.join(ROOT, "gold_security_v1", "release");

function parseCsv(text) {
  const lines = text.replace(/^\uFEFF/, "").split(/\r?\n/).filter(Boolean);
  function split(line) {
    const out = [];
    let cur = "";
    let q = false;
    for (let i = 0; i < line.length; i++) {
      const c = line[i];
      if (q) {
        if (c === '"' && line[i + 1] === '"') {
          cur += '"';
          i++;
        } else if (c === '"') q = false;
        else cur += c;
      } else if (c === '"') q = true;
      else if (c === ",") {
        out.push(cur);
        cur = "";
      } else cur += c;
    }
    out.push(cur);
    return out;
  }
  const h = split(lines[0]);
  return lines.slice(1).map((l) => {
    const c = split(l);
    const o = {};
    h.forEach((k, i) => (o[k] = c[i] ?? ""));
    return o;
  });
}

function esc(v) {
  const s = v == null ? "" : String(v);
  return /[",\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s;
}

function writeCsv(file, rows, cols) {
  const body =
    [cols.join(","), ...rows.map((r) => cols.map((c) => esc(r[c])).join(","))].join("\n") +
    "\n";
  fs.writeFileSync(file, body);
}

fs.mkdirSync(OUT, { recursive: true });

const all = parseCsv(fs.readFileSync(MANIFEST, "utf8"));
const gold = all.filter((r) => r.gold_status === "human_gold_v1");

const labels = ["malicious", "benign_but_dangerous", "benign", "uncertain"];

// confusion: rows = detection_label (银标/预测), cols = gold_security_label (金标/真值)
const matrix = {};
for (const d of labels) {
  matrix[d] = {};
  for (const g of labels) matrix[d][g] = 0;
}

let agree = 0;
const mismatches = [];
for (const r of gold) {
  const d = r.detection_label || "uncertain";
  const g = r.gold_security_label || "uncertain";
  if (!matrix[d]) matrix[d] = Object.fromEntries(labels.map((x) => [x, 0]));
  if (matrix[d][g] === undefined) matrix[d][g] = 0;
  matrix[d][g]++;
  if (d === g) agree++;
  else {
    mismatches.push({
      id: r.id,
      slug: r.slug,
      sample_bucket: "",
      detection_label: d,
      gold_security_label: g,
      function_label: r.function_label,
      gold_confidence: r.gold_confidence,
      gold_reviewer: r.gold_reviewer,
      gold_review_notes: r.gold_review_notes,
      local_path: r.local_path,
    });
  }
}

const goldCounts = Object.fromEntries(labels.map((l) => [l, gold.filter((r) => r.gold_security_label === l).length]));
const detCounts = Object.fromEntries(labels.map((l) => [l, gold.filter((r) => r.detection_label === l).length]));
const funCounts = {};
for (const r of gold) {
  const f = r.function_label || "?";
  funCounts[f] = (funCounts[f] || 0) + 1;
}

// per-class metrics treating each label as positive vs rest (multiclass one-vs-rest)
function metricsFor(label) {
  let tp = 0,
    fp = 0,
    fn = 0,
    tn = 0;
  for (const d of labels) {
    for (const g of labels) {
      const n = matrix[d]?.[g] || 0;
      const predPos = d === label;
      const truePos = g === label;
      if (predPos && truePos) tp += n;
      else if (predPos && !truePos) fp += n;
      else if (!predPos && truePos) fn += n;
      else tn += n;
    }
  }
  const precision = tp + fp ? tp / (tp + fp) : null;
  const recall = tp + fn ? tp / (tp + fn) : null;
  const f1 = precision != null && recall != null && precision + recall ? (2 * precision * recall) / (precision + recall) : null;
  return {
    tp,
    fp,
    fn,
    tn,
    precision: precision == null ? null : Number(precision.toFixed(4)),
    recall: recall == null ? null : Number(recall.toFixed(4)),
    f1: f1 == null ? null : Number(f1.toFixed(4)),
  };
}

const perClass = Object.fromEntries(labels.map((l) => [l, metricsFor(l)]));

const release = {
  name: "gold_security_v1",
  n: gold.length,
  source_manifest: "datasets/security_merged_v1/manifest.csv",
  agree_with_detection: agree,
  agree_rate: Number((agree / gold.length).toFixed(4)),
  mismatch_n: mismatches.length,
  gold_counts: goldCounts,
  detection_counts_on_gold_subset: detCounts,
  function_counts: funCounts,
  confusion_detection_rows_gold_cols: matrix,
  per_class_metrics_detection_as_prediction: perClass,
  created_at: new Date().toISOString(),
};

// export gold352
const cols = [
  "id",
  "slug",
  "source",
  "cohort",
  "detection_label",
  "gold_security_label",
  "function_label",
  "gold_confidence",
  "gold_reviewer",
  "gold_review_notes",
  "gold_sample_id",
  "gold_status",
  "local_path",
];
writeCsv(path.join(OUT, "gold352.csv"), gold, cols);
fs.writeFileSync(
  path.join(OUT, "gold352.jsonl"),
  gold.map((r) => JSON.stringify(Object.fromEntries(cols.map((c) => [c, r[c] ?? ""])))).join("\n") + "\n"
);

writeCsv(
  path.join(OUT, "mismatches_detection_vs_gold.csv"),
  mismatches,
  [
    "id",
    "slug",
    "detection_label",
    "gold_security_label",
    "function_label",
    "gold_confidence",
    "gold_reviewer",
    "gold_review_notes",
    "local_path",
  ]
);

fs.writeFileSync(path.join(OUT, "confusion_and_metrics.json"), JSON.stringify(release, null, 2));

// human-readable matrix markdown
const header = "| detection\\\\gold | " + labels.join(" | ") + " | row sum |";
const sep = "|---|" + labels.map(() => "---:").join("|") + "|---:|";
const body = labels
  .map((d) => {
    const cells = labels.map((g) => matrix[d][g] || 0);
    const sum = cells.reduce((a, b) => a + b, 0);
    return `| **${d}** | ${cells.join(" | ")} | ${sum} |`;
  })
  .join("\n");
const colSums = labels.map((g) => labels.reduce((a, d) => a + (matrix[d][g] || 0), 0));
const footer = `| **col sum** | ${colSums.join(" | ")} | ${gold.length} |`;

const md = `# Gold Security v1 Release Notes

## 1. 这是什么
人工金标子集（\`gold_status=human_gold_v1\`），从 \`security_merged_v1\` 导出，用于评测安全检测器与分析银标偏差。

- 样本数：**${gold.length}**
- 标注人：见各行 \`gold_reviewer\`（主要为 A01）
- 同时含功能八类：\`function_label\`

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
${labels.map((l) => `| ${l} | ${goldCounts[l] || 0} |`).join("\n")}

## 4. 功能分布
| function_label | n |
|---|---:|
${Object.entries(funCounts)
  .sort((a, b) => b[1] - a[1])
  .map(([k, v]) => `| ${k} | ${v} |`)
  .join("\n")}

## 5. 银标 vs 金标混淆矩阵

**怎么读：**
- **行（detection_label）** = 银标 / 自动检测结果（当作“预测”）
- **列（gold_security_label）** = 人工金标（当作“真值”）
- **对角线** = 银标与金标一致
- **非对角线** = 不一致（翻转）

一致：**${agree} / ${gold.length} = ${(agree / gold.length).toFixed(4)}**
不一致：${mismatches.length}（详见 \`mismatches_detection_vs_gold.csv\`）

${header}
${sep}
${body}
${footer}

### 分标签指标（把银标当预测，金标当真值；一对多）
| label | precision | recall | F1 |
|---|---:|---:|---:|
${labels
  .map((l) => {
    const m = perClass[l];
    return `| ${l} | ${m.precision ?? "-"} | ${m.recall ?? "-"} | ${m.f1 ?? "-"} |`;
  })
  .join("\n")}

## 6. 主要不一致模式
- 最多见：银标 \`benign\` → 金标 \`benign_but_dangerous\`（银标偏松，低估高权限）
- 少见：\`malicious\` → \`benign_but_dangerous\`；\`benign_but_dangerous\` → \`benign\`

## 7. 文件清单
| 文件 | 说明 |
|------|------|
| gold352.csv / .jsonl | 金标全集 |
| confusion_and_metrics.json | 矩阵与指标机器可读 |
| mismatches_detection_vs_gold.csv | 全部不一致样本 |
| RELEASE_NOTES.md | 本说明 |

## 8. 使用建议
- 评测检测器时：以 \`gold_security_label\` 为真值
- 不要用银标 \`detection_label\` 当真值
- 报告时写明：n=${gold.length}，标注规范见 \`../guidelines.md\`

## 9. 版本
- release 生成时间：${new Date().toISOString()}
- 源表：\`security_merged_v1/manifest.csv\`
`;

fs.writeFileSync(path.join(OUT, "RELEASE_NOTES.md"), md);
console.log(JSON.stringify({ out: OUT, n: gold.length, agree, mismatches: mismatches.length }, null, 2));
