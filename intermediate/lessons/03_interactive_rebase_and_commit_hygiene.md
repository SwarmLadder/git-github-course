# Interactive rebase and commit hygiene

**Intermediate · Lesson 03 · Suggested time: 75–110 minutes**

## Purpose
Before sharing, you can clean up a local feature history into understandable commits. Rebase rewrites hashes; use it on branches whose history you own.

## Concepts and commands
Examples run in disposable repositories. Commands marked as examples need a pre-existing branch, configured remote, or GitHub access; never paste unresolved placeholders.

### 1. Understand the rebase todo
`git rebase -i` opens a list of commits in replay order. Options include pick, reword, edit, squash, and fixup. Begin in a disposable branch rather than experimenting on main.

```bash
git switch feature/notes
git log --oneline --max-count=8
# Opens an editor; intentionally not automated:
# git rebase -i HEAD~3
```

**Verify:** Only run HEAD~3 if this branch has at least three commits.

### 2. Combine fixup commits
A `fixup!` commit marks intent to fold into an earlier commit. `--autosquash` arranges fixups during interactive rebase, subject to an editor review.

```bash
git log --oneline -5
# After editing files to fix an earlier commit:
# git add affected-file
# git commit --fixup=<commit-hash>
# git rebase -i --autosquash <base-commit>
```

**Verify:** Avoid rewriting already reviewed shared history without team agreement.

### 3. Recover from conflicts
During a rebase conflict, inspect markers, resolve intentionally, stage the resolved file, and continue. `git rebase --abort` returns the original branch to its pre-rebase state.

```bash
git status
git diff --name-only --diff-filter=U
# After editing conflict markers:
# git add affected-file
# git rebase --continue
# Or: git rebase --abort
```

**Verify:** Don't create an extra git commit manually unless the specific workflow requires it.

### 4. Keep author and reviewer context
Use reword for messages and edit for content changes. A polished history should remain logically bisectable: independent fixes should not be fused only to reduce the number of commits.

```bash
git log --format='%h %s' -10
git show --stat --oneline HEAD
git diff --check HEAD~1 HEAD
```

**Verify:** A good commit can be explained and, ideally, reverted independently.

## Practice tasks
1. Create three commits and use interactive rebase to combine only two.
2. Resolve a rebase conflict and verify tests afterward.
3. Explain when one large squash is worse than retaining two logical commits.

## Interview check
- Is interactive rebase safe for already shared main history?
- How does fixup differ from a normal follow-up commit?

**Evidence:** A clear commit graph, tested behavior, and a short explanation of why the workflow is appropriate.

## Put this lesson into practice — I05

The feature branch was created before main advanced. Rebase the private feature commit onto the newer main. Record its old and new commit hashes and explain why shared branch history must not be casually rewritten.

From the **course root**, run `python tools/practice.py start I05`, work inside `.practice/I05/repo`, then run `python tools/practice.py check I05`. Save the before/after Git state in your evidence journal. Continue with the [guided workshop](../../workshops/03_reviewable_history.md).
