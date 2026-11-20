# History inspection, blame, and searching

**Track:** Basics · **Lesson:** 04 · **Time:** 60–90 min including practice

## Objective
Find when a behavior changed before editing it. Git can search by path, content, author, date, or changes introduced to a particular line.

## Guided walkthrough
Commands assume a disposable **local practice repository**, not this course checkout. Git and a shell are required. Commands are illustrative and may require completing earlier lessons.

### 1. Read log shapes
git log --graph gives history topology, while --stat and --patch show changed files and lines. Filter by a path when finding the origin of a specific function or document.

```bash
git log --oneline --graph --decorate --all -12
git log --stat -3
git log --oneline -- settings.txt
git show --format=short HEAD
```

**Verify:** History is a graph; chronological listing alone hides branches and merges.

### 2. Search for introduced strings
git log -S looks for changes in the number of occurrences of a literal string. -G searches matching diff lines with a regular expression. Results depend on commit history and should be inspected.

```bash
git log --oneline -S 'color=' -- settings.txt
git log --oneline -G 'color=(red|green)' -- settings.txt
git grep -n 'color' HEAD -- '*.txt'
```

**Verify:** git grep searches tracked content in a named revision when supplied HEAD.

### 3. Trace responsibility without blame games
git blame identifies the last commit modifying each line in the chosen revision, but formatting and file moves can obscure the history. Use it to locate context, not assign fault to people.

```bash
git blame -- settings.txt
git show --format=fuller --no-patch HEAD
git log --follow --oneline -- settings.txt
```

**Verify:** --follow tracks simple renames for one path but is not a universal rename-history solver.

### 4. Compare file versions precisely
Use git diff hash1 hash2 -- path to compare endpoints and git show revision:path to inspect old content. Use hashes shown by your own log; avoid blindly pasting example object IDs.

```bash
git rev-parse HEAD
git rev-parse HEAD~1
git diff HEAD~1 HEAD -- settings.txt
git show HEAD~1:settings.txt
```

**Verify:** HEAD~1 means first parent of HEAD, which matters around merge commits.

## Practice
1. Find the commit that introduced a chosen string in a test file.
2. Use blame and show to explain one line's history.
3. Compare the same file across two commits without checking out either one.

## Interview check
- When is git blame misleading?
- How does git log -S differ from ordinary git grep?

**Finish when:** You can reproduce the commands in a fresh practice repo and explain every changed file, ref, and staged state.
