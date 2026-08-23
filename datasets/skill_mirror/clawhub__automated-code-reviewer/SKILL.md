---
name: automated-code-reviewer
slug: automated-code-reviewer
version: 1.0.0
description: "Automated code review for AI agents. Analyze pull requests, detect bugs, enforce coding standards, and suggest improvements. Triggers: code review, PR review, code quality, automated review, code analysis."
author: SKY-lv
license: MIT-0
tags: [automation, code-quality, review]
keywords: [code review, PR review, automated review, code analysis, code quality, pull request, bug detection, coding standards]
triggers: automated-code-reviewer
---

# Code Review Automation

Automated code review system for AI agents. Analyze pull requests, detect bugs, enforce coding standards, and provide actionable improvement suggestions.

## Overview

A comprehensive code review automation tool that helps agents perform thorough, consistent code reviews. Detects bugs, security vulnerabilities, style violations, and performance issues while providing contextual improvement suggestions.

## Capabilities

### 1. Pull Request Analysis

```bash
node review.js analyze --pr 42 --repo owner/repo
node review.js analyze --diff HEAD~3 --full-context
```

Reviews the entire PR diff with full file context for accurate suggestions.

### 2. Bug Detection

```bash
node review.js detect-bugs --src ./src --severity medium+
node review.js detect-bugs --focus null-pointer,resource-leak,off-by-one
```

Identifies potential bugs including null pointers, resource leaks, race conditions, and off-by-one errors.

### 3. Standards Enforcement

```bash
node review.js lint --standard airbnb --fix-suggestions
node review.js lint --custom-rules .reviewrules.json
```

Enforces coding standards (Airbnb, Google, Custom) with auto-fix suggestions.

### 4. Security Scan

```bash
node review.js security --check owasp-top10
node review.js security --focus injection,xss,auth
```

Scans for OWASP Top 10 vulnerabilities, injection attacks, and authentication issues.

### 5. Performance Review

```bash
node review.js performance --detect n+1,mem-leak,slow-loop
node review.js performance --benchmark-compare base-branch
```

Identifies N+1 queries, memory leaks, and inefficient algorithms.

## Configuration

```json
{
  "review": {
    "severity": "medium",
    "categories": ["bugs", "security", "performance", "style"],
    "autoApprove": ["docs-only", "formatting"],
    "requireApproval": ["security", "breaking-change"],
    "languageRules": {
      "javascript": "airbnb",
      "python": "pep8",
      "go": "effective-go"
    }
  }
}
```

## Use Cases

- PR Gate: Automatically review every pull request before merge
- Pre-commit Hook: Catch issues before they reach CI
- Batch Review: Review multiple repositories for compliance
- Onboarding: Help new developers learn coding standards
- Security Audit: Periodic security-focused code reviews
