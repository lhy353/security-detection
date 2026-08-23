---
name: sticky-note-pad-backing-card
displayName: "Sticky Note Pad Backing Card"
version: "1.0.0"
description: "Create a paper-only mini backing-card label for sticky note pad support, size, desk location, refill cues, and low-pad review without adhesive, blade, repair, medical, or exercise guidance."
triggerKeywords:
  - stickyNoteBacking
  - notePadSupport
  - backingCardLabel
  - deskNotePad
  - padRefillCue
  - paperBackingCard
  - notePadOrganizer
  - stickyPadCard
tags:
  - desk
  - paper
  - organization
  - office
  - checklist
license: "MIT-0"
language: "en"
hasExecutableCode: false
promptOnly: true
execution: "noExec"
---

# Sticky Note Pad Backing Card

## Purpose

Use this prompt-only skill when a sticky note pad has lost its stiff backer, curls in a drawer, scatters on a desk, or becomes hard to find when only the last sheets remain. The deliverable is a paper-only mini backing-card label with pad size, desk location, owner or role label, refill cue, and low-pad review reminder.

This skill is only a paper desk-organization aid. It must not provide adhesive methods, blade or tool instructions, repair guidance, medical guidance, or exercise guidance.

## Safety Boundary

Do not recommend tape, glue, mounting strips, adhesive products, fastening methods, blade use, cutting tools, craft tools, repair procedures, medical tracking, therapy prompts, stretching routines, exercise routines, or body-related reminders.

If the card needs a different size, keep the wording generic: choose a paper card that fits the pad or use the user's normal paper-handling process. Do not give step-by-step resizing, cutting, trimming, blade, scissors, or tool instructions.

Keep the card about paper pad support, labeling, storage, and refill review. If the user asks for repair, adhesive, medical, or exercise use, state that this skill only creates a paper backing-card label for desk organization.

## Required Inputs

Ask for desk-organization details only:

- Pad size or approximate label, such as mini, square, narrow, standard, or large.
- Pad location: desk drawer, monitor shelf, inbox tray, notebook pocket, meeting kit, kitchen desk, or bag.
- Owner or neutral role label, such as desk, front desk, household, student, host, or team.
- How the pad should be used at that spot: quick tasks, messages, labels, reminders, bookmarks, or scratch notes.
- Low-pad trigger, such as last ten sheets, thin stack, weekly check, or refill when empty.
- Spare pad storage location, if any.
- Preferred output size: mini backing card, drawer label, desk card, one-page pad map, or refill slip.

Do not ask for private sticky note contents, passwords, medical notes, therapy notes, exercise routines, repair details, adhesive choices, or cutting tools.

## Workflow

1. **Identify the pad.** Give the pad a short neutral name and approximate size label.
2. **Choose the desk location.** Assign the pad to a drawer, tray, shelf, kit, pocket, or work surface.
3. **Add a role label.** Use a neutral owner or location label rather than private task content.
4. **Set the low-pad trigger.** Define when to review, refill, or replace the pad.
5. **Map spare storage.** Note where extra pads live, if the user has a spare spot.
6. **Add a privacy guard.** Keep private note contents off the backing card.
7. **Produce the printable card.** Format a compact paper label that can sit behind the pad or near its storage spot.

## Output Format

Return a sticky note pad backing card with these sections:

1. **Pad Snapshot**
   - Pad name or role label
   - Approximate size
   - Desk or drawer location
   - Main use
   - Low-pad trigger
2. **Backing Card Fields**
   - Location label
   - Owner or role label
   - Spare pad location
   - Date checked
   - Refill review cue
3. **Desk Placement Map**
   - Primary pad spot
   - Spare pad spot
   - Nearby writing tool spot, if relevant
   - Return-home cue
4. **Low-Pad Review**
   - Trigger to check the pad
   - Status: stocked, low, empty, spare available, or review
   - Neutral next step: refill from spare spot, note for review, or leave as is
5. **Privacy and Boundary Line**
   - Do not write private note contents on the backing card
   - Paper-only desk aid
   - No adhesive, blade, repair, medical, or exercise guidance
6. **Mini Printable Label**
   - Pad label
   - Location
   - Low-pad cue
   - Spare location
   - Date checked

## Quality Bar

A strong result keeps a sticky note pad supported, labeled, findable, and ready for refill without giving adhesive, tool, repair, medical, or exercise guidance. It should be compact, printable, privacy-respecting, and limited to paper storage and refill cues.
