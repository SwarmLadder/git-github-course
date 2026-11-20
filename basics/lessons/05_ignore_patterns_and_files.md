# Tracked files, .gitignore, and file removal

**Track:** Basics · **Lesson:** 05 · **Time:** 60–90 min including practice

## Objective
Protect a repository from build output and accidental secrets. Ignoring a file only affects untracked paths; it does not untrack a file already committed.

## Guided walkthrough
Commands assume a disposable **local practice repository**, not this course checkout. Git and a shell are required. Commands are illustrative and may require completing earlier lessons.

### 1. Write effective ignore rules
Use project-specific ignore rules rather than hiding everything. `git check-ignore -v` shows which pattern applies. A leading slash anchors at the .gitignore location; a trailing slash targets directories.

```bash
printf ".venv/\n__pycache__/\n*.log\n.env\n" > .gitignore
git add .gitignore
git commit -m "Ignore local outputs and credentials"
mkdir -p .venv
touch .venv/cache.txt app.log
git status --short
git check-ignore -v .venv/cache.txt app.log
```

**Verify:** The ignored files do not appear as untracked paths.

### 2. Understand tracked exceptions
A previously tracked file stays tracked after an ignore rule is added. `git rm --cached` stages removing it from Git while leaving the local working-tree file intact. Committed secrets require rotation and often history cleanup.

```bash
printf "temporary\n" > example.log
git add -f example.log
git commit -m "Track example log for demonstration"
git ls-files example.log
git rm --cached example.log
git status --short
git commit -m "Stop tracking generated log"
```

**Verify:** Removing from the current tree does not erase old commits.

### 3. Move and remove files intentionally
git mv and git rm stage a rename or deletion; Git may later detect renames by similarity, not by storing a permanent rename record.

```bash
printf "note\n" > old-name.txt
git add old-name.txt && git commit -m "Add example file"
git mv old-name.txt new-name.txt
git status --short
git commit -m "Rename example file"
git log --follow --oneline -- new-name.txt
```

**Verify:** Renames are detected when comparing snapshots.

### 4. Avoid leaking sensitive files
Never commit credentials, access tokens, or private keys—even in demo values that look real. Prevent exposure using ignore rules and secret scanning, but assume anything pushed publicly may have been copied.

```bash
git status --ignored --short
git ls-files
git diff --cached --name-only
```

**Verify:** Always review staged paths before pushing.

## Practice
1. Ignore .env and a directory of generated output, then verify each rule.
2. Demonstrate safely untracking a committed .log file.
3. Explain how to respond if an actual access token reached a public repository.

## Interview check
- Does adding .env to .gitignore purge old commits?
- Why is git rm --cached different from git rm?

**Finish when:** You can reproduce the commands in a fresh practice repo and explain every changed file, ref, and staged state.

## Put this lesson into practice — B05

Predict what Git ignores before touching the index. In the fixture, create a committed .gitignore that excludes generated data but explicitly keeps important.log. Verify with git check-ignore --no-index and git ls-files; ignored paths remain on disk.

From the **course root**, run `python tools/practice.py start B05`, work inside `.practice/B05/repo`, then run `python tools/practice.py check B05`. Save the before/after Git state in your evidence journal. Continue with the [guided workshop](../../workshops/01_worktree_index_safety.md).
