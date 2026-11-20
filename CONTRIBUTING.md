# Contributing

Keep lessons focused and technically correct.

- Pair each concept with commands, expected Git state, failure modes, and exercises.
- Use disposable repositories for tests; never require production credentials.
- Avoid unreviewed destructive commands or promises that Git is a backup of untracked files.
- Keep code samples compatible with Git 2.28+ unless labeled optional.
- Run `python -m unittest discover -s tests -v` before proposing a PR.


## Enriched course conventions

- Maintain **36 numbered lessons** (12 per level) and **24 independent graded local labs** (8 per level). New tasks require a starter fixture, state-checking rubric, at least one valid-solution test and a failure/shortcut test.
- All generated practice data must remain inside `.practice/` or a test-owned temporary directory, and existing user files must never be overwritten. No network, credentials, third-party downloads, real GitHub repository writes or automatic production changes are permitted in grading fixtures.
- If changing `tools/practice.py` or `tools/extended_practice.py`, run both the original and extended practice tests. Never execute learner-authored scripts in a grader.
- Keep workshop submissions evidence-oriented and avoid claiming actual hosted approvals or releases from locally simulated workflows.
- Maintain [the eight-week study plan](CURRICULUM.md), [workshop index](workshops/README.md), [task catalog](practice/tasks.json) and [final assessment](ASSESSMENT.md) together when modifying counts.
- Validate from the course root: `python -m unittest discover -s tests -v`, then `python tools/practice.py list`. CI enforces lesson structure, practice fixtures and cross-document links.
