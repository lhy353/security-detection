import { FormEvent, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { uploadSkill } from "../api";

export default function UploadPage() {
  const nav = useNavigate();
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setError("");
    setBusy(true);
    const form = new FormData(e.currentTarget);
    const file = form.get("file");
    if (file instanceof File && file.size === 0) {
      form.delete("file");
    }
    try {
      const res = await uploadSkill(form);
      nav(`/skill/${encodeURIComponent(res.id)}`);
    } catch (err) {
      setError(String((err as Error).message || err));
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="detail">
      <section className="hero">
        <h1>上传技能</h1>
        <p>
          写入 <code>datasets/skills_relational_v1/skills/</code> 并更新 manifest。
          若 slug 与已有 <code>skilldag:</code> 或 <code>clawhub:</code> 记录相同，将<strong>覆盖</strong>该条记录。
          随后可自动 push 到 GitHub。
        </p>
      </section>

      <section className="panel">
        <form className="form-grid" onSubmit={onSubmit}>
          <label>
            名称 *
            <input name="name" required placeholder="my-skill" />
          </label>
          <label>
            Slug（可选，默认由名称生成）
            <input name="slug" placeholder="my-skill" />
          </label>
          <label>
            主要功能
            <select name="function_label" defaultValue="Other">
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
          </label>
          <label>
            检测标签 / 是否恶意
            <select name="detection_label" defaultValue="benign">
              <option value="benign">benign（非恶意）</option>
              <option value="benign_but_dangerous">
                benign_but_dangerous（非恶意·高权限）
              </option>
              <option value="uncertain">uncertain</option>
              <option value="malicious">malicious（恶意）</option>
            </select>
          </label>
          <label>
            自定义标签（逗号分隔）
            <input name="tags" placeholder="demo, research" />
          </label>
          <label>
            简短描述
            <textarea name="description" rows={3} placeholder="主要做什么…" />
          </label>
          <label>
            SKILL.md 文本（可选）
            <textarea
              name="skill_md"
              rows={8}
              placeholder={"---\nname: ...\ndescription: ...\n---\n\n# ..."}
            />
          </label>
          <label>
            或上传文件（SKILL.md / zip）
            <input name="file" type="file" accept=".md,.zip,text/markdown" />
          </label>
          {error ? <div className="error">{error}</div> : null}
          <div className="actions">
            <button className="btn" disabled={busy} type="submit">
              {busy ? "上传中…" : "提交上传"}
            </button>
            <Link className="btn ghost" to="/">
              取消
            </Link>
          </div>
        </form>
      </section>
    </div>
  );
}
