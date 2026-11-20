# Working tree, staging, diffs, and commits

**Track:** Basics · **Lesson:** 01 · **Time:** 60–90 min including practice

## Objective
Use the index to control exactly what a commit contains. Git records the staged version, which may differ from the latest working-tree version.

## Guided walkthrough
Commands assume a disposable **local practice repository**, not this course checkout. Git and a shell are required. Commands are illustrative and may require completing earlier lessons.

### 1. Separate unstaged and staged changes
A file can contain staged edits and later unstaged edits simultaneously. Use git diff for working-tree vs index and git diff --cached for index vs HEAD; inspect both before every commit.

```bash
printf "first\n" > memo.txt
git add memo.txt
printf "second\n" >> memo.txt
git status --short
git diff -- memo.txt
git diff --cached -- memo.txt
```

**Verify:** Only 'first' is staged; 'second' remains unstaged.

### 2. Stage selective edits
git add -p lets you choose individual hunks instead of staging a whole edited file. For automated practice, stage only explicit paths and avoid git add . when unrelated output files may exist.

```bash
git add -- memo.txt
git diff --cached --stat
git diff --cached --check
git commit -m "Document first and second lines"
git status --short
```

**Verify:** git diff --cached --check detects whitespace problems in the staged diff.

### 3. Read historical changes
git show shows the contents of a commit; git log lists history. Use path filters when investigating a file. Commit messages should state intent, not simply 'changes' or 'update'.

```bash
git log --oneline --decorate -5
git show --format=short --stat HEAD
git log --oneline -- memo.txt
git show HEAD:memo.txt
```

**Verify:** The colon syntax reads a file from a commit without rewriting disk content.

### 4. Undo a staged choice without deleting work
git restore --staged moves a path out of the index but keeps working-tree edits. git restore without --staged overwrites local edits—do not confuse the two.

```bash
printf "draft\n" >> memo.txt
git add memo.txt
git restore --staged memo.txt
git status --short
git diff -- memo.txt
```

**Verify:** The draft edit still exists in your working tree.

## Practice
1. Create one commit containing only one of two changed files.
2. Stage and unstage a file, showing which diff changes at each step.
3. Inspect the last commit's patch and explain its message.

## Interview check
- Does git commit record unstaged edits automatically?
- Which command removes an edit from the index but keeps it in the working tree?

**Finish when:** You can reproduce the commands in a fresh practice repo and explain every changed file, ref, and staged state.

## Put this lesson into practice — B06

Compare HEAD, the index and the worktree for one 50-line file. Stage only the first hunk while preserving the second as an unstaged draft. Explain the differences between git diff and git diff --cached.

From the **course root**, run `python tools/practice.py start B06`, work inside `.practice/B06/repo`, then run `python tools/practice.py check B06`. Save the before/after Git state in your evidence journal. Continue with the [guided workshop](../../workshops/01_worktree_index_safety.md).
