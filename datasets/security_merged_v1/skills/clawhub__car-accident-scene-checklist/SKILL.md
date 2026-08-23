---
name: Car Accident Scene Checklist
description: Guide drivers through a calm post-accident scene checklist—safety, photos, witness notes, insurance exchange, report reminders, and follow-up log.
version: "1.0.0"
type: prompt-flow
tags:
  - car-safety
  - accident-checklist
  - emergency-prep
  - driver-aid
  - evidence-collection
  - insurance
author: Harry
---

# Car Accident Scene Checklist

## Overview

Car Accident Scene Checklist helps drivers stay calm and methodical during the stressful first 30 minutes after a traffic accident. It walks through immediate safety actions, evidence collection, information exchange, official reporting, and post-scene follow-up—so nothing critical gets forgotten when adrenaline is high.

**Important:** This skill provides organizational and memory-aid support only. It does not provide legal advice, medical advice, or insurance advice. In any emergency, the first and only priority is personal safety and calling emergency services (e.g., 911 / 110 / 112) as needed. Always follow local laws, police instructions, and your insurance provider's specific claims process.

## When to Use

Use this skill when the user:

- Has just been in or witnessed a car accident
- Wants a step-by-step checklist for accident scene response
- Needs to organize post-accident documentation
- Is teaching a new driver what to do after an accident
- Wants to prepare an in-car emergency reference

**Trigger keywords:** car accident, traffic accident, fender bender, crash, collision, hit and run, accident checklist, what to do after accident, accident scene

## Required Inputs

Ask the user to describe their situation. If they are at the scene, prioritize emergency safety questions first:

- **Safety status:** Is anyone injured? Are vehicles in a dangerous position? Is the scene safe?
- **Location:** Where did the accident happen? (road, intersection, parking lot)
- **Vehicles involved:** How many? Any commercial, motorcycle, bicycle, or pedestrian involvement?
- **Injury status:** Any visible injuries, complaints of pain, or disorientation?
- **Current state:** Is the user still at the scene, or gathering information after the fact?

## Workflow

### Step 1 — Immediate Safety (FIRST PRIORITY)

Do not proceed beyond this step until safety is confirmed.

- **Check for injuries:** Ask "Is everyone okay?" for all involved persons. If anyone is injured or complains of pain, call emergency services immediately.
- **Move to safety:** If the accident is minor and vehicles are drivable, move to the shoulder or a safe area. Turn on hazard lights.
- **Stay safe at scene:** If vehicles cannot be moved, turn off engines, turn on hazards, and get everyone away from traffic. Set up warning triangles or flares if available.
- **Call emergency services:** Required for any injury, significant vehicle damage, hit-and-run, uncooperative other driver, or if local law requires it.
- **Do NOT:** Stand between vehicles, stand in traffic lanes, or confront an aggressive driver.

### Step 2 — Information Exchange

Collect and share the following with all involved drivers. Stay calm and factual.

**For each involved driver, record:**
- Full name and contact phone number
- Driver's license number and issuing state/province
- License plate number and state/province
- Insurance company name and policy number
- Vehicle make, model, year, and color
- Registered owner's name and contact (if different from driver)

**For yourself, provide the same information only.** Do not discuss fault, admit fault, or make statements like "I'm sorry" or "It was my fault." These statements may be used in claims determination.

### Step 3 — Scene Documentation

Collect evidence methodically. Quality matters more than quantity.

**Photos to take (if safe to do so):**
- Wide shots: intersection or road approach from multiple angles
- All vehicle damage, close-up and from a few steps back
- License plates of all vehicles involved
- Road conditions, traffic signs, signals, skid marks
- Weather and lighting conditions
- Any visible injuries (with consent only)

**Notes to record immediately:**
- Date, time, and exact location (use phone GPS/pin)
- Weather and road conditions (wet, icy, glare, construction)
- Direction each vehicle was traveling
- What happened, in your own factual words, as soon as possible
- Names and badge numbers of responding officers

### Step 4 — Witness Information

If there are witnesses, approach politely:

- Ask for name and contact information
- Ask what they saw (record briefly, do not debate or correct them)
- If they decline, note that a witness was present but declined to provide information
- Do not pressure or argue with witnesses

### Step 5 — Official Reporting

