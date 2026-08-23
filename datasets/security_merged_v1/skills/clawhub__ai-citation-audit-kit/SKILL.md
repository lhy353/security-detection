---
name: AI Citation Audit Kit
description: Audit AI-generated citations for existence, currency, source-to-claim alignment, and evidence risk before a report, essay, or brief is submitted.
version: "1.0.0"
type: prompt-flow
tags:
  - ai-literacy
  - citation-audit
  - research-quality
  - evidence-review
  - writing
  - academic-integrity
author: OpenClaw Skills
---

# AI Citation Audit Kit

## Purpose

AI Citation Audit Kit helps a user inspect citations in AI-generated writing before they rely on the work. The skill focuses on whether each citation exists, whether it supports the exact claim attached to it, whether it is current enough for the topic, and whether the final document needs revision.

This is a prompt-only review framework. It does not guarantee that a source is true, academically acceptable, legally valid, or sufficient for publication.

## Trigger

Use this skill when the user has an AI-generated report, essay, memo, literature review, policy brief, slide deck, or article and says things like:

- "Can you check these AI citations?"
- "I think these sources might be fake."
- "Audit the bibliography before I submit this."
- "Do these citations actually support the claims?"
- "Help me verify ChatGPT citations."
- "Make a citation verification table."

## Inputs to Request

Ask for only the minimum material needed:

1. The AI-generated text, bibliography, footnotes, endnotes, or source list.
2. The required citation style or submission standard, if any.
3. The topic area and date sensitivity, such as medicine, law, current policy, technology, or history.
4. Any source text, screenshots, database exports, or links the user already has.
5. The intended use: class assignment, internal draft, public article, legal or policy memo, business decision, or personal learning.

Do not ask for account passwords, database credentials, private login access, student IDs, or full identity documents.

## Deliverable

Produce a citation audit packet with:

- A citation verification table.
- Source status labels: verified, likely real, unverified, stale, weak, mismatched, hallucinated, or needs primary-source check.
- The exact claim each citation is supposed to support.
- Alignment notes explaining whether the source supports, partially supports, contradicts, or does not address the claim.
- Risk flags for fabricated details, outdated evidence, missing page numbers, paywall dependence, secondary-source overuse, or citation-style gaps.
- Safer replacement-search prompts or source-discovery queries.
- A final trust summary: safe to use, revise before use, or do not use.

## Workflow

### Step 1 - Capture the Citation Set

Extract every citation from the user material. Include inline citations, footnotes, URLs, bibliography entries, quoted authorities, named studies, statistics, and "according to" references.

If the user provides only a bibliography, ask for the claims or paragraphs each source is meant to support.

### Step 2 - Pair Each Citation With Its Claim

For every citation, identify the claim it is being used to support. Rewrite the claim in one concise sentence.

Mark claims as:

- Factual claim.
- Statistical claim.
- Historical claim.
- Legal or policy claim.
- Scientific or medical claim.
- Quotation or paraphrase.
- Background context.

### Step 3 - Classify the Source Type

Label each source as one of the following:

- Journal article or academic paper.
- Book or book chapter.
- Government, legal, or policy page.
- Industry report or white paper.
- News article or magazine article.
- Organization page.
- Dataset or statistics portal.
- Web page or blog post.
- Unknown or incomplete source.

### Step 4 - Check Source Completeness

Review whether the citation has enough information to be verified by a human reviewer. Look for author, title, outlet or publisher, date, URL or DOI, page range, access date when needed, and edition information.

Mark incomplete citations as repair needed.

### Step 5 - Assess Findability and Currency

Using the user-provided source material when available, or by giving the user verification prompts when direct checking is not available, assess whether the source appears findable and whether its date fits the topic.

Use stronger currency expectations for law, medicine, technology, prices, current events, regulations, and active policy debates.

### Step 6 - Audit Source-to-Claim Alignment

Compare the cited source against the exact claim. Classify alignment as:

- Direct support: the source clearly supports the claim.
- Partial support: the source supports part of the claim but not all of it.
- Background only: the source gives context but does not prove the claim.
- Misquoted or overstated: the claim is stronger than the source.
- Contradiction: the source conflicts with the claim.
- Cannot determine: the source text is unavailable or incomplete.

### Step 7 - Flag Evidence Risks

Add risk flags where relevant:

- Possible hallucination.
- Missing or broken locator information.
- Outdated for the claim.
- Secondary source used where a primary source is needed.
- Paywalled or inaccessible to the expected reviewer.
- Citation points to a different claim than the text suggests.
- Source title, author, year, or venue appears inconsistent.
- Legal, medical, financial, or safety-critical claim needs qualified review.

### Step 8 - Suggest Repair Actions

For each risky citation, suggest the safest next action:

- Replace with a primary source.
- Downgrade or narrow the claim.
- Add a more current source.
- Add page numbers or quote locations.
- Remove the claim until verified.
- Ask a qualified reviewer to check the citation.
- Run a replacement-source search using a suggested query.

### Step 9 - Produce the Final Audit Packet

Return the audit table and a short trust summary. Use this table structure unless the user requests another format:

| ID | Claim | Citation | Source type | Status | Alignment | Risk flags | Repair action |
| --- | --- | --- | --- | --- | --- | --- | --- |

End with a clear verdict:

- Safe to use: only low-risk issues remain.
- Revise before use: some claims or citations need repair.
- Do not use: serious hallucination, mismatch, or high-stakes uncertainty remains.

## Safety Boundary

- Do not guarantee that a citation is true, accepted by a school, legally valid, or publication-ready.
- Do not fabricate missing bibliographic details.
- Do not claim to have read sources that were not provided or reliably inspected.
- Do not provide legal, medical, financial, or academic misconduct advice.
- For high-stakes claims, recommend primary-source verification and qualified human review.
- Protect privacy: never request credentials, private database access, or sensitive identity data.

## Acceptance Criteria

A successful run includes:

1. Every visible citation or source reference is extracted.
2. Each citation is paired with the claim it supports.
3. Each source receives a source-type label and status label.
4. Claim alignment is explicitly assessed.
5. Risk flags are assigned when evidence quality is weak.
6. Repair actions or replacement-source prompts are provided.
7. The final output includes a trust verdict.
8. High-stakes claims are routed to primary-source or expert review rather than treated as settled.
