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


## Extended decision guide — applied labs

| Goal | Command | Caution |
|---|---|---|
| Review one version in the index | `git show :path` | Reads staged content without checking it out |
| Stage a single hunk | `git add -p path` | Compare both `git diff` and `git diff --cached` afterward |
| Check ignore rules | `git check-ignore --no-index -v path` | Ignore patterns do not untrack existing commits |
| Fetch without merging | `git fetch origin` | `origin/main` is local remote-tracking state |
| Inspect commits not yet on main | `git log --oneline main..origin/main` | Review before integration |
| Rebase a private feature | `git rebase main` | Changes feature commit IDs; avoid rewriting shared branches |
| Abort a failed rebase | `git rebase --abort` | Review `git status` first |
| Save tracked + untracked work | `git stash push -u -m "WIP"` | Ignored files still excluded; stash is not a backup |
| Make a squash commit | `git merge --squash feature/name` then `git commit` | Does not retain feature commits as mainline ancestry |
| Undo a merged feature | `git revert -m 1 <merge-hash>` | Parent 1 is an explicit mainline choice, not a universal rule |
| Attach metadata without changing HEAD | `git notes add -m "reviewed" HEAD` | Notes refs are not pushed by ordinary branch push |
| Enable sparse checkout | `git sparse-checkout init --cone` then `git sparse-checkout set docs` | Does not reduce history or delete committed paths |
| Inspect gitlink | `git ls-tree HEAD vendor/library` | A `160000 commit` entry is not ordinary tracked source |
| Add a trusted local submodule | `git -c protocol.file.allow=always submodule add ../library vendor/library` | Scope file-protocol allowance to this single trusted fixture |
| Inspect a commit graph | `git log --graph --decorate --oneline --all` | Check refs before reset, rebase or merging |

For tested, guided scenarios use [24 offline labs](practice/README.md), [six workshops](workshops/README.md) and the [final assessment](ASSESSMENT.md). The commands are examples, **not** a script to paste into a production repo.
