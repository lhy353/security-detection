---
name: AI Repetitive Task Finder
description: Map repeated weekly computer work into a one-page repeat-task board and identify the top three safe AI-assist candidates without building live automation.
version: "1.0.0"
type: prompt-flow
tags:
  - ai-productivity
  - repetitive-tasks
  - workflow-mapping
  - automation-planning
  - time-savings
author: Bell (design)
---

# AI Repetitive Task Finder

## Overview

AI Repetitive Task Finder helps a user who keeps losing time to the same computer tasks each week. It turns vague frustration into a one-page repeat-task map: what repeats, how often it happens, what inputs it needs, where AI might help, and which three candidates are safest to test first.

This skill is for task discovery and planning only. It does not create live automations, connect to accounts, process private files, or run scripts. Any task involving private data, external messages, payments, account changes, or irreversible actions must be reviewed by the user before any later implementation.

## When to Use

Use this skill when the user says things like:

- "I do the same computer task every week."
- "I want AI to save me time but do not know where to start."
- "I keep copying information between apps manually."
- "Can this recurring admin work be automated?"
- "Help me find the best first AI workflow to try."

## Workflow

### Step 1 - List the Repeats

Ask the user to name recurring computer tasks from the last two to four weeks. Keep the prompt lightweight so they do not need a perfect inventory.

Capture each repeat as:

- Task name
- Where it happens, such as email, spreadsheets, documents, browser, chat, CRM, calendar, or file folders
- Who receives the output, if anyone
- Current time spent per occurrence
- Frequency per week or month
- Pain point, such as boring, error-prone, slow, hard to start, or easy to forget

If the user is stuck, offer categories:

- Copying or reformatting text
- Summarizing documents, threads, or notes
- Drafting routine replies
- Updating trackers
- Renaming or organizing files
- Checking websites or dashboards
- Preparing meeting notes or follow-ups
- Turning raw notes into a finished format

### Step 2 - Score Frequency and Friction

Create a simple score for each repeated task:

- Frequency: 1 = monthly, 2 = weekly, 3 = several times weekly, 4 = daily
- Time cost: 1 = under 10 minutes, 2 = 10-30 minutes, 3 = 30-60 minutes, 4 = over 60 minutes
- Error risk: 1 = low, 2 = medium, 3 = high
- Annoyance: 1 = mild, 2 = moderate, 3 = strong
- Safety caution: 0 = low risk, -2 = private data or external action, -4 = payments, legal, medical, employment, or irreversible change

Rank candidates by total score, but do not let a high score override safety caution.

### Step 3 - Capture Inputs and Outputs

For the leading candidates, map the work in plain language:

- Inputs: what the user starts with
- Decisions: what judgment the user applies
- Output: what must be produced
- Quality checks: what makes the output acceptable
- Data sensitivity: public, internal, personal, confidential, financial, health, legal, or account-related
- Human approval point: where the user must review before anything is sent, saved, or changed

Keep this as a planning artifact, not an implementation spec with credentials or private data.

### Step 4 - Sketch Possible AI Assistance

For each candidate, identify the safest AI-assist pattern:

- Draft: AI creates a first draft for human review
- Summarize: AI condenses source material
- Extract: AI pulls fields into a structured checklist
- Compare: AI highlights changes, mismatches, or options
- Transform: AI rewrites or reformats existing text
- Checklist: AI generates a repeatable quality-control list
- Reminder script: AI helps the user remember steps, without executing them

Mark boundaries clearly:

- Human reviews before sending or publishing
- No private files pasted unless the user approves
- No account actions, purchases, deletions, or external messages
- No hidden background automation

### Step 5 - Select the Top Three Automation Candidates

Choose the top three candidates using this priority order:

1. High frequency and high time cost
2. Clear inputs and outputs
3. Low privacy or external-action risk
4. Easy to test in under 20 minutes
5. Human review can catch mistakes before harm

For each top candidate, provide:

- Why it is a good candidate
- What AI could assist with
- What must remain human-reviewed
- First tiny test
- Success measure
- Risk flag, if any

### Step 6 - Make the First Tiny Test

Design a tiny test that can be done safely without live automation. Examples:

- Use one sanitized sample paragraph to test a rewrite prompt
- Turn one fake invoice line into a sample tracker row
- Summarize one non-sensitive meeting note
- Draft a template response without sending it
- Compare two made-up examples to test the desired output shape

The test should answer: "Is this workflow worth building further?"

## Output Format

Produce a one-page repeat-task map:

```text
AI Repetitive Task Finder

Goal:
- What the user wants to save time on:

Repeat Task Inventory:
| Task | Frequency | Time Cost | Friction | Inputs | Output | Safety Caution | Score |

Top 3 AI-Assist Candidates:
1. Candidate:
   - Why this one:
   - AI assist pattern:
   - Human review point:
   - First tiny test:
   - Success measure:
   - Risk flag:

2. Candidate:
   - Why this one:
   - AI assist pattern:
   - Human review point:
   - First tiny test:
   - Success measure:
   - Risk flag:

3. Candidate:
   - Why this one:
   - AI assist pattern:
   - Human review point:
   - First tiny test:
   - Success measure:
   - Risk flag:

Do Not Automate Yet:
- Tasks blocked by private data, account access, irreversible action, external sending, or unclear quality checks.

Next Safe Step:
- One tiny test the user can run manually before building anything live.
```

## Safety Boundaries

- Planning only; do not build, run, or connect automation.
- Do not request credentials, API keys, private documents, or account access.
- Do not handle live personal, financial, health, legal, employment, or confidential data unless the user explicitly approves a safe review process.
- Do not send messages, update records, make purchases, delete files, or change accounts.
- If a candidate affects other people or external systems, require human review before action.
- Use sanitized or fictional samples for the first tiny test when possible.

## Acceptance Criteria

1. The response inventories recurring computer tasks instead of jumping to tools.
2. Frequency, time cost, friction, inputs, outputs, and safety caution are captured.
3. The top three candidates are selected with clear reasoning.
4. Each candidate includes an AI-assist pattern, human review point, first tiny test, and success measure.
5. The output stays at discovery/planning level and does not implement live automation.
6. Private data handling, credentials, external sending, and irreversible actions are explicitly avoided or gated by review.

## Example Prompts

- "I do the same computer tasks every week and I'm losing hours. Help me find which ones AI could safely assist with."
- "Identify three repetitive tasks in my workflow that are safe to start testing with AI."
- "I keep copying data between spreadsheets and emails every Friday. Map my repeats and find the top AI candidate."

## Example

**User says:** "Every Friday I spend an hour turning notes from three calls into a client update email. I also copy numbers into a spreadsheet and rename files."

**Skill output:** Builds a repeat-task inventory, scores all three tasks, selects the client update draft, spreadsheet row extraction, and file naming checklist as possible candidates, then proposes one tiny test using sanitized notes to draft a non-sent update for review.
