# Pull request lifecycle and reviewable changes

**Intermediate · Lesson 00 · Suggested time: 75–110 minutes**

## Purpose
A pull request compares a proposed branch with a target and records conversation, checks, and merge decisions. It is a GitHub feature, not a Git command.

## Concepts and commands
Examples run in disposable repositories. Commands marked as examples need a pre-existing branch, configured remote, or GitHub access; never paste unresolved placeholders.

### 1. Prepare a focused PR
Start from an up-to-date base, make one logical change, run tests, and push the topic branch. Review the diff yourself before requesting review.

```bash
git switch main
git pull --ff-only
git switch -c feature/readme-example
# Edit one relevant file.
git diff --check
git add README.md
git commit -m "Explain local setup"
git push -u origin feature/readme-example
```

**Verify:** Commands require a configured remote; never commit an unchanged file.

### 2. Write a useful PR description
A good PR states problem, implementation, how it was tested, and risks. Use screenshots for UI changes and link related issues when useful. Avoid listing each commit as if it were the explanation.

```bash
# Suggested PR structure (write this on GitHub):
# Why: clarify installation for new contributors.
# What: document setup and prerequisites.
# Verification: followed steps in a fresh checkout.
# Risk: documentation only.
```

**Verify:** Reviewers should understand intent without reverse-engineering the patch.

### 3. Follow status checks and reviews
CI checks run against a GitHub event/ref according to workflow configuration. Review comments may be suggestions, blocking changes, or questions; respond with code and evidence, not just 'resolved'.

```bash
git status -sb
git log main..HEAD --oneline
git diff --stat main...HEAD
git diff --check main...HEAD
```

**Verify:** No accidental files or whitespace errors appear in the proposed change.

### 4. Merge and clean up
Team policy determines merge, squash, or rebase strategy. After a merge, update local main and remove stale feature branches after verifying the result.

```bash
git switch main
git pull --ff-only
git branch --merged
git branch -d feature/readme-example
git fetch --prune origin
```

**Verify:** Branch deletion is safe only after integration is confirmed.

## Practice tasks
1. Draft a PR body for a one-file bug fix including reproducible test steps.
2. Review a sample diff and flag one unclear naming decision.
3. Explain what happens when CI fails after review approval.

## Interview check
- Why is a pull request not the same as a Git merge?
- Should you merge before all required checks complete?

**Evidence:** A clear commit graph, tested behavior, and a short explanation of why the workflow is appropriate.
