# Advanced capstone: regression to trustworthy release

**Advanced · Lesson 11 · Study time: 90–120 min**

## Goal
Combine Git internals, bisect, recovery, CI, release workflow, and governance into a realistic exercise. The goal is reproducible evidence, not memorizing commands.

## Worked technical sections
Practice in throwaway repositories. Commands with placeholders or commented examples require setup and judgment; do not paste them into a production repository.

### 1. Start from a known good milestone
In a disposable repository, build a small program with deterministic tests. Create a tag on a known good commit and then a sequence containing a regression.

```bash
git init -b main release-lab
cd release-lab
git config user.name "Course Learner"
git config user.email "learner@example.test"
# Add code and tests; create a baseline commit.
# git add . && git commit -m "Create verified baseline"
# git tag -a v0.1.0 -m "Known good"
```

**Verify:** The tag only counts as a known-good milestone after tests pass.

### 2. Find regression with evidence
Introduce commits where one breaks a test; use git bisect run with a deterministic command. Save the log and record the first bad commit.

```bash
git log --oneline --graph -12
# git bisect start
# git bisect bad HEAD
# git bisect good v0.1.0
# git bisect run ./scripts/check.sh
# git bisect log
# git bisect reset
```

**Verify:** The test command must work on the revisions being bisected.

### 3. Repair without breaking history
Fix the behavior on a topic branch and test. Prefer adding a new commit when correcting shared history, with a PR review and CI gates before merge.

```bash
git switch -c fix/regression
# Edit implementation and regression test.
git status --short
git diff --check
# git add paths && git commit -m "Fix regression"
git log --oneline --graph -6
```

**Verify:** Do not rewrite published main merely to conceal the bug.

### 4. Publish a verifiable release
Create an annotated tag on the tested merge result and draft notes summarizing changes, checks, compatibility, and rollback steps. Push the tag only when permission/policy permits.

```bash
git switch main
git status -sb
git log -1 --oneline
# After verified integration:
# git tag -a v0.1.1 -m "Regression fix"
# git push origin v0.1.1
```

**Verify:** Trace release tag to tested source, review, and CI evidence.

## Applied exercises
1. Complete an offline regression and bisect investigation with a report.
2. Demonstrate reflog-based recovery of a misplaced pre-release commit.
3. Write an incident-free release checklist covering signing, CI, rollback, and permission boundaries.

## Interview prompts
- Why should a release tag point to a tested commit?
- What evidence should accompany a production hotfix PR?

**Completion:** Explain performance, security, and recovery trade-offs with reproducible evidence.
