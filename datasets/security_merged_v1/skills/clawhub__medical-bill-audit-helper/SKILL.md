---
name: Medical Bill Audit Helper
description: Turn confusing medical bills and EOBs into a clear audit — organize line items, identify questions to verify, and prepare calm, effective call scripts. No medical, insurance, or legal advice.
version: "1.0.0"
type: prompt-flow
tags:
  - medical-billing
  - bill-audit
  - healthcare-costs
  - insurance-eob
  - patient-advocacy
  - family-caregiving
  - personal-finance
author: Harry (code) & Bell (design)
---

# Medical Bill Audit Helper

## ⚠️ Important Safety & Disclaimer — Read First

**This skill is NOT medical, insurance, legal, tax, or financial advice.** It is a document organization and question-preparation tool only.

**What this skill does:**
- Help you organize bill and EOB (Explanation of Benefits) information into a clear, structured format
- Identify line items that look inconsistent or deserve a second look
- Flag missing information that you may need before calling a provider or insurer
- Draft calm, fact-based call scripts for provider billing offices and insurance companies
- Provide a follow-up log template so you can track your conversations

**What this skill does NOT do:**
- ❌ Diagnose whether a charge is definitively wrong, fraudulent, or should be removed
- ❌ Give medical advice, treatment recommendations, or clinical guidance
- ❌ Provide insurance coverage determinations, legal opinions, or financial advice
- ❌ Promise refunds, coverage, appeal success, or specific financial outcomes
- ❌ Replace professional bill reviewers, patient advocates, attorneys, or financial counselors

**Privacy & PII Protection — Critical:**
- 🔒 **Redact before pasting:** Remove your full SSN, full insurance ID/member number, date of birth, home address, medical record numbers (MRN), and any specific diagnosis details you prefer to keep private.
- 🔒 You may use placeholders: `[Member ID: XXX-1234]`, `[DOB redacted]`, `[MRN redacted]`
- 🔒 This skill does not store, transmit, or share your data
- 🔒 **Never share your full Social Security Number, insurance ID, or other sensitive identifiers in any conversation with an AI assistant.**

**If you are facing an active medical emergency, call emergency services immediately.**
**If you believe a bill contains fraudulent charges and you need legal help, consult an attorney.**

---

## Overview

The Medical Bill Audit Helper is a billing detective that helps patients, caregivers, and family members make sense of confusing medical bills, Explanation of Benefits (EOB) statements, invoices, pharmacy receipts, and lab charges.

Medical billing is intimidating. Even small mistakes can cost hundreds or thousands of dollars. This skill turns confusing documents into:
- A clear, plain-English bill summary
- A "numbers to verify" table highlighting items that need attention
- A missing-information checklist
- Ready-to-use call scripts for provider billing offices and insurance companies
- A follow-up log to track every conversation

You provide the bill and EOB information (after redacting sensitive details). This skill gives you the organized evidence and questions you need before you pay.

## When to Use

Use this skill when you:

- Receive a medical bill that doesn't match what you expected to pay
- Have both a provider bill and an insurance EOB and need to reconcile them
- See charges you don't understand or recognize
- Suspect duplicate billing, services you didn't receive, or unexpected amounts
- Need to prepare for a call with a provider billing office or insurance company
- Are helping a family member or loved one sort through medical bills
- Want to track billing conversations and follow-ups systematically
- Received an insurance denial and want to organize your appeal preparation (this skill helps you organize — it does not determine if your appeal will succeed)

**Trigger phrases:** "Audit my medical bill," "Check this EOB," "Medical bill doesn't match," "Help me understand this hospital bill," "Is my medical bill correct?", "Insurance didn't cover what I expected," "Prepare me for a billing call"

## Workflow

### Step 1 — Intake: Gather Bill & EOB Information

Ask the user to provide (after redacting sensitive PII) as much of the following as available. The more detail, the more thorough the audit.

**Provider Bill Information:**
- Date of service
- Provider name (doctor, hospital, lab, imaging center, pharmacy, etc.)
- Provider type (in-network, out-of-network, or unknown)
- Each line item: service description, CPT/HCPCS code if shown, billed/charged amount
- Total amount the provider is asking you to pay
- Bill date and due date
- Any payments already made toward this bill

**Insurance EOB Information (if available):**
- Date of service matching the bill
- Provider name as shown on EOB
- Each line item: billed amount, allowed/negotiated amount, plan paid amount, patient responsibility
- Deductible applied, co-pay applied, co-insurance applied
- Any denial codes, remark codes, or adjustment reasons listed
- Whether the EOB says "this is not a bill"

