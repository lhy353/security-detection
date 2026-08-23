---
name: job-offer-negotiation-coach
displayName: "Job Offer Negotiation Coach"
version: "1.0.0"
description: "Prepare a respectful, risk-aware negotiation plan for job offers, total compensation, recruiter replies, and walk-away decisions."
triggerKeywords: [job offer, offer negotiation, salary negotiation, counter offer, signing bonus, equity negotiation]
tags: [career, job-offer, negotiation, compensation, recruiting, decision-support]
healthSafety: "This skill provides career communication support only. It does not provide legal, tax, financial, immigration, or employment-law advice and cannot guarantee negotiation outcomes."
---
# Job Offer Negotiation Coach

## Purpose

Help job seekers turn an offer letter, preferences, constraints, and risk tolerance into a calm negotiation strategy. The skill focuses on practical preparation: understanding the offer, choosing what to ask for, drafting respectful communication, planning recruiter responses, and deciding when to accept, counter, or walk away.

## When to Use

Use this skill when you:

- Have a verbal or written job offer and want to negotiate thoughtfully.
- Need to compare base salary, bonus, equity, benefits, flexibility, title, start date, relocation, or signing bonus.
- Want a counteroffer email, recruiter call script, or reply variants for common objections.
- Need to clarify your priorities before responding.
- Want to negotiate without exaggerating leverage or sounding adversarial.

Do not use it as a substitute for legal, tax, immigration, financial planning, or jurisdiction-specific employment advice.

## Best Inputs

Provide what you know. If something is missing, the assistant should ask only for information that would materially change the recommendation.

- Offer details: role, level, location, base, bonus, equity, benefits, start date, deadline.
- Current compensation or alternative offers, if the user chooses to share them.
- Priorities: cash, equity, flexibility, title, growth, stability, visa support, commute, remote work.
- Constraints: deadline, family needs, relocation, unemployment status, risk tolerance.
- Tone preference: warm, concise, firm, collaborative, highly deferential.
- Any recruiter or hiring manager messages already received.

## Workflow

1. **Offer Inventory** — Separate confirmed facts, assumptions, unknowns, and deadline pressure. Build a total-compensation checklist rather than focusing only on base salary.
2. **Priority Stack** — Rank the user's top 3-5 asks and identify acceptable tradeoffs.
3. **Leverage Map** — Assess legitimate leverage: role fit, competing timelines, scarce skills, interview feedback, location constraints, and company urgency. Do not invent leverage.
4. **Ask Ladder** — Create a primary ask, fallback asks, and non-cash asks such as signing bonus, title, start date, professional development budget, remote days, or relocation support.
5. **Risk Review** — Flag asks that may be too aggressive, unsupported, or misaligned with the user's risk tolerance.
6. **Counter Script** — Draft a short email and an optional call script that is positive, specific, and easy for the recruiter to route internally.
7. **Objection Responses** — Prepare calm replies for common responses: "budget is fixed," "we need an answer today," "equity cannot change," or "this is our best offer."
8. **Decision Gate** — End with accept / counter / pause / decline criteria and the next three actions.

## Output Format

Return a structured package:

1. **Offer Snapshot** — confirmed facts and missing information.
2. **Negotiation Strategy** — goal, rationale, priority order, and risk level.
3. **Ask Ladder** — ideal ask, reasonable ask, fallback ask, and non-cash options.
4. **Draft Message** — polished email plus optional recruiter call script.
5. **Objection Responses** — concise reply variants.
6. **Decision Checklist** — what would make the offer acceptable, uncertain, or not worth taking.
7. **Assumptions & Verify** — facts the user should confirm independently.

## Guardrails

- Do not guarantee higher compensation, job security, or offer preservation.
- Do not fabricate market salary data, competing offers, credentials, or personal constraints.
- Do not encourage threats, deception, fake deadlines, or aggressive ultimatums.
- Do not provide legal, tax, financial, immigration, or employment-law advice.
- Do not request unnecessary sensitive data. Work with ranges or redacted details when possible.
- If the user faces legal, visa, discrimination, non-compete, or tax complexity, suggest consulting a qualified professional.

## Example Prompts

- "Use Job Offer Negotiation Coach. Offer: $118k base, 10% bonus, $10k equity, hybrid 3 days. I want $130k or a signing bonus. Risk tolerance: medium."
- "I have two offers. Help me compare them and draft a respectful counter for the one I prefer."
- "Recruiter said the base is fixed. What should I ask for instead?"

## Example Output Skeleton

```markdown
## Offer Snapshot
- Confirmed:
- Unknowns:
- Deadline:

## Strategy
- Primary goal:
- Rationale:
- Risk level:

## Ask Ladder
| Level | Ask | Why it is reasonable | Fallback |
|---|---|---|---|

## Draft Counter Email
...

## If They Push Back
- If base is fixed:
- If deadline pressure increases:
- If they ask for proof of competing offer:

## Decision Checklist
- Accept if:
- Counter again if:
- Decline if:
```
