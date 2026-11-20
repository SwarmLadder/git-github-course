# Git & GitHub — Complete Developer Course

**36 detailed lessons · 24 graded offline Git labs · 6 applied workshops · 3 portfolio projects · 45 interview Q&As**

Learn version control from your first commit through collaborative code review, advanced recovery, dependency management, CI security and trustworthy releases.

## Learning paths

| Level | Lessons | Graded labs | Applied work |
|---|---:|---:|---|
| [Basics](basics/README.md) | 12 | B01–B08 | Index/worktree safety, local teamwork and remotes |
| [Intermediate](intermediate/README.md) | 12 | I01–I08 | PR review, rebase/squash, stash, conflict and merge recovery |
| [Advanced](advanced/README.md) | 12 | A01–A08 | Reflog/bisect, worktrees, notes, sparse checkout, submodules and releases |

**Requirements:** Git 2.28+ and Python 3.10+ for local grading. A shell is useful. A GitHub account and GitHub CLI (`gh`) are optional for the basic/automatically graded labs; online platform workflows are presented as optional applications or clearly marked simulations.

## Start

```bash
git clone https://github.com/SwarmLadder/git-github-course.git
cd git-github-course
python tools/practice.py list
python tools/practice.py start B01
```

Each task works inside **`.practice/<ID>/`**, not your existing source repository. For example:

```bash
cd .practice/B01/repo
git status -sb
# Complete the goal printed by start.
cd ../../..
python tools/practice.py check B01
python -m unittest discover -s tests -v
```

The checker inspects Git state; it does not run learner scripts or connect to GitHub. Graded tasks use isolated local repositories, including local bare remotes where needed. **Do not use the course checkout itself for history-rewriting experiments.**

## Study routine

1. Follow the [eight-week curriculum](CURRICULUM.md) at your own pace.
2. Read one of the **36 lessons**, predict each command's effect on `HEAD`, index, worktree and refs, then reproduce examples in a disposable repository.
3. Complete the corresponding [24 graded labs](practice/README.md). Examine the failure message, not just the pass result.
4. Work through the [six guided workshops](workshops/README.md) to build an evidence journal, rehearse diagnosis, and explain collaboration/security tradeoffs.
5. Build all [three portfolio projects](projects/README.md) and review the [45 interview Q&As](interview/README.md).
6. Finish with the [100-point final assessment](ASSESSMENT.md), including mandatory safety gates.

## Choose a starting point

- **New to Git?** Begin with [the Git data model](basics/lessons/00_git_model_and_setup.md), then B01 and B02.
- **Already committing?** Practice [fetch without merging](workshops/02_offline_remotes.md) and B08.
- **Preparing to contribute?** Follow [reviewable history](workshops/03_reviewable_history.md), then I05 and I07.
- **Recovering from mistakes?** Try [stash/merge triage](workshops/04_undo_and_conflict_triage.md) and A01/A02.
- **Working on releases?** Take [CI and release security](workshops/06_release_and_ci_security.md) and [project 3](projects/03_regression_release.md).

## References

- [Command decision guide](CHEATSHEET.md) — safe undo, comparison, remotes, recovery and advanced Git.
- [Glossary](GLOSSARY.md) — index, objects, refs, worktrees, forks, CI and GitHub governance.
- [Practice](practice/README.md) — setup, goals, caveats and results for 24 checked labs.
- [Continuous integration](.github/workflows/course-tests.yml) — validates all course content, fixtures and local Git checking code.

**Safety and privacy:** No account, real network access, production token or credential is needed for local labs. They never modify unrelated repositories. Manual GitHub/CI exercises do not create real releases or verify production approval. The exercises are teaching environments, not hardened sandboxes for arbitrary hostile Git hooks or scripts.

[MIT License](LICENSE) · [Contributing](CONTRIBUTING.md)
