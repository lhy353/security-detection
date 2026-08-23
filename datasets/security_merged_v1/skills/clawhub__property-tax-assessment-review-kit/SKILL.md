---
name: property-tax-assessment-review-kit
displayName: Property Tax Assessment Review Kit
description: Organize a property tax assessment notice, deadline, evidence checklist, assessor questions, and appeal packet outline before the review window closes.
version: 1.1.0
license: MIT-0
language: en
tags: [property-tax, assessment-review, appeal-preparation, real-estate]
---

# Property Tax Assessment Review Kit

## Safety Boundary

This skill helps organize facts and paperwork for reviewing a property tax assessment or reassessment notice. It does not provide legal, tax, appraisal, real estate, or jurisdiction-specific advice. It does not estimate official property value, determine whether an appeal should be filed, complete official forms, contact government offices, or guarantee savings.

The user must verify local rules, deadlines, filing requirements, evidence standards, hearing procedures, and official forms with the relevant assessor, tax office, assessment review board, county, city, or qualified professional.

Do not ask for full parcel account credentials, payment details, Social Security numbers, national ID numbers, tax portal passwords, bank information, or copies of private identity documents. Use placeholders for sensitive identifiers.

## When to Use

Use this skill when the user needs to:

- Review a property tax assessment or reassessment notice that seems too high.
- Understand what information to verify before an appeal deadline.
- Organize evidence such as comparable sales, property condition, photos, appraisals, or record errors.
- Prepare neutral questions for the assessor's office.
- Draft a factual appeal narrative outline without exaggeration.
- Build a deadline and follow-up tracker.

Do not use this skill to:

- Decide legal eligibility for appeal.
- Estimate market value or assessed value as an official appraisal.
- Interpret local tax law or binding appeal rules.
- Prepare formal legal filings as a representative.
- Promise a tax reduction or refund.
- Create misleading claims or omit known facts.

## Intake Questions

Ask for user-provided details only:

- What jurisdiction issued the notice? City, county, state, province, or country is enough.
- What is the notice date and stated appeal or review deadline?
- What property type is involved: primary home, condo, rental, land, commercial, inherited property, or other?
- What assessed value is listed, and what was the prior assessed value if known?
- What changed on the notice: land value, building value, classification, exemptions, square footage, rooms, condition, ownership, or tax rate?
- Why does the user think the notice may be wrong?
- What evidence does the user already have: comparable sales, photos, repair estimates, appraisal, inspection report, listing data, prior notices, exemption paperwork, or public records?
- Has the user contacted the assessor's office already? If yes, what was said?

If the appeal deadline is missing or unclear, make deadline verification the first action item.

## Response Workflow

Follow this sequence:

1. State the legal/tax/appraisal boundary and deadline caution.
2. Summarize the notice in user-provided terms.
3. Identify what changed and what must be verified on the notice.
4. Build an evidence checklist grouped by comparable properties, record errors, property condition, exemptions, and supporting documents.
5. Create a folder structure and document naming plan.
6. Draft neutral questions for the assessor or tax office.
7. Create a factual appeal narrative outline that avoids overstatement.
8. Build a deadline and follow-up tracker.
9. Present decision points: informal review, formal appeal, professional appraisal, tax advisor, attorney, or no action after verification.

## Notice Summary

Start with this table:

| Item | User-provided details |
|---|---|
| Jurisdiction | [city/county/state/province/country] |
| Notice date | [date] |
| Appeal or review deadline | [date or unknown] |
| Property type | [home/condo/rental/land/commercial/other] |
| Current assessed value | [amount] |
| Prior assessed value | [amount or unknown] |
| Change amount or percentage | [amount/percent if user provides enough information] |
| Main concern | [too high / record error / exemption issue / condition issue / comparable sales / other] |
| Contact already made | [none or summary] |

Do not calculate official tax impact unless the user provides all numbers and asks for simple arithmetic. Label any arithmetic as user-provided estimate, not advice.

## Notice Verification Checklist

Create a checklist for the user to compare against the notice and public record:

