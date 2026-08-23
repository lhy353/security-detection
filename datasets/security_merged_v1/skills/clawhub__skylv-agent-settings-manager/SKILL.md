---
name: agent-settings-manager
slug: agent-settings-manager
version: 1.0.0
description: "Configuration management for AI agents. Manage, validate, version, and sync configs across environments. Triggers: config management, configuration, env variables, config validation, config sync."
author: SKY-lv
license: MIT-0
tags: [configuration, management, devops]
keywords: [config management, configuration, env variables, config validation, config sync, config versioning, secrets management, environment config]
triggers: agent-settings-manager
---

# Config Management

Configuration management for AI agents. Manage, validate, version, and sync configurations across environments securely.

## Overview

A configuration management system that helps agents handle application settings, environment variables, secrets, and feature flags. Provides validation, versioning, diffing, and secure sync across environments.

## Capabilities

### 1. Config Validation

```bash
node config.js validate --file config.json --schema config.schema.json
node config.js validate --strict --check-types --check-required
```

Validates configuration files against JSON schemas with type checking and required field enforcement.

### 2. Environment Management

```bash
node config.js env create --name staging --from dev --override api.url,staging.api.com
node config.js env diff --from dev --to production
node config.js env promote --from staging --to production --dry-run
```

Create, compare, and promote configurations across environments with override support.

### 3. Secret Handling

```bash
node config.js secrets set --key DB_PASSWORD --env production
node config.js secrets rotate --env production --keys API_KEY,DB_PASSWORD
node config.js secrets check --scan-for-leaks
```

Secure secret management with rotation and leak detection.

### 4. Version Control

```bash
node config.js history --file config.json --last 10
node config.js rollback --file config.json --to-version 5
node config.js diff --version 5 vs 7
```

Full version history with diff and rollback capabilities.

### 5. Sync & Distribution

```bash
node config.js sync --source git --repo org/configs --path /production
node config.js sync --watch --auto-reload --debounce 5s
```

Sync configurations from git repositories with auto-reload on changes.

## Configuration

```json
{
  "configManagement": {
    "environments": ["dev", "staging", "production"],
    "validation": {
      "strict": true,
      "schema": "./schemas/config.schema.json"
    },
    "secrets": {
      "provider": "vault",
      "rotation": "90d",
      "scanForLeaks": true
    },
    "versioning": {
      "enabled": true,
      "maxVersions": 50
    },
    "sync": {
      "source": "git",
      "watch": true,
      "autoReload": true,
      "debounceMs": 5000
    }
  }
}
```

## Use Cases

- Multi-Environment: Manage different configs for dev, staging, production
- Agent Configuration: Centralize AI agent configuration management
- Compliance: Validate configs meet security and compliance standards
- Disaster Recovery: Rollback configurations to known-good versions
- Team Collaboration: Share and sync configs across team members
