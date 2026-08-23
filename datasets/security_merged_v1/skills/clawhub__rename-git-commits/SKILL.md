---
name: rename-git-commits
description: Rewrite commit messages in git history. Non-interactive methods for Windows/MSYS environments. Safe patterns without PTY.
version: 1.1.0
metadata:
  openclaw:
    tags: [git, github, rebase, commits, workflow]
---

# Rename Git Commits

## When to use

- Fix typo in commit message
- Change lowercase to capitalized ("update" → "Update")
- Add missing context
- Remove sensitive info

## Safety rules

⚠️ **Never rewrite commits that are pushed and cloned by others** — breaks their history.

If commits are already on GitHub and others may have them:
- ✅ Create a new commit with fix
- ❌ Don't force push shared branches

---

## Method 1: Last commit (before push)

```bash
git commit --amend -m "Update: proper capitalization"
```

---

## Method 2: Multiple commits (before push, no PTY needed)

Works on Windows/MSYS without interactive editor:

```bash
# 1. Create backup branch
git branch backup-main

# 2. Reset to commit BEFORE the ones you want to change
git reset --hard COMMIT_BEFORE_TARGET

# 3. Cherry-pick each commit without auto-commit
git cherry-pick --no-commit TARGET_COMMIT

# 4. Commit with corrected message
git commit -m "Update: new correct message"

# 5. Repeat for next commit
git cherry-pick --no-commit NEXT_COMMIT
git commit -m "Update: another correct message"

# 6. Verify
git log --oneline -5

# 7. If OK, force push
git push --force-with-lease origin main
```

Example — fix last 2 commits:

```bash
git branch backup
git reset --hard HEAD~2
git cherry-pick --no-commit HEAD@{2}
git commit -m "Update openplanet-plugin-dev to v2.1.0 - merged skills.md, emoji, all quirks"
git cherry-pick --no-commit HEAD@{1}
git commit -m "Update openplanet-plugin-dev to v2.2.0"
git push --force-with-lease origin main
```

---

## Method 3: Already pushed — create follow-up commit (safest)

When force push is too risky, add a note:

```bash
git commit --allow-empty -m "Update: correct previous commit messages (capitalization)"
git push origin main
```

---

## Method 4: Single older commit (before push)

Using interactive rebase with non-interactive editor:

```bash
# Set non-interactive editor
GIT_SEQUENCE_EDITOR="sed -i 's/^pick/reword/'" git rebase -i COMMIT_HASH^

# Then provide new message via EDITOR
EDITOR="sed -i '1s/.*/Update: new message/'" git rebase --continue
```

Note: This may not work on all MSYS setups. Method 2 (cherry-pick) is more reliable.

---

## Quick reference

| Goal | Command |
|------|---------|
| Amend last commit | `git commit --amend -m "New message"` |
| Show last N commits | `git log --oneline -N` |
| Fix multiple commits | cherry-pick --no-commit + re-commit |
| Undo all local changes | `git reset --hard origin/main` |
| Safe force push | `git push --force-with-lease origin main` |

---

## Remember

- ❌ `update skill` — lowercase first letter
- ✅ `Update skill` — capital first letter
- ❌ `feat: add feature` — conventional commit prefix
- ✅ `Add feature` — plain English, no prefix
- After push: either amend + force-push (dangerous on shared branches) OR new empty commit (safe)