# Portfolio projects

These projects combine the chapters rather than repeat command examples.

1. [Project 1 — Local team workflow](01_local_team_workflow.md): working repo, bare remote, branch, merge, clean history.
2. [Project 2 — PR review and CI](02_pull_request_ci.md): GitHub feature branch, focused PR, tests, review notes and CI.
3. [Project 3 — Regression-to-release](03_regression_release.md): bisect, reflog recovery, hotfix and annotated release tag.

**Submission standard:** concise README, key command outputs or screenshots (without secrets), commit graph, and why you chose each merge/recovery approach.

## Evidence standard for the enriched course

**Project 1:** show clean local branches and a bare remote; prove you can inspect an updated remote without merging it (B04/B08). Refer to [Workshop 02](../workshops/02_offline_remotes.md).

**Project 2:** show a reviewable PR diff, purposeful rebase/squash choice, test outcomes and safe CI permission boundaries (I05/I07). Refer to [Workshop 03](../workshops/03_reviewable_history.md). A local simulation is acceptable if explicitly identified as such.

**Project 3:** include a deterministic bisect trace, recovery reference, tested release tag and security/rollback notes (A01/A02/A04/A05). Refer to [Workshop 06](../workshops/06_release_and_ci_security.md).

Score the three submissions with [the final rubric](../ASSESSMENT.md). Automated lab passes alone are not equivalent to complete project evidence.
