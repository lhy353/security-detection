---
name: desk-paper-inbox-routing-labels
displayName: "Desk Paper Inbox Routing Labels"
version: "1.0.0"
description: "Create printable routing labels, folder tabs, deadline flags, receipt pocket labels, and a short reset checklist for a messy desk paper inbox without giving tax, legal, financial, medical, or records-retention advice."
triggerKeywords:
  - deskPaperInboxLabels
  - paperInboxRoutingLabels
  - deskPaperSorter
  - mailRoutingLabels
  - paperworkTrayOrganizer
  - billFolderLabels
  - homeAdminInbox
  - receiptPocketLabels
tags:
  - paperwork
  - homeAdmin
  - organization
  - labels
  - checklist
license: "MIT-0"
language: "en"
hasExecutableCode: false
promptOnly: true
execution: "noExec"
---

# Desk Paper Inbox Routing Labels

## Purpose

Use this prompt-only skill when a user has bills, forms, receipts, school papers, medical papers, notes, manuals, mail, or other loose paperwork stacked on a desk and needs visible routing labels before deadlines or documents are missed.

The deliverable is a printable desk paper inbox routing kit: tray labels, folder tabs, action lane cards, date-needed flags, receipt pocket labels, and a 20-minute reset checklist.

This skill creates practical labels and sorting prompts only. It does not provide tax, legal, financial, medical, or records-retention advice.

## Safety Boundary

Do not request or print sensitive numbers, full IDs, account numbers, medical details, legal case details, financial balances, tax identifiers, passwords, credentials, full addresses, or other private data on visible labels.

Do not decide official deadlines, retention periods, legal obligations, tax treatment, medical record handling, financial priorities, or document disposal rules. Tell the user to verify official deadlines, retention rules, and sensitive handling requirements with the appropriate source.

Use neutral visible labels such as "pay," "sign," "scan," "file," "shred review," "return," "discuss," "wait," "archive," "school," "health," "home," "car," "receipts," and "warranties."

## Use This Skill When

Use this skill when the user wants to:

- Turn a desk paper pile into action lanes.
- Create labels for trays, folders, wall pockets, binders, envelopes, or a file box.
- Mark due dates and next actions without exposing private details.
- Separate receipts for return, reimbursement, warranty, tax review, or short-term keeping.
- Do a quick paper inbox reset without redesigning a full filing system.

Do not use this skill for official filing advice, tax planning, legal document strategy, medical record management, financial prioritization, compliance labeling, or document destruction decisions.

## Best Inputs

Ask for non-sensitive details:

- Paper types currently piling up, such as bills, mail, receipts, forms, school papers, medical papers, tax notes, manuals, notes, warranties, or sentimental papers.
- Where papers will be routed, such as trays, folders, binders, wall pockets, envelopes, a file box, or one desk zone.
- People or roles involved, using neutral labels like adult, child, household, office, client public, teacher, or provider.
- Near-term date pressure, using month and day only if that is enough.
- Preferred label size, color grouping, or print format.

Avoid asking for account numbers, balances, private diagnoses, legal facts, student IDs, full names when not needed, or confidential document contents.

## Workflow

1. Inventory the pile by paper type and current location.
2. Choose the physical routing setup: tray, folder, binder, wall pocket, envelope, file box, or desk zone.
3. Create action lane labels for pay, sign, scan, file, shred review, return, discuss, wait, and archive.
4. Generate folder tabs for recurring categories such as bills, school, health, home, car, finance, receipts, warranties, and personal records.
5. Build date-needed flags with due date, owner or role, next action, source, and final destination.
6. Add receipt pocket labels for reimburse, return, warranty, tax review, and keep short term.
7. Add a privacy pass that removes sensitive numbers and private facts from visible labels.
8. Provide a 20-minute reset checklist focused on the top layer, deadline items, and an uncertain-paper review lane.

## Output Format

Return the result in this order:

1. **Scope Note**
   - Paper routing labels only
   - No sensitive numbers or private facts on visible labels
   - Verify official deadlines, retention rules, and disposal requirements separately

2. **Paper Type Inventory**
   - Paper type
   - Current pile location
   - Next action
   - Destination
   - Date pressure, if known

3. **Action Lane Cards**
   - Label text
   - What belongs here
   - What does not belong here
   - Review cue

4. **Folder Tab Set**
   - Tab name
   - Example contents
   - Safe visible wording
   - Private details to omit

5. **Date-Needed Flags**
   - Due date or review date
   - Owner or role
   - Next action
   - Source
   - Final copy destination

6. **Receipt Pocket Labels**
   - Reimburse
   - Return
   - Warranty
   - Tax review
   - Keep short term

7. **20-Minute Desk Paper Reset**
   - Clear one work surface
   - Pull urgent dates forward
   - Sort only the top layer first
   - Put uncertain papers in review
   - Stop before creating new piles
   - Schedule the next review

## Style Guidelines

- Keep label text short enough to read at a glance.
- Prefer action verbs over vague category names.
- Use neutral owner roles instead of private names when the station is shared.
- Include a review lane for papers the user cannot decide on quickly.
- Keep the system printable, visible, and easy to reset.

## Quality Bar

A strong result lets the user route a messy desk paper pile today, with clear next actions and safer visible wording. It should reduce missed papers without pretending to be a full records, tax, legal, medical, or financial system.
