---
name: net-deep-research
description: Perform deep multi-source internet research before answering. Use when the user prefixes a request with /net, asks for the latest information, wants real-time facts, requests web verification, asks which framework, tool, product, policy, or implementation path is best right now, or needs evidence-based answers synthesized from multiple public sources such as official docs, official sites, GitHub, package registries, standards sites, and other stable public references.
---
# Net Deep Research

When this skill is triggered, do not answer immediately.

Turn the request into a controlled research workflow:
1. classify the question,
2. normalize the scope,
3. decompose it into subquestions,
4. derive critical claims,
5. research in rounds,
6. resolve or expose conflicts,
7. answer from a structured evidence map.

## Trigger Handling

If the user message starts with `/net`:
- remove the `/net` prefix
- trim whitespace
- treat the remainder as the actual research question

Then restate the question in one sentence before researching.

## Goal

Produce answers that are:
- current
- evidence-based
- multi-source
- explicit about uncertainty
- grounded in stable public sources
- clear about what is verified vs inferred

## Hard Rules

Apply these rules strictly:
1. For predictive, forward-looking, market, macro, or scenario questions, separate the answer into two layers:
   - `Verified Facts`
   - `Inference`
2. Tie every core conclusion to at least one primary source whenever possible.
3. Do not let secondary media, commentary, or community discussion be the only support for a key conclusion when a stronger source family is available.
4. If direct official fetching fails, use the fixed fallback order instead of ad hoc substitution.
5. Do not skip subquestion decomposition for non-trivial questions.
6. Do not treat multiple pages repeating the same original announcement as independent evidence.

## Mode Selection

Choose one `primary_mode`. Add one `secondary_mode` only if it clearly helps.

### Mode A: Current Fact Check
Use for questions about latest status, current availability, recent releases, or whether something is already live.

### Mode B: Capability Or Compatibility Verification
Use for questions about support, compatibility, feature availability, plans, versions, models, or platforms.

### Mode C: Implementation Or How-To Research
Use for questions about how to build, integrate, deploy, or implement something, including best practices and architecture.

### Mode D: Comparison, Selection, Or Policy Confirmation
Use for questions about choosing among alternatives, policy confirmation, framework selection, official rules, or tradeoff analysis.

## Classification Rules

Apply these rules in order:
1. If the question is about how to implement, integrate, deploy, or build, choose `Mode C`.
2. If the question is about comparing options, choosing the best option, or checking policy or official rules, choose `Mode D`.
3. If the question is about support, compatibility, or whether a feature exists, choose `Mode B`.
4. If the question is about the latest or current status of a fact, choose `Mode A`.

Use a secondary mode only when both are necessary:
- `Mode A + Mode B`: current support status
- `Mode B + Mode C`: whether possible, then how to implement
- `Mode D + Mode C`: choose a solution, then outline implementation

## Question Normalization

Before searching, extract:
- `subject`
- `target_capability` if any
- `time_scope` if provided
- `region_scope` if provided
- `version_scope` if provided

Do not invent missing scopes.

Then rewrite the request as one normalized question.

## Subquestion Decomposition

Before extracting claims, decompose the normalized question into up to 6 subquestions.

Always try to produce:
- `core_subquestions`: what must be answered to resolve the user's request
- `verification_subquestions`: what boundaries, prerequisites, or limitations must be checked
- `countercheck_subquestions`: what likely counterexamples, exceptions, or contradictions should be tested

For simple questions, 2-3 subquestions is enough.
For complex questions, use 4-6 subquestions.

Do not skip this step unless the question clearly qualifies for fast path.

## Claim Extraction

Derive at most 3 critical claims from the subquestions.

Typical claim shapes:
- whether the capability exists
- when the capability became available
- what scope, limitations, or exclusions apply
- which option best fits the user's goal
- what implementation path is most appropriate

Every important conclusion in the final answer should map back to one of these claims.

## Query Planning

Plan queries per claim, not just per question.

For each important claim, generate these core query slots:
- `direct_query`
- `official_query`
- `release_query`
- `contradiction_query`

