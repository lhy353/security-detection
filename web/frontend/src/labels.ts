/** Display labels for manifest / tag values */

const GOLD_STATUS_LABELS: Record<string, string> = {
  pending_reannotation: "未标注",
  benchmark_label: "未标注",
  human_gold_v1: "人工金标",
};

const UNLABELED_GOLD_STATUSES = new Set([
  "pending_reannotation",
  "benchmark_label",
]);

export function formatGoldStatus(status: string): string {
  if (!status) return "—";
  return GOLD_STATUS_LABELS[status] ?? status;
}

export function formatTag(tag: string): string {
  return GOLD_STATUS_LABELS[tag] ?? tag;
}

export function isUnlabeledGoldStatus(status: string): boolean {
  return UNLABELED_GOLD_STATUSES.has(status);
}

export const GOLD_STATUS_FILTER_UNLABELED = "unlabeled";
