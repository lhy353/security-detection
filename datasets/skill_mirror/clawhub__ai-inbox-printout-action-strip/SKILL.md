---
name: ai-inbox-printout-action-strip
displayName: "AI Inbox Printout Action Strip"
version: "1.0.0"
description: "Create a one-page printable action strip for printed email, AI notes, and desk inbox pages using short labels, physical placement cues, and done boxes without exposing sensitive details."
triggerKeywords:
  - aiInboxPrintoutActionStrip
  - printoutActionStrip
  - paperInboxCue
  - aiNotePrintout
  - dailyPrintoutClear
  - shortLabelTask
  - doneBoxStrip
  - paperTaskDrift
tags:
  - productivity
  - inbox
  - paper
  - printable
  - workflow
license: "MIT-0"
language: "en"
hasExecutableCode: false
promptOnly: true
execution: "noExec"
---

# AI Inbox Printout Action Strip

## Purpose

Use this prompt-only skill to make a one-page cutout strip that attaches to a printed email, AI summary, meeting note, research note, or desk inbox page. The strip turns a vague printout into a visible next-action cue with a short action label, owner role, due cue, urgency mark, and done box.

This is a physical paper workflow aid only. It is not an email archive, case file, personal data log, legal record, medical record, password note, or task database.

## Safety Boundary

Do not ask for or print sensitive details from the source page. Avoid names, addresses, account numbers, order numbers, health details, legal details, private message content, full email subjects, client names, or confidential project names.

Use short neutral labels such as "reply," "review," "file," "call," "sign," "pay," "scan," "delegate," "waiting," or "archive." If a detail is needed to complete the work, keep it on the original private document or inside the user's trusted task system, not on the visible action strip.

## Core Principles

- Make the next physical action obvious at a glance.
- Use short labels only.
- Keep the strip useful even when the printout is face down or stacked.
- Separate urgency, owner, and done status.
- Give every printout one clear home: act today, waiting, file, scan, shred, or trash.
- Clear the strip daily so paper does not become a second inbox.

## Required Inputs

Ask only for practical workflow details:

- Printout source type: email, AI note, meeting note, web page, receipt, form, or research page.
- Usual paper location: desk tray, clipboard, folder, wall clip, notebook, or bag.
- Allowed short action labels.
- Owner role labels: me, team, admin, finance, household, client, vendor, or waiting.
- Due style: today, this week, date box, no date, or waiting.
- Preferred strip size: margin strip, half-page strips, sticky-note size, or folder tab.
- Daily clear time or reset trigger.

Do not ask for private content, full message text, contact details, account details, project secrets, or anything that should not sit visibly on a desk.

## Workflow

1. **Pick the printout lane.** Decide whether the page belongs in act today, waiting, file, scan, shred, or trash.
2. **Name the next action.** Choose one short label that describes the next physical or administrative move.
3. **Assign the owner role.** Use a neutral role label rather than a full person name when the strip may be visible.
4. **Mark urgency.** Add a simple cue such as today, this week, waiting, or date box.
5. **Attach the strip.** Place it on the top edge, side margin, folder tab, or clipboard line so the action remains visible.
6. **Complete and check.** Mark the done box when the page has been handled.
7. **Clear daily.** Move completed printouts to file, scan, shred, trash, or archive and remove stale strips.

## Output Format

Return a printable action strip sheet with these sections:

1. **Strip Header**
   - Source type
   - Paper location
   - Reset time
   - Privacy line: "Short labels only. No sensitive details."
2. **Action Strip Template**
   - Action label
   - Owner role
   - Due cue
   - Lane: act, waiting, file, scan, shred, trash
   - Done box
3. **Short Label Bank**
   - Reply
   - Review
   - Sign
   - Pay
   - Call
   - Scan
   - File
   - Delegate
   - Waiting
   - Archive
4. **Daily Clear Routine**
   - Gather marked printouts
   - Finish or move each page
   - Check done boxes
   - Remove old strips
   - Leave no loose action strips on the desk
5. **Cut Lines and Placement Notes**
   - Top margin strip
   - Side tab strip
   - Clipboard strip
   - Folder strip

## Quality Bar

A strong result lets the user look at a paper stack and know what to do next without exposing the private content of the printouts. It should be short, printable, desk-safe, and focused on physical action cues.
