# Project 3 — Regression investigation and release

**Goal:** Find a regression, recover work, apply a fix, and create a verifiable tag.

1. Create a disposable repo with a deterministic test.
2. Make at least 7 logical commits; one introduces a regression.
3. Use `git bisect` and keep the first-bad-commit evidence.
4. On a separate disposable branch, simulate a mistaken reset; recover using reflog.
5. Fix the regression on a topic branch and demonstrate tests.
6. Explain whether the fix should be merged, cherry-picked, or reverted.
7. Create an annotated release tag on the tested final commit.
8. Write a short release note: changes, tests, risks, and rollback procedure.

**Deliverables:** bisect findings, recovery proof, graph, tested release tag, notes.

**Avoid:** rewriting a real shared main branch or using force pushes to hide mistakes.
