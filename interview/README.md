# Git & GitHub interview practice

Use the [45 short Q&As](QUESTIONS.md) after completing the respective lessons.

**Three mock rounds**

- Junior (30 minutes): staging/index, safe undo, branches, merge conflicts, remotes.
- Mid-level (45 minutes): PR reviews, squash/rebase/cherry-pick, forks, CI, check failures.
- Senior (60 minutes): reflog/bisect, history policy, monorepo performance, supply-chain safety, protected releases.

**Score out of 100:** correct concepts 30; command choice 25; failure recovery 20; collaboration/security 15; explanation 10. Aim for 80+ and explain unsafe alternatives.

Interview evidence should come from [graded labs](../practice/README.md) and [projects](../projects/README.md), not memorized command strings.


## Demonstration rounds for the enriched course

- **Junior:** show a staged hunk, identify what belongs to index vs worktree, explain why fetching does not merge (B06, B08).
- **Mid-level:** draw a feature rebase and squash graph, show a stash with an untracked draft, explain the correct mainline for a merge revert (I05–I08).
- **Senior:** find a regression, verify a sparse checkout and submodule pointer, explain untrusted GitHub Actions PR boundaries and a release rollback (A02, A07, A08).

Ask each learner for one real command output and one safe recovery strategy per answer. For preparation use the [six guided workshops](../workshops/README.md) and the [100-point assessment](../ASSESSMENT.md); a simulated GitHub review must not be presented as a real accepted PR.
