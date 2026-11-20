# Contributing through forks and upstream pull requests

**Intermediate · Lesson 06 · Study time: 75–110 minutes**

## Purpose
Fork-based contributions let developers propose changes without push access to the source repository. Git operations happen locally; permission checks and pull requests happen on GitHub.

## Concepts and guided examples
Examples may require a fork, a configured remote, an authenticated account or pre-existing files. Execute them only after confirming context.

### 1. Verify remote topology
Typically origin is your fork and upstream is the source repository. Names are conventions; verify actual URLs before pushing. Never assume the same remote setup in every clone.

```bash
git remote -v
git branch -avv
git fetch --prune upstream
git log --oneline upstream/main -3
```

**Check:** Inspect which remote points at a repository you own.

### 2. Keep the local base up to date
If the fork's main has no divergent work, fast-forward it from upstream/main. Where fork main is shared, plan sync to avoid disrupting others.

```bash
git switch main
git fetch upstream
git merge --ff-only upstream/main
git status -sb
```

**Check:** The command refuses divergence rather than creating an unexpected merge.

### 3. Propose from a dedicated branch
Create a short-lived branch and push it to your fork, then submit a PR to the upstream repository. Good contributions contain tests and a concise change description.

```bash
git switch -c fix/typo
# Edit, review, and test the actual fix.
git add -- path/to/file
git commit -m "Fix installation example"
git push -u origin fix/typo
```

**Check:** Use your fork as push destination; GitHub may require checks or reviews.

### 4. Update an in-review branch
If upstream advanced, fetch first; integrate according to repository policy. Rebase rewrites the feature's commit hashes and may require a lease-protected force push to your own branch only, after coordinating with collaborators.

```bash
git fetch upstream
git diff --stat upstream/main...HEAD
git status -sb
# Optional, only if you own the feature history:
# git rebase upstream/main
```

**Check:** Never force push a shared upstream default branch.

## Practice
1. Draw remotes and branches for a contributor without upstream write access.
2. Review a change from upstream and explain the safest integration strategy.
3. Prepare a PR checklist for external contributors.

## Interview prompts
- What prevents a contributor's fork from directly changing upstream main?
- When is a lease-protected force push appropriate?

**Done when:** You can explain decisions, show a reviewable change, and point to reproducible test evidence.