- Owner name or mailing address, using partial or redacted details in the output.
- Parcel or account identifier, redacted if needed.
- Property classification or use code.
- Land size or lot dimensions.
- Building square footage.
- Number of bedrooms, bathrooms, units, parking spaces, or structures.
- Year built, remodel year, or condition rating.
- Exemptions, abatements, caps, freezes, homestead status, senior status, veteran status, disability status, agricultural status, or other local programs.
- Prior assessed value and current assessed value.
- Notice date, appeal deadline, required form, filing method, and hearing or review process.

Mark each as "verified," "possible error," "unknown," or "not applicable."

## Evidence Checklist

Group evidence by type:

### Comparable Property Evidence

- Recent comparable sales near the assessment date, if allowed locally.
- Similar properties by location, size, age, condition, lot, property type, and features.
- Public sales records, listing sheets, closing data, or assessor comparable worksheets.
- Notes explaining why each comparable is similar or different.

### Property Record Error Evidence

- Public record screenshot or copy showing the listed detail.
- User's factual correction: square footage, rooms, lot size, building type, condition, basement, garage, accessory structure, or classification.
- Supporting source such as survey, floor plan, appraisal, permit record, inspection, photos, or prior assessment.

### Condition Evidence

- Dated photos of needed repairs or condition issues.
- Inspection reports.
- Contractor estimates.
- Insurance claim documents, if relevant and safe to share.
- Notes about limitations that existed near the assessment date.

### Exemption or Program Evidence

- Prior exemption approval letters.
- Application receipts.
- Eligibility documents, with sensitive details redacted.
- Correspondence with the tax office.

### Process Evidence

- Notice envelope or delivery date proof, if relevant.
- Call notes, email confirmations, reference numbers, and staff names when voluntarily provided.
- Copies of submitted forms and confirmation receipts.

## Evidence Folder Structure

Suggest a simple folder structure:

```text
Property Tax Assessment Review - [Property Short Name]
01 Notice and Deadlines
02 Property Record Verification
03 Comparable Sales
04 Condition Photos and Repair Evidence
05 Exemptions and Prior Assessments
06 Assessor Questions and Call Log
07 Appeal Draft and Submission Receipts
```

Use consistent filenames:

```text
YYYY-MM-DD_notice_[jurisdiction].pdf
YYYY-MM-DD_photo_[issue].jpg
YYYY-MM-DD_comparable_[address-or-short-label].pdf
YYYY-MM-DD_call-log_assessor-office.txt
```

Do not require the user to upload or expose sensitive documents inside the chat.

## Assessor Office Questions

Draft neutral questions such as:

- What is the appeal or informal review deadline for this notice?
- Which value or property record detail changed from the prior notice?
- What evidence is accepted for comparable sales, condition issues, or record corrections?
- Is there an informal review step before a formal appeal?
- Which form, portal, mailing address, or in-person process is required?
- How should I correct a possible record error such as square footage, rooms, condition, or exemption status?
- What date should comparable sales or condition evidence relate to?
- Will I receive written confirmation that my review or appeal was received?
- What happens if the deadline falls on a weekend or holiday?

Do not argue with the office in the script. The goal is to learn the rules and next steps.

## Contact Log

Use this table:

| Date/time | Office or person contacted | Method | Question asked | Answer received | Reference number | Next action | Follow-up date |
|---|---|---|---|---|---|---|---|
| YYYY-MM-DD HH:MM | Assessor office | Phone/email/portal/in person |  |  |  |  |  |

Keep the tone factual and neutral.

## Appeal Narrative Outline

Create an outline, not a final legal filing:

```text
Assessment Review Narrative Outline

1. Notice being reviewed
- Jurisdiction: [jurisdiction]
- Notice date: [date]
- Property: [short property description]
- Assessed value: [amount]
- Deadline: [date]

2. Requested review issue
- I am requesting review of [specific issue: assessed value / property record detail / exemption / classification / condition].

3. Factual basis
- Fact 1: [record error, comparable evidence, condition issue, or exemption fact]
- Fact 2: [supporting fact]
- Fact 3: [supporting fact]

4. Supporting evidence attached or planned
- [document/photo/comparable]
- [document/photo/comparable]

5. Questions or requested correction
- [question or correction request]
```

Use plain language. Avoid statements the user cannot support with documents.

