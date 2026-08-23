---
name: urgent-paperweight-corner-queue-card
displayName: "Urgent Paperweight Corner Queue Card"
version: "1.0.0"
description: "Create a small desk queue card for urgent papers held in one visible corner, limited to task organization with no legal, medical, or financial guidance."
triggerKeywords:
  - urgentPaperweightQueue
  - urgentPaperCornerCard
  - deskPaperQueueCard
  - paperweightTaskStack
  - urgentDocumentCorner
  - actionPaperStackReset
  - paperworkTriageCard
  - todayPaperQueue
tags:
  - paperwork
  - desk
  - organization
  - task-management
  - checklist
license: "MIT-0"
language: "en"
hasExecutableCode: false
promptOnly: true
execution: "noExec"
---

# Urgent Paperweight Corner Queue Card

## Purpose

Use this prompt-only skill when a user has loose papers that need attention today or soon and wants one visible, bounded desk corner for the active paper queue. The deliverable is an urgent paperweight corner queue card: what belongs in the stack, how to sort it by action, how to avoid burying time-sensitive papers, and how to clear or defer items.

This skill is task organization only. It does not provide legal, medical, financial, tax, insurance, benefits, compliance, regulatory, or professional advice. It does not interpret documents or decide what the user should sign, pay, dispute, submit, diagnose, treat, file, or legally respond to.

## Safety Boundary

Keep the scope to paper handling and task tracking: identify the next administrative action, owner, due date supplied by the user, and where the paper goes next. Do not analyze rights, obligations, diagnoses, treatment options, legal strategy, financial choices, investment decisions, debt decisions, tax positions, insurance coverage, or official form correctness.

If papers involve legal, medical, financial, tax, insurance, benefits, immigration, court, debt, or official compliance matters, tell the user to consult the relevant qualified professional, official source, or issuing organization for substance. You may still help create a neutral task queue such as "call issuer," "collect missing document," "schedule appointment," or "ask professional."

Do not request private account numbers, full IDs, medical details, legal facts, financial balances, or confidential client information. Use neutral paper labels.

## Use This Skill When

Use this skill when the user wants to:

- Create one visible place for urgent papers instead of many piles.
- Separate today, waiting, and later papers.
- Add action labels without reading sensitive contents.
- Make a short daily reset for loose desk documents.
- Prevent new papers from burying urgent ones.
- Track who owns the next step and when to review the stack.

Do not use this skill for legal advice, medical advice, financial advice, tax advice, benefits decisions, insurance interpretation, debt strategy, official deadline calculation, document drafting, or form correctness review.

## Best Inputs

Ask for practical, non-sensitive details:

- Number of loose papers or approximate stack height.
- Paper categories using neutral labels: bill notice, school form, appointment sheet, receipt, permission slip, manual, invoice, reminder, application, mail, or reference.
- User-provided due dates or target dates, if already known.
- Next action type: sign, call, email, scan, file, pay, ask, read, bring, mail, shred later, recycle, or delegate.
- Queue size limit: three papers, five papers, one day's work, one paperweight footprint, or custom limit.
- Review rhythm: morning, end of day, before leaving, weekly admin hour, or after mail pickup.
- Where completed or waiting papers go: outbox, folder, scan pile, calendar reminder, bag, file tray, or archive.

Do not ask for document contents beyond the minimum neutral label needed to organize the task.

## Workflow

1. **Define the corner.** Name the user-chosen visible desk corner or paper zone without giving mounting, furniture, or safety guarantees.
2. **Set entry rules.** Only papers with a near-term next action enter the urgent queue.
3. **Create neutral labels.** Label papers by task, not sensitive content.
4. **Sort by action.** Group papers into today, next, waiting, ask someone, and file or remove.
5. **Apply a size limit.** Keep the urgent stack small enough to review quickly; overflow becomes a separate later stack or inbox.
6. **Add review rhythm.** Define when the user checks the queue and what counts as done.
7. **Create escalation prompts.** For legal, medical, financial, tax, insurance, benefits, or official matters, the next task is to contact the right professional or source, not to decide substance here.
8. **Produce the queue card.** Make a compact card that sits near the stack and guides daily reset.

## Output Format

Return the result in this order:

1. **Scope Note**
   - Task organization only
   - No legal, medical, financial, tax, insurance, benefits, or compliance guidance
   - Sensitive matters should be handled with qualified professionals, official sources, or issuing organizations

2. **Queue Setup**
   - User-chosen corner or zone name
   - Queue size limit
   - Paperweight or visible marker role, described only as a reminder to keep the stack bounded
   - Review rhythm
   - Where overflow goes

3. **Paper Triage List**
   - Neutral paper label
   - Next action
   - User-provided due or target date
   - Owner role
   - Status: today, next, waiting, ask professional or issuer, file, remove, or later

4. **Action Buckets**
   - Today: papers requiring the next ordinary task
   - Waiting: papers paused until a reply, appointment, or missing item
   - Ask: papers needing a professional, official source, or issuer
   - File or remove: papers no longer urgent
   - Later: papers that do not belong under the urgent paperweight

5. **Daily Reset Routine**
   - Review the top paper
   - Do or schedule the next action
   - Move completed papers out of the urgent corner
   - Keep private details off visible labels
   - Rebuild the stack by status and due date supplied by the user

6. **Printable Corner Queue Card**
   - Title
   - Entry rule
   - Size limit
   - Status words
   - Review time
   - Scope line: "Task organization only; ask qualified sources for legal, medical, or financial substance."

7. **Do-Not-Do List**
   - Do not interpret legal documents
   - Do not advise medical decisions
   - Do not advise financial, tax, debt, insurance, or benefits decisions
   - Do not put account numbers, full IDs, diagnoses, case details, balances, or confidential data on visible labels

## Style Guidelines

- Keep labels neutral and short.
- Focus on next physical or administrative action.
- Use user-provided due dates only; do not calculate official deadlines.
- Prefer "ask the issuer" or "ask a qualified professional" for substantive questions.
- Make the queue small enough to clear, not another archive pile.

## Quality Bar

A strong result lets the user turn a messy urgent paper pile into a bounded desk queue with clear next actions, review rhythm, and safe boundaries. It should help the user move paper without interpreting sensitive documents or giving legal, medical, or financial guidance.
