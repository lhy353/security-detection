export type SyncStatus = {
  status: string;
  message: string;
  last_pull_at: number | null;
  data_version: number;
  remote_updated?: boolean;
  n?: number;
};

export type SkillListItem = {
  id: string;
  slug: string;
  name: string;
  function: string;
  detection_label: string;
  is_malicious: boolean;
  source: string;
  cohort: string;
  function_label: string;
  gold_status: string;
  tags: string[];
  dataset_name?: string;
};

export type SkillDetail = SkillListItem & {
  attack_vector: string;
  behavior: string;
  insertion_strategy: string;
  function_status: string;
  gold_security_label: string;
  gold_confidence: string;
  gold_reviewer: string;
  gold_review_notes: string;
  gold_sample_id: string;
  local_path: string;
  description: string;
  skill_md: string | null;
  content_source: string;
  relational_edges: RelationalEdge[];
};

export type RelationalEdge = {
  type: string;
  direction: string;
  slug: string;
  skill_id: string;
  name: string;
  reason: string;
};

export type Stats = {
  n: number;
  detection_label_counts: Record<string, number>;
  by_source: Record<string, number>;
  by_dataset?: Record<string, number>;
  datasets?: string[];
  summary: Record<string, unknown>;
  dataset?: string;
  sync?: SyncStatus;
};

export type ListResponse = {
  total: number;
  page: number;
  page_size: number;
  items: SkillListItem[];
};

async function parseError(res: Response): Promise<string> {
  try {
    const data = await res.json();
    if (typeof data.detail === "string") return data.detail;
    return JSON.stringify(data.detail ?? data);
  } catch {
    return res.statusText;
  }
}

export async function fetchSyncStatus(): Promise<SyncStatus> {
  const res = await fetch("/api/sync-status");
  if (!res.ok) throw new Error(await parseError(res));
  return res.json();
}

export async function fetchStats(): Promise<Stats> {
  const res = await fetch("/api/stats");
  if (!res.ok) throw new Error(await parseError(res));
  return res.json();
}

export async function fetchSkills(params: URLSearchParams): Promise<ListResponse> {
  const res = await fetch(`/api/skills?${params}`);
  if (!res.ok) throw new Error(await parseError(res));
  return res.json();
}

export async function fetchSkill(id: string): Promise<SkillDetail> {
  const res = await fetch(`/api/skill?id=${encodeURIComponent(id)}`);
  if (!res.ok) throw new Error(await parseError(res));
  return res.json();
}

export async function fetchRelated(id: string): Promise<SkillListItem[]> {
  const res = await fetch(
    `/api/skill-related?id=${encodeURIComponent(id)}&limit=8`
  );
  if (!res.ok) throw new Error(await parseError(res));
  const data = await res.json();
  return data.items;
}

export function skillDownloadUrl(id: string, full = false): string {
  const q = new URLSearchParams({ id });
  if (full) q.set("full", "true");
  return `/api/skill-download?${q}`;
}

export async function uploadSkill(form: FormData): Promise<{ id: string }> {
  const res = await fetch("/api/skills/upload", { method: "POST", body: form });
  if (!res.ok) throw new Error(await parseError(res));
  return res.json();
}
