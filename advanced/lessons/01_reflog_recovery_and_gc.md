# Reflog recovery and unreachable commits

**Advanced · Lesson 01 · Study: 90–120 minutes**

## What you will learn
The reflog records local reference movements; it can recover commits after an accidental branch move. Its entries are local and expire, so recovery is time-sensitive and not a backup policy.

## Technical walkthrough
Unless marked otherwise, use a disposable local practice repository. Read command comments: example placeholders and risky operations are intentionally not executable.

### 1. Inspect recent reference changes
`git reflog` reports where HEAD or a branch pointed over time. Use it to locate a lost-looking commit after reset or rebase. reflog is not necessarily synchronized between clones.

```bash
git reflog -10
git reflog show main -10
git log --all --oneline -10
```

**Verification:** Find the old tip before attempting any recovery.

### 2. Recover by creating a reference
When a commit still exists, create a new branch pointing at its hash rather than immediately resetting a shared branch. Verify files and tests on the recovered branch.

```bash
git reflog -8
# Replace <real-old-hash> from your own reflog:
# git branch recovered-work <real-old-hash>
# git switch recovered-work
git branch --list
```

**Verification:** Recovery branch preserves access to the commit for later inspection.

### 3. Understand garbage collection
Unreachable objects may eventually be pruned after expiration and housekeeping. `git fsck` can help locate dangling objects, but availability is not guaranteed; avoid manually running aggressive prune commands on important repos.

```bash
git fsck --no-reflogs --unreachable
git count-objects -v
git gc --help
```

**Verification:** Unreachable does not always mean immediately unrecoverable.

### 4. Choose backups over hope
Push reviewed branches to appropriate remotes and use independent backups for critical repos. Git does not automatically protect untracked files, ignored files, or unsaved editor state.

```bash
git status --short
git branch -avv
git remote -v
git log --oneline --all -8
```

**Verification:** Git history is strong for committed work; uncommitted files need other protections.

## Applied exercises
1. Create a disposable commit, move its branch backward, then recover using reflog.
2. Explain why cloning a repo may not reproduce another developer's reflog.
3. Design a repository backup plan for commits and assets.

## Interview checks
- Does a reflog entry last forever?
- What is the safest first action after discovering a lost commit?

**Pass condition:** Explain the state transition, failure path, and safeguards before running advanced commands.
