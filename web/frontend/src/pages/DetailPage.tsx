import { useEffect, useState } from "react";
import ReactMarkdown from "react-markdown";
import { Link, useParams } from "react-router-dom";
import {
  fetchRelated,
  fetchSkill,
  skillDownloadUrl,
  type RelationalEdge,
  type SkillDetail,
  type SkillListItem,
} from "../api";
import { formatGoldStatus, formatTag } from "../labels";

function labelClass(label: string): string {
  if (label === "malicious") return "chip malicious";
  if (label === "benign") return "chip benign";
  if (label === "benign_but_dangerous") return "chip bbd";
  if (label === "uncertain") return "chip uncertain";
  return "chip";
}

function edgeLabel(edge: RelationalEdge): string {
  const dir = edge.direction === "out" ? "→" : "←";
  return `${edge.type} ${dir} ${edge.name || edge.slug}`;
}

export default function DetailPage() {
  const { id: raw } = useParams();
  const id = raw ? decodeURIComponent(raw) : "";
  const [skill, setSkill] = useState<SkillDetail | null>(null);
  const [related, setRelated] = useState<SkillListItem[]>([]);
  const [error, setError] = useState("");

  useEffect(() => {
    if (!id) return;
    let cancelled = false;
    setSkill(null);
    setError("");
    Promise.all([fetchSkill(id), fetchRelated(id)])
      .then(([detail, rel]) => {
        if (cancelled) return;
        setSkill(detail);
        setRelated(rel);
      })
      .catch((e) => {
        if (!cancelled) setError(String(e.message || e));
      });
    return () => {
      cancelled = true;
    };
  }, [id]);

  if (error) {
    return (
      <div className="detail">
        <Link className="btn ghost" to="/">
          ← 返回
        </Link>
        <div className="error">{error}</div>
      </div>
    );
  }

  if (!skill) {
    return <div className="empty">加载详情…</div>;
  }

  return (
    <div className="detail">
      <div className="actions">
        <Link className="btn ghost" to="/">
          ← 返回列表
        </Link>
        <a className="btn" href={skillDownloadUrl(skill.id)}>
          下载 SKILL 包
        </a>
        {skill.local_path ? (
          <a className="btn secondary" href={skillDownloadUrl(skill.id, true)}>
            下载完整目录
          </a>
        ) : null}
      </div>

      {skill.is_malicious ? (
        <div className="warn-banner">
          该样本标记为恶意（{skill.detection_label}）。仅供安全研究与检测评测，请勿在生产或未隔离环境执行。
        </div>
      ) : null}

      <section className="panel">
        <h2>{skill.name}</h2>
        <p className="muted" style={{ marginTop: 0 }}>
          {skill.description || skill.function || "无描述"}
        </p>
        <div className="meta-row" style={{ marginBottom: "1rem" }}>
          <span className={labelClass(skill.detection_label)}>
            {skill.is_malicious ? "恶意" : "非恶意"} · {skill.detection_label}
          </span>
          {skill.tags.map((t) => (
            <span className="chip" key={t}>
              {formatTag(t)}
            </span>
          ))}
        </div>
        <dl className="kv">
          <dt>数据集</dt>
          <dd>{skill.dataset_name || "—"}</dd>
          <dt>ID</dt>
          <dd>{skill.id}</dd>
          <dt>Slug</dt>
          <dd>{skill.slug}</dd>
          <dt>主要功能</dt>
          <dd>{skill.function_label || skill.function || "—"}</dd>
          <dt>来源 / 批次</dt>
          <dd>
            {skill.source} / {skill.cohort || "—"}
          </dd>
          <dt>金标状态</dt>
          <dd>{formatGoldStatus(skill.gold_status)}</dd>
          <dt>内容来源</dt>
          <dd>{skill.content_source}</dd>
          {skill.gold_review_notes ? (
            <>
              <dt>金标备注</dt>
              <dd>{skill.gold_review_notes}</dd>
            </>
          ) : null}
        </dl>
      </section>

      <section className="panel">
        <h2>SKILL.md</h2>
        {skill.skill_md ? (
          <div className="md">
            <ReactMarkdown>{skill.skill_md}</ReactMarkdown>
          </div>
        ) : (
          <p className="muted">
            暂无内容。请在本机运行{" "}
            <code>python scripts/build_skill_mirror.py</code>{" "}
            生成镜像，或确认 local_path 可访问。
          </p>
        )}
      </section>

      <section className="panel">
        <h2>关系边（SkillGraph）</h2>
        <p className="muted" style={{ marginTop: 0 }}>
          来自 SkillDAG skillgraph_200：specializes、similar_to 等类型化边。
        </p>
        {skill.relational_edges?.length ? (
          <div className="related-list">
            {skill.relational_edges.map((edge) => (
              <Link
                key={`${edge.type}-${edge.direction}-${edge.skill_id}`}
                to={`/skill/${encodeURIComponent(edge.skill_id)}`}
              >
                <span>{edgeLabel(edge)}</span>
                <span className="chip">{edge.type}</span>
              </Link>
            ))}
          </div>
        ) : (
          <p className="muted">该节点在图中无直接连边</p>
        )}
      </section>

      <section className="panel">
        <h2>相关技能</h2>
        <p className="muted" style={{ marginTop: 0 }}>
          优先使用关系图邻接；不足时按功能类 / 标签 / 来源启发式补充。
        </p>
        {related.length === 0 ? (
          <p className="muted">暂无相关项</p>
        ) : (
          <div className="related-list">
            {related.map((r) => (
              <Link key={r.id} to={`/skill/${encodeURIComponent(r.id)}`}>
                <span>{r.name}</span>
                <span className={labelClass(r.detection_label)}>
                  {r.detection_label}
                </span>
              </Link>
            ))}
          </div>
        )}
      </section>
    </div>
  );
}
