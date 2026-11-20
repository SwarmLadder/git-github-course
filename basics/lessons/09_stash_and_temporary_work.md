# Stash, patches, and temporary contexts

**Track:** Basics · **Lesson:** 09 · **Time:** 60–90 minutes

## Goal
A stash shelves changes when you need to switch tasks. Understand its coverage and limits; stashes are not a substitute for reviewed commits.

## Worked walkthrough
Unless otherwise stated, run these commands in a **disposable practice repository**. Commands requiring a remote or live GitHub account are identified. Do not run destructive examples against important work.

### 1. Inspect before stashing
By default, stash includes tracked modifications and staged work, not untracked files. Use `-u` when necessary, but inspect ignored and secret files before including them.

```bash
git status --short
git stash push -m "Work before urgent fix"
git stash list
git status --short
```

**Check:** After stashing, tracked changes are normally absent from the worktree.

### 2. Restore safely
`stash apply` keeps the stash entry for recovery, while `stash pop` removes it after successful application. A conflicting application requires manual resolution.

```bash
git stash list
git stash show --stat stash@{0}
git stash apply stash@{0}
git status --short
```

**Check:** Use apply first when you're unsure whether restoration will conflict.

### 3. Move unfinished work to its own branch
`git stash branch` creates a new branch at the original base for a stash and applies its changes; useful after the current main branch has changed substantially.

```bash
git stash list
# Example only when a stash exists:
# git stash branch feature/continue-work stash@{0}
git branch --list
```

**Check:** Avoid deleting the stash until work is verified on the new branch.

### 4. Use a patch for review or transfer
`git diff > change.patch` produces a textual patch for unstaged tracked changes; `git apply --check` tests whether it can apply. Patches omit some metadata and are not a replacement for Git history.

```bash
git diff --stat
git diff --binary > local-change.patch
git apply --check local-change.patch
git status --short
```

**Check:** The patch file itself becomes untracked; do not accidentally commit a duplicate diff.

## Exercises
1. Stash tracked and untracked files, then restore on a throwaway branch.
2. Compare apply and pop when a conflict occurs.
3. Make and check a patch without modifying committed history.

## Interview prompts
- Will plain git stash include new untracked files?
- Why is a stash a poor long-term backup?

**Completion:** You can explain the intended history change and reproduce the workflow without disturbing another repository.

## Put this lesson into practice — I06

This later Intermediate lab includes a staged edit and an untracked draft. Prove why a plain stash would miss the draft; use git stash push -u and inspect the saved content without popping it.

From the **course root**, run `python tools/practice.py start I06`, work inside `.practice/I06/repo`, then run `python tools/practice.py check I06`. Save the before/after Git state in your evidence journal. Continue with the [guided workshop](../../workshops/04_undo_and_conflict_triage.md).