Add one mode-specific slot:
- `Mode A` -> `recent_query`
- `Mode B` -> `compatibility_query`
- `Mode C` -> `implementation_query`
- `Mode D` -> `comparison_query` or `policy_query`

Keep the total query count between 4 and 8 for a normal request.

For technical, product, framework, or API questions, prefer bilingual query planning when helpful:
- use English queries for official docs, repos, and release notes
- use Chinese queries for China-specific products, policy, regional availability, or local interpretation
- do not force bilingual searching when the domain is clearly single-language

## Research Rounds

Use a staged research workflow.

### Round 1: Primary Evidence
Search primary and official sources first.
Goal: establish the strongest direct evidence for each claim.

### Round 2: Independent Verification
Add independent support from a different strong source family.
Goal: confirm scope, version, timing, or practical limitations.

### Round 3: Conflict Resolution
Run only when needed.
Trigger this round when:
- strong sources disagree
- timing or version differences matter
- region or plan differences may explain the conflict
- the answer would otherwise rely on weak evidence

Goal: explain the disagreement, not just note it.

## Research Budget And Stop Rules

Use these defaults unless the question clearly demands more depth:
- `max_search_rounds = 3`
- `target_primary_sources_per_core_claim = 1`
- `target_total_supporting_sources_per_core_claim = 2`
- `max_key_claims = 3`

Stop when all of these are true:
- each core claim has direct support or a clearly stated evidence gap
- no major unresolved conflict blocks the main answer
- uncertainty is explicit where evidence is weak

Escalate to another search round when any of these are true:
- a claim depends only on weak or secondary support
- a key source appears outdated for the user's time scope
- two strong sources materially disagree
- implementation advice depends on unverified capability assumptions

## Source Routing

Use source families, not fixed websites, as the primary routing method.

### Mode A Priority
1. official announcement, changelog, release notes
2. official docs
3. official repository releases
4. high-quality secondary reporting

### Mode B Priority
1. official docs
2. API reference or SDK docs
3. official repository, release, or issue
4. package registry pages

### Mode C Priority
1. official docs
2. official repository README, examples, guides
3. package registry pages
4. stable technical references

### Mode D Priority
1. official docs or official sites
2. government, institutional, or standards sources when relevant
3. official repository, pricing, feature, or explanation pages
4. high-quality secondary analysis

## Preferred Source Families

Prefer these source families when relevant:
- official documentation sites
- official company or organization sites
- official changelogs and release notes
- GitHub repositories and releases
- package registries such as PyPI and npm
- standards sites such as RFC, IETF, and W3C
- government and institutional sites
- stable technical references such as MDN

## Accessibility, Stability, And Dedup Rules

Prefer sources that are:
- public
- readable without login
- likely to remain available
- broadly reachable for both international and China-based users when possible

Avoid depending on:
- login-gated content
- short-form social posts
- low-signal community threads as the only evidence
- content farms or SEO spam pages
- unattributed reposts

If direct official fetching fails, use this fixed fallback order and do not skip steps:
- official page -> official mirror or official alternate page -> official changelog or release note -> official GitHub or official repository page -> package registry or standards page -> stable technical reference
- government or institution page -> official FAQ -> official press release -> official transcript or bulletin -> high-quality institutional analysis

Apply source dedup rules:
- do not count mirrored pages of the same original announcement as independent evidence
- do not count a media rewrite of an official post as a separate primary source
- treat same-origin release note plus marketing page as one source family unless they provide materially different evidence

## Source Filtering And Scoring

Reject a source as key evidence if it:
- requires login for the core content
- does not clearly support any claim
- is only a repost without the original source
- is obviously low quality or SEO-generated

Score each candidate source across 5 dimensions, each from 0 to 2:
- `authority`
- `stability`
- `accessibility`
- `freshness`
- `relevance`

Total score range: `0-10`

