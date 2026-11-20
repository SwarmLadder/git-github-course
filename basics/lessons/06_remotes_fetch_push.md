# Remotes, fetch, pull, and push

**Track:** Basics · **Lesson:** 06 · **Time:** 60–90 minutes

## Goal
Separate local commit creation from sharing changes. A remote is a named repository location; tracking branches are local records of the last fetched remote state.

## Worked walkthrough
Unless otherwise stated, run these commands in a **disposable practice repository**. Commands requiring a remote or live GitHub account are identified. Do not run destructive examples against important work.

### 1. Understand origin and remote-tracking refs
Clone usually configures `origin`, while `git init` does not. `origin/main` describes fetched knowledge, not a live link that updates continuously. A local main and origin/main may move independently.

```bash
git remote -v
git branch -avv
git remote show origin
git log --oneline --decorate -5
```

**Check:** In an offline practice repository, `remote show origin` needs a configured remote; use the local remote lab.

### 2. Use fetch before merging
`git fetch` downloads objects and updates remote-tracking references without merging into your current branch. Review `main..origin/main` and `main...origin/main` before integrating.

```bash
git fetch origin
git log --oneline main..origin/main
git diff --stat main...origin/main
git merge --ff-only origin/main
```

**Check:** Fast-forward-only integration avoids unexpected merge commits.

### 3. Understand push and upstream
`git push -u origin feature/name` publishes a branch and configures its upstream. Pushing can be rejected if the remote branch has advanced. Fetch and integrate first; do not force-push shared branches.

```bash
git switch -c feature/readme
git push -u origin feature/readme
git status -sb
git branch -vv
```

**Check:** The push commands need a remote you own and an authenticated connection.

### 4. Use pull intentionally
`git pull` combines fetch with reconciliation. Configure merge or rebase deliberately per team policy; `--ff-only` is safest for branches that should have no local divergence.

```bash
git pull --ff-only
git fetch --prune origin
git branch -r
```

**Check:** Fetch/prune removes stale remote-tracking names, not local topic branches.

## Exercises
1. Set up a second local repository as a bare remote and push a branch.
2. Fetch from the remote, inspect differences, and fast-forward deliberately.
3. Explain why a rejected push should not trigger an automatic `--force`.

## Interview prompts
- What changes when you run fetch versus pull?
- How is origin/main different from local main?

**Completion:** You can explain the intended history change and reproduce the workflow without disturbing another repository.

## Put this lesson into practice — B08

One local publisher has pushed an update to a local bare origin. Fetch it without moving your own main, then explain the difference between main and origin/main. Do not use git pull for this exercise.

From the **course root**, run `python tools/practice.py start B08`, work inside `.practice/B08/repo`, then run `python tools/practice.py check B08`. Save the before/after Git state in your evidence journal. Continue with the [guided workshop](../../workshops/02_offline_remotes.md).
