# Secret incidents and sensitive-history cleanup

**Advanced · Lesson 09 · Study time: 90–120 min**

## Goal
If credentials enter a repo, treat them as compromised. Removing a file or rebasing history does not guarantee they have not been copied. Correct response starts with revocation.

## Worked technical sections
Practice in throwaway repositories. Commands with placeholders or commented examples require setup and judgment; do not paste them into a production repository.

### 1. Contain and rotate first
Identify the credential's scope and immediately revoke or rotate it in its provider. Avoid putting the leaked value into issues, PR descriptions, chat logs, or diagnostic commands.

```bash
# Incident checklist:
# 1. Revoke/rotate affected key at its provider
# 2. Identify exposure window and affected systems
# 3. Replace integrations with a new managed secret
# 4. Document remedial actions without the secret value
```

**Verify:** No history rewrite can make an already copied credential private.

### 2. Remove from the current tree
Untrack the sensitive file, add an appropriate ignore rule, and commit the correction. This prevents continued distribution from HEAD but does not remove the value from earlier commits.

```bash
# If a tracked .env exists in a disposable repo:
# git rm --cached -- .env
# printf ".env\n" >> .gitignore
# git add .gitignore
# git commit -m "Stop tracking local configuration"
git status --short
```

**Verify:** Keep secrets entirely out of course examples.

### 3. Understand history rewrite scope
Specialized tools such as git-filter-repo can rewrite historical content, but they change commit IDs, tags, and clone coordination requirements. GitHub caches, forks, and downloaded copies can retain old data.

```bash
# Before any cleanup:
git branch -avv
git tag --list
git remote -v
# Do not run a blanket rewrite command without a full incident plan.
```

**Verify:** Rewrites need backups, coordination, and an explicit force-push strategy.

### 4. Prevent recurrence
Use secret scanning, scoped credentials, protected branches, code reviews, and safe environment configuration. Checks reduce incidents but cannot replace training and incident response.

```bash
# Review staged file names:
git diff --cached --name-only
git status --ignored --short
git check-ignore -v .env
```

**Verify:** A clean commit should contain no credential material or private data.

## Applied exercises
1. Write an incident response plan for a leaked token in a public repo.
2. Explain why `git rm` and `.gitignore` are insufficient for leaked history.
3. Audit a CI workflow for overprivileged secrets.

## Interview prompts
- What is the first priority after discovering a leaked API key?
- Can force-pushing rewritten history retract copies from other clones?

**Completion:** Explain performance, security, and recovery trade-offs with reproducible evidence.
