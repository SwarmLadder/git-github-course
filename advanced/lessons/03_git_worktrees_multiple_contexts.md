# git worktree: parallel local checkouts

**Advanced · Lesson 03 · Study: 90–120 minutes**

## What you will learn
Worktrees let one repository object database support multiple working directories at different branch checkouts. Useful for hotfixes, reviews, and maintaining separate environments without repeated clones.

## Technical walkthrough
Unless marked otherwise, use a disposable local practice repository. Read command comments: example placeholders and risky operations are intentionally not executable.

### 1. Create a linked worktree
Run worktree add from an existing repository to create a new directory checked out on a new or existing branch. The linked directory shares commits but has its own index and working tree.

```bash
git worktree list
git worktree add -b fix/urgent ../urgent-fix HEAD
git worktree list
git -C ../urgent-fix status -sb
```

**Verification:** Each working tree has independent tracked-file edits.

### 2. Respect branch checkout constraints
Git normally prevents checking out the same branch in two worktrees. Use dedicated branches per worktree instead of disabling safety checks.

```bash
git branch -vv
git worktree list --porcelain
git -C ../urgent-fix branch --show-current
```

**Verification:** Main can remain open in its original directory while the hotfix is edited elsewhere.

### 3. Use worktrees for review
A reviewer can add a separate worktree at a commit or branch, run tests, and remove it when done. Do not assume untracked build output is shared across worktrees.

```bash
git worktree add --detach ../review-snapshot HEAD
git -C ../review-snapshot log -1 --oneline
git -C ../review-snapshot status --short
git worktree remove ../review-snapshot
```

**Verification:** Remove only after confirming there is no valuable uncommitted work inside.

### 4. Clean up metadata safely
`git worktree list` displays linked directories. `git worktree prune` removes stale metadata for missing worktrees; it does not replace checking the filesystem and status carefully.

```bash
git worktree list
git status --short
# After finishing the hotfix and ensuring it is clean:
# git worktree remove ../urgent-fix
git worktree list
```

**Verification:** Deleting a linked directory by hand can leave stale metadata.

## Applied exercises
1. Create a hotfix worktree and commit without changing files in main's directory.
2. Open a detached review worktree and remove it safely.
3. Explain the difference between linked worktrees and separate clones.

## Interview checks
- Can two worktrees normally check out the same branch at once?
- Does each worktree get its own .git object database?

**Pass condition:** Explain the state transition, failure path, and safeguards before running advanced commands.
