# Merging and resolving conflicts

**Track:** Basics · **Lesson:** 03 · **Time:** 60–90 min including practice

## Objective
A merge integrates histories. Fast-forward moves a branch tip; a three-way merge creates a commit joining two lines of development when both diverged.

## Guided walkthrough
Commands assume a disposable **local practice repository**, not this course checkout. Git and a shell are required. Commands are illustrative and may require completing earlier lessons.

### 1. Fast-forward merge
When main is an ancestor of the feature branch, Git can move main forward without a merge commit. This preserves commits as-is, but it does not create an explicit merge record.

```bash
git switch main
git merge --ff-only feature/notes
git log --graph --oneline --decorate -5
```

**Verify:** --ff-only refuses if histories have diverged; it never silently creates a merge commit.

### 2. Create divergence deliberately
Use two branches to change the same line differently. A line conflict is evidence that Git cannot safely choose an intended result, not that your repository is corrupted.

```bash
printf "color=blue\n" > settings.txt
git add settings.txt
git commit -m "Add color preference"
git switch -c feature/red
printf "color=red\n" > settings.txt
git commit -am "Prefer red"
git switch main
printf "color=green\n" > settings.txt
git commit -am "Prefer green"
```

**Verify:** Branches now disagree about the same line in settings.txt.

### 3. Resolve conflict as a decision
Attempt the merge. On conflict, inspect git status and the conflict markers; choose an intentional final value, delete the markers, stage the file, and complete the merge.

```bash
git merge feature/red
# Expected conflict: inspect settings.txt and git status.
# Edit settings.txt manually to your chosen color; remove markers.
git add settings.txt
git commit -m "Resolve color preference conflict"
git log --graph --oneline --all -6
```

**Verify:** Do not run the commands after the comment without actually editing the conflicted file.

### 4. Abort safely if needed
When you cannot resolve a merge immediately, git merge --abort normally restores the pre-merge state. Resolve carefully if you had unrelated local changes when starting the merge.

```bash
git status
git diff --name-only --diff-filter=U
git log --oneline --graph --all -8
```

**Verify:** No unmerged paths should remain after resolution.

## Practice
1. Construct both a fast-forward and a conflict-producing merge in separate repos.
2. Resolve a conflict by combining both sides' intent, not choosing blindly.
3. Explain what parents a non-fast-forward merge commit has.

## Interview check
- Why should merge conflict markers never be committed?
- When does git merge --ff-only reject a merge?

**Finish when:** You can reproduce the commands in a fresh practice repo and explain every changed file, ref, and staged state.