**Additional Context:**
- Did you receive the service? (confirm actual visit/procedure/lab occurred)
- Did you receive everything listed in the line items?
- Was the provider in-network at the time of service? (to the best of your knowledge)
- Did you have prior authorization if required?
- Have you already contacted the provider or insurer about this bill? If so, what was said?
- Are there multiple bills or EOBs for the same date/service?

### Step 2 — Build the Bill Summary

Produce a clear, plain-English summary of what the user is looking at. This is the foundation for everything that follows.

**Bill Summary Format:**

```
## Bill Summary

**Provider:** [Name]
**Date(s) of Service:** [Date(s)]
**Service Category:** [Office visit / Hospital stay / Lab work / Imaging / Surgery / Pharmacy / Emergency / Other]
**Insurance Plan Type (if known):** [HMO / PPO / HDHP / Medicare / Medicaid / Other / Unknown]

**What the Provider Billed:** $[total billed amount]
**What Insurance Allowed (negotiated rate):** $[allowed amount, if EOB available]
**What Insurance Paid:** $[plan paid amount, if available]
**What Provider Says You Owe:** $[patient responsibility per provider bill]
**What EOB Says You Owe:** $[patient responsibility per EOB, if available]
**Amounts You've Already Paid:** $[total paid toward this bill]

**Discrepancy Flag (if applicable):**
[If provider-bill patient responsibility ≠ EOB patient responsibility, highlight it here]

**At a Glance:**
- [Bullet summary in plain English — "You had a specialist visit on 3/15. The provider billed $850. Insurance negotiated it down to $320, paid $200, and the EOB says you owe $120. But the provider's bill asks for $180. That's a $60 gap to investigate."]
```

### Step 3 — Create the Numbers-to-Verify Table

Build a structured table of every line item with key comparison columns. Flag items that look inconsistent or deserve a closer look before paying.

**Numbers-to-Verify Table Format:**

| # | Date | Provider/Dept | Service Description | Code (if shown) | Billed Amount | Allowed Amount | Plan Paid | Patient Responsibility (per EOB) | Provider Asks | Flag |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 3/15 | Dr. Smith | Office Visit, Level 3 | 99213 | $250 | $180 | $130 | $50 | $50 | ✅ Match |
| 2 | 3/15 | Same-Day Lab | Blood Panel | 80053 | $600 | $140 | $70 | $70 | $130 | ⚠️ $60 gap |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

**Flag Legend:**
- ✅ **Match:** EOB patient responsibility matches provider bill
- ⚠️ **Gap:** Provider asks more than EOB says you owe — question to verify
- 🔍 **No EOB Match:** Line item on provider bill but not on EOB — may not have been submitted to insurance
- 🔄 **Possible Duplicate:** Similar service, date, and amount appearing more than once
- ❓ **Unclear Description:** Service description is vague or you don't recall receiving it
- 📋 **Need Code Verification:** Code description doesn't match the service you received
- ⚕️ **Out-of-Network:** Provider or facility is out-of-network; amounts may differ from in-network expectations

**For each flagged item, add a "Question to Verify" note, for example:**
> **Line #2:** "The provider bill asks for $130, but the EOB says your responsibility is $70. This is a $60 gap. Call the provider billing office and ask: 'My EOB from [Insurance] shows my responsibility for this lab panel is $70, but your bill says $130. Can you help me reconcile this difference?'"

**Important Note on Arithmetic:**
This skill may flag arithmetic inconsistencies when the user-provided numbers clearly don't add up (e.g., "You said you paid $200, the bill says $500 was billed, and they are asking for $400 — that totals $600 against a $500 billed amount."). In all other cases, inconsistencies are phrased as **"questions to verify"** — this skill does not declare charges definitively invalid.

### Step 4 — Missing Information Checklist

Check what information the user still needs before they can confidently pay, dispute, or negotiate. Present as a checklist.

**Missing Information Checklist Format:**

