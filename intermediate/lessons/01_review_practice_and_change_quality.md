# Code review: correctness, security, and communication

**Intermediate · Lesson 01 · Suggested time: 75–110 minutes**

## Purpose
Reviewing is not primarily about style preference. Check behavior, test coverage, change scope, and known risks while keeping feedback specific and respectful.

## Concepts and commands
Examples run in disposable repositories. Commands marked as examples need a pre-existing branch, configured remote, or GitHub access; never paste unresolved placeholders.

### 1. Review the diff at the right granularity
Compare the branch against its merge base, not just the last commit. Watch for accidentally committed generated files, dependency changes, or unrelated refactors.

```bash
git fetch origin
git diff --stat origin/main...HEAD
git diff --check origin/main...HEAD
git log origin/main..HEAD --oneline
```

**Verify:** A PR diff shows the feature's net effect even if the branch contains several commits.

### 2. Use a consistent review checklist
Review requirements, edge cases, tests, access control, and performance relevant to the change. Ask which behavior changes and why. Request an example for ambiguous assumptions.

```bash
# Review questions:
# 1. Which input case would fail now?
# 2. Is the security boundary affected?
# 3. Are tests deterministic and independent?
# 4. Will old clients still work?
# 5. Can this be rolled back safely?
```

**Verify:** High-impact observations should cite specific changed lines and outcomes.

### 3. Separate must-fix from optional suggestions
A correctness bug or leaked credential must block release. A naming preference can be a nonblocking suggestion. Give a concrete example, trade-off, or proposed patch.

```bash
# Blocking: "This query lacks tenant_id filter; another user can see rows."
# Suggestion: "Could we rename x to request_count for clarity?"
# Question: "Is retrying this action idempotent?"
```

**Verify:** Feedback should make it easy for the author to act.

### 4. Verify fixes and preserve context
Re-run relevant checks after change; a response such as 'fixed' is insufficient unless the new commit addresses the issue. Re-review dependent changes when a fix touches another module.

```bash
git status -sb
git diff origin/main...HEAD
git log --oneline -5
git diff --check origin/main...HEAD
```

**Verify:** A resolved comment must correspond to changed code or a documented rationale.

## Practice tasks
1. Review a hypothetical PR adding database access without tenant scoping.
2. Categorize five comments into blocking, suggestion, or question.
3. Write a concise review summary with test evidence and one risk.

## Interview check
- Why might a passing CI run still be insufficient to approve a PR?
- What makes a review comment actionable?

**Evidence:** A clear commit graph, tested behavior, and a short explanation of why the workflow is appropriate.
