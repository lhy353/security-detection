# security-detection

Skill 安全检测数据集工作区，含可推送到 GitHub 的 **数据集门户**。

## 主数据集：`datasets/security_merged_v1`

| detection_label | 数量 | 来源 |
|---|---|---|
| benign | 5000 | flash FP→benign (520) + ClawGuard benign 抽样 (4480) |
| benign_but_dangerous | 150 | flash 首轮检测 |
| uncertain | 2 | flash |
| malicious | 3368 | MalSkillBench（可读 `SKILL.md`） |

主表：`manifest.jsonl` / `manifest.csv`  
说明书：[`DATASHEET.md`](datasets/security_merged_v1/DATASHEET.md)

## 金标底稿：`datasets/gold_security_v1`

- [`to_annotate.csv`](datasets/gold_security_v1/to_annotate.csv)（352 条）已回写主表（`gold_status=human_gold_v1`）
- 规范：[`guidelines.md`](datasets/gold_security_v1/guidelines.md)

## 数据集门户（Web）

浏览 / 筛选 / 详情 / 下载 / 上传。每条 skill 展示：**名称、主要功能、标签、是否恶意**（及四分类 `detection_label`）。

### 启动

```bash
# 依赖
pip install -r requirements-web.txt
cd web/frontend && npm install && npm run build && cd ../..

# 服务（本机 http://127.0.0.1:8000；局域网 http://<你的IP>:8000）
python -m web.backend

# 仅本机访问
python -m web.backend --host 127.0.0.1
```

开发时也可前后端分离（Vite 需加 `--host` 才能在局域网访问前端）：

```bash
# 终端 1
python -m web.backend

# 终端 2
cd web/frontend && npm run dev -- --host
```

局域网其他设备访问：`http://<本机IP>:8000`（生产构建）或 `http://<本机IP>:5173`（开发模式）。若无法访问，检查 Windows 防火墙是否放行对应端口。

### 生成本地可发布镜像（推荐再 push GitHub）

ClawHub / MalSkillBench 的 `local_path` 依赖本机磁盘。推仓库前先导出 `SKILL.md`：

```bash
python scripts/build_skill_mirror.py
# 可选：--limit 100  --force
```

英文 skill 批量补中文标题：

```bash
python scripts/backfill_chinese_titles.py
```

（从 SKILL.md 提取英文标题并翻译，结果写入 `meta.json` 的 `title` 字段）

功能八类自动标注（Coding / Research / Browser / File-Agent / Communication / Data-Agent / Automation / Other）：

```bash
python scripts/label_function_categories.py
```

已有人工金标（`human_gold_v1`）的 352 条不会被覆盖；其余 skill 读取 `SKILL.md` 内容自动打标，写入 manifest 的 `function_label`。

输出：`datasets/skill_mirror/<id>/SKILL.md`。默认被 `.gitignore` 忽略；若要随仓库提供下载，请去掉对应 ignore 规则或 `git add -f datasets/skill_mirror`。

大体积整包更适合放到 **GitHub Releases**，门户「下载数据集」按钮导出的是元数据 zip（manifest + datasheet）。

### 同步到 GitHub

门户数据（manifest、`skill_mirror`、上传目录）可推送到 GitHub，供他人 clone 后直接使用。

**首次同步（本机已有约 8498 条 skill 镜像，约 90MB）：**

1. 在 GitHub 新建空仓库（例如 `security-detection`）
2. 复制 `.env.example` 为 `.env` 并填写：

```bash
GITHUB_REPO=https://github.com/你的用户名/security-detection.git
GITHUB_TOKEN=ghp_你的Personal_Access_Token
```

3. 执行：

```bash
python scripts/sync_to_github.py --message "chore: initial skill dataset sync"
```

**说明：** GitHub 已不支持用账号密码推送，请使用 [Personal Access Token](https://github.com/settings/tokens)（勾选 `repo` 权限）。

**以后上传自动同步：** 在 `.env` 中增加 `GITHUB_AUTO_PUSH=1`，门户上传 skill 后会后台 commit + push。

**手动同步：**

```bash
python scripts/sync_to_github.py --message "chore: sync skills"
```

仅提交不推送：`python scripts/sync_to_github.py --no-push`

### API 摘要

| 方法 | 路径 | 说明 |
|---|---|---|
| GET | `/api/stats` | 汇总 |
| GET | `/api/skills` | 分页列表（`q/label/source/function/gold_status`） |
| GET | `/api/skill?id=` | 详情 + SKILL.md |
| GET | `/api/skill-download?id=` | 单条 zip（镜像优先） |
| GET | `/api/skill-related?id=` | 相关 skill（启发式占位） |
| GET | `/api/dataset/download` | 数据集元数据 zip |
| POST | `/api/skills/upload` | 上传 |

恶意样本仅供研究检测，门户不提供在线执行。

## 说明

- 其余样本仍为 `pending_reannotation` / `benchmark_label`
- ClawHub 技能路径指向 `E:\clawhub_datasets\<slug>`
- MalSkillBench 路径指向 `external\MalSkillBench-main\Dataset\Skills\malware`
- 关联推荐目前按功能类 / 标签启发式；后续可替换为检索类 skill
