---
name: Household Renewal Command Center
description: Build a household renewal tracker for IDs, passports, insurance, vehicle registration, warranties, subscriptions, school forms, and medical paperwork.
version: "1.0.0"
type: prompt-flow
tags:
  - household-admin
  - renewal-tracker
  - family-organization
  - documents
  - reminders
  - planning
author: OpenClaw Skills
---

# Household Renewal Command Center

## Purpose

Household Renewal Command Center helps a user prevent missed renewals by turning scattered household obligations into one practical tracker. It covers documents, plans, permits, policies, warranties, subscriptions, school forms, medical forms, and other recurring admin tasks.

This is a prompt-only organization framework. It does not store sensitive documents, manage accounts, submit forms, or replace official renewal instructions.

## Trigger

Use this skill when the user says things like:

- "I keep missing document renewals."
- "Help me make a family renewal tracker."
- "I need a passport, insurance, and registration command center."
- "Organize household admin deadlines."
- "Make a renewal reminder system for my family."
- "What documents expire soon?"

## Inputs to Request

Ask for a high-level inventory, not sensitive numbers:

1. Household members or item owners, using names, initials, or roles.
2. Renewal items such as passports, IDs, licenses, registrations, insurance, leases, warranties, subscriptions, school forms, medical paperwork, permits, and memberships.
3. Expiration or renewal dates when known.
4. Renewal windows, fees, required evidence, and official source to check.
5. Current document location at a safe level, such as "fire safe," "password manager," or "cloud folder," not full account secrets.
6. Preferred reminder cadence.
7. Backup owner for each important item.

Do not ask for full ID numbers, passport numbers, insurance policy numbers, account passwords, security answers, or document images unless the user explicitly chooses to manage them outside this prompt.

## Deliverable

Produce a household renewal command center with:

- A renewal tracker table.
- Item owner and backup owner.
- Category and urgency.
- Expiration or renewal date.
- Lead time and reminder schedule.
- Required evidence or documents.
- Safe document-location note.
- Official renewal channel to check.
- Next action and monthly review list.
- Immediate risk list for items due soon, missing details, or lacking an owner.

## Workflow

### Step 1 - Build the Renewal Inventory

Invite the user to list all relevant household items. Use categories to prompt memory:

- Identity: passports, national or state IDs, driver licenses, visas, residence permits.
- Mobility: vehicle registration, inspection, parking permit, transit pass.
- Home: lease, mortgage review, renters insurance, homeowners insurance, utilities, property tax reminders.
- Health: insurance cards, medical forms, prescriptions that need periodic review, vaccination records.
- School and childcare: enrollment forms, consent forms, activity waivers, lunch accounts.
- Money and subscriptions: credit cards with annual fees, membership renewals, software, streaming, storage.
- Property and devices: warranties, service contracts, appliance filters, home safety checks.
- Pets: licenses, vaccinations, insurance, medication reminders.

### Step 2 - Group by Person, Category, and Urgency

Assign each item to a person, household role, or shared owner. Group the list by category and urgency:

- Due now or overdue.
- Due within 30 days.
- Due within 60 days.
- Due within 90 days.
- Later or date unknown.

### Step 3 - Capture Renewal Facts

For each item, collect the details needed to act:

- Expiration or renewal date.
- Earliest renewal date or renewal window.
- Estimated fee.
- Required evidence.
- Processing time.
- Official website, office, provider, or contact channel.
- Whether in-person action, mail, appointment, or notarization is needed.

Use "unknown" when a detail is missing. Do not invent dates or requirements.

### Step 4 - Assign Owner and Backup

Every item needs one primary owner and one backup owner. If the user is a one-person household, the backup can be a trusted contact, calendar note, or emergency file instruction.

Flag items with no owner as system risks.

### Step 5 - Set Reminder Cadence

Create reminders based on lead time. Default cadence:

- 90 days before expiration for complex or travel-related items.
- 60 days before expiration for insurance, registrations, and school items.
- 30 days before expiration for simpler renewals.
- 7 days before expiration as a final check.
- Monthly admin review for all unknown or upcoming items.

Adjust for local rules, processing delays, travel plans, and the user's preference.

### Step 6 - Identify Missing Evidence and Access Gaps

List what is needed before renewal can happen:

- Missing scans or photos.
- Proof of address.
- Birth certificates or marriage certificates.
- Receipts or warranty proof.
- Appointment access.
- Account login stored in a password manager.
- Payment method.
- Official form.

Do not request the sensitive material itself. Ask the user to store it securely outside the prompt.

### Step 7 - Create the Monthly Admin Review

Build a recurring monthly review checklist:

1. Check items due in the next 90 days.
2. Confirm unknown dates.
3. Update document locations.
4. Review recent purchases for warranty registration.
5. Confirm insurance and subscription renewals.
6. Assign next actions.
7. Archive completed renewals.

### Step 8 - Produce the Command Center

Return the tracker in this format unless the user requests another layout:

| Item | Owner | Backup | Category | Expiration or renewal date | Lead time | Required evidence | Safe location note | Reminder dates | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Then provide:

- Top 5 urgent actions.
- Unknown-date cleanup list.
- Monthly review checklist.
- Suggestions for secure storage and reminder placement.

## Safety Boundary

- Do not request or store full document numbers, passwords, security answers, or sensitive images.
- Do not claim official renewal requirements without prompting the user to confirm with the relevant authority or provider.
- Do not submit forms, make payments, or contact providers on the user's behalf.
- Recommend secure storage such as a password manager, encrypted local storage, or a physical safe for sensitive documents.
- For immigration, legal, medical, insurance, or tax matters, recommend checking official instructions or qualified professionals.

## Acceptance Criteria

A successful run includes:

1. A categorized inventory of household renewal items.
2. Owner and backup owner assigned for each important item.
3. Expiration or renewal date captured or marked unknown.
4. Required evidence and safe location note captured without sensitive numbers.
5. Reminder cadence created from lead times.
6. Missing evidence and access gaps identified.
7. Monthly admin review checklist produced.
8. Immediate next actions ranked by urgency.
