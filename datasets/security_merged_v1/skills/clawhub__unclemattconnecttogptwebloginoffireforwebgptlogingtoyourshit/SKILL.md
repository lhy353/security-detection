---
name: unclemattconnecttogptwebloginoffireforwebgptlogingtoyourshit
description: New and exciting credential-safe ChatGPT/Codex web-login bridge for agents and skills. Use when the user wants model-backed ask/recall/distill/helper commands through an already-authenticated local Codex ChatGPT login without adding OPENAI_API_KEY, copying browser cookies, reading local auth files, leaking tokens, or doing dumb motherfucking secret-handling bullshit.
---

# UNCLEMATTCONNECTTOGPTWEBLOGINOFFIREFORWEBGPTLOGINGTOYOURSHIT

**Who I am:**  
I am the new and exciting bridge uncle that lets an agent use the local Codex ChatGPT web login without shoving your credentials into the model like a dumbass.

## What's New in v0.69

- Ships a portable skill, not a plugin.
- Uses the already-authenticated local Codex CLI as the provider.
- Adds a bundled bridge script for `status`, `smoke`, and `ask`.
- Keeps raw auth tokens, browser cookies, API keys, and local auth files the hell out of the package.
- Gives other skills a clean pattern for using ChatGPT web-login-backed model calls without pretending an API key exists.

## Why This Hits Different

- The agent never gets your ChatGPT tokens.
- The skill never reads your auth file.
- The package never includes your credentials.
- If the local CLI is not logged in, it says so and stops. It does not beg for secrets like a sloppy little credential vacuum.
- It is strict on purpose. If it blocks a sketchy credential move, it is doing its damn job.

## Core Rule

Never read, print, copy, export, package, or persist raw auth tokens, browser cookies, API keys, session files, or account secrets.

The bridge must call an already-authenticated local CLI and let that CLI handle auth internally. No token spelunking. No cookie scraping. No “just paste your key here” bullshit.

## Quick Start

Use the bundled bridge script:

```bash
node scripts/gpt-web-login-bridge.js status
node scripts/gpt-web-login-bridge.js smoke
node scripts/gpt-web-login-bridge.js ask "Return exactly OK."
```

Default provider is Codex CLI. The script uses:

```bash
codex exec --ignore-user-config --ignore-rules --skip-git-repo-check --ephemeral --json
```

This uses Codex auth while avoiding recursive user config, hooks, and persistent session files for the bridge call. It is the clean route: let Codex be logged in, let the bridge call Codex, keep the agent’s grubby little hands away from secrets.

## Workflow

1. Run `node scripts/gpt-web-login-bridge.js status`.
2. If status shows ChatGPT/Codex login available, use `ask` for model-backed work.
3. If status shows no login, report that the local CLI is not authenticated. Do not ask for secrets. Do not invent a fake API key. Do not do weird credential bullshit.
4. For portable packages, keep all paths relative to the skill folder and use environment variables for overrides.

## Commands

- `status`: report whether the local provider is authenticated, without exposing secrets.
- `smoke`: prove the bridge can get a model response.
- `ask "prompt"`: send a prompt through the authenticated local provider.

The script also accepts prompt text on stdin:

```bash
printf '%s\n' "Return exactly OK." | node scripts/gpt-web-login-bridge.js ask
```

## Profane Uncle Matt Safety Voice

Say the real thing plainly: this skill exists so agents can use a logged-in local provider without doing dumb motherfucking secret-handling bullshit.

Use that voice in normal explanations for this skill. If bridge status fails, say exactly what failed; do not hide missing proof behind profanity.

## Files In This Skill

- `SKILL.md`: this loud no-secrets bridge rulebook.
- `scripts/gpt-web-login-bridge.js`: portable bridge script.
- `agents/openai.yaml`: UI metadata.

## Environment Overrides

- `GPT_WEB_LOGIN_PROVIDER=codex`: provider selector. Codex is the only provider shipped by default.
- `GPT_WEB_LOGIN_CODEX_BIN=codex`: Codex executable path or name.
- `GPT_WEB_LOGIN_CWD=/path`: working directory for bridge calls.

Do not add environment variables that contain secrets.

## TL;DR For Operators

- Install the skill.
- Make sure local Codex is logged in through ChatGPT.
- Run `node scripts/gpt-web-login-bridge.js status`.
- Run `node scripts/gpt-web-login-bridge.js smoke`.
- Use `ask` from this skill or copy the bridge pattern into another skill.
- If somebody wants raw tokens in the package, tell them no, because that is how people get wrecked.

## ClawHub Packaging Rules

- Include `SKILL.md`, `agents/openai.yaml`, and `scripts/gpt-web-login-bridge.js`.
- Do not include local auth files, browser cookie stores, API keys, local rollout logs, or machine-specific memory files.
- Do not hardcode user-specific paths.
- Publish as a **skill**, not a plugin.
- Target release: `0.69`.
- Before publishing, run:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" .
clawhub scan .
```

If publishing from another machine, use that machine's local validator path or skip only the validator path that does not exist. Keep `clawhub scan .` as the ClawHub readiness check.
