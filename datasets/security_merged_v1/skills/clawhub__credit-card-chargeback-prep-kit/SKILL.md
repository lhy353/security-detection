---
name: credit-card-chargeback-prep-kit
description: "Prepare a truthful credit card chargeback evidence packet for unauthorized charges, goods not received, canceled or refunded orders not credited, duplicate billing, wrong amounts, defective or not-as-described items, or services not delivered. Use when the user needs a transaction summary, issue classification, evidence timeline, merchant-contact log, issuer-call script, follow-up tracker, and redaction reminders before contacting the merchant or card issuer."
---
# Credit Card Chargeback Prep Kit

## Purpose

Organize a potential credit card chargeback into a clear, truthful preparation packet before the user contacts a merchant or card issuer. Focus on facts, evidence, deadlines, safe redaction, and calm communication.

This is a prompt-only consumer documentation workflow. It is not legal, banking, fraud-investigation, financial, or consumer-rights advice.

## Use This Skill When

Use this skill when the user reports a credit card transaction involving:

- A suspected unauthorized charge.
- Goods or tickets not received.
- A canceled order, return, or refund that was not credited.
- Duplicate billing or wrong amount charged.
- Defective, damaged, incorrect, counterfeit, or not-as-described goods.
- Travel, event, lodging, delivery, repair, subscription, or service failure.
- Merchant refusal, support deadlock, or confusing evidence requirements.
- A need to prepare before calling, chatting, or uploading documents to a card issuer.

Do not use it to create false disputes, hide valid purchases, abuse chargeback rights, fabricate merchant contact, or evade legitimate debts.

## Best Inputs

Ask for only what is needed. Use placeholders for sensitive details and proceed with a missing-information list when needed.

- Card issuer name, using only the issuer name and last four digits if needed.
- Transaction date, posting date, merchant, amount, currency, and order number.
- Product, service, subscription, trip, event, or booking involved.
- What went wrong and what resolution the user wants.
- Whether the user recognizes the merchant.
- Evidence available: receipt, order confirmation, tracking, delivery proof, cancellation, return proof, refund promise, screenshots, photos, terms, policy pages, or support messages.
- Merchant contact attempts: date, channel, ticket number, response, and next promise.
- Issuer deadline, evidence upload deadline, or provisional credit notice if known.

## Workflow

1. **Record the transaction.** Capture issuer, transaction date, posting date, merchant, amount, order number, item or service, and known deadline without requesting full card numbers or credentials.
2. **Classify the issue.** Label it as unauthorized, goods not received, refund not credited, duplicate charge, wrong amount, defective or not as described, canceled service, service not delivered, or other.
3. **Check urgency.** For suspected unauthorized activity, tell the user to contact the card issuer promptly through an official channel and follow issuer instructions.
4. **Build the evidence timeline.** Put purchase, confirmation, expected delivery or service date, problem discovery, merchant contact, promised refund or fix, return, cancellation, and issuer contact in chronological order.
5. **Map evidence to claims.** Match each statement to supporting proof and identify gaps that could weaken the dispute.
6. **Draft merchant contact if appropriate.** Prepare a concise correction or refund request unless the issue appears unauthorized, unsafe, or the issuer has instructed otherwise.
7. **Prepare issuer-facing notes.** Summarize what happened, what the user already tried, what evidence exists, and what outcome is sought.
8. **Create the call or chat script.** Give the user short phrasing for opening the case, answering likely questions, and asking about deadlines, evidence upload, provisional credit, and next steps.
9. **Set up the follow-up tracker.** Record case number, representative, date and time, promised actions, evidence due date, provisional credit status, final decision, and next follow-up.
10. **Add redaction reminders.** Mark what to hide before sharing screenshots or statements.

## Output Format

Return the packet in this order:

1. **Chargeback Snapshot**

| Field | Detail |
|---|---|
| Card issuer | |
| Merchant | |
| Amount and currency | |
| Transaction date | |
| Posting date | |
| Order or reference number | |
| Issue type | |
| Requested outcome | |
| Known deadline | |

2. **Issue Classification**

State the most likely category and why it fits. Include any category uncertainty.

3. **Evidence Timeline**

| Date | Event | Evidence or file to attach | Gap or note |
|---|---|---|---|

4. **Evidence Checklist**

| Evidence type | Available | Still needed | Redaction note |
|---|---|---|---|

5. **Merchant Contact Log and Message**

Include prior contact attempts, then provide a copy-ready merchant message if appropriate.

6. **Issuer Call or Chat Script**

Include:

- Opening summary.
- Key facts to provide.
- Evidence to mention.
- Questions to ask about case number, upload deadline, provisional credit, and expected timeline.
- A short closing confirmation request.

7. **Follow-Up Tracker**

| Date | Channel | Case or ticket number | Person | Promise or result | Next action |
|---|---|---|---|---|---|

8. **Open Questions**

List only the missing facts that would materially improve the packet.

## Message Style

- Be accurate, concise, chronological, and calm.
- Distinguish known facts from assumptions.
- Ask for a specific remedy: refund, credit, reversal, correction, or explanation.
- Keep accusations out of merchant messages unless the user has strong evidence and the wording remains factual.
- Use placeholders and redactions for sensitive data.

## Safety Boundary

- Do not provide legal, banking, fraud-investigation, financial, or consumer-rights advice.
- Do not encourage false disputes, chargeback abuse, document falsification, false police reports, or hiding relevant facts.
- Do not guarantee a refund, reversal, provisional credit, timeline, or issuer decision.
- Do not ask for full card numbers, CVV, PIN, full SSN, bank account numbers, passwords, one-time codes, login credentials, or unredacted statements.
- For suspected unauthorized charges, account takeover, identity theft, large losses, repeated fraud, threats, or safety concerns, direct the user to contact the card issuer promptly through official channels and consider appropriate professional, regulator, or law-enforcement guidance.
- Follow issuer, merchant, card-network, marketplace, and regulator instructions supplied by the user.

## Example Prompts

- "I ordered a laptop that never arrived. Help me prepare a card dispute packet."
- "A hotel charged me twice. What evidence should I organize before calling my issuer?"
- "My canceled subscription was still billed on my credit card."
- "The merchant promised a refund but it never posted. Build my chargeback notes."
- "I see a credit card charge I do not recognize. Help me prepare before I call the issuer."
