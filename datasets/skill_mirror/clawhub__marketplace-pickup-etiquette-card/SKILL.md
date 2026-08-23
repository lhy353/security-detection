---
name: marketplace-pickup-etiquette-card
displayName: "Marketplace Pickup Etiquette Card"
version: "1.0.0"
description: "Create a courteous marketplace pickup etiquette card for arranging simple public or common-area handoffs, timing, item checks, message templates, and polite reset steps without fraud, payment, identity, or legal claims."
triggerKeywords:
  - marketplace pickup etiquette
  - pickup handoff card
  - local sale pickup message
  - porch pickup etiquette
  - public pickup meetup
  - buyer seller handoff
  - common area pickup
  - marketplace meetup checklist
tags:
  - marketplace
  - etiquette
  - local-pickup
  - communication
  - checklist
license: "MIT-0"
language: "en"
hasExecutableCode: false
promptOnly: true
execution: "noExec"
---

# Marketplace Pickup Etiquette Card

## Purpose

Use this prompt-only skill when a user wants a short etiquette card for arranging a local marketplace pickup or handoff. The deliverable helps buyer and seller agree on a safe-feeling public or common-area location, arrival window, item description, check steps, and polite messages for delays, changes, and completion.

This skill is for ordinary scheduling and courtesy only. It does not provide fraud prevention guarantees, payment advice, identity verification advice, legal advice, dispute handling, platform policy interpretation, or law enforcement guidance.

## Safety Boundary

Keep guidance limited to courteous, practical handoff planning in public places or shared common areas. Encourage meeting during reasonable hours, choosing a visible location, keeping the plan simple, and letting someone know the pickup plan if the user wants extra comfort.

Do not make claims about fraud prevention, payment safety, identity confirmation, legal rights, contracts, liability, trespass, weapon carry, surveillance, police involvement, or platform enforcement. Do not advise sharing sensitive personal data, private home access codes, full daily schedules, financial information, identity documents, or legal threats.

## Core Principles

- Make the handoff easy to find and easy to leave.
- Use clear time windows instead of vague timing.
- Confirm item, location, and arrival details in writing.
- Keep messages brief, polite, and specific.
- Prefer visible public or common-area handoff points.
- Avoid sensitive personal, financial, identity, or legal details.

## Required Inputs

Ask only for details needed to draft the card:

- User role: buyer, seller, giver, receiver, or both.
- Item type and size: small, bulky, fragile, heavy, or curbside item.
- Pickup style: public meet, apartment lobby, building common area, workplace reception, curbside, or porch pickup.
- Preferred timing: exact time, short arrival window, same-day pickup, or scheduled date.
- Communication channel: marketplace chat, text, email, or other plain message channel.
- Accessibility or logistics needs: parking, elevator, loading zone, weather cover, carrying help, or no-contact preference.
- Whether the user needs buyer messages, seller messages, or both.

Do not ask for addresses, phone numbers, payment details, legal documents, ID details, or private access codes unless the user has already provided them and they are necessary to restate as placeholders.

## Workflow

1. **Clarify the handoff type.** Identify whether the user needs a public meet, common-area pickup, porch pickup, curbside handoff, or bulky-item plan.
2. **Set a simple location description.** Use a visible public place or common-area description, with placeholders instead of private details when possible.
3. **Set the time window.** Convert vague timing into a clear arrival window and a cutoff for rescheduling.
4. **Confirm item basics.** Include item name, color or distinguishing detail, quantity, and whether help is needed to carry it.
5. **Draft etiquette rules.** Include arrive on time, message before leaving, keep messages brief, check the item promptly, and leave the spot tidy.
6. **Draft message templates.** Provide short templates for initial confirmation, on my way, running late, arrived, need to reschedule, pickup complete, and courteous cancellation.
7. **Add reset steps.** Include what to do if timing slips: send one clear update, offer a new window, or pause the pickup plan.
8. **Remove unsafe overreach.** Strip fraud, payment, identity, legal, platform-policy, or enforcement claims from the final card.

## Output Format

Return a marketplace pickup etiquette card with these sections:

1. **Pickup Snapshot**
   - Role
   - Item
   - Pickup style
   - Location placeholder
   - Time window
   - Weather or access note
2. **Before Pickup**
   - Confirm item and time
   - Share concise location details
   - Agree on arrival message
   - Prepare item for quick handoff
   - Bring carry help if needed
3. **Good Handoff Manners**
   - Arrive within the window
   - Message before leaving or on arrival
   - Keep the handoff brief
   - Check the item promptly
   - Leave the area tidy
4. **Message Templates**
   - Confirming the pickup
   - On my way
   - Running late
   - Arrived
   - Need to reschedule
   - Pickup complete
   - Courteous cancellation
5. **Public or Common-Area Comfort Checks**
   - Visible meeting spot
   - Reasonable hour
   - Easy parking or loading note
   - No private access codes in chat
   - Let someone know the plan if desired
6. **Delay Reset**
   - Send one clear update
   - Offer a new short window
   - Pause if timing no longer works
   - Keep the tone neutral
7. **Keep Out of the Card**
   - Payment claims
   - Identity claims
   - Fraud guarantees
   - Legal threats or legal advice
   - Sensitive personal details

## Example Prompts

Copy any prompt below and paste it to your AI agent. Fill in your pickup details.

**Public meetup for a used chair:**
> I'm selling a desk chair on a local marketplace and a buyer wants to pick it up. I'd prefer to meet at the coffee shop on Main Street. Help me create a pickup etiquette card with message templates for confirming, arriving, and completing the handoff. The chair is bulky so they may need help carrying it.

**Porch pickup for a small item:**
> I'm giving away a set of plant pots for free on a neighborhood group. Someone is coming by tomorrow between 10 AM and noon to pick them up from my porch. I want a simple etiquette card with a confirmation message template and a note about leaving the area tidy. No-contact pickup is fine.

**Apartment lobby handoff:**
> I bought a used bookshelf and I'm picking it up from someone's apartment building lobby this evening. I want a buyer-side etiquette card with: confirming the time, what to message when I arrive, and how to check the item quickly without being awkward.

## Quality Bar

A strong result feels like a concise etiquette card someone can paste into a marketplace chat or keep as a pickup checklist. It should make timing and handoff expectations clear while avoiding fraud, payment, identity, and legal claims.
