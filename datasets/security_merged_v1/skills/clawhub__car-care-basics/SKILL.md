---
name: Car Care Basics
description: Master basic car maintenance with schedules, warning light guides, and repair cost estimates. For educational reference only.
version: "1.0.0"
type: prompt-flow
tags:
  - car-maintenance
  - automotive
  - repair-estimate
  - warning-lights
  - vehicle-care
  - maintenance-schedule
  - DIY-car-care
author: Golden Bean
---

# Car Care Basics

## Overview

Car Care Basics helps vehicle owners stay on top of maintenance, understand warning signs, and make informed decisions about repairs. It provides maintenance schedules, dashboard warning light guides, repair cost estimates, and DIY vs. mechanic guidance—so users can avoid breakdowns and overpaying.

**Important:** This skill provides educational reference only. It is not a substitute for professional automotive diagnosis or repair. Users should consult a certified mechanic for safety-critical issues.

## When to Use

Use this skill when the user asks to:

- Set up a car maintenance schedule
- Understand a dashboard warning light
- Estimate repair costs
- Conduct pre-trip vehicle checks
- Decide between DIY and mechanic

**Trigger keywords:** car maintenance, car care, warning light meaning, oil change schedule, car repair cost, tire maintenance, check engine light, car service schedule

## Workflow

### Step 1 — Vehicle Profile

Collect from the user:
- Make, model, year, and mileage
- Fuel type (gasoline, diesel, hybrid, electric)
- Driving conditions (city, highway, off-road, extreme climate)
- Maintenance history (if known: last oil change, tire rotation, brake check)
- Current concerns or warning lights

### Step 2 — Maintenance Schedule

Build a time- and mileage-based schedule:
- **Monthly:** Tire pressure, lights, fluid levels (washer, coolant, oil, brake)
- **Quarterly:** Tire tread depth, wiper blades, battery terminals
- **Every 5,000–7,500 miles:** Oil and filter change (check owner's manual for exact interval)
- **Every 15,000–30,000 miles:** Air filter, cabin filter, spark plugs, transmission fluid
- **Every 30,000–60,000 miles:** Brake pads, belts, hoses, coolant exchange
- **As needed:** Tires, battery, brake rotors, alignment

Note: Intervals vary by manufacturer. Always defer to the owner's manual.

### Step 3 — Warning Light Guide

Explain common dashboard indicators:
- **Check Engine:** Solid = schedule diagnostic soon; flashing = stop driving, call mechanic
- **Oil Pressure:** Stop immediately, check oil level, tow if necessary
- **Battery:** Charging system issue; drive to service if safe, or call for jump/tow
- **Brake System:** Check parking brake, fluid level, or pad wear; stop if braking feels abnormal
- **Coolant Temperature:** Pull over, turn off engine, let cool before checking coolant
- **Tire Pressure (TPMS):** Inflate to door-jamb spec; if flashing then solid, sensor may be faulty
- **ABS:** Anti-lock brake system fault; brakes still work but ABS is disabled
- **Airbag (SRS):** Safety system fault; schedule service promptly

For each: meaning, urgency level, safe action, when to call a professional.

### Step 4 — Repair Cost Estimates

Provide ballpark cost ranges for common services (regional variation noted):
- Oil change: $40–$100 (conventional vs. synthetic)
- Brake pad replacement: $150–$400 per axle
- Tire replacement: $80–$300 per tire (economy vs. premium)
- Battery replacement: $100–$250
- Alternator: $400–$800
- Timing belt: $500–$1,200
- Transmission service: $150–$400

Emphasize that these are rough estimates and actual costs depend on vehicle, region, and shop rates.

### Step 5 — DIY vs. Mechanic Decision Framework

Help users decide what to do themselves:
- **Safe DIY:** Check fluids, tire pressure, replace wipers, change air filter, jump-start battery
- **Cautious DIY:** Oil change (with proper disposal), brake pad replacement (if experienced), tire rotation (with jack and stands)
- **Mechanic recommended:** Transmission work, electrical diagnostics, suspension, timing belt, airbag systems

For each DIY item: tools needed, safety precautions, and disposal requirements.

### Step 6 — Pre-Trip Checklist

Quick 10-point inspection before road trips:
1. Tire pressure and tread
2. Oil level
3. Coolant level
4. Brake fluid level
5. Washer fluid
6. Lights (headlights, brake lights, turn signals)
7. Spare tire and jack
8. Emergency kit (first aid, flashlight, jumper cables, water)
9. Wiper condition
10. Fuel range and planned stops

## Templates

### New Car Owner
Focus on understanding the owner's manual, warranty maintenance, and basic checks.

### High-Mileage Vehicle
Focus on aging-component monitoring, fluid changes, and proactive replacement.

### Extreme Climate Driver
Focus on battery, coolant, tires, and seasonal preparation.

### Electric / Hybrid Owner
Focus on regenerative braking, battery health, and EV-specific maintenance differences.

## Output Format

The output includes:

1. **Vehicle Profile Summary** — Make/model/year and driving context
2. **Maintenance Schedule** — Time- and mileage-based tasks
3. **Warning Light Reference** — Meaning, urgency, and action for each relevant light
4. **Cost Estimates** — Ballpark ranges for requested or likely services
5. **DIY vs. Mechanic Guide** — Decision framework for specific tasks
6. **Pre-Trip Checklist** — 10-point inspection list

## Safety & Compliance

- **Not mechanical advice:** Always defer to the owner's manual and certified mechanics for diagnosis and repair
- No instructions for dangerous repairs (fuel system, airbag, high-voltage EV components)
- Emphasize safety: proper jack stands, eye protection, ventilation
- No guarantee of accuracy for cost estimates due to regional and vehicle variation
- This is a descriptive prompt-flow skill with zero code execution, zero network calls, and zero credential requirements

## Acceptance Criteria

1. User provides vehicle info; output includes a tailored maintenance schedule
2. Warning light explanations include urgency levels and safe actions
3. Cost estimates are presented as rough ranges with variation noted
4. DIY guidance stays within safe, low-risk tasks
5. No encouragement of dangerous repairs or misrepresentation of mechanical expertise

## Examples

### Example 1: Warning Light

**User says:** "My check engine light came on. It's solid, not flashing. What should I do?"

**Skill guides:** Confirm light behavior and any symptoms. Explain solid vs. flashing difference, suggest OBD-II scan or mechanic visit, and provide a safe action plan.

### Example 2: Maintenance Setup

**User says:** "I just bought a 2018 Honda Civic with 60k miles. I don't know what maintenance it needs."

**Skill guides:** Collect driving conditions and known history. Produce a maintenance schedule from 60k forward, flagging timing belt, transmission service, and brake inspection.
