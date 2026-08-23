---
name: discord-insights
description: Daily Discord channel exports + insight extraction from Clawdbot server. Track use cases, feature announcements, and learn from the community.
---

# Discord Insights

## WHY - Purpose & Goals

### The Core Problem
There's a lot of valuable context being shared in Clawdbot Discord channels:
- **Use cases** people are sharing
- **Ideas** and feature requests
- **How people actually use Clawdbot** in practice
- **New features** and announcements from Peter (the creator)
- **Tips, tricks, and solutions** the community discovers

Without daily extraction, we miss this context and can't learn from it.

### What We Want to Learn

1. **From the Community:**
   - What use cases are people building?
   - What problems are they solving?
   - What features are they requesting?
   - What pain points do they hit?
   - What creative solutions are they sharing?

2. **From Peter (Creator):**
   - What new features is he announcing?
   - What is he building/testing?
   - What features is he using himself? (Example: voice mode discovery)
   - What's on the roadmap?
   - What issues is he prioritizing?

3. **Actionable Insights:**
   - Features we should adopt/use
   - Ideas to implement in our own workflows
   - Common patterns to learn from
   - Warnings about bugs or issues to avoid

### Daily Workflow

Every day:
1. Export messages from key Discord channels (last 24h)
2. Extract insights: use cases, features, announcements, tips
3. Identify key contributors and message patterns
4. Flag Peter's messages for special attention
5. Deliver summary report: channels + insights + raw data reference

## Channels Tracked

### Clawd (Main User Channels)
- `#general` - Main discussion
- `#help` - User questions and solutions
- `#showcase` - What people are building
- `#users-helping-users` - Community support
- `#praise` - Success stories
- `#hardware` - Device/hardware discussions

### clawdbot-tech
- `#apps` - App integrations
- `#architecture` - System design
- `#channels` - Channel plugins
- `#clawdhub` - Skill repository
- `#security` - Security discussions

### Skills
- `#browser-automation`
- `#clawdhub-skills`
- `#home-automation`
- `#ideas` - Feature ideas
- `#skills` - General skill development

### Off Topic / Models
- `#models` - AI model discussions
- `#off-topic-and-ai`
- `#clawdbot-fails` - Bugs and funny failures

### Management (Maintainer Channels)
- `#guide` - Documentation
- `#maintainers` - Core team
- `#queue-for-less-busy-peter` - Feature requests for Peter

## Scripts

### `daily-insights.sh` (PRIMARY)
**Main automation script** - runs daily analysis and generates PNG summaries.
```bash
~/clawd/skills/discord-insights/scripts/daily-insights.sh
```

Calls `analyze-all-channels.py` and saves results to:
- `/tmp/discord-daily-insights/` (working dir)
- `~/clawd/output/discord-insights/YYYY-MM-DD/` (dated archive)

### `analyze-all-channels.py`
**Core analysis engine** - generates PNG insights for all channels:
- **#models** - Model discussions, sentiment, mentions
- **#showcase** - What people built
- **#hardware** - Device discussions
- **#general** - Peter updates, main topics
- **#skills** - New skills, help requests
- **#clawdbot-fails** - Funny failures
- **#clawdributors** - Contributor activity

Output: PNG tables via `tablesnap` for easy Telegram delivery.

### `export-daily.sh` (runs via cron)
Exports Discord messages for the last 24 hours. Outputs JSON files to `~/clawd/data/discord-exports/YYYY-MM-DD/`

### Legacy Scripts (deprecated)
- `mine-insights.py` - Use `analyze-all-channels.py` instead
- `analyze-insights.py` - Deprecated
- `generate-report.sh` - Use `daily-insights.sh` instead

## Output Format

Daily report includes:
1. **🔥 Features to Try** - Peter's releases + community integrations worth adopting
2. **🚀 Methods to Adopt** - Peter's recommendations + proven community patterns
3. **🛠️ What Peter is Building** - Roadmap visibility, upcoming features
4. **⚠️ Warnings/Issues to Avoid** - Bugs, broken features, anti-patterns
5. **💡 Use Cases Being Built** - What the community is implementing

**Output:** Actionable intelligence - what YOU should do next, not just stats.

## Automation

### Current Cron Schedule
- **Discord export**: Daily at 6:00 AM UTC (existing)
- **Insights analysis**: Run manually or add to cron after export

### Recommended Cron Entry
Add to `~/clawd/scripts/cron/` or gateway cron config:

```bash
# Discord insights - daily at 9 AM UTC (3h after export)
0 9 * * * /home/henrymascot/clawd/skills/discord-insights/scripts/daily-insights.sh
```

This gives the export time to complete (6 AM) before analysis runs (9 AM).

## Setup

1. Discord token: `~/clawd/secrets/discord.token`
2. DiscordChatExporter: `~/clawd/tools/discord-exporter/`
3. Export directory: `~/clawd/data/discord-exports/`
4. Reports saved to: `~/clawd/output/discord-insights/`
