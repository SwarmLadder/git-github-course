# Hands-on practice: 24 graded Git labs

**Everything runs on disposable local repositories**; no GitHub account, internet, credentials, external remote, or cloud deployment is needed. The starter never alters your real projects. The checker reads Git state and selected files; it never executes a learner-authored program or shell script.

## Start, inspect and finish

Run these commands from the root of a checkout of this course:

```bash
python tools/practice.py list
python tools/practice.py start B01
cd .practice/B01/repo
git status -sb
# Make the required changes here. Return to the course root before checking.
cd ../../..
python tools/practice.py check B01
```

Each task creates an independent fixture in `.practice/<ID>/repo` and, where appropriate, a local bare remote, publisher checkout, adjacent library, or linked worktree. **Start never overwrites an existing task directory.** If you want to begin again, first inspect and back up any work you care about; then remove only that task's directory under `.practice/`. Do not delete the course repository.

The command `python tools/practice.py start <ID>` prints the goal and a clue. `check <ID>` grades the resulting repository state. If a check fails, read the error, inspect `git status`, `git log`, `git diff` and `git diff --cached`, then try again. Most tasks have several acceptable command sequences—the state, not the keystrokes, is graded.

## Basics — 8 labs

| ID | Skill | Observable success |
|---|---|---|
| B01 | First committed snapshot | notes.txt committed on main |
| B02 | Index vs worktree | Stage only notes.txt, leave config.txt unstaged |
| B03 | Topic branch | Feature commit without moving main |
| B04 | Push locally | main matches local bare origin |
| **B05** | Ignore rules and exceptions | Ignore generated paths while tracking important.log |
| **B06** | Partial staging | One hunk staged; a second remains unstaged |
| **B07** | Restore safely | Discard a tracked edit without deleting unrelated untracked notes |
| **B08** | Fetch without merging | origin/main advances while main stays put |

After Basics, complete [Workshop 01](../workshops/01_worktree_index_safety.md) and [Workshop 02](../workshops/02_offline_remotes.md).

## Intermediate — 8 labs

| ID | Skill | Observable success |
|---|---|---|
| I01 | Fast-forward | Main adopts feature tip with no merge commit |
| I02 | Merge conflict | Two-parent merge with resolved content |
| I03 | Safe shared undo | Revert preserves the original commit in history |
| I04 | Cherry-pick | Fix copied onto maintenance branch |
| **I05** | Rebase onto main | New feature commit descends from latest main |
| **I06** | Stash including untracked | Stash saves both kinds of unfinished work |
| **I07** | Squash merge | One new mainline commit, no feature ancestry |
| **I08** | Revert a merge | Preserve mainline files, undo feature changes safely |

After Intermediate, complete [Workshop 03](../workshops/03_reviewable_history.md) and [Workshop 04](../workshops/04_undo_and_conflict_triage.md).

## Advanced — 8 labs

| ID | Skill | Observable success |
|---|---|---|
| A01 | Reflog recovery | Recreate a ref at lost commit |
| A02 | Bisect | Name first bad commit and exit bisect |
| A03 | Parallel worktrees | Commit hotfix in linked checkout |
| A04 | Annotated tag | Release tag object points at verified commit |
| **A05** | Git notes | Record review evidence without amending a commit |
| **A06** | Rewrite local feature history | Squash two commits without modifying main |
| **A07** | Sparse checkout | Materialize selected directories only |
| **A08** | Local submodule | Commit gitlink and .gitmodules pointing to local library |

After Advanced, complete [Workshop 05](../workshops/05_internals_and_dependencies.md) and [Workshop 06](../workshops/06_release_and_ci_security.md).

## Safety and scope

- Fixture remotes are **local directories**. Running `git push` in B04 does not contact GitHub; fetching in B08 also stays local.
- B07's `git restore` discards edits only in a deliberately disposable practice repository. Never reuse the command on valuable work before reviewing your diffs.
- I05 and A06 rewrite only local private feature history. Do not force-push shared branches to satisfy an exercise.
- A08 needs one-command authorization for a local file transport (`git -c protocol.file.allow=always submodule add ...`); **do not set** `protocol.file.allow=always` globally.
- The course is not a hardened sandbox for executing untrusted Git hooks or scripts. Use only fixtures that you have created and trust.
- Some GitHub collaboration concepts (PR review, branch rules and approvals) require manual evaluation; these labs cannot award a real GitHub certificate or verify a production deployment.

## Practice evidence journal

For each ID, write a brief report in your own notebook (not inside the fixture unless the task asks for it): goal, predicted index/worktree/ref changes, commands used, key `status`/`log` output, failed attempt and fix, and how you would undo the operation safely. Use the [assessment rubric](../ASSESSMENT.md) to self-grade. **Do not copy solutions from the test suite; derive your commands from Git state.**