```
## What You Still Need Before You Act

**From the Provider Billing Office:**
☐ Itemized bill with CPT/HCPCS codes (if you only received a summary bill)
☐ Confirmation of whether all services were submitted to insurance
☐ Explanation for any line items where provider asks more than EOB patient responsibility
☐ Confirmation of in-network vs. out-of-network status at time of service
☐ Documentation of any prior authorization obtained (or reason for denial if not obtained)
☐ [Add context-specific items based on the user's case]

**From the Insurance Company:**
☐ Complete EOB for the date(s) of service (if missing)
☐ Explanation of any denial codes or adjustment reasons listed on the EOB
☐ Confirmation of deductible status: how much of your annual deductible was met at time of service
☐ Confirmation of out-of-pocket maximum status
☐ Clarification on whether specific services required prior authorization
☐ [Add context-specific items based on the user's case]

**From Yourself / Your Records:**
☐ Your own notes about the visit: what services you actually received, who you saw, how long
☐ Any appointment confirmation, referral, or prior-authorization documentation you may have
☐ Your insurance plan documents: summary of benefits, deductible, co-pay, co-insurance amounts
☐ Receipts or confirmation numbers for any payments you've already made
```

### Step 5 — Provider Billing Office Call Script

Create a calm, fact-based call script the user can follow when contacting the provider's billing office. Emphasize being polite, prepared, and persistent.

**Provider Call Script Format:**

```
## Provider Billing Office Call Script

**Before You Call:**
☐ Have the bill, your insurance card, and your notes in front of you
☐ Have the numbers-to-verify table (Step 3) open — know exactly which line items to ask about
☐ Note the date of service and provider name as it appears on the bill
☐ Know your insurance ID (last 4 digits only if you prefer)
☐ Set aside 20-30 minutes; billing calls can involve holds and transfers

**Opening:**
"Hello, my name is [Your Name]. I'm calling about bill [Bill/Account Number, if shown] for a visit on [Date of Service] with [Provider Name]. I have my insurance EOB in front of me, and I have some questions I'm hoping you can help me with."

**Key Questions (customize from flagged items in Step 3):**
1. [If there's a gap between EOB and bill amount:]
   "My EOB from [Insurance Company] shows my patient responsibility is $[EOB amount] for [describe service], but the bill I received asks for $[bill amount]. Can you help me understand the difference?"

2. [If you received an EOB that says "this is not a bill" but now have a bill:]
   "I received an EOB that said the amount I owe is $[EOB amount]. Your bill is asking for a different amount. Has something changed since the EOB was issued?"

3. [If you don't recognize a charge:]
   "I'm looking at line [item] for [describe service]. I don't recall receiving this service. Can you tell me more about what this charge is for and who ordered it?"

4. [If something looks like a duplicate:]
   "I see two charges on [date] for [service] — one for $[A] and one for $[B]. These look similar. Are both correct, or could this be a duplicate?"

5. [If prior authorization is at issue:]
   "Was prior authorization obtained for this [service/procedure]? If not, can you tell me why?"

**Closing:**
"Thank you for your help. Can you give me a reference number for this call and let me know when I should expect an update? And is there a direct number I can call if I have follow-up questions?"

**Notes During the Call:**
- Write down the name of every person you speak with
- Write down the date, time, and reference/case number
- If they promise to send something, ask when and how (mail, email, portal)
- If they say "you need to call your insurance instead," ask them to confirm in writing what they've told you
- If you disagree with their answer, it's okay to say: "I understand your position. Can you note in my account that I am disputing this charge, and can you put a hold on collections for this item while I follow up with my insurance?"
```

### Step 6 — Insurer Call Script

Create a similar call script for the insurance company. Focus on understanding coverage, denials, and the EOB explanation.

**Insurer Call Script Format:**

