import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { Link, useSearchParams } from "react-router-dom";
import {
  fetchSkills,
  fetchStats,
  fetchSyncStatus,
  type SkillListItem,
  type Stats,
} from "../api";
import {
  GOLD_STATUS_FILTER_UNLABELED,
  formatGoldStatus,
  formatTag,
} from "../labels";

function labelClass(label: string): string {
  if (label === "malicious") return "chip malicious";
  if (label === "benign") return "chip benign";
  if (label === "benign_but_dangerous") return "chip bbd";
  if (label === "uncertain") return "chip uncertain";
  return "chip";
}

function SkillCard({ item }: { item: SkillListItem }) {
  return (
    <Link className="card" to={`/skill/${encodeURIComponent(item.id)}`}>
      <h3>{item.name}</h3>
      <div className="fn">{item.function || "功能待标注"}</div>
      <div className="meta-row">
        <span className={labelClass(item.detection_label)}>
          {item.is_malicious ? "恶意" : "非恶意"} · {item.detection_label}
        </span>
        {item.function_label ? (
          <span className="chip">{item.function_label}</span>
        ) : null}
        <span className="chip">{item.source}</span>
      </div>
    </Link>
  );
}

export default function BrowsePage() {
  const [params, setParams] = useSearchParams();
  const [stats, setStats] = useState<Stats | null>(null);
  const [items, setItems] = useState<SkillListItem[]>([]);
  const [total, setTotal] = useState(0);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);
  const [syncHint, setSyncHint] = useState("");
  const dataVersionRef = useRef<number | null>(null);

  const q = params.get("q") ?? "";
  const label = params.get("label") ?? "";
  const source = params.get("source") ?? "";
  const functionFilter = params.get("function") ?? "";
  const gold = params.get("gold_status") ?? "";
  const page = Number(params.get("page") ?? "1");

  const query = useMemo(() => {
    const p = new URLSearchParams();
    if (q) p.set("q", q);
    if (label) p.set("label", label);
    if (source) p.set("source", source);
    if (functionFilter) p.set("function", functionFilter);
    if (gold) p.set("gold_status", gold);
    p.set("page", String(page));
    p.set("page_size", "24");
    return p;
  }, [q, label, source, functionFilter, gold, page]);

  const reloadList = useCallback(() => {
    fetchSkills(query)
      .then((data) => {
        setItems(data.items);
        setTotal(data.total);
        setError("");
      })
      .catch((e) => setError(String(e.message || e)))
      .finally(() => setLoading(false));
    fetchStats()
      .then(setStats)
      .catch(() => undefined);
  }, [query]);

  useEffect(() => {
    fetchStats()
      .then((s) => {
        setStats(s);
        const ver = s.sync?.data_version;
        if (typeof ver === "number") dataVersionRef.current = ver;
      })
      .catch((e) => setError(String(e.message || e)));
  }, []);

  useEffect(() => {
    const timer = window.setInterval(() => {
      fetchSyncStatus()
        .then((sync) => {
          const ver = sync.data_version;
          if (
            dataVersionRef.current !== null &&
            ver !== dataVersionRef.current
          ) {
            dataVersionRef.current = ver;
            setSyncHint("已从 GitHub 同步远程更新");
            window.setTimeout(() => setSyncHint(""), 4000);
            setLoading(true);
            reloadList();
          } else if (dataVersionRef.current === null) {
            dataVersionRef.current = ver;
          }
        })
        .catch(() => undefined);
    }, 20000);
    return () => window.clearInterval(timer);
  }, [reloadList]);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    fetchSkills(query)
      .then((data) => {
        if (cancelled) return;
        setItems(data.items);
        setTotal(data.total);
        setError("");
      })
      .catch((e) => {
        if (!cancelled) setError(String(e.message || e));
      })
      .finally(() => {
        if (!cancelled) setLoading(false);
      });
    return () => {
      cancelled = true;
    };
  }, [query]);

  function update(key: string, value: string) {
    const next = new URLSearchParams(params);
    if (value) next.set(key, value);
    else next.delete(key);
    if (key !== "page") next.set("page", "1");
    setParams(next);
  }

  const pages = Math.max(1, Math.ceil(total / 24));
  const counts = stats?.detection_label_counts ?? {};

  return (
    <>
      <section className="hero">
        <h1>SkillDAG 关系型 Skill 数据集</h1>
        <p>
          浏览 <code>skills_relational_v1</code>（SkillDAG skills_200）：200 个 skill 节点与
          specializes / similar_to 等关系边。支持筛选、下载与上传；GitHub 同步后自动刷新列表。
        </p>
        <div className="stat-row">
          <div className="stat">
            <div className="label">总计</div>
            <div className="value">{stats?.n ?? "—"}</div>
          </div>
          <div className="stat">
            <div className="label">Benign</div>
            <div className="value">{counts.benign ?? "—"}</div>
          </div>
          <div className="stat">
            <div className="label">Malicious</div>
            <div className="value">{counts.malicious ?? "—"}</div>
          </div>
          <div className="stat">
            <div className="label">BBD</div>
            <div className="value">{counts.benign_but_dangerous ?? "—"}</div>
          </div>
        </div>
      </section>

      <div className="toolbar">
        <input
          placeholder="搜索名称 / slug / 功能…"
          value={q}
          onChange={(e) => update("q", e.target.value)}
        />
        <select value={label} onChange={(e) => update("label", e.target.value)}>
          <option value="">全部标签</option>
          <option value="benign">benign</option>
          <option value="benign_but_dangerous">benign_but_dangerous</option>
          <option value="malicious">malicious</option>
          <option value="uncertain">uncertain</option>
        </select>
        <select value={source} onChange={(e) => update("source", e.target.value)}>
          <option value="">全部来源</option>
          <option value="clawhub">clawhub</option>
          <option value="malskillbench">malskillbench</option>
          <option value="upload">upload</option>
        </select>
        <select
          value={functionFilter}
          onChange={(e) => update("function", e.target.value)}
        >
          <option value="">全部功能</option>
          {[
            "Coding",
            "Research",
            "Browser",
            "File-Agent",
            "Communication",
            "Data-Agent",
            "Automation",
            "Other",
          ].map((f) => (
            <option key={f} value={f}>
              {f}
            </option>
          ))}
        </select>
        <select value={gold} onChange={(e) => update("gold_status", e.target.value)}>
          <option value="">金标状态</option>
          <option value="human_gold_v1">人工金标</option>
          <option value={GOLD_STATUS_FILTER_UNLABELED}>未标注</option>
        </select>
      </div>

      {syncHint ? <div className="chip">{syncHint}</div> : null}

      {error ? <div className="error">{error}</div> : null}
      {loading ? <div className="empty">加载中…</div> : null}
      {!loading && !error && items.length === 0 ? (
        <div className="empty">没有匹配的 skill</div>
      ) : null}

      <div className="grid">
        {items.map((item) => (
          <SkillCard key={item.id} item={item} />
        ))}
      </div>

      <div className="pager">
        <span>
          共 {total} 条 · 第 {page}/{pages} 页
        </span>
        <div className="actions">
          <button
            className="btn ghost"
            disabled={page <= 1}
            onClick={() => update("page", String(page - 1))}
            type="button"
          >
            上一页
          </button>
          <button
            className="btn ghost"
            disabled={page >= pages}
            onClick={() => update("page", String(page + 1))}
            type="button"
          >
            下一页
          </button>
        </div>
      </div>
    </>
  );
}