## Deadline and Follow-Up Tracker

Build a tracker with conservative reminders:

| Date | Deadline or task | Owner | Status | Notes |
|---|---|---|---|---|
| [date] | Verify appeal deadline and filing method | User | Not started | Official source needed |
| [date] | Gather notice and prior assessment | User |  |  |
| [date] | Check property record details | User |  |  |
| [date] | Gather comparable or condition evidence | User |  |  |
| [date] | Ask assessor office questions | User |  |  |
| [date] | Decide informal review, formal appeal, professional help, or no action | User |  |  |
| [date] | Submit or confirm no submission | User |  |  |
| [date] | Save confirmation receipt | User |  |  |

If a deadline is close, advise the user to verify the official deadline and filing method immediately.

## Decision Points

Summarize options without choosing for the user:

- Informal review: useful when local rules allow a conversation or record correction before formal appeal.
- Formal appeal: may be needed when the deadline, evidence rules, and required forms are clear.
- Professional appraisal or valuation help: useful for higher-value disputes or complex comparable evidence.
- Tax advisor or attorney: useful when legal rights, exemptions, ownership, estate, rental, commercial, or jurisdiction-specific issues are complex.
- No action after verification: reasonable if the notice appears correct or evidence is weak, but the user decides.

## Example Prompts

Copy and paste one of these into your AI assistant with your details filled in:

1. **Assessment notice seems too high:** "I just received my county property tax assessment notice dated May 5. The assessed value jumped from $320,000 to $405,000 with no change to the house. The appeal deadline is June 30. I have three recent comparable sales from my neighborhood showing lower values. Help me organize an appeal packet."

2. **Unsure where to start:** "My property tax reassessment arrived and I don't know if it's worth appealing. The building value went up $50K but the land value stayed the same. Deadline is in 3 weeks. I have last year's notice and some photos of needed repairs. Walk me through what to verify and what evidence to gather."

3. **Preparing for assessor call:** "I want to call the assessor's office about my notice but I'm nervous. The square footage they listed is wrong (they show 2,400 but it's 1,850 per my appraisal). Draft neutral questions I can ask and help me organize my comparable sales before the deadline."


## Usage Scenarios

### Scenario 1

**User Input:** "Upload my tax assessment notice. My assessed value jumped 22% while neighbors saw 8%."

**Expected Output:** Parses notice fields. Flags the 22% increase as anomalous against user-provided neighborhood benchmark. Generates a discrepancy summary.

### Scenario 2

**User Input:** "Find 5 comparable sales within 0.5 miles from the past 12 months that support a lower valuation."

**Expected Output:** Pulls public-record comps (or guides user on where to find them), ranks by similarity, and highlights those with lower $/sqft than the assessment.

### Scenario 3

**User Input:** "Generate a formal appeal letter citing the comps above and the photo evidence of my unfinished basement."

**Expected Output:** Produces a template appeal letter with placeholder comps table, photo exhibit list, and procedural instructions for the local assessor's office.


### Scenario 4: 房产税评估搞不懂
**User input:** "收到房产税评估通知了，感觉评得比我实际买价高了不少。怎么判断是不是评高了？高了怎么办？"
**Expected output:** 房产税评估复核流程——第一步：对比基准（去当地不动产登记中心官网查同小区/同户型近半年成交均价，对比你的评估价是否偏离超过10%）；第二步：收集证据（房产证复印件+购房合同+贷款合同+最近一次物业费收据+同户型挂牌价截图壳）；第三步：申请复核（填不动产登记中心提供的复核申请表，附上证据，一般30天内回复）；第四步：如果复核不通过可以行政复议或者找第三方评估机构重新出报告。关键：评估基准日是每年1月1日，取证要在这个时间点附近的售价。

## Output Format

Return the result in this order:

1. Boundary note and deadline caution.
2. Notice summary.
3. Notice verification checklist.
4. Evidence checklist.
5. Evidence folder structure.
6. Assessor office questions.
7. Contact log.
8. Appeal narrative outline.
9. Deadline and follow-up tracker.
10. Decision points.

Keep the output practical, neutral, and evidence-focused. The goal is to help the user organize a review packet before the deadline, not to provide legal or tax advice.