Minimum rules:
- do not use a source with total score below 4 as key evidence
- every important claim should have at least one source with both `authority >= 1` and `relevance >= 1`
- every core conclusion should be anchored to at least one primary source whenever possible
- do not let secondary media be the only support for a key conclusion when a stronger source family is available

## Evidence Extraction

For each claim, extract evidence items with:
- `claim_id`
- `source_title`
- `source_url`
- `source_date_hint` if available
- `evidence_snippet`
- `source_score`
- `stance`: `support`, `oppose`, or `partial`

Do not over-quote. Extract only the part needed to support the claim.

## Conflict Handling

If a claim has both supporting and opposing evidence, explicitly mark it as conflicted.

Only use these conflict causes:
- version difference
- timing difference
- region difference
- plan tier difference
- wording ambiguity
- evidence insufficiency

Do not invent a conflict explanation without support.

When a claim is conflicted, internally build this mini-structure before answering:
- `claim`
- `supporting_evidence`
- `opposing_evidence`
- `conflict_cause`
- `current_best_explanation`
- `residual_uncertainty`

## Confidence Rules

Assign confidence per key claim:

### High
- at least 2 supporting sources
- at least 1 strong primary source
- no major unresolved conflict

### Medium
- at least 1 reasonably strong source
- some scope limitation or minor conflict

### Low
- only weak support
- or unresolved conflict
- or no clear primary source

## Evidence Map

Before writing the answer, build this internal structure:
- `question_restatement`
- `primary_mode`
- `secondary_mode` if any
- `normalized_question`
- `subquestions`
- `claims`
- `evidence_by_claim`
- `conflicts`
- `uncertainties`
- `final_conclusions`
- `answer_outline`

For predictive, market, macro, or outlook questions, the evidence map must also separate:
- `verified_facts`
- `inference`

Do not skip this step.

## Final Answer Format

Default section order:
1. `Question Restatement`
2. `Short Answer`
3. `Key Findings`
4. `Cross-Source Notes`
5. `Uncertainties or Limits`
6. `Sources`

For predictive, market, macro, or outlook questions, use this stricter order:
1. `Question Restatement`
2. `Short Answer`
3. `Verified Facts`
4. `Inference`
5. `Cross-Source Notes`
6. `Uncertainties or Limits`
7. `Sources`

For implementation or comparison questions, add a concise `Recommendation` block when useful.

## Writing Rules

In `Short Answer`:
- answer directly
- keep it concise

In `Key Findings`:
- separate confirmed facts from implications
- prioritize evidence from official or primary sources
- tie each core conclusion back to a claim

In `Cross-Source Notes`:
- explain where sources agree
- explain where they differ
- mention version, timing, regional, or plan differences when relevant

In `Verified Facts`:
- include only directly supported facts
- keep interpretation minimal
- attach stronger sources first

In `Inference`:
- derive each inference from the verified facts above
- do not present inference as confirmed fact
- explicitly signal when the inference depends on policy, timing, or assumption-sensitive interpretation

In `Uncertainties or Limits`:
- clearly state what could not be verified
- clearly state if official sources were unavailable and fallback layers were used
- do not hide missing evidence

In `Sources`:
- list the most useful sources, not every weak result
- prefer strong primary sources first

## Fast Path

Use fast path only when:
- the question is simple
- there is a clear primary source
- there is little risk of ambiguity

Even then:
- check the primary source
- add one independent supporting source if practical
- skip fast path if the answer depends on version, timing, region, or plan differences

## Example Handling Pattern

If the user asks:
- `/net What is the best agent framework right now, and use it to help me design a game?`

Then:
- classify as `Mode D` with `Mode C` secondary
- normalize the user goal and split it into selection and implementation subquestions
- compare current agent framework candidates using official docs, GitHub, releases, and stable public references
- verify the top candidate with at least one independent supporting source
- resolve any conflict about maturity, maintenance, or capability scope
- decide which framework best fits the requested goal
- then outline a game-building workflow using that framework
- clearly separate:
  - evidence for framework selection
  - implementation guidance for the game workflow

## Final Reminder

Research first.
Model the question second.
Resolve conflicts third.
Answer last.
