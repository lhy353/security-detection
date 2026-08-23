---
name: morning-med-spot-check-card
displayName: "Morning Med Spot Check Card"
version: "1.0.0"
description: "Create a small morning spot card that anchors an existing medication-taking habit at a visible location, using a date line and taken checkbox only, without dosage, diagnosis, treatment, medication, or condition-specific guidance."
triggerKeywords:
  - morningMedCheck
  - medSpotCard
  - takenCheckbox
  - bathroomCounterReminder
  - morningHabitAnchor
  - dailyTakenCheck
tags:
  - routine
  - habit
  - morning
  - printable
  - checklist
license: "MIT-0"
language: "en"
hasExecutableCode: false
promptOnly: true
execution: "noExec"
---

# Morning Med Spot Check Card

## Purpose

Use this prompt-only skill when a user wants a visible, non-medical reminder card for an already-established morning medication routine. The deliverable is a small printable spot card with a date line and a taken checkbox only.

This skill is a habit anchor, not health guidance. It does not provide dosage, diagnosis, treatment, medication, condition-specific, side-effect, interaction, refill, adherence, emergency, or clinical advice.

## Safety Boundary

Keep every output non-medical. Do not name medications unless the user already uses a neutral label and wants it copied exactly. Do not discuss doses, timing changes, missed-dose handling, side effects, interactions, diagnosis, treatment, conditions, refill decisions, stopping, starting, skipping, or changing any medication.

The card may include only:

- Date
- Morning location
- One taken checkbox
- Reset cue

If the user asks for medical instructions, missed-dose advice, medication changes, symptom interpretation, condition-specific advice, or refill decisions, decline that part and suggest they follow their clinician or pharmacist's instructions. Then offer a plain taken-checkbox habit card if useful.

## Best Inputs

Ask only for placement and format details:

- Morning spot: bathroom counter, kitchen counter, bedside table, coffee station, bag shelf, or another visible location.
- Card size: small square, wallet card, sticky-note size, half index card, or phone-note format.
- Reset cue: flip card, replace card, erase mark, or start a new line tomorrow.
- Date style: daily card, seven-day row, or one reusable line.

Do not ask what medicine it is, what dose it is, why the user takes it, what condition it treats, when it should be taken, or what to do if a dose is missed.

## Workflow

1. **Choose the visible spot.** Pick the morning location where the user's existing routine already happens.
2. **Set the card format.** Use a small printable card, sticky-note layout, or phone-note version.
3. **Keep the check simple.** Include one "Taken" checkbox only.
4. **Add the date line.** Make the mark easy to reset daily or weekly.
5. **Add the reset cue.** Tell the card where to go after the morning mark is complete.
6. **Remove medical content.** Exclude dosage, condition, medication instructions, refill prompts, treatment notes, or missed-dose guidance.
7. **Produce the spot card.** Format a compact card that can sit at the selected location.

## Output Format

Return the spot check card in this order:

1. **Spot Setup**
   - Morning spot:
   - Card size:
   - Reset cue:

2. **Printable Spot Card**
   - Date:
   - [ ] Taken

3. **Seven-Day Option**
   - Mon [ ] Taken
   - Tue [ ] Taken
   - Wed [ ] Taken
   - Thu [ ] Taken
   - Fri [ ] Taken
   - Sat [ ] Taken
   - Sun [ ] Taken

4. **Reset Line**
   - After marking the checkbox, return or reset the card for tomorrow.

5. **Boundary Note**
   - This is a non-medical habit anchor only. Follow clinician or pharmacist instructions for any medication questions.

## Example Prompts

Copy and paste one of these prompts to start:

- "I need a simple printable card for my bathroom counter with just a date and a taken checkbox so I don't forget my morning routine. No medical advice, just a visible habit anchor."
- "Create a seven-day spot check card I can put by the coffee station. I just need to mark each day with a checkbox — nothing about dosage or conditions."
- "Make a small wallet-sized morning check card with a daily date line and a single taken checkbox that I can reset each day."

## Quality Bar

A strong result is boring, visible, and safe: one location, one taken checkbox, one reset cue, and no medication guidance.
