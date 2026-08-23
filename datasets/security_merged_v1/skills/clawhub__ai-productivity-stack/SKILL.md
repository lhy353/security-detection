---
name: AI Productivity Stack
description: Design a personal AI-enhanced workflow that saves time without creating tech debt.
version: "1.0.0"
type: prompt-flow
tags:
  - ai-productivity
  - workflow-design
  - productivity-system
  - automation
  - time-management
  - ai-tools
author: Bell (design)
---

# AI Productivity Stack

## Overview

AI Productivity Stack is a workflow design workshop that helps users build a personal AI-enhanced productivity system. It guides users through auditing their current tasks, identifying where AI adds genuine value, and constructing a stack for email, writing, research, scheduling, and task management — with "human-in-the-loop" checkpoints to prevent over-automation.

This skill focuses on personal productivity, not automating away jobs or responsibilities that require human judgment.

## When to Use

Use this skill when the user asks to:

- Use AI for productivity
- Build an AI workflow
- Automate tasks with AI
- Find AI tools for getting things done
- Work faster with AI

**Trigger phrases:** "AI for productivity", "Build an AI workflow", "Automate with AI", "AI tools for getting things done", "Work faster with AI"

## Workflow

### Step 1 — Greet and Assess

Acknowledge the user's productivity goals. Ask:
- What does a typical workday or week look like?
- What tools do they currently use?
- What are their biggest productivity pain points? (email overload, writer's block, research time, meeting prep, task prioritization)
- How comfortable are they with trying new tools?

### Step 2 — Task Audit

Guide the user through listing their regular tasks. For each task, assess:
- **Frequency:** How often does it occur?
- **Time consumed:** How long does it take?
- **Cognitive load:** Is it draining or mechanical?
- **AI fit:** Could AI help? (high/medium/low/none)

Categorize tasks into:
- **High AI fit:** Drafting, summarizing, brainstorming, formatting, transcribing
- **Medium AI fit:** Research, scheduling, note organization, first-pass editing
- **Low/none AI fit:** Final decision-making, sensitive communication, creative direction, relationship building

### Step 3 — Design the AI Touchpoints

For high and medium-fit tasks, design specific AI touchpoints:

**Email:**
- AI drafts responses to routine emails
- Human reviews, personalizes, and sends
- Never AI-send without human review for important communications

**Writing:**
- AI generates outlines and first drafts
- Human provides voice, examples, and final polish
- AI helps with editing and clarity, not authorship

**Research:**
- AI summarizes long articles and reports
- Human verifies key facts and reads primary sources for critical decisions
- AI generates questions to guide deeper reading

**Scheduling and Task Management:**
- AI suggests time blocks based on priorities
- Human approves and adjusts
- AI generates meeting agendas; human owns the outcomes

### Step 4 — Build the Stack

Recommend a lightweight, integrated stack based on the user's tools and comfort level:
- **Minimal stack:** One AI chatbot + existing tools (lowest friction)
- **Balanced stack:** AI chatbot + one specialized tool (e.g., meeting transcriber, research assistant)
- **Advanced stack:** Multiple AI tools with clear role separation

Emphasize: start with the minimal stack. Add tools only when a clear gap exists.

### Step 5 — Human-in-the-Loop Checkpoints

Establish rules for when the human must be involved:
- **Never fully automate:** Sensitive emails, performance reviews, conflict resolution, any communication with emotional weight
- **Always review:** Anything sent externally, factual claims, data analysis
- **Human owns:** Final decisions, creative direction, relationship management

Create a personal "AI boundary list" — tasks the user decides AI will never touch.

### Step 6 — Summarize and Exit

Recap the user's personalized productivity audit and recommended stack. Provide:
- A staged implementation plan (start with highest-impact, lowest-risk change)
- A reminder to review the stack after 2-4 weeks of use
- Suggest related skills: Prompt Library Builder for reusable productivity prompts, AI Decision Framework for prioritization

## Safety & Compliance

- Focuses on personal productivity, not automating away jobs or responsibilities
- Does not encourage AI use where human judgment is critical (e.g., final editing of important communications)
- Does not recommend tools that violate platform terms of service
- Emphasizes human-in-the-loop for all external-facing work
- This is a descriptive prompt-flow skill with zero code execution, zero network calls, and zero credential requirements

## Acceptance Criteria

1. User describes their work/tasks; output includes a task-by-task AI fit assessment
2. A recommended stack is provided at an appropriate complexity level for the user
3. Human-in-the-loop checkpoints are explicitly defined
4. A staged implementation plan is provided
5. Does not recommend fully automating sensitive or relationship-critical tasks

## Examples

### Example 1: Knowledge Worker

**User says:** "I spend too much time on email and meeting notes. How can AI help?"

**Skill guides:** Audit typical week. Identify high-fit tasks (email drafting, meeting summarization). Design touchpoints: AI drafts, human reviews. Recommend minimal stack: AI chatbot for drafting + existing note app. Set boundary: human reviews all external emails. Provide staged plan: week 1 — email drafting; week 2 — meeting notes; week 3 — review and adjust.

### Example 2: Freelancer Overwhelmed by Admin

**User says:** "I'm a freelancer drowning in admin tasks. Can AI save me?"

**Skill guides:** List admin tasks (invoicing, client communication, scheduling, proposal writing). Assess AI fit for each. Design touchpoints: AI drafts proposals from templates, AI suggests schedule blocks, AI generates invoice reminders. Emphasize: client relationships stay human. Recommend balanced stack. Create boundary list.
