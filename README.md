# Git & GitHub — Developer Course

**36 detailed lessons · 12 graded local Git labs · 3 projects · 45 interview Q&As**

Learn to work confidently with Git history, GitHub collaboration, CI, recovery, and release governance.

| Level | Lessons | What you'll build |
|---|---:|---|
| [Basics](basics/README.md) | 12 | Branch, merge, recover, and push to a local remote |
| [Intermediate](intermediate/README.md) | 12 | Reviewable pull requests, CI, issues and release collaboration |
| [Advanced](advanced/README.md) | 12 | Reflog recovery, bisect, worktrees, safe history changes and release practices |

**Requirements:** Git 2.28+ and Python 3.10+ for local grading. GitHub CLI (`gh`) and an account are optional until GitHub-specific lessons.

## Start

```bash
git clone https://github.com/SwarmLadder/git-github-course.git
cd git-github-course
python tools/practice.py list
python tools/practice.py start B01
```

Follow the printed instructions. A practice task works inside **`.practice/`**, not your existing source repository.

```bash
python tools/practice.py check B01
python -m unittest discover -s tests -v
```

## Study routine

1. Read one lesson; predict each command's effect.
2. Reproduce examples in a disposable Git repository.
3. Complete the chapter exercises and corresponding [graded labs](practice/README.md).
4. Explain what changed in the working tree, index, refs, and history.
5. Complete [projects](projects/README.md) and [interview questions](interview/README.md).

## Quick reference

- [Command decision guide](CHEATSHEET.md) — undo, compare, merge, and recovery.
- [Git glossary](GLOSSARY.md) — key terms without filler.
- [Four-week plan](CURRICULUM.md) — milestones and competencies.
- [CI workflow](.github/workflows/course-tests.yml) — validates course content and local Git practice tooling.

**Safety:** Real network access, credentials, force pushes, repository settings, and GitHub API actions are not required for the auto-graded labs. Practice scripts never modify unrelated repositories.

[MIT License](LICENSE).
