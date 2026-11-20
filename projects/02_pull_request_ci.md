# Project 2 — Reviewable pull request with CI

**Goal:** Deliver one change through GitHub without bypassing collaboration controls.

1. Use a repository you control (or a fork with permission).
2. Create a specific issue with acceptance criteria.
3. Create a topic branch, implement one feature and a regression test.
4. Add a small GitHub Actions workflow running tests on push/PR.
5. Push, create a PR, and document why/what/tests/risks.
6. Review a peer's PR or perform a structured self-review.
7. Fix a review finding and verify checks.
8. Merge using the team's selected strategy and confirm behavior on main.

**Deliverables:** issue, PR, CI run, review notes, merged commit graph.

**Safety:** Test jobs use least-privilege tokens, no secrets for untrusted PR code, and no `pull_request_target` shortcuts.
