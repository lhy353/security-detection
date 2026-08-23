---
name: auto-insight-engine
description: 自主洞察引擎 — 从6个来源采集洞察：HackerNews/GitHub/Wikipedia/RSS/ArXiv/扩展搜索，NVIDIA NIM深度分析，趋势跟踪
metadata: {"openclaw": {"requires": {"bins": ["python"]}, "install": []}}
tags: [insight, intelligence, trend, analysis, learning, automation]
version: 1.0.0
author: laosi
source: adapted
---

# Auto Insight Engine - 自主洞察引擎

> 激活词: 洞察引擎 / insight engine / 采集洞察 / collect insights

## 功能
- 6个数据来源：HackerNews 15条 + GitHub Trending 8条 + Wikipedia 5条 + RSS订阅4源20条 + ArXiv API + 扩展搜索
- 每周期约48条原始洞察
- NVIDIA NIM每周期5条深度分析
- 趋势关键词跟踪 + 上升趋势检测
- 6阶段引擎闭环

## 命令

### 执行采集
```bash
python -c "from auto_insight_engine import run_cycle; run_cycle()"
```

### 查看状态
```bash
python -c "from auto_insight_engine import get_status; print(get_status())"
```

## 依赖
- Python 3.10+
- NVIDIA NIM API (可选, 用于深度分析)
- requests, feedparser, arxiv
