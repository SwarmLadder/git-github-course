# Git's model, setup, and identity

**Track:** Basics · **Lesson:** 00 · **Time:** 60–90 min including practice

## Objective
Understand what Git stores before learning commands. A Git repository holds objects, references, and an index; it is not a running backup of every editor action.

## Guided walkthrough
Commands assume a disposable **local practice repository**, not this course checkout. Git and a shell are required. Commands are illustrative and may require completing earlier lessons.

### 1. Configure a safe practice environment
Use repository-local identity so the course does not change global settings. Modern Git identifies commits by their contents and parents; author name and email are metadata, not GitHub authentication.

```bash
git --version
mkdir -p git-practice && cd git-practice
git init -b main
git config user.name "Course Learner"
git config user.email "learner@example.test"
git config --local --list
```

**Verify:** Identity is local to this repo; it won't alter other repos.

### 2. Inspect working tree, index, and history
Files you edit live in the working tree; files you stage make up the next commit snapshot. Committed snapshots are referenced by names such as branches. A fresh repo has a branch name but no commit yet.

```bash
git status --short --branch
printf "Start here\n" > notes.txt
git status --short
git add notes.txt
git status --short
git commit -m "Add first note"
git log -1 --oneline
```

**Verify:** Before git add, a new file is untracked; afterward it is staged.

### 3. See commit identity and content
A commit references a tree and zero or more parent commits. Its hash identifies content including metadata. Git stores snapshots efficiently through object reuse; thinking 'every commit is a complete copy on disk' is misleading.

```bash
git show --stat --oneline HEAD
git show --format=fuller --no-patch HEAD
git rev-parse HEAD
git ls-tree -r --name-only HEAD
```

**Verify:** Compare commit hash and parent information to the tracked file list.

### 4. Choose safe defaults
Set a clear main branch and leave remote configuration for the later GitHub lesson. Never paste credentials into shell commands or put secrets in tracked files. Run this material inside a disposable practice directory.

```bash
git branch --show-current
git config --local --get user.email
git status --porcelain=v1
git remote -v
```

**Verify:** No remote means local work does not require an internet connection.

## Practice
1. Explain what changes when editing a tracked file without staging.
2. Create a second commit with a meaningful message and inspect its parent.
3. Identify the repository's HEAD commit, tracked files, and configured identity.

## Interview check
- Why can a newly initialized branch have no commits?
- Does git config user.email grant permission to push to GitHub?

**Finish when:** You can reproduce the commands in a fresh practice repo and explain every changed file, ref, and staged state.
