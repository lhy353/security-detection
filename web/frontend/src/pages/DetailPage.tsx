import { useEffect, useState } from "react";
import ReactMarkdown from "react-markdown";
import { Link, useParams } from "react-router-dom";
import {
  fetchRelated,
  fetchSkill,
  skillDownloadUrl,
  type RelatedSkill,
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

function relatedLabel(item: RelatedSkill): string {
  const arrow = item.direction === "outgoing" ? "→" : "←";
  return `${item.type} ${arrow} ${item.name || item.slug}`;
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

  const relatedSkills = skill.related_skills ?? [];
  const isRelational = skill.source === "skilldag" || skill.dataset_name === "skills_relational_v1";

  function relatedSkillsSummary(): string {
    if (relatedSkills.length > 0) {
      return relatedSkills.map((r) => r.slug).join(", ");
    }
    if (!isRelational) {
      return "不适用（非关系型 skill）";
    }
    return "无（SkillGraph 中无 specializes / similar_to 连边）";
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
          <dt>关联 Skill</dt>
          <dd>{relatedSkillsSummary()}</dd>
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

      {isRelational && relatedSkills.length === 0 ? (
        <section className="panel">
          <h2>关联 Skill</h2>
          <p className="muted" style={{ marginTop: 0 }}>
            该节点在 SkillDAG skills_200 图中没有直接连边（200 条里约 107
            条为孤立节点）。可点击顶部「关系型集」浏览有连边的 skill，例如{" "}
            <Link to="/skill/skilldag%3Aharbor">harbor</Link>。
          </p>
        </section>
      ) : null}

      {relatedSkills.length > 0 ? (
        <section className="panel">
          <h2>关联 Skill</h2>
          <p className="muted" style={{ marginTop: 0 }}>
            来自 <code>meta.json</code> 的 <code>related_skills</code>（SkillGraph
            边：specializes / similar_to）。
          </p>
          <div className="related-list">
            {relatedSkills.map((item) => (
              <Link
                key={`${item.type}-${item.slug}`}
                to={`/skill/${encodeURIComponent(item.skill_id)}`}
              >
                <span>{relatedLabel(item)}</span>
                <span className="chip">{item.type}</span>
              </Link>
            ))}
          </div>
        </section>
      ) : null}

      {related.length > 0 && relatedSkills.length === 0 ? (
        <section className="panel">
          <h2>相关技能</h2>
          <p className="muted" style={{ marginTop: 0 }}>
            按功能类 / 标签 / 来源启发式推荐。
          </p>
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
        </section>
      ) : null}
    </div>
  );
}
