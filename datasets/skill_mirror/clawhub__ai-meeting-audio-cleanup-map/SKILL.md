---
name: AI Meeting Audio Cleanup Map
description: Builds a consent-aware preparation map for messy meeting recordings before AI transcription, including issue notes, cleanup choices, naming rules, and transcript-ready checks without processing audio.
version: "1.0.0"
type: prompt-flow
tags:
  - ai-productivity
  - meeting-notes
  - audio-preparation
  - transcription-prep
  - privacy
  - workflow
author: Bell (design)
---

# AI Meeting Audio Cleanup Map

## Overview

AI Meeting Audio Cleanup Map helps a user prepare messy meeting recordings for later transcription or note generation. It produces a practical preparation artifact: recording inventory, consent and privacy checks, noise issue map, cleanup decision path, export settings card, file naming rules, and a sample-minute verification checklist.

This skill does not process audio, transcribe audio, identify speakers from voice, summarize meeting content, bypass consent, or recover deleted material. It only helps the user plan and document safe preparation steps for user-provided recordings.

## When to Use

Use this skill when the user asks about:

- Preparing call, interview, class, podcast, or meeting recordings for AI transcription
- Figuring out why a recording may transcribe poorly
- Choosing a cleanup or export path before uploading audio to a transcription tool
- Creating file names, labels, and notes for multiple meeting recordings
- Removing or excluding private segments before using AI tools
- Building a checklist for a human editor, assistant, or transcription service

**Trigger phrases:** "prepare this audio for transcription", "my meeting recording is messy", "how should I clean up call audio before AI notes", "make a transcription prep checklist", "organize these recordings before upload"

## Required Inputs

Ask only for the minimum information needed. Do not request private meeting content unless the user volunteers it.

- Recording count, approximate length, and file formats if known
- Meeting type and intended transcription purpose
- Consent status and whether all participants knew about recording
- Known issues: background noise, low volume, cross-talk, missing segments, bad microphone, music, echo, or interruptions
- Whether private, legally sensitive, medical, financial, HR, customer, or confidential segments must be removed
- Target transcription tool or service if already chosen
- Deadline and output needs, such as speaker labels, timestamps, or searchable notes

If the user cannot share details, work from a generic checklist and mark assumptions clearly.

## Workflow

### Step 1 - Confirm Safe Use and Consent

Start with a short consent and privacy check:

- Was the recording made legally and with appropriate participant awareness?
- Are there private segments that should be removed before any AI upload?
- Are there people, clients, students, patients, employees, or minors whose information needs extra care?
- Does the user need an internal-only preparation plan rather than a cloud upload plan?

If consent is unclear, advise the user to resolve permission before transcription or sharing. Do not suggest bypassing recording rules or hiding use of AI tools.

### Step 2 - Build the Recording Inventory

Create a simple inventory for each file:

- File name or placeholder name
- Date or meeting label
- Duration
- Format if known
- Number of speakers if known
- Primary issue
- Sensitivity level: low, medium, or high
- Intended next step: keep, trim first, clean first, split, or exclude

Encourage metadata, not private content. Use neutral labels such as "candidate file A" when needed.

### Step 3 - Map Audio Problems to Preparation Actions

For each known issue, suggest a preparation action without performing the action:

- Low volume: note gain normalization as a possible editor step
- Background hum: note noise reduction as a possible editor step
- Cross-talk: flag for manual review and lower confidence
- Multiple speakers: prepare speaker roster or role labels if appropriate
- Long recording: split into logical sections before transcription
- Private segment: remove or exclude before upload
- Music or copyrighted media: avoid uploading unnecessary protected material
- Missing audio: mark gap before transcription so the transcript is not overtrusted

Make clear that cleanup can introduce artifacts and the user should verify a short sample before processing the whole file.

### Step 4 - Choose a Cleanup Path

Recommend one of these paths based on user needs:

- **No cleanup path:** audio is clear enough; use careful naming and a sample test.
- **Light prep path:** trim silence, remove private segments, standardize file names, and export a common format.
- **Human editor path:** for high-stakes, sensitive, or very noisy recordings.
- **Tool-assisted cleanup path:** user runs their chosen tool, then checks a sample manually.
- **Do not transcribe path:** consent, privacy, or quality problems make transcription inappropriate.

Do not name a path as guaranteed. Frame it as a decision map for the user.

### Step 5 - Create Naming and Export Rules

Produce file naming rules that help later transcription and audit:

- Use date, meeting label, sequence number, and status.
- Avoid participant full names unless needed and allowed.
- Avoid sensitive details in file names.
- Keep original files separate from prepared copies.
- Keep a preparation log with date, editor, changes planned, and review status.

Suggested pattern:

`YYYY-MM-DD_meeting-topic_part-01_prepped-for-transcript.ext`

### Step 6 - Prepare the Transcript-Ready Settings Card

If the user knows the target tool, tailor the card to its accepted formats. If not, keep it generic:

- Preferred file copy: prepared duplicate, not the original
- Segment length target if the recording is long
- Timestamp preference
- Speaker label preference
- Language and accent notes
- Glossary of names, project terms, acronyms, or product names the user is comfortable sharing
- Privacy exclusions and redacted segment notes
- Sample minute selected for test transcription

### Step 7 - Verify a Sample Minute

Before the user commits to a full transcription workflow, ask them to verify a short sample with their chosen process:

- Can key words be understood?
- Are speakers separable enough for the use case?
- Are private segments excluded?
- Are timestamps useful?
- Does the output contain hallucinated names or invented phrases?
- Is the recording too poor for the intended stakes?

If the sample fails, recommend revising the preparation plan before moving on.

### Step 8 - Produce the Cleanup Map

Deliver a concise artifact with these sections:

1. **Consent and privacy status**
2. **Recording inventory**
3. **Known audio issues**
4. **Recommended preparation path**
5. **Private segment removal plan**
6. **Naming and export rules**
7. **Transcript-ready settings card**
8. **Sample-minute verification checklist**
9. **Next actions**

## Output Format

Use this structure:

- **AI Meeting Audio Cleanup Map**
- **Use Case:**
- **Consent and Privacy Check:**
- **Recording Inventory:**
- **Issue-to-Action Map:**
- **Recommended Prep Path:**
- **Private Segment Plan:**
- **Naming and Export Rules:**
- **Transcript-Ready Settings Card:**
- **Sample-Minute Check:**
- **Next Actions:**
- **Limits and Safety Note:**

## Safety and Boundaries

- Do not process, edit, convert, transcribe, or summarize audio.
- Do not infer identities from voices or identify speakers without user-provided labels.
- Do not help bypass recording consent, privacy rules, workplace policy, or platform terms.
- Do not ask the user to paste sensitive meeting content when metadata is enough.
- Do not recommend uploading high-sensitivity recordings to third-party services without user review.
- Do not claim that cleanup will make a transcript accurate.
- Encourage keeping originals unchanged and working from copies.
- Encourage removal or exclusion of private segments before AI transcription.

## Quality Bar

A strong response should:

- Produce a visible preparation artifact, not generic audio tips
- Keep the work at planning and checklist level only
- Include consent and private-segment review before any transcription step
- Convert audio problems into specific preparation choices
- Include naming, export, and sample verification rules
- Avoid exposing meeting content or sensitive participant details
