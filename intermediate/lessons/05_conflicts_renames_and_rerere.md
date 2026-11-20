# Complex conflicts, renames, and recorded resolutions

**Intermediate · Lesson 05 · Suggested time: 75–110 minutes**

## Purpose
Conflict resolution can involve rename/delete conflicts, changed interfaces, or commits moved to a new base. Git's rerere can remember repeated conflict resolutions, but never replaces code review.

## Concepts and commands
Examples run in disposable repositories. Commands marked as examples need a pre-existing branch, configured remote, or GitHub access; never paste unresolved placeholders.

### 1. Read conflict state
Unmerged paths have multiple index stages (base, ours, theirs). Inspect them before editing. During a merge, 'ours' generally means the current branch; during rebase the terms can be confusing.

```bash
git status
git ls-files -u
git diff --name-only --diff-filter=U
git diff --cc
```

**Verify:** Understand which side introduced each behavior, not just line text.

### 2. Use conflict markers carefully
Markers separate competing edits; the final file should contain valid code and both required behaviors. Some conflicts are semantic despite no textual overlap.

```bash
# Typical conflict text:
# <<<<<<< HEAD
# color=green
# =======
# color=red
# >>>>>>> feature/red
# Edit to an intentional final line, then run tests.
git diff --check
```

**Verify:** Search for lingering <<<<<<< markers before committing.

### 3. Learn rerere
`rerere.enabled` allows Git to record conflict preimages and resolutions. It can automate repeat resolutions in long-running rebases, but the reused result still needs tests and inspection.

```bash
git config --local rerere.enabled true
git config --local --get rerere.enabled
git status --short
```

**Verify:** Only enable in a disposable or team-approved repo; always review applied results.

### 4. Abort versus finish
Abort a merge or rebase when unable to validate the change. After resolving and staging, use the correct continuation command for the operation in progress.

```bash
git status
git ls-files -u
# For merge: git add ... && git commit
# For rebase: git add ... && git rebase --continue
# For cherry-pick: git add ... && git cherry-pick --continue
```

**Verify:** Different operations have different continue/abort commands.

## Practice tasks
1. Simulate a rename/delete conflict and choose a final path.
2. Enable rerere on a throwaway repo and resolve a repeated conflict.
3. Explain why a conflict-free merge can still introduce a logical bug.

## Interview check
- What does `git ls-files -u` show?
- Can rerere guarantee the reused fix remains correct?

**Evidence:** A clear commit graph, tested behavior, and a short explanation of why the workflow is appropriate.