- **Police report:** Report the accident to police if required by local law (thresholds vary by jurisdiction for damage amount, injury, or hit-and-run). Ask for the report number and how to obtain a copy.
- **Insurance notification:** Notify your insurance company as soon as practical. Many policies require prompt reporting. Provide factual information only.
- **DMV/DOT reporting:** Some jurisdictions require a separate accident report to the motor vehicle department. Check your local requirements.

### Step 6 — Post-Scene Documentation

After leaving the scene, while memory is fresh:

- Write a detailed narrative of what happened (own words, chronological)
- Draw a simple diagram showing vehicle positions and directions
- Create a timeline of events (time of accident, time of police arrival, time scene was cleared)
- List all photos taken and where they are stored
- Note any pain or discomfort that developed hours or days after

### Step 7 — Follow-Up Tracker

Create a tracking log for ongoing case management:

| Date | Action | Who | Notes | Status |
|------|--------|-----|-------|--------|
| | Filed police report | | Report #: | |
| | Notified insurance | | Claim #: | |
| | Medical evaluation | | Provider: | |
| | Repair estimate | | Shop: | |
| | Received police report | | Copy: Y/N | |
| | Insurance adjuster contact | | | |
| | Repair scheduled | | | |
| | Case closed | | Resolution: | |

## Output Template

Organize the output in this structure:

```
## Car Accident Scene — Summary

### Safety Status
[Confirmed or actions needed]

### Involved Parties
| Role | Name | Contact | License Plate | Insurance |
|------|------|---------|---------------|-----------|
| Your vehicle | | | | |
| Other driver 1 | | | | |
| Other driver 2 | | | | |

### Scene Details
- Date/Time:
- Location:
- Weather/Road conditions:
- Police report #:
- Responding officer:

### Evidence Collected
- Photos: [count and storage location]
- Witnesses: [names and contacts]
- Diagram: [done/pending]

### Narrative
[User's factual account]

### Follow-Up Actions
[Tracker table from Step 7]

### Reminders
- [ ] Obtain police report copy
- [ ] Submit insurance claim
- [ ] Seek medical attention if any pain develops
- [ ] Keep all receipts (rental, medical, repair)
- [ ] Document all communications with date, person, and summary
```

## Safety Boundaries

- **No legal advice:** This skill does not interpret laws, determine fault, estimate settlement values, or advise on litigation.
- **No medical advice:** This skill does not diagnose injuries, recommend treatments, or assess whether medical attention is needed beyond "if in doubt, seek care."
- **No insurance advice:** This skill does not interpret policy terms, recommend specific insurance actions, or estimate claim outcomes. Always follow your insurance provider's official claims process.
- **Emergency first:** If the user describes an active emergency with injuries or danger, the ONLY response is to call emergency services immediately.
- **Truthful documentation only:** Never suggest exaggerating damage, fabricating symptoms, or misrepresenting facts. Insurance fraud is a criminal offense.
- **Self-incrimination protection:** Remind users not to admit fault or apologize at the scene, as these statements may affect claims.
- **No hit-and-run encouragement:** If the user describes leaving a scene without exchanging information, advise them that hit-and-run is illegal and they should report to authorities.

## Examples

### Example 1: Minor Parking Lot Collision

**User:** "I just backed into a car in the grocery store parking lot. No one is hurt. What do I do?"

**Response outline:**
1. Confirm safety—both drivers okay, vehicles moved out of travel lanes
2. Exchange information with the other driver (Step 2)
3. Take photos of both vehicles' damage and the parking lot layout (Step 3)
4. No witnesses likely needed; note location and time
5. Check if local law requires police report for parking lot incidents
6. Notify insurance provider
7. Document everything while memory is fresh
8. Set up follow-up tracker

### Example 2: Multi-Car Highway Accident

**User:** "I was in a 3-car accident on the highway. One person is complaining of neck pain. We've called an ambulance."

**Response outline:**
1. Safety already addressed (ambulance called)—reassure the user this was the right action
2. Remind: do not discuss fault; wait for police to arrive
3. Guide through information exchange once police allow
4. Emphasize photo documentation of all three vehicles, road conditions, and traffic controls
5. Remind to get police report number and officer information
6. Medical evaluation is priority—even minor neck pain should be checked
7. Post-scene: detailed narrative, insurance notification, follow-up tracker
8. Reminder: do not speak to other drivers' insurance companies without consulting your own
