# Merge commit, squash, and rebase strategies

**Intermediate · Lesson 02 · Suggested time: 75–110 minutes**

## Purpose
Three common integration approaches produce different histories. Choose deliberately based on traceability, branch shape, and team policy.

## Concepts and commands
Examples run in disposable repositories. Commands marked as examples need a pre-existing branch, configured remote, or GitHub access; never paste unresolved placeholders.

### 1. Recognize a merge commit
A non-fast-forward merge commit records multiple parents and preserves the source branch's commits. Useful when the sequence of feature commits matters for audit or bisectability.

```bash
git log --graph --decorate --oneline --all -12
git show --no-patch --format='%h %p %s' HEAD
git rev-list --parents -n 1 HEAD
```

**Verify:** A merge commit normally has at least two parent hashes.

### 2. Understand squash integration
Squashing combines a feature's net changes into one new commit on the target. It makes main history concise but removes original per-commit steps from that branch's first-parent path.

```bash
# In a disposable repo with a feature branch:
git switch main
git merge --squash feature/notes
git status --short
git diff --cached --stat
git commit -m "Add feature as one change"
```

**Verify:** A squash commit is not a two-parent merge commit.

### 3. Rebase replays commits
Rebase places each commit's patch onto a new base, creating new commit identities. It can yield linear history, but should not be used to silently rewrite a branch others depend on.

```bash
git switch feature/notes
git fetch origin
git rebase origin/main
git log --oneline --graph -8
```

**Verify:** If conflicts arise, resolve and git rebase --continue or abort.

### 4. Choose strategy under policy
Squash for noisy incremental branches, merge for preserved context, rebase for clean topic history. Required checks and branch rules can constrain available buttons on GitHub.

```bash
git log --first-parent --oneline main -8
git merge-base main feature/notes
git diff --stat main...feature/notes
```

**Verify:** Avoid universal claims about a single best strategy.

## Practice tasks
1. Draw three histories for a two-commit feature under merge, squash, and rebase.
2. Explain why rebase creates different hashes for replayed commits.
3. Recommend a merge policy for a small shared library and justify it.

## Interview check
- Is a squash commit a merge commit?
- Why is rebase risky on a shared published branch?

**Evidence:** A clear commit graph, tested behavior, and a short explanation of why the workflow is appropriate.

## Put this lesson into practice — I07

Compare squash and merge ancestry in a disposable repository. Squash a two-commit feature into one mainline commit without making its source commits ancestors. A squash does not create the commit automatically.

From the **course root**, run `python tools/practice.py start I07`, work inside `.practice/I07/repo`, then run `python tools/practice.py check I07`. Save the before/after Git state in your evidence journal. Continue with the [guided workshop](../../workshops/03_reviewable_history.md).