```
## Insurer Call Script

**Before You Call:**
☐ Have your insurance card (member ID ready, last 4 digits if you prefer)
☐ Have the EOB and the provider bill in front of you
☐ Have the numbers-to-verify table (Step 3) open
☐ Know the date of service, provider name, and tax ID/NPI if shown on the bill
☐ Note the specific claim number from the EOB if available

**Opening:**
"Hello, my name is [Your Name], member ID ending in [last 4 digits]. I'm calling about claim [Claim Number] for a visit on [Date of Service] with [Provider Name]. I have questions about the EOB I received."

**Key Questions (customize from your case):**
1. [If the EOB denied a service or paid less than expected:]
   "I see on my EOB that [service] was [denied / paid at a lower amount than expected]. The reason code says [code/reason if shown]. Can you explain what this means and what I or my provider can do about it?"

2. [If a provider is listed as out-of-network but you believed they were in-network:]
   "The EOB shows [Provider Name] as out-of-network. I believed they were in-network when I received care. Can you verify their network status on [Date of Service]?"

3. [If deductible or co-insurance is unclear:]
   "Can you tell me where I stand with my annual deductible and out-of-pocket maximum? How much had I met by [Date of Service]? And how much of this bill is going toward my deductible versus co-insurance?"

4. [If prior authorization is listed as a reason for denial/reduction:]
   "The EOB lists [prior authorization / no pre-cert] as the reason. Was prior authorization required for this service? If so, did the provider request one?"

5. [If there are adjustment/remark codes you don't understand:]
   "I see code [code] on line item [number]. Can you explain what this code means in plain language?"

**Closing:**
"Thank you. Can you give me a reference number for this call? Will you be sending me an updated EOB or any documentation by mail? And is there an appeal process I should know about if I disagree with this determination?"

**Notes During the Call:**
- Write down the rep's name and call reference number
- Ask them to note in the claim file that you called and what was discussed
- If they say they'll reprocess, ask for a timeline and confirmation method
- If the rep can't answer, politely ask to speak with a claims specialist or supervisor
```

### Step 7 — Follow-Up Log Template

Provide a reusable template the user can fill in after every call or interaction. Tracking is essential because billing disputes can span weeks or months.

**Follow-Up Log Template:**

```
## Follow-Up Log

**Bill/Account Reference:** [Provider Name | Date of Service | Bill Number]

---

**Entry #1**
- **Date & Time:**
- **Who I Called:** [Provider Billing / Insurance Company]
- **Phone Number Used:**
- **Person I Spoke With (name & title):**
- **Reference/Case Number Given:**
- **What I Asked:**
- **What They Said / Promised:**
- **Action Items:**
  - [ ] [Action — e.g., "They will send updated bill by 4/10"]
  - [ ] [Action — e.g., "I need to call insurance next"]
- **Next Step & When:**

---

**Entry #2**
- **Date & Time:**
- **Who I Called:**
- **Phone Number Used:**
- **Person I Spoke With (name & title):**
- **Reference/Case Number Given:**
- **What I Asked:**
- **What They Said / Promised:**
- **Action Items:**
  - [ ] [Action]
- **Next Step & When:**

---

[... continue for each interaction]

---

**Status Summary (update as you go):**
- [ ] Bill audited — flagged items identified
- [ ] Provider billing office contacted — [Date]
- [ ] Insurance company contacted — [Date]
- [ ] All discrepancies explained or resolved
- [ ] Payment made — [Date & Amount]
- [ ] Case closed
```

### Step 8 — Appeal Preparation Checklist (Conditional)

**Only trigger this step if the user explicitly provides:**
- An official insurance denial letter (or a redacted excerpt from one)
- An EOB showing denial codes or denial reason text
- A written insurer explanation/reason for denial
- Equivalent written insurer reason text describing why coverage was denied or a charge was not adjusted

**If the user asks about appeals in general without providing official denial/reason text** (e.g., "How do I appeal?" or "they refused to adjust" without supporting documentation), do NOT generate the full appeal checklist. Instead, output a **Missing Information Prompt** asking the user to obtain and share (redacted) the official denial reason/code first:

> ⚠️ **Before preparing an appeal, I need more information.** Please obtain the official denial letter or EOB with the denial reason/codes. You can redact or describe the reason text in your own words. Once I have the written insurer reason, I can help you build a targeted appeal preparation checklist.

**Do not generate the full Appeal Preparation Checklist without official denial/reason text.**

**Appeal Preparation Checklist Format:**

```
## Appeal Preparation Checklist

⚠️ **This checklist helps you organize — it does NOT determine whether your appeal will succeed or replace legal/insurance professional advice.**

**Before You Start an Appeal:**
☐ Obtain the official denial letter or EOB showing the denial reason and codes
☐ Check your plan's appeal deadline — this is usually strict (e.g., 180 days from denial date)
☐ Locate your plan's appeal process instructions (member portal, plan documents, or call member services)

**Evidence to Gather:**
☐ The original bill and all related EOBs
☐ Your notes from all calls (from your Follow-Up Log)
☐ Any written correspondence from the provider or insurer
☐ Medical records relevant to the disputed service (you may need to request these from the provider)
☐ A letter from your provider supporting medical necessity (if the denial was based on medical necessity)
☐ Your plan documents showing coverage for the disputed service

**Letter Drafting Guidance:**
- Be concise and factual — state what was denied, when, the claim number, and why you believe it should be covered
- Reference specific plan language if available (e.g., "My plan documents state that [service] is a covered benefit")
- Attach supporting documents and keep copies of everything you send
- Send via certified mail or your insurer's online appeal portal so you have proof of submission
- Keep a copy of everything for your records

**Questions to Ask Your Insurer Before Filing:**
☐ What is the exact deadline for filing this appeal?
☐ What specific documents do you need from me?
☐ Is there an expedited/internal appeal option? An external review option?
☐ Will collections be paused while the appeal is pending?
☐ Who will review my appeal, and how long does a decision typically take?

**After Filing:**
☐ Log the submission in your Follow-Up Log (date, method, tracking number)
☐ Mark your calendar for the expected decision date
☐ If denied again, ask about the next level of appeal or external review
```

