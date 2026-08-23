---
name: energy-crash-pattern-log
description: "Create a 7-day observation log for recurring afternoon or evening energy crashes, brain fog, post-meal slumps, workout drop-offs, or bedtime rebound energy. Use when the user wants to spot routine patterns before changing sleep, food, caffeine, workload, movement, or screen habits."
---
# Energy Crash Pattern Log

## Purpose

Help the user turn vague energy dips into a simple observation record. The skill produces a 7-day energy pattern log, a short pattern summary, and low-risk routine experiments the user can try or discuss with a clinician.

This is a prompt-only self-observation workflow. It is not medical, nutrition, sleep, fitness, or mental-health advice.

## Use This Skill When

Use this skill when the user reports any of these situations:

- Afternoon or evening crashes that disrupt work, study, caregiving, workouts, chores, or sleep.
- Brain fog, post-meal slump, low motivation, or sudden fatigue that seems routine-linked.
- Rebound energy at bedtime after feeling drained earlier.
- Uncertainty about whether sleep, meals, caffeine, hydration, movement, stress, sunlight, screens, or workload timing is involved.
- A desire to observe patterns before making major lifestyle changes.

Do not use it to diagnose medical conditions, prescribe supplements, set restrictive diets, interpret lab results, or replace care from a qualified professional.

## Best Inputs

Ask only for details the user can comfortably share. If information is missing, proceed with placeholders.

- Main crash window: time of day, duration, frequency, and what it interrupts.
- Typical wake time, bedtime, meal timing, caffeine timing, and work or school blocks.
- Recent changes: schedule, stress, exercise, medications, illness, travel, or sleep disruption.
- Symptoms the user wants to track, without interpreting them diagnostically.
- Logging preference: hourly blocks, morning/afternoon/evening blocks, or custom schedule.
- Any red-flag symptoms or concern level.

## Workflow

1. **Define the crash pattern.** Capture when the dip usually happens, how long it lasts, what it disrupts, and what the user hopes to learn.
2. **Choose a simple energy scale.** Use a 1-5 scale where 1 means depleted and 5 means steady, alert energy. Let the user rename labels if helpful.
3. **Build the 7-day log.** Create time blocks for energy score, sleep, meals, caffeine, hydration, movement, stress, sunlight, screen load, workload intensity, and symptoms.
4. **Add context notes.** Include a small field for unusual events such as poor sleep, skipped meal, intense meeting, long commute, late workout, alcohol, illness, or emotional stress.
5. **Keep logging lightweight.** Encourage short entries at 2-4 anchor times per day rather than constant tracking if the user is busy or overwhelmed.
6. **Review entries after 3-7 days.** Look for repeated timing, possible routine links, protective factors, and unknowns to observe longer.
7. **Summarize without diagnosing.** Label observations as likely routine links, possible protective factors, and open questions, not causes or medical conclusions.
8. **Suggest low-risk experiments.** Offer small experiments such as break timing, light movement, hydration reminders, caffeine cutoff notes, meal composition notes, sunlight exposure, screen breaks, or workload reshaping.
9. **Prepare clinician notes when needed.** If symptoms are new, severe, worsening, persistent, or concerning, turn the log into a concise doctor-visit prep summary.

## Output Format

Return the log package in this order:

1. **Energy Crash Snapshot**

| Field | Detail |
|---|---|
| Main crash window | |
| Frequency | |
| What it disrupts | |
| Current hypothesis, if any | |
| Concern level | |

2. **1-5 Energy Scale**

| Score | Meaning |
|---|---|
| 1 | Depleted; hard to function |
| 2 | Low; pushing through |
| 3 | Usable but uneven |
| 4 | Steady and focused |
| 5 | Strong, clear energy |

3. **7-Day Energy Pattern Log**

| Day | Time block | Energy 1-5 | Sleep notes | Meals or snacks | Caffeine or alcohol | Hydration | Movement | Stress or workload | Screen load | Symptoms or context |
|---|---|---:|---|---|---|---|---|---|---|---|

4. **Pattern Review**

| Pattern noticed | Evidence from log | Confidence | What to observe next |
|---|---|---|---|

5. **Low-Risk Experiment Menu**

| Experiment | When to try | What to track | Stop or adjust if |
|---|---|---|---|

6. **Doctor-Visit Prep Note, If Relevant**

A short summary of the crash timing, duration, symptoms, repeated context, and questions to ask a qualified clinician.

7. **Open Questions**

A short list of missing details that would improve the next review.

## Message Style

- Stay practical, calm, and nonjudgmental.
- Use observation language such as "appears linked," "worth tracking," and "unknown."
- Avoid certainty, diagnosis, fear, diet culture, productivity shaming, or moralizing about habits.
- Prefer tiny experiments the user can test for a few days.
- If the user is overwhelmed, reduce the log to morning, crash window, and evening check-ins.

## Safety Boundary

- Do not provide medical, nutrition, sleep, fitness, psychiatric, or medication advice.
- Do not diagnose fatigue, blood sugar issues, sleep disorders, depression, ADHD, burnout, anemia, thyroid problems, long COVID, or any other condition.
- Do not recommend supplements, medication changes, fasting, restrictive diets, intense exercise, or sleep deprivation.
- Encourage professional medical help for chest pain, fainting, severe dizziness, shortness of breath, sudden weakness, confusion, severe headache, persistent fatigue, disordered eating concerns, symptoms that are new or worsening, or any symptom the user finds alarming.
- If the user may be in immediate danger, advise urgent local medical or emergency help.
- Minimize sensitive data. The user can describe medications, diagnoses, or personal details only if they choose; never request account credentials, insurance IDs, full legal identifiers, or private medical record access.

## Example Prompts

- "I crash every day around 3 PM. Help me build a log."
- "I get brain fog after lunch and want to find patterns."
- "My workouts keep falling apart after work. Make a 7-day energy tracker."
- "I feel exhausted all evening but wired at bedtime. What should I track?"
- "Turn these notes into a doctor-visit summary about recurring fatigue."
