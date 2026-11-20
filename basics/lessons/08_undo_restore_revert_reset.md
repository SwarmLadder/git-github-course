# Undoing mistakes: restore, revert, and reset

**Track:** Basics · **Lesson:** 08 · **Time:** 60–90 minutes

## Goal
Choose recovery based on whether the change is unstaged, staged, committed locally, or already shared. The safest command differs by situation.

## Worked walkthrough
Unless otherwise stated, run these commands in a **disposable practice repository**. Commands requiring a remote or live GitHub account are identified. Do not run destructive examples against important work.

### 1. Restore a working-tree edit
`git restore path` replaces unstaged working-tree content with the staged version, destroying that unstaged edit. Use `git diff` first; avoid discarding work you cannot recreate.

```bash
git status --short
git diff -- some-file.txt
# Destructive to unstaged changes in this path:
# git restore -- some-file.txt
```

**Check:** Read the diff and identify whether the edit exists elsewhere before restoring.

### 2. Unstage without discarding
`git restore --staged` updates the index from HEAD, leaving working-tree content intact. It is the standard way to undo an accidental `git add`.

```bash
git add some-file.txt
git diff --cached -- some-file.txt
git restore --staged -- some-file.txt
git diff -- some-file.txt
```

**Check:** The file is still edited after unstaging.

### 3. Revert published changes
`git revert` creates a new commit reversing a prior commit's effects. It preserves shared history, although reverting a merge commit needs an explicit mainline parent and more care.

```bash
git log --oneline -5
# For an ordinary commit on your practice branch:
# git revert <commit-hash>
git log --oneline --graph -5
```

**Check:** Do not paste literal angle brackets as a commit hash; use an actual hash from your log.

### 4. Understand reset modes
`reset --soft` moves HEAD while preserving index and worktree; `--mixed` resets index; `--hard` also resets tracked working-tree files. Never use reset --hard to fix shared history blindly.

```bash
git status -sb
git reflog -5
# DANGEROUS example, intentionally not executed:
# git reset --hard HEAD~1
```

**Check:** A reset rewrites branch positioning; it does not create a compensating commit.

## Exercises
1. Recover a staged file without losing its working-tree edit.
2. Explain which command to use for undoing a published faulty commit.
3. Demonstrate reset --soft on a disposable branch and inspect status.

## Interview prompts
- When should you use revert instead of reset?
- Why is `git reset --hard` dangerous?

**Completion:** You can explain the intended history change and reproduce the workflow without disturbing another repository.
