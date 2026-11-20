# Finding regressions with git bisect

**Advanced · Lesson 02 · Study: 90–120 minutes**

## What you will learn
Bisect performs a binary search across commits between a known good and bad revision. Reliable automated tests turn a long hunt into a bounded sequence of checks.

## Technical walkthrough
Unless marked otherwise, use a disposable local practice repository. Read command comments: example placeholders and risky operations are intentionally not executable.

### 1. Define reliable test boundaries
Identify a failing current commit and a known working older commit. A test must return exit code 0 for good and nonzero for bad, with 125 signaling that the revision cannot be tested.

```bash
git log --oneline -12
git status --short
# Confirm a reproducible test exists:
# python -m unittest tests/test_behavior.py
```

**Verification:** A flaky test can mislead bisect; establish repeatability first.

### 2. Start a manual bisect
Run git bisect start, mark bad and good endpoints, and classify each checked-out revision. Git chooses a midpoint in the relevant ancestry graph.

```bash
# Use real hashes or refs from a disposable history:
# git bisect start
# git bisect bad HEAD
# git bisect good <known-good-commit>
# Run the test, then: git bisect good OR git bisect bad
```

**Verification:** Each classification reduces the candidate history.

### 3. Automate test classification
`git bisect run` executes a script for each selected commit. Script behavior must remain compatible with the revisions being tested and avoid changing shared state.

```bash
# Example test script body:
# #!/bin/sh
# python -m unittest discover -s tests -q
#
# git bisect run ./check-regression.sh
```

**Verification:** A useful script exits 0 for passing revisions and 1–124 (except 125) for failure.

### 4. Restore the original working state
`git bisect reset` leaves bisect mode and restores your original checkout. Verify HEAD and the worktree afterward, then inspect the candidate commit and fix the underlying regression.

```bash
git bisect log
git bisect reset
git status -sb
git log --oneline -3
```

**Verification:** Do not start a destructive checkout with unrelated uncommitted edits.

## Applied exercises
1. Build a six-commit toy history with a defect introduced at commit four.
2. Use bisect run to locate the bad commit.
3. Explain how a flaky or missing test changes confidence in the result.

## Interview checks
- What does exit code 125 mean during bisect?
- Why is bisect more reliable with deterministic tests?

**Pass condition:** Explain the state transition, failure path, and safeguards before running advanced commands.
