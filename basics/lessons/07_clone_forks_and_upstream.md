# Cloning, forks, and upstream contributions

**Track:** Basics · **Lesson:** 07 · **Time:** 60–90 minutes

## Goal
A clone copies a Git repository's history and configures a remote. A GitHub fork is a separate server-side repository that commonly enables contributions without write access to the original.

## Worked walkthrough
Unless otherwise stated, run these commands in a **disposable practice repository**. Commands requiring a remote or live GitHub account are identified. Do not run destructive examples against important work.

### 1. Clone and inspect safely
Cloning into a new directory avoids changing your existing project. Inspect remotes and the active branch immediately. For large repos, limited history may reduce download size, but shallow clones have history restrictions.

```bash
git clone https://github.com/SwarmLadder/python-notebook.git course-example
cd course-example
git remote -v
git status -sb
git log --oneline -3
```

**Check:** This example needs internet access; do not clone inside another repo unintentionally.

### 2. Know origin and upstream
For a fork, origin usually points to your fork; upstream conventionally points to the source project. These are names, not special Git privileges.

```bash
git remote -v
# After forking on GitHub, in your clone:
git remote add upstream https://github.com/SwarmLadder/python-notebook.git
git fetch upstream
git branch -r
```

**Check:** If upstream already exists, inspect it instead of adding another.

### 3. Sync without rewriting collaborators' work
Before contributing, fetch upstream and update your local main according to team policy. Use `--ff-only` if you expect your local main to track upstream without local commits.

```bash
git switch main
git fetch upstream
git merge --ff-only upstream/main
git status -sb
```

**Check:** Never assume your local default branch is named main without checking.

### 4. Make a focused contribution
Branch, implement one change, test, push to your fork, and propose a pull request with motivation and evidence. Keep PRs reviewable rather than mixing unrelated work.

```bash
git switch -c docs/improve-setup
git status -sb
# Edit a file, then review and commit it.
git diff --check
git add README.md
git commit -m "Clarify setup steps"
git push -u origin docs/improve-setup
```

**Check:** The remote must be your fork to allow pushes; commands require an actual edit.

## Exercises
1. Draw where origin, upstream, and a contributor's branch point.
2. Sync a fork in a disposable example using a second local repo as upstream.
3. Draft a PR description that includes purpose, tests, and risks.

## Interview prompts
- Does git clone create a GitHub fork?
- Why would you not commit directly on the main branch of a fork?

**Completion:** You can explain the intended history change and reproduce the workflow without disturbing another repository.