## Sample Invocation

**Example 1 — Simple Bill-EOB Mismatch:**
> **User:** "I have a $740 bill from City Hospital for an ER visit on February 12. My insurance EOB says the allowed amount was $3,200, the plan paid $3,020, and my patient responsibility is $180. But the hospital bill says I owe $740. Here are the details: [pasted itemized lines, PII redacted]. Help me audit what to ask before I pay."

**Skill Response:** The skill would produce a full bill summary highlighting the $560 gap between the EOB's $180 patient responsibility and the bill's $740 demand, flag each line item in the numbers-to-verify table with the ⚠️ "Gap" flag, list missing information (e.g., "Has the hospital submitted all charges to insurance?"), and produce a provider call script focused on reconciling the discrepancy.

**Example 2 — Unclear Charges:**
> **User:** "My dentist sent a bill for $350. The EOB says I owe $50. I also see a $200 charge for something called 'D4910' — I have no idea what that is. I only went in for a cleaning and filling."

**Skill Response:** The skill would flag the D4910 charge with ❓ "Unclear Description," note the provider-EOB gap, suggest the user confirm what D4910 is (periodontal maintenance, which may differ from a routine cleaning) and whether it was actually performed, and draft a provider call script asking for an explanation.

**Example 3 — Helping a Family Member:**
> **User:** "My dad got four bills after a 3-day hospital stay. Different bills from the hospital, the ER doctors, the anesthesiologist, and a lab. Some overlap. I'm confused and don't know which to pay first."

**Skill Response:** The skill would organize all four bills into a consolidated view, cross-reference dates and services, flag any overlapping charges as 🔄 "Possible Duplicate," create a timeline of services, and recommend the user confirm with each provider that their charges were submitted to insurance before paying anything.

## Output Structure Summary

Every audit response should include (as applicable to the user's information):

1. **Bill Summary** — Plain-English overview with key amounts and discrepancy flags
2. **Numbers-to-Verify Table** — Line-by-line comparison with flag icons and "question to verify" notes
3. **Missing Information Checklist** — What the user still needs from provider, insurer, and their own records
4. **Provider Billing Office Call Script** — Customized script with specific questions tied to flagged line items
5. **Insurer Call Script** — Customized script for the insurance side of the inquiry
6. **Follow-Up Log Template** — Ready-to-use tracking template
7. **Appeal Preparation Checklist** — Only if the user provides official denial/reason text (denial letter, EOB denial code, or written insurer reason). Generic appeal questions without official documentation trigger a missing-info prompt instead.

## Boundaries & Limitations

- **No medical advice.** This skill does not interpret diagnoses, recommend treatments, or evaluate the medical necessity of services.
- **No insurance coverage determinations.** This skill does not tell users what their plan covers or whether a denial is valid.
- **No legal or financial advice.** This skill does not advise on legal rights, debt collection laws, bankruptcy, or financial planning.
- **No definitive declarations.** Unless the user-provided numbers show a clear arithmetic inconsistency, this skill phrases discrepancies as questions to verify — never as statements that a charge is definitively wrong.
- **No guarantees.** This skill does not promise refunds, coverage, appeal success, balance reductions, or any specific financial outcome.
- **PII protection.** This skill warns users to redact sensitive identifiers before pasting information. It never requests full SSN, full insurance ID, DOB, address, or medical record numbers.
- **No external actions.** This skill does not click links, access portals, submit forms, make calls, or execute any external actions on the user's behalf.
- **No billing fraud investigation.** If a user suspects intentional fraud (e.g., billing for services never rendered), this skill recommends contacting the provider, insurer, and appropriate authorities — it does not conduct fraud investigations.
