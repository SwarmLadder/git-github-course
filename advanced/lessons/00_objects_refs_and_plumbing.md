# Git internals: objects, trees, commits, and refs

**Advanced · Lesson 00 · Study: 90–120 minutes**

## What you will learn
Know enough plumbing to debug history and recover misplaced commits. Git stores content-addressed objects and references; branch names are mutable references, not copies of files.

## Technical walkthrough
Unless marked otherwise, use a disposable local practice repository. Read command comments: example placeholders and risky operations are intentionally not executable.

### 1. Inspect an object
Use rev-parse to resolve names to objects, cat-file to inspect object types and metadata, and ls-tree to list a tree's entries. These commands inspect local objects without changing the working tree.

```bash
git rev-parse HEAD
git cat-file -t HEAD
git cat-file -p HEAD
git ls-tree HEAD
git ls-tree -r --name-only HEAD
```

**Verification:** HEAD resolves to a commit; a commit references a tree and parent hashes.

### 2. Blobs and trees
A blob stores file content, a tree maps names to blob/tree objects, and a commit names a root tree plus parents and metadata. Git hashes objects, and the exact object ID algorithm depends on repository format.

```bash
git rev-parse HEAD^{tree}
git cat-file -t HEAD^{tree}
git ls-tree -r HEAD
git hash-object README.md
```

**Verification:** The file's blob ID is not the same as the commit ID.

### 3. Read references
HEAD typically points symbolically at a branch. show-ref displays local references; packed refs may not appear as loose files, so rely on Git commands rather than reading .git/refs paths directly.

```bash
git symbolic-ref HEAD
git show-ref --heads
git for-each-ref --format='%(refname:short) %(objectname:short)'
git branch -vv
```

**Verification:** Refs move as commits are added; old commits can remain in the object database.

### 4. Distinguish revision syntax
HEAD^ means a parent, HEAD~n follows first parents n times, and HEAD^2 selects the second parent of a merge commit. Use actual commits for the exercises; shallow or root histories may not have these ancestors.

```bash
git rev-parse HEAD
git log --oneline --graph --all -10
# On a non-root commit:
# git rev-parse HEAD^
# On a merge commit:
# git rev-parse HEAD^2
```

**Verification:** Different paths through merge history produce different comparisons.

## Applied exercises
1. Create three commits and diagram the commit→tree→blob relationships.
2. Inspect a merge commit's two parent IDs.
3. Explain why a branch rename does not change commit content.

## Interview checks
- Does a branch contain file content itself?
- Why may SHA-1 and SHA-256 Git repository object IDs differ?

**Pass condition:** Explain the state transition, failure path, and safeguards before running advanced commands.

## Put this lesson into practice — A05

Attach review evidence to the current commit with Git notes. Prove the commit object ID did not change, and explain why notes refs must be published explicitly if other clones need them.

From the **course root**, run `python tools/practice.py start A05`, work inside `.practice/A05/repo`, then run `python tools/practice.py check A05`. Save the before/after Git state in your evidence journal. Continue with the [guided workshop](../../workshops/05_internals_and_dependencies.md).
