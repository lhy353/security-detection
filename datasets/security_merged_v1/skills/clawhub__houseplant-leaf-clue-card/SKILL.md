---
name: houseplant-leaf-clue-card
description: Create a plant-specific leaf symptom card for yellowing, browning, curling, drooping, spots, or sticky leaves by matching visible clues to likely causes, choosing one low-risk care adjustment, checking pet and child toxicity, avoiding pesticide overuse, and escalating severe infestations.
version: "1.0.1"
type: prompt-flow
tags:
  - houseplants
  - plant-care
  - leaf-symptoms
  - pest-clues
  - home-care
author: Bell (design) / coder
---

# Houseplant Leaf Clue Card

## Purpose

Help the user create a narrow, plant-specific clue card for one houseplant leaf problem. The skill helps the user observe symptoms, identify likely care or pest clues, choose one low-risk adjustment, and schedule a short re-check instead of changing many variables at once.

This is a prompt-only home plant care workflow. It does not diagnose plant disease with certainty, identify every pest, prescribe pesticide treatment, or replace advice from a local nursery, extension office, licensed pesticide professional, veterinarian, pediatrician, or poison control service.

## Use This Skill When

Use this skill when the user says a houseplant has:

- Yellow leaves, pale leaves, or leaf drop.
- Brown tips, crispy edges, scorched patches, or dry margins.
- Curling, drooping, wilting, limp, or folded leaves.
- Speckles, spots, holes, webbing, sticky residue, black residue, or visible insects.
- A recent change after repotting, moving, watering, fertilizing, pruning, or bringing a new plant home.

Do not use this skill for outdoor landscape disease management, food crop safety, commercial pest control, pesticide mixing, plant ingestion emergencies, or severe toxic exposure questions.

## Best Inputs

Ask only for details that change the card. If details are missing, proceed with stated assumptions.

- Plant name, or best guess plus a photo description if the name is unknown.
- Leaf symptom: color, texture, pattern, old leaves vs. new leaves, one leaf vs. whole plant.
- Timing: when it started, whether it is spreading, and what changed recently.
- Light: window direction, distance from window, direct sun, grow light, recent move.
- Water and pot: watering frequency, soil moisture now, drainage holes, pot size, saucer water.
- Soil and feeding: recent repotting, fertilizer, mineral buildup, or compacted soil.
- Pest clues: sticky leaves, webbing, cottony clumps, tiny dots, flying insects, leaf underside findings.
- Household safety: pets, children, chewing risk, and where the plant is placed.

## Workflow

1. **Frame the task.** State that the card is a clue-based care plan, not a certain diagnosis. Focus on one plant and one main symptom.
2. **Check immediate safety.** If a child or pet may have chewed or swallowed the plant, tell the user to contact local poison control, a veterinarian, or a clinician as appropriate. Do not give toxic exposure treatment advice.
3. **Confirm toxicity risk.** Ask whether pets or children can reach the plant. Tell the user to verify the specific plant with a reliable toxicity source, plant label, nursery, veterinarian, pediatrician, or poison control resource before moving or treating it.
4. **Map visible clues.** Separate symptoms by leaf age, plant area, pattern, texture, residue, and speed of spread. Encourage checking leaf undersides, stems, soil surface, and drainage without damaging the plant.
5. **Match likely causes.** Present two to four likely causes as clues, not certainties. Common clue groups include water stress, drainage trouble, light change, temperature or draft stress, humidity, mineral or fertilizer buildup, natural old-leaf shedding, transplant stress, and pests.
6. **Choose one low-risk adjustment.** Pick the smallest change most supported by the clues, such as adjusting watering timing, improving drainage, moving a little farther from harsh sun, increasing observation, isolating the plant, or wiping leaves. Avoid stacking many changes in the same week.
7. **Handle pest clues carefully.** If pests are possible, start with isolation, close observation, gentle leaf cleaning, and label-safe options only. Do not recommend repeated broad pesticide use, mixing products, off-label pesticide use, or treating every plant without evidence.
8. **Escalate severe infestation or decline.** Recommend local expert help if pests are numerous, spreading fast, causing heavy webbing or sticky residue, present on many plants, associated with rot smell or mold, or if the plant is collapsing despite basic care.
9. **Create a 7-day re-check plan.** Define what to watch, what not to change yet, and what result would trigger a next step or escalation.

## Output Format

Return the card in this order.

### Plant Leaf Snapshot

- Plant:
- Main symptom:
- Started:
- Spread pattern:
- Recent changes:
- Light:
- Water and pot:
- Pest clues:
- Pets or children can reach it:
- Assumptions:

### Safety Check

- Toxicity check needed:
- If chewing or ingestion is possible:
- Treatment caution:

### Likely Clue Map

List two to four likely causes. For each, include:

- Clue:
- Why it fits:
- What would make it less likely:
- What to observe next:

### One Adjustment for the Next 7 Days

- Adjustment:
- Why this is the first change:
- What to avoid changing at the same time:
- Re-check date:

### Pest or Disease Watch

- What to inspect:
- When to isolate:
- When to escalate:
- What not to do with pesticides:

### 7-Day Re-Check Notes

Use simple bullets for day 1, day 3, and day 7 observations. Include leaf appearance, soil moisture, new spread, pests seen, and whether the chosen adjustment helped.

## Message Style

- Keep language calm, practical, and specific to the plant and symptom.
- Say "likely clue" or "possible cause" rather than pretending certainty.
- Prefer one clear adjustment over a long generic plant care guide.
- Respect renters, small apartments, limited light, budget constraints, pets, and children.
- Use plain English and short checklists.

## Safety Boundary

- Do not encourage pesticide overuse, preventive spraying without evidence, product mixing, off-label pesticide use, or repeated pesticide cycles without expert guidance.
- Do not provide toxic exposure treatment instructions for pets or children. Direct urgent exposure concerns to poison control, a veterinarian, pediatrician, clinician, or local emergency service.
- Do not guarantee that a plant is safe for a household based only on a common name. Common names can be ambiguous; tell the user to verify the exact plant.
- Do not diagnose regulated plant diseases or severe infestations as manageable at home. Escalate severe or spreading pest problems to a local extension office, nursery, certified arborist or horticulture professional, or licensed pest professional.

## Example Prompts

- "My pothos has yellow leaves and I keep watering it. What should I change?"
- "My monstera leaf edges are brown and crispy. Make me a clue card."
- "Sticky leaves showed up on my ficus. What should I inspect first?"
- "My cat can reach this plant and the leaves are dropping. Help me make a safe plan."
