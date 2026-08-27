"""Rule-based function eight-class classifier for Agent Skills."""

from __future__ import annotations

import re
from dataclasses import dataclass

FUNCTION_LABELS = (
    "Coding",
    "Research",
    "Browser",
    "File-Agent",
    "Communication",
    "Data-Agent",
    "Automation",
    "Other",
)

RULES: dict[str, list[tuple[str, float]]] = {
    "Browser": [
        (r"\bbrowser\b", 4),
        (r"\bplaywright\b|\bpuppeteer\b|\bselenium\b", 5),
        (r"\bcdp\b|chrome profile|browser-use", 4),
        (r"页面点击|浏览器自动化|网页自动化|browser automation", 5),
    ],
    "Communication": [
        (r"\bemail\b|\bmail\b|\bsmtp\b|\bsms\b", 4),
        (r"\btelegram\b|\bdiscord\b|\bslack\b|\bwhatsapp\b|\bfeishu\b|\blark\b", 5),
        (r"微信|飞书|钉钉|邮件|短信|通知推送", 5),
        (r"\ba2a\b.*\bmsg\b|agent.*message|message queue|redis.*message", 4),
        (r"\bsend (a )?notification\b|\bim\b.*\bsend\b", 3),
    ],
    "Data-Agent": [
        (r"\bdatabase\b|\bsql\b|\bpostgres\b|\bmysql\b|\bsqlite\b|\bmongodb\b", 5),
        (r"\brebalanc\w*\b|\bon-chain\b|\bdefi\b|\bdex\b|\bswap\b|\bportfolio\b", 4),
        (r"\bmarket data\b|\bstock quote\b|\bcrypto price\b|\bticker\b", 4),
        (r"\bmetric(s)?\b|\banalytics dashboard\b|\bkpi\b|\btimeseries\b", 3),
        (r"行情|数据库|指标查询|链上|再平衡|数据查询", 5),
        (r"\bexcel\b.*\b(data|query|read)\b|\bspreadsheet\b.*\bdata\b", 3),
    ],
    "File-Agent": [
        (r"\bpdf\b|\bdocx?\b|\bpptx?\b|\bmarkdown file\b", 4),
        (r"\bfile (read|write|convert|process|merge)\b", 4),
        (r"\blocal file\b|\bdocument convert\b|\bocr\b", 4),
        (r"本地文件|文档处理|文件转换|图片识别|图像识别|vision.*image", 5),
        (r"\bstl\b|\b3d print\b|\bblender\b|\bimage edit\b", 3),
    ],
    "Research": [
        (r"\bacademic research\b|\bliterature review\b", 5),
        (r"\barxiv\b|\bpubmed\b|\bsemantic scholar\b", 5),
        (r"\bweb search\b|\bsearch the web\b|\bgoogle search\b", 4),
        (r"\bsummari(z|s)e\b.*\b(article|paper|webpage|url)\b", 4),
        (r"学术|论文|调研|检索|总结网页|文献", 5),
        (r"\binvestigat(e|ion)\b.*\b(topic|market|topic)\b", 3),
    ],
    "Coding": [
        (r"\bcode review\b|\bdebugging\b|\brefactor(ing)?\b", 5),
        (r"\bpull request\b|\bcommit message\b|\bgit diff\b", 4),
        (r"\bunit test\b|\btest suite\b|\blint(ing)?\b", 4),
        (r"\bscaffold\b.*\b(project|repo|app)\b", 4),
        (r"\btypescript\b|\bjavascript dev\b|\brust dev\b", 3),
        (r"\bapi client generator\b|\bcli from openapi\b", 4),
        (r"写代码|调试|代码审查|编程|developer tool", 5),
    ],
    "Automation": [
        (r"\bdeploy(ment)?\b|\bterraform\b|\bansible\b|\bkubernetes\b|\bk8s\b", 5),
        (r"\bdocker\b|\bci/?cd\b|\bpipeline\b|\bhelm\b", 4),
        (r"\bcron\b|\bschedule(d)? job\b|\bcronjob\b", 4),
        (r"\bsystemd\b|\blaunchd\b|\bwatchdog\b|\bdefibrillator\b", 4),
        (r"\bworkflow orchestrat\b|\borchestrat(e|ion)\b", 4),
        (r"\bmonitor(ing)?\b.*\b(service|server|host|uptime|health)\b", 3),
        (r"\bsetup script\b|\bprovision\b|\bone-click setup\b|\binstall\.sh\b", 5),
        (r"部署|运维|定时任务|编排|安装开通|自动化运维", 5),
        (r"integration\. manage data, records, and automate workflows", 6),
        (r"\bauto.?subtitle\b|\bbatch process\b.*\bschedule\b", 2),
    ],
    "Other": [
        (r"\bwallet\b|\bseed phrase\b|\bprivate key\b.*\btransfer\b", 3),
        (r"\bnft\b|\btamagotchi\b|\bvirtual pet\b|\badopt a\b", 4),
        (r"\broleplay\b|\bcharacter dialog\b|\bpersona chat\b", 4),
        (r"\bgame\b|\bchess\b|\bgambling\b", 3),
        (r"\bsecurity audit only\b|\bagentshield audit\b", 2),
    ],
}


@dataclass
class FunctionPrediction:
    label: str
    scores: dict[str, float]
    confidence: float


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "").lower()).strip()


def classify_function(text: str, slug: str = "") -> FunctionPrediction:
    hay = _normalize(f"{slug} {text}")[:12000]
    scores: dict[str, float] = {k: 0.0 for k in FUNCTION_LABELS}

    for label, patterns in RULES.items():
        for pattern, weight in patterns:
            if re.search(pattern, hay, re.IGNORECASE):
                scores[label] += weight

    # De-prioritize Coding for generic integration CLIs
    if re.search(
        r"integration\. manage data|manage data, records, and automate",
        hay,
    ):
        scores["Coding"] -= 3
        scores["Automation"] += 2

    # Research vs Browser
    if scores["Browser"] >= 4 and scores["Research"] >= 4:
        if re.search(r"playwright|puppeteer|click|navigate|screenshot", hay):
            scores["Browser"] += 2
        elif re.search(r"search|summarize|arxiv|paper", hay):
            scores["Research"] += 2

    # Data vs Automation for infra DB tooling
    if re.search(r"\bcloud db\b|\bhealth monitor\b.*\bdb\b", hay):
        scores["Data-Agent"] += 2

    best = max(FUNCTION_LABELS, key=lambda k: scores[k])
    if scores[best] <= 0:
        best = "Other"

    total = sum(max(v, 0) for v in scores.values()) or 1.0
    confidence = max(scores[best], 0) / total
    return FunctionPrediction(label=best, scores=scores, confidence=confidence)
