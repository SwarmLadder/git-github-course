# Branches, HEAD, and switching

**Track:** Basics · **Lesson:** 02 · **Time:** 60–90 min including practice

## Objective
A branch is a movable name pointing at a commit, not a second full copy of the repository. Switching changes your current HEAD and may update tracked working-tree files.

## Guided walkthrough
Commands assume a disposable **local practice repository**, not this course checkout. Git and a shell are required. Commands are illustrative and may require completing earlier lessons.

### 1. Create a topic branch
Branch from an existing commit, work on the branch, and keep main stable. Use descriptive names such as feature/search; a slash is just a naming convention.

```bash
git switch -c feature/notes
git branch --show-current
git branch -vv
printf "feature work\n" >> memo.txt
git add memo.txt
git commit -m "Extend notes on feature branch"
```

**Verify:** The new commit advances feature/notes but leaves main at its previous tip.

### 2. Compare branches
Branch tips may differ. Use git log --graph --all to see history and git diff main...feature/notes to inspect a topic's changes relative to their merge base.

```bash
git log --graph --decorate --oneline --all -8
git diff --stat main...feature/notes
git merge-base main feature/notes
```

**Verify:** Three-dot diff is useful for reviewing a feature from its common ancestor.

### 3. Switch without losing work
A switch may be refused when local changes would be overwritten. Commit, stash, or explicitly discard edits after inspection. Avoid forcing checkout as a default solution.

```bash
git status --short
git switch main
git branch --show-current
git log --oneline -2
git switch feature/notes
```

**Verify:** Your feature commit remains reachable through its branch name.

### 4. Branch deletion rules
After changes are integrated, delete an unnecessary branch with -d; Git checks merge status. -D forces deletion and can hide otherwise unreferenced commits, so understand recoverability first.

```bash
git branch --list
git branch --merged main
git status --short
```

**Verify:** Inspect integration before deleting branches; do not run forced deletion casually.

## Practice
1. Create a feature branch and commit a new file without changing main.
2. Show the merge base and a three-dot diff.
3. Switch back to main and verify the feature file is absent there.

## Interview check
- Does deleting a branch immediately delete all its commit objects?
- What happens when switching would overwrite uncommitted edits?

**Finish when:** You can reproduce the commands in a fresh practice repo and explain every changed file, ref, and staged state.
