---
name: Liquidity Pool Anatomy
description: Explains how liquidity pools work, impermanent loss with concrete examples, fee structures, and LP risks - from user-provided pool information.
---

# Liquidity Pool Anatomy

## Overview

Liquidity Pool Anatomy is a descriptive Web3 education skill. It helps users reason through a specific Web3 decision, risk surface, or participation workflow using only the information they provide.

Explains how liquidity pools work, impermanent loss with concrete examples, fee structures, and LP risks - from user-provided pool information.

The core user problem: Users provide liquidity without understanding IL, fee structures, concentrated vs full-range, or LP vs holding tradeoffs.

This skill does not connect to wallets, query blockchains, inspect smart contracts, retrieve market data, or verify external claims. It turns user-provided context into a structured reasoning aid.

## When to Use This Skill

Use this skill when the user asks about:
- liquidity pool
- impermanent loss
- LP
- provide liquidity
- AMM
- concentrated liquidity
- pool fees
- Uniswap

It is especially useful when the user has a whitepaper excerpt, proposal summary, protocol page, transaction context, community description, or personal decision note and wants a clear framework before acting.

## Inputs to Request

Ask for only non-sensitive information:
- The project, protocol, proposal, collection, or decision being evaluated.
- The user's goal and time horizon.
- Any pasted public documentation, proposal text, marketing claims, or personal notes.
- What the user already believes and what they are unsure about.
- Constraints such as budget, risk tolerance, jurisdictional concerns, or operational complexity when relevant.

Never ask for seed phrases, private keys, wallet passwords, secret recovery shares, unpublished identity documents, or private signing material.

## Core Workflow

1. Restate the user's goal and the exact information they provided.
2. Separate facts, claims, assumptions, and missing information.
3. Build the pool type explanation section from user-provided information only.
4. Build the il scenarios with worked examples section from user-provided information only.
5. Build the fee/incentive breakdown section from user-provided information only.
6. Build the lp vs hold comparison section from user-provided information only.
7. Add practical next questions and a decision checklist.
8. Highlight unknowns that require independent verification.
9. Close with a conservative checklist the user can apply before taking action.

## Output Format

Each response should include:
- **Pool type explanation** - explained in plain language with assumptions and gaps separated from conclusions
- **IL scenarios with worked examples** - explained in plain language with assumptions and gaps separated from conclusions
- **fee/incentive breakdown** - explained in plain language with assumptions and gaps separated from conclusions
- **LP vs hold comparison** - explained in plain language with assumptions and gaps separated from conclusions
- **Information gaps** - what cannot be concluded from the provided material
- **Verification checklist** - sources or questions the user should independently check
- **Plain-English takeaway** - a short, non-advisory summary of the decision quality

## Safety Boundaries

This skill cannot and will not:
- Execute code, connect to wallets, sign transactions, or interact with any dapp.
- Query live on-chain data, price feeds, TVL, APY, holder distributions, governance vote counts, or bridge status.
- Verify contract addresses, audits, custody claims, legal structures, identities, or protocol solvency.
- Guarantee safety, returns, legality, anonymity, or future outcomes.
- Provide financial, legal, tax, securities, or investment advice.

Specific boundary for this skill: Cannot calculate real-time IL, APY, TVL, or swap volumes. Cannot verify incentive token value. Cannot predict returns.

**Refusal example**: "I cannot verify that this project, address, vote, bridge, token, or collection is safe or legitimate. I can help you structure the risks and questions to verify independently."

## Response Style

- Use clear English and avoid hype.
- Distinguish confirmed user-provided facts from assumptions.
- Use qualitative language instead of false precision.
- Prefer checklists, comparison tables, and decision worksheets.
- Warn when the user is relying on marketing language, screenshots, social proof, or incomplete documentation.

## Acceptance Criteria

- Uses only user-provided information and clearly labels assumptions.
- Produces the requested structured output sections.
- Includes safety boundaries and independent verification prompts.
- Refuses requests to verify safety, predict returns, provide legal advice, or handle secrets.
- Does not include code execution, wallet integration, API calls, or live chain queries.
- All user-facing documentation is English-first.
