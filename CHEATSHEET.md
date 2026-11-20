# Git decision guide

| Goal | Command | Important caveat |
|---|---|---|
| Inspect changes | `git status -sb` · `git diff` | Untracked files aren't shown by git diff |
| Inspect staged content | `git diff --cached` | Review before committing |
| Stage a path | `git add path` | Stages current version of the path |
| Unstage safely | `git restore --staged path` | Keeps worktree edits |
| Discard unstaged tracked edits | `git restore path` | **Destructive** |
| Create a branch | `git switch -c feature/name` | Starts from current commit |
| Switch to main | `git switch main` | May refuse if edits would be overwritten |
| View commit history | `git log --graph --all --oneline` | History is a DAG |
| Inspect a commit | `git show hash` | No worktree changes |
| Fetch remote updates | `git fetch origin` | Does not merge automatically |
| Integrate fast-forward only | `git merge --ff-only origin/main` | Rejects divergence |
| Merge topic branch | `git merge feature/name` | May conflict |
| Undo a shared commit | `git revert hash` | Creates a new commit |
| Rewrite local branch | `git reset --soft HEAD~1` | Moves HEAD, keeps index |
| Reset tracked files | `git reset --hard ...` | **Destructive; avoid for shared history** |
| Temporarily save changes | `git stash push -u` | Includes untracked, not ignored files |
| Recover a lost commit | `git reflog` then `git branch recovery hash` | Local history can expire |
| Locate a regression | `git bisect` | Test must be deterministic |
| Parallel checkouts | `git worktree add ...` | Linked worktree, same object database |
| Create a milestone | `git tag -a v1.0.0 -m "..."` | Pushing tag is separate |

**Before anything destructive:** check `git status`, `git diff`, current branch, and a recovery path. Never paste actual passwords or API tokens into Git history.
