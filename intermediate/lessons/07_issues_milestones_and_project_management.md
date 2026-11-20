# GitHub Issues, labels, and project planning

**Intermediate · Lesson 07 · Study time: 75–110 minutes**

## Purpose
Issues record actionable work and context. Well-written issues improve collaboration; milestones and project views help track priorities but do not replace clear acceptance criteria.

## Concepts and guided examples
Examples may require a fork, a configured remote, an authenticated account or pre-existing files. Execute them only after confirming context.

### 1. Write reproducible bug reports
Include current behavior, expected behavior, concise reproduction, environment, and minimal logs without secrets. A label such as bug or documentation organizes work; it is not the severity itself.

```bash
# Issue example
# Title: Setup guide omits Python prerequisite
# Expected: clean install works on documented versions
# Actual: install fails on unsupported version
# Reproduce: follow README in clean environment
# Done: document version and add validation step
```

**Check:** Reviewers should reproduce the bug without guessing hidden assumptions.

### 2. Break a feature into finishable work
A feature issue should list behavior, constraints, and acceptance tests. Avoid creating vague tasks like 'improve backend' that cannot be verified.

```bash
# Feature acceptance criteria
# [ ] CLI accepts --format csv
# [ ] Invalid format gives nonzero exit
# [ ] Output rows are deterministic
# [ ] Unit tests cover empty data
```

**Check:** Each checkbox describes behavior that can be checked.

### 3. Link work to GitHub issues
Many repositories use issue-closing keywords in PR descriptions (e.g. 'Fixes #42') to close linked issues after merge, subject to GitHub's default-branch behavior. Use references without automatic closure when appropriate.

```bash
# PR body example:
# Why: output format needed for reporting.
# What: add explicit CSV support.
# Tests: unittest + fresh manual run.
# Fixes #42
```

**Check:** Use a real issue number; do not invent references in actual PRs.

### 4. Plan release milestones
Group related issues into a deliverable scope with an owner and acceptance criteria. GitHub Projects supports flexible board and table views; avoid using board status as a substitute for tested delivery.

```bash
# Milestone example:
# v0.2.0: documentation + CSV export + regression fixes
# Exclusions: authentication rewrite
# Release gate: tests pass, changelog updated
```

**Check:** A milestone is a planning object, not a Git tag or deployment.

## Practice
1. Draft a complete bug issue for a broken command.
2. Split a large feature into three verifiable issues.
3. Define a release milestone with exclusions and acceptance checks.

## Interview prompts
- What makes an issue actionable?
- Does closing an issue mean the feature was deployed?

**Done when:** You can explain decisions, show a reviewable change, and point to reproducible test evidence.
