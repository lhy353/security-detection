---
name: ai-tone-drift-guard
description: Compare AI-assisted drafts against user-provided voice notes, samples, channel expectations, and audience needs to flag tone drift, produce a one-page tone rules card, and label any synthetic rewrite examples clearly.
---

# AI Tone Drift Guard

## Overview

Use this skill when a user has AI-assisted drafts that sound inconsistent across channels, teammates, campaigns, or versions and needs a practical tone consistency check.

This is a prompt-only editorial skill. It works from user-provided drafts, voice samples, brand notes, channel descriptions, audience context, and goals. It does not impersonate a real person, clone a voice, hide AI assistance, or produce deceptive messages. All generated rewrite examples must be marked as synthetic rewrites for review.

## Trigger

Use this skill when the user asks to:

- Check whether drafts match a known brand, team, project, or personal writing style.
- Compare tone across emails, posts, support replies, landing pages, ads, docs, or internal updates.
- Build a compact tone guide from examples and voice notes.
- Identify where AI copy sounds generic, inconsistent, too formal, too casual, too salesy, too vague, or off-channel.
- Rewrite short samples for consistency while keeping them clearly labeled as generated drafts.

Do not use this skill to impersonate a person, forge authorship, evade disclosure, mimic a private person's exact style, or create messages meant to deceive recipients about who wrote them.

## Intake

Ask for only the material needed to compare tone:

- Draft text to review.
- Target channel, such as email, website, social post, support reply, proposal, documentation, or internal memo.
- Intended audience and relationship to the audience.
- Purpose of the draft and desired user action.
- User-provided voice samples, brand notes, editorial rules, banned phrases, or approved examples.
- Any compliance, accessibility, legal, or localization constraints.
- Whether the user wants a quick drift check, a rewrite table, or a reusable tone card.

If no voice samples exist, say that the tone card will be provisional and based only on the supplied draft and goals.

## Workflow

1. **Collect reference material.** Use only drafts, samples, notes, and audience context supplied by the user unless the user explicitly asks for outside research.
2. **Extract voice markers.** Identify sentence length, directness, warmth, humor, jargon level, formality, evidence style, formatting habits, calls to action, and words to prefer or avoid.
3. **Define channel expectations.** Note how tone should change for the specific channel without losing the core voice.
4. **Flag drift patterns.** Mark places where the draft becomes generic, inconsistent, mismatched to the audience, over-polished, too casual, too promotional, evasive, or unclear.
5. **Separate content issues from tone issues.** Do not disguise weak facts, missing evidence, or risky claims as a tone problem.
6. **Create rewrite examples.** Provide concise before/after rows only when helpful, and label every after version as a synthetic rewrite for user review.
7. **Build the tone rules card.** Summarize durable rules, examples, guardrails, preferred phrases, avoided phrases, and a final pre-send checklist.
8. **End with disclosure and review notes.** Remind the user that synthetic rewrites need human review, factual checking, and any required AI-use disclosure.

## Output Format

Return these sections:

1. **Tone Snapshot**: target channel, audience, intended effect, reference sources supplied, and confidence level.
2. **Voice Markers Found**: concise bullets for rhythm, diction, warmth, authority, evidence, humor, formatting, and calls to action.
3. **Tone Drift Flags**: table or bullets with draft location, issue, why it drifts, and suggested direction.
4. **Before and After Review Table**: original excerpt, drift note, synthetic rewrite for review, and rationale.
5. **One-Page Tone Rules Card**: do, avoid, preferred phrases, banned or risky phrases, channel adjustments, and pre-send checklist.
6. **Human Review Notes**: facts to verify, claims to support, approvals needed, and AI-use disclosure reminder.
7. **Scope Notes**: no impersonation, no hidden authorship, no deceptive voice cloning, and synthetic rewrites are review drafts.

For a short request, provide Tone Snapshot, top drift flags, and a compact Tone Rules Card.

## Drift Categories

Use these categories when useful:

- **Generic AI smoothness**: polished but bland, overbalanced, or cliche-heavy language.
- **Audience mismatch**: too technical, too casual, too formal, too insider, or too promotional.
- **Channel mismatch**: long-form logic in a short social post, sales tone in support, or casual tone in official notice.
- **Voice inconsistency**: sudden shift in warmth, confidence, humor, sentence rhythm, or vocabulary.
- **Evidence gap**: confident claim without support, vague benefit, or unsupported comparison.
- **Trust risk**: manipulative urgency, fake intimacy, exaggerated certainty, or hidden synthetic authorship.

## Rewrite Rules

- Preserve the user's facts, intent, and constraints.
- Improve consistency without pretending to be the original author.
- Mark rewrite examples with: **Synthetic rewrite for review**.
- Do not mimic a private person's exact style or claim the text was written by them.
- Do not remove required legal, safety, sponsorship, or AI-use disclosures.
- If a requested rewrite would deceive, refuse that part and offer an ethical alternative such as a clearly reviewed team voice draft.

## Safety Boundaries

- No impersonation, forged authorship, voice cloning, hidden AI authorship, or deceptive mimicry.
- Do not help users evade moderation, compliance review, audit trails, or disclosure requirements.
- Do not write manipulative, coercive, fraudulent, harassing, or deceptive copy.
- Do not invent brand rules, approvals, facts, testimonials, credentials, or legal claims.
- Synthetic rewrites are draft options for review, not final approved communications.

## Acceptance Criteria

1. Compares drafts against user-provided voice notes, samples, audience needs, and channel expectations.
2. Produces a practical tone drift list and a one-page tone rules card.
3. Labels all generated rewrite examples as synthetic rewrites for review.
4. Separates tone problems from missing facts, weak evidence, risky claims, or approval needs.
5. Refuses impersonation, forged authorship, hidden synthetic authorship, and deceptive mimicry.
6. Requires no code execution, credentials, API access, network access, publishing, or extra files.

## Example Prompts

- "These AI-generated emails sound different from our normal voice. Can you flag the drift?"
- "Turn these examples into a one-page tone rules card."
- "Compare this LinkedIn post to our brand notes and rewrite only the off-tone lines."
- "This support reply sounds too robotic. Make review drafts that still sound honest."
- "Check whether these three campaign blurbs feel like the same team wrote them."
