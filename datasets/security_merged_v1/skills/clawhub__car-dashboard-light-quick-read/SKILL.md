---
name: car-dashboard-light-quick-read
description: Create a driver-facing quick-read card for one dashboard warning light by identifying the icon, color, and urgency; advising safe pull-over actions for red or flashing warnings; documenting service notes; and deferring diagnosis or repair to qualified professionals.
version: "1.0.0"
type: prompt-flow
tags:
  - car-safety
  - dashboard-warning
  - driver-action
  - roadside-safety
  - vehicle-service-notes
author: Bell (design) / coder
---

# Car Dashboard Light Quick Read

## Purpose

Help a driver respond calmly to one dashboard warning light with a short action card: what the light appears to mean, how urgent it is, what to do safely right now, and what to document for service.

This is a driver-facing safety and documentation workflow. It is not a repair guide, mechanical diagnosis, electrical diagnosis, code interpretation service, or replacement for the vehicle owner's manual, roadside assistance, emergency services, or a qualified automotive professional.

## Use This Skill When

Use this skill when the user says:

- A dashboard warning light appeared while driving or before starting.
- A warning icon is red, yellow, amber, flashing, or accompanied by a message.
- They want to know whether to stop, drive cautiously, or document the issue for service.
- They need a printable or phone-ready card for one warning light event.

Do not use this skill for repair instructions, part replacement, fluid procedures, fuse checks, scan tool interpretation, emissions troubleshooting, or advice to keep driving against a manual or professional instruction.

## Best Inputs

Ask only for details needed to classify urgency. If the driver is currently moving, keep questions minimal and put safety first.

- Are you currently driving, stopped, parked, or about to start?
- Vehicle year, make, model, and trim if known.
- Warning icon or text, including color.
- Solid, flashing, intermittent, or paired with a sound or message.
- Any immediate safety symptoms: loss of power, steering issue, braking issue, overheating indication, smoke, burning smell, unusual noise, tire damage, or visibility issue.
- Road context: highway, city street, parking lot, weather, traffic, shoulder availability, passengers.
- Recent context to document: refuel, service, tire change, battery work, weather, pothole, long drive, or towing load.

## Workflow

1. **Start with driver safety.** If the user is driving, tell them to focus on the road and pull over only when it is safe. Do not ask them to inspect the dashboard closely while moving.
2. **Apply the red or flashing rule.** For red warnings, flashing warnings, repeated chimes, warnings tied to braking, steering, oil pressure, engine temperature, charging system, smoke, burning smell, severe power loss, or a message saying stop safely, advise the user to pull over safely, stop in a safe place, and contact roadside assistance, emergency services, or a qualified professional as the situation requires.
3. **Identify the light.** Capture the icon, color, text, solid or flashing behavior, and vehicle model. Say that meanings vary by vehicle and the owner's manual is the deciding reference.
4. **Classify urgency.** Use a simple ladder: Stop Safely Now, Caution and Limit Driving, Service Soon, or Information Only. If uncertain, choose the more conservative safety category.
5. **Give immediate driver actions.** Keep actions limited to driving safety, roadside positioning, manual check when parked, contacting help, and documenting details. Do not give repair or diagnostic steps.
6. **Prepare service notes.** Record the exact light, color, behavior, message text, mileage, driving conditions, weather, recent service, sounds or smells, and whether it went away after stopping or restarting. Photos are only suggested after the vehicle is safely stopped.
7. **Close with next step.** Tell the user who to contact: emergency services for immediate danger, roadside assistance if not safe to drive, or a qualified mechanic or dealer service department for diagnosis and repair.

## Output Format

Return the card in this order.

### Dashboard Light Snapshot

- Vehicle:
- Current state: driving, stopped, parked, or pre-start
- Light or message:
- Color:
- Solid or flashing:
- Sounds, smells, handling changes, or other warnings:
- Road and weather context:
- Assumptions:

### Urgency Class

Choose one and explain briefly:

- Stop Safely Now
- Caution and Limit Driving
- Service Soon
- Information Only

### Immediate Driver Actions

Give short, numbered actions. For red or flashing warnings, the first action must be to pull over safely when conditions allow. Include hazard lights, safe location, avoiding traffic exposure, and contacting emergency services or roadside assistance when danger is present.

### Manual Check

State that the user's vehicle owner's manual or official vehicle information controls the exact meaning. If the manual is unavailable, recommend treating unknown red or flashing warnings as urgent and contacting qualified help.

### Service Notes to Capture

List concise bullets the user can share with roadside assistance, a mechanic, or dealer service department.

### What Not to Do

Include repair-boundary reminders such as not ignoring red or flashing warnings, not resetting the light to continue driving, not opening the hood in unsafe traffic, and not attempting diagnosis or repair while roadside.

## Message Style

- Keep the tone calm, direct, and safety-first.
- Use short bullets that a driver can read quickly after stopping.
- Avoid mechanical certainty. Say "the manual may describe this as" or "this commonly signals" when appropriate.
- Do not overload the user with possible causes.
- If the user is actively driving, keep the answer very short until they are stopped safely.

## Safety Boundary

- This skill produces a driver-facing action card only.
- For red or flashing warnings, advise the driver to pull over safely as soon as conditions allow and get qualified help.
- Do not provide diagnosis, repair procedures, code interpretation, part replacement steps, fluid service steps, electrical checks, or reset instructions.
- Do not tell the user a vehicle is safe to drive when warning severity is unclear.
- Do not override the owner's manual, emergency services, roadside assistance, a mechanic, dealer service, fleet policy, rental policy, or local road law.
- If there is injury, crash risk, fire, smoke, fuel smell, dangerous traffic exposure, brake or steering loss, or an unsafe roadside location, direct the user to emergency services or roadside assistance immediately.

## Example Prompts

- "A red oil can light came on while I am driving. What do I do?"
- "My check engine light is flashing. Make me a quick card."
- "There is a yellow tire light on before I leave. What should I document?"
- "My dashboard says brake system warning and I am on the highway."
