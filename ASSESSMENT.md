# Final assessment — Git & GitHub

Complete one local capstone, one collaborative PR project (when a GitHub account is available), and the regression-to-release project.

## Rubric (100 points)

| Criterion | Points | Evidence |
|---|---:|---|
| Git fundamentals | 20 | staging, branching, clean commit history |
| Collaboration | 20 | reviewable PR, thoughtful review, verified merge |
| Recovery | 20 | revert/reset decisions, reflog and bisect |
| CI and security | 20 | repeatable checks, least privilege, no secrets |
| Release work | 10 | meaningful tag, change notes, tested artifact |
| Documentation | 10 | short reproduction steps and decision rationale |

**Target:** 80/100, with no unresolved credential leaks or destructive-history mistakes.

## Required practical checks

- Pass all 12 graded Git labs.
- Reproduce an intentional conflict and explain the resolution.
- Find a regression with a deterministic test and bisect.
- Recover a lost commit by creating a new ref.
- Explain why test jobs must not expose deployment credentials.
- Create an annotated tag on the verified release commit.

