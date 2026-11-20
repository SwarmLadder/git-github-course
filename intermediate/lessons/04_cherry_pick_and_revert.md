# Cherry-pick and revert for targeted changes

**Intermediate · Lesson 04 · Suggested time: 75–110 minutes**

## Purpose
Cherry-pick applies the change introduced by a chosen commit onto another branch; revert makes a new inverse change. Both require attention to dependencies and conflicts.

## Concepts and commands
Examples run in disposable repositories. Commands marked as examples need a pre-existing branch, configured remote, or GitHub access; never paste unresolved placeholders.

### 1. Pick one change, not a whole feature
Cherry-pick is useful for a specific fix across maintenance branches when merging an entire feature would be inappropriate. It creates a new commit identity on the target.

```bash
git log --oneline feature/notes -5
git switch maintenance
# Choose a hash shown in the above log:
# git cherry-pick <commit-hash>
git log --oneline -4
```

**Verify:** If the picked commit depends on earlier changes, one commit may not be enough.

### 2. Handle cherry-pick conflicts
A cherry-pick can conflict when context has diverged. Inspect and resolve like a merge; use --continue to finish or --abort to restore the branch.

```bash
git status
git diff --name-only --diff-filter=U
# After resolving:
# git add affected-file
# git cherry-pick --continue
# Or git cherry-pick --abort
```

**Verify:** Do not assume Git can preserve correctness across API changes.

### 3. Revert without rewriting shared history
Revert makes a new commit that reverses the specified change. It is generally suitable for already published branches; reverting a merge requires a parent choice and may affect future merges.

```bash
git log --oneline -5
# Inspect the change first:
# git show <commit-hash>
# Then, if rollback is intended:
# git revert <commit-hash>
```

**Verify:** A revert is an additive change to history, not removal of the original commit.

### 4. Backport verification
A backported fix should be tested against the maintenance release, not only on the original branch. Dependencies and data formats may differ.

```bash
git status --short
git log --oneline -5
git diff --check HEAD~1 HEAD
```

**Verify:** Record the original issue/commit in the new commit or PR description.

## Practice tasks
1. Backport a one-file fix from a feature branch into a maintenance branch.
2. Create a revert commit and confirm the original commit still appears in history.
3. Describe why cherry-picking a database migration without its code can be unsafe.

## Interview check
- Does cherry-pick preserve the original commit hash?
- When should a published change be reverted rather than reset?

**Evidence:** A clear commit graph, tested behavior, and a short explanation of why the workflow is appropriate.
