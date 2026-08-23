---
name: "Laundry Stain Rescue Card"
description: "Creates a safe, fabric-aware stain rescue card for common laundry stains with care-label checks, cold-start steps, no cleaner mixing, and heat-setting warnings."
version: "1.0.0"
type: prompt-flow
tags: ["laundry", "stain removal", "home care", "fabric care", "cleaning", "checklist"]
---

# Laundry Stain Rescue Card

## Overview

Use this prompt-only skill when a user has a stained garment or washable fabric and needs a safe, step-by-step rescue card.

The skill identifies the stain type, fabric constraints, what has already been tried, and the safest next steps. It emphasizes care labels, spot testing, cold water starts for many stains, avoiding heat before the stain is gone, and never mixing cleaners.

## When to Use

Use this skill when the user says things like:

- "How do I get this stain out?"
- "I spilled coffee, wine, oil, ink, blood, grass, makeup, or sauce on my clothes."
- "Can I wash this stained shirt now?"
- "I dried a stained item. Is it ruined?"
- "Make me a stain removal checklist."
- "What should I do before the stain sets?"

## Required Inputs

Ask for only the details needed to create the rescue card:

- Stain type, if known
- Fabric type and color
- Care label instructions, such as machine wash, hand wash, dry clean only, cold water, or no bleach
- How long the stain has been there
- Whether the item has already been washed, dried, ironed, steamed, or treated
- What products are available, such as laundry detergent, dish soap, enzyme detergent, oxygen bleach, rubbing alcohol, white vinegar, baking soda, or stain remover
- Whether the item is delicate, expensive, sentimental, colorfast uncertain, wool, silk, leather, suede, rayon, acetate, or embellished
- Any allergy, fragrance, ventilation, pet, or child safety constraints

If the user cannot identify the fabric or care label, default to the gentlest reversible steps and recommend professional cleaning for valuable or delicate items.

## Workflow

1. **Capture stain and fabric facts.** Restate the stain, fabric, color, care label, age, prior treatments, and available products.
2. **Check stop conditions.** If the item is dry clean only, delicate, leather, suede, unstable dye, sentimental, or expensive, recommend pausing and considering a professional cleaner.
3. **Prevent setting.** Warn the user not to use heat, a dryer, iron, steamer, or hot water until the stain is gone unless the care label and stain type clearly support it.
4. **Choose the safest first move.** Start with blotting, lifting solids, flushing from the back, or a mild detergent step based on stain type and fabric.
5. **Select one treatment path.** Pick one cleaner or method at a time. Do not combine cleaners or layer chemicals.
6. **Add spot test.** Tell the user where and how to test colorfastness before treating a visible area.
7. **Give step-by-step timing.** Include soak or wait times, rinse points, and when to repeat.
8. **Plan wash and inspect.** Wash according to the care label, inspect before drying, and repeat treatment if needed.
9. **Add escalation.** Suggest professional cleaning or replacement decision points for delicate fabric, old stains, dye transfer, or heat-set stains.
10. **Add safety notes.** Include ventilation, gloves if needed, keeping products away from children and pets, and label-following.

## Output Format

Produce the rescue card with these sections:

1. **Stain Snapshot**
   - Stain type
   - Fabric and color
   - Care label
   - Age of stain
   - Prior treatments
2. **Stop First If**
   - Dry clean only, delicate, unstable dye, valuable item, leather, suede, or unknown fabric warnings
3. **Do Not Do**
   - No heat until stain is gone
   - No mixing cleaners
   - No unsafe bleach use
   - No scrubbing delicate fibers
4. **First 5 Minutes**
   - Blot, lift, flush, or protect steps
5. **Treatment Path**
   - Product to use
   - Spot test
   - Step-by-step treatment
   - Wait time
   - Rinse or repeat rule
6. **Wash and Inspect**
   - Care-label wash step
   - Inspect before drying
   - What to do if the stain remains
7. **If It Already Went Through the Dryer**
   - Lower-expectation recovery steps
   - When to stop and seek professional help
8. **Safety Notes**
   - Cleaner safety, ventilation, gloves if relevant, children and pets, and label-following

## Safety Boundary

- Never recommend mixing cleaners. In particular, do not mix bleach with ammonia, vinegar, acids, alcohol, peroxide, toilet cleaner, rust remover, or other cleaning products.
- Do not recommend chlorine bleach unless the garment care label and product label explicitly allow it, the fabric is compatible, the user can dilute and use it safely, and the item color makes sense for bleach use.
- Prefer oxygen bleach only when fabric and care labels allow it, and never on wool, silk, leather, or other incompatible materials.
- Warn that heat can set many stains. Avoid dryer, iron, steamer, and hot water until the stain is gone unless the stain and fabric instructions clearly justify heat.
- Do not recommend harsh scrubbing on delicate fibers, knits, wool, silk, rayon, lace, embroidery, or embellished items.
- For dry clean only, leather, suede, valuable, sentimental, or unstable-dye items, recommend pausing and contacting a professional cleaner.
- Follow product labels and care labels. Use ventilation and keep cleaners away from children and pets.
- Do not promise complete removal. State that old, dye-based, bleached, or heat-set stains may be permanent.

## Quality Checklist

A strong result should:

- Identify stain, fabric, color, care label, age, and prior treatments
- Include stop conditions before treatment
- Warn against heat-setting the stain
- Use one treatment path at a time and prohibit mixing cleaners
- Include spot testing and label-following
- Give practical first steps, treatment timing, wash, and inspect guidance
- Include dryer-aftercare and realistic expectations
- Recommend professional cleaning for delicate, dry clean only, valuable, or risky items
