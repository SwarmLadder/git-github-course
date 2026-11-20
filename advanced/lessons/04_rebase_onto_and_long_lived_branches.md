# Advanced rebasing and branch retargeting

**Advanced · Lesson 04 · Study: 90–120 minutes**

## What you will learn
A topic branch may have been based on the wrong ancestor. `git rebase --onto` retargets a range of commits without bringing along unrelated earlier work.

## Technical walkthrough
Unless marked otherwise, use a disposable local practice repository. Read command comments: example placeholders and risky operations are intentionally not executable.

### 1. Define three revision points
Identify old base, new base, and feature tip before rewriting anything. Draw the commit graph and compare patch ranges. Prefer merge if teammates rely on existing commit IDs.

```bash
git log --graph --all --oneline -15
git merge-base main feature/experiment
git log main..feature/experiment --oneline
git diff --stat main...feature/experiment
```

**Verification:** You should be able to state which commits will be replayed.

### 2. Use --onto with correct boundaries
`git rebase --onto newbase upstream branch` replays commits reachable from branch but not upstream onto newbase. It changes commit hashes and may conflict.

```bash
# Conceptual example (requires branches to exist):
# git rebase --onto main old-feature-base feature/subtask
#
# Read carefully:
# newbase = main
# upstream = old-feature-base
# branch  = feature/subtask
```

**Verification:** Mistaken boundaries can omit or duplicate commits; inspect range before executing.

### 3. Check results rather than trusting success
After rebase, compare the final diff with the intended change set. Use range-diff to compare sequences before and after when you have both tip references.

```bash
git log --oneline --graph -12
git diff --stat main...feature/subtask
# Example after saving original tip:
# git range-diff main..old-tip main..feature/subtask
```

**Verification:** Range-diff helps catch changed or dropped patches but does not replace tests.

### 4. Use a controlled remote update
If a branch you own was rebased and is published, `--force-with-lease` checks the expected remote state before overwriting it. It is still unsafe when people depend on that branch without coordination.

```bash
git fetch origin
git status -sb
# Only on your own rewritable feature branch:
# git push --force-with-lease origin feature/subtask
```

**Verification:** Never force-push a protected/shared default branch.

## Applied exercises
1. Draw a graph where a feature subtask was branched from another feature.
2. Write the correct --onto command from the graph without executing it.
3. Explain why range-diff should precede a lease-protected push.

## Interview checks
- What does the upstream argument in rebase --onto mean?
- Does force-with-lease guarantee that collaborators won't be disrupted?

**Pass condition:** Explain the state transition, failure path, and safeguards before running advanced commands.

## Put this lesson into practice — A06

Turn two local feature commits into one new commit while keeping main fixed. Record commit graph before and after; explain why the operation is limited to a private branch.

From the **course root**, run `python tools/practice.py start A06`, work inside `.practice/A06/repo`, then run `python tools/practice.py check A06`. Save the before/after Git state in your evidence journal. Continue with the [guided workshop](../../workshops/03_reviewable_history.md).
