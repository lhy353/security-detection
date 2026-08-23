---
name: slack-cleanup
description: Detect and remove duplicate Slack messages with safety checks. Use when you need to find duplicate messages in Slack channels (same content posted multiple times with close timestamps) or clean up duplicate posts. CRITICAL - Always show duplicates to user and get explicit confirmation before any deletion.
---

# Slack Cleanup Skill

Safe detection and removal of duplicate Slack messages with mandatory user confirmation.

## ⚠️ CRITICAL SAFETY RULE

**NEVER delete any messages without explicit user confirmation.** This is a hard requirement from memory.md:

> **NEVER delete messages, files, or make code modifications without explicit permission**
> **Always aggregate data first and show the user**
> **Ask for explicit "yes delete" or "yes modify" before taking destructive actions**

## Workflow

### 1. Find Duplicates

Use `scripts/find-duplicates.sh` to scan a channel for duplicate messages:

```bash
scripts/find-duplicates.sh <channel-id> [time-window-seconds] [min-duplicates]
```

Parameters:
- `channel-id`: Slack channel ID (required)
- `time-window-seconds`: Max time between duplicates (default: 300 = 5 minutes)
- `min-duplicates`: Minimum duplicate count to report (default: 2)

**Output format:**
```json
{
  "text": "Message content",
  "instances": [
    {
      "ts": "1234567890.123456",
      "user": "U0LGU88M8",
      "thread_ts": "1234567890.123456",
      "reply_count": 3,
      "permalink": "https://..."
    }
  ]
}
```

### 2. Present to User

**MANDATORY STEP - DO NOT SKIP**

Show the user:
- Full message text for each duplicate group
- Number of duplicates found
- Timestamps and permalinks
- Thread information (if in thread or has replies)
- Clear indication of deletion order (replies first, then parents)

Format the presentation clearly with emojis and proper structure:

```
🔍 Found 3 duplicate groups:

📝 Group 1: "This is a duplicate message"
   • 3 instances found
   • Posted between 10:00:00 and 10:02:30
   
   Deletion order:
   1. Reply at 10:02:00 (2 replies to this) - Delete replies first
   2. Original at 10:00:00 - Delete parent last
   3. Duplicate at 10:01:00
   
   [Permalinks]

Would you like me to delete these duplicates? Reply "yes delete" to confirm.
```

### 3. Get Explicit Confirmation

Wait for user response. Only proceed if user says:
- "yes delete"
- "delete them"
- "go ahead and delete"
- Similar explicit confirmation

**DO NOT proceed if user says:**
- "ok" / "sure" / "sounds good" (too vague)
- Anything ambiguous
- No response

When in doubt, ask for clarification.

### 4. Delete Messages

Use `scripts/delete-message.sh` for each message:

```bash
scripts/delete-message.sh <channel-id> <message-ts>
```

**Deletion order rules:**
1. **Check for replies** - If message has replies, delete ALL replies first
2. **Delete in reverse chronological order** - Newest replies first, then oldest
3. **Delete parent last** - Only delete parent message after all replies are gone
4. **Rate limit handling** - Wait 1 second between deletions, increase on rate limit errors

### 5. Handle Rate Limits

If you encounter rate limiting:
- Script automatically waits and retries with exponential backoff
- Initial retry: 5 seconds
- Max retry: 60 seconds
- After 3 failures, report to user and pause

## Token Requirements

**User token required** - Message deletion requires user token permissions. The user token should be loaded from:
```
~/clawd/secrets/slack-super-ada.json
```

Format:
```json
{
  "user_token": "xoxp-..."
}
```

## Common Patterns

### Find duplicates in last hour
```bash
scripts/find-duplicates.sh C1234567890 3600
```

### Find only groups with 3+ duplicates
```bash
scripts/find-duplicates.sh C1234567890 300 3
```

### Check specific time range
Use Slack API with `oldest` and `latest` parameters in the script.

## Error Handling

The scripts handle:
- Invalid channel IDs
- Missing tokens
- Rate limiting (429 responses)
- Network errors
- Permission errors
- Thread reply dependencies

All errors are reported clearly to the user with actionable guidance.

## References

- Slack Web API: https://api.slack.com/methods
- chat.delete: https://api.slack.com/methods/chat.delete
- conversations.history: https://api.slack.com/methods/conversations.history
- conversations.replies: https://api.slack.com/methods/conversations.replies

## Notes

- Duplicates are matched by exact text content only
- Timestamps must be within the specified time window
- Bot messages and system messages are excluded
- Deleted messages cannot be recovered
- Always maintain audit log of deletions in memory files
