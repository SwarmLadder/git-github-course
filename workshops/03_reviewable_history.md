# Workshop 03 — Rebase, squash and reviewable pull requests

**Track:** Intermediate · **Recommended after:** lessons 00–04 · **Labs:** I01, I05, I07 · **Time:** 90–120 minutes

## Outcome

Practice a focused feature rebase and a squash merge, then prepare a reviewer-friendly change explanation. The goal is not simply a green check; it is a history that tells the truth and a diff that a teammate can inspect.

## Decision guide

| Strategy | Preserve feature commit IDs? | Merge commit? | Good fit |
|---|---|---|---|
| Fast-forward | Yes | No | Topic branch is already on main's history |
| Merge commit | Yes | Yes | Preserve collaboration and branch topology |
| Squash merge | No, creates new commit | No | Collapse a small feature into a single mainline change |
| Rebase local feature | No, replays commits | No by itself | Update your private topic branch before review |

Rebasing *shared* history requires careful coordination. This workshop uses private disposable branches only.

## Guided procedure

1. Complete I05. Before rebasing, draw this graph with commit letters:

```text
base --- newer-main            (main)
  \
   feature-work                (feature/reports)
```

Predict the new feature parent after `git rebase main`. Run it from the feature branch. Verify the result with `git merge-base main feature/reports`, `git rev-list --count main..feature/reports` and `git log --graph --all --oneline`. The feature commit ID will change even though its net content remains.

2. Complete I07 from main. Compare `git merge feature/promo` with `git merge --squash feature/promo` *before* running anything. A squash stages the resulting content but requires a separate commit; it does not record the feature commits as ancestors of the new main tip.

3. Draft a pull request description **without needing GitHub**:

```markdown
## Why
Explain the user-visible problem.

## Changes
Summarize the net diff and any deliberately excluded work.

## Tests
List exact commands and outcomes.

## Risks and rollback
State whether the change can be reverted independently.

## Review request
Point to one design or behavior you want challenged.
```

4. Pretend to review a teammate's PR. Inspect `git diff main...feature/reports` to compare from merge base. Ask whether the feature includes unexpected files, test updates, secret material, or unrelated formatting.

## Failure clinic

**My rebase stops with conflicts.** Read `git status`, resolve the displayed files, stage them and `git rebase --continue`. If the branch is not safe to continue, `git rebase --abort` restores the pre-rebase position.

**I squashed but no commit appeared.** `git merge --squash` populates the index and working tree; you must commit the squashed change yourself.

**I rebased published history.** Do not immediately force-push. Coordinate with collaborators, assess what changed, and use a fresh branch or a safer merge when possible.

## Evidence to submit

An ASCII commit graph before and after I05, a one-parent squashed mainline commit in I07, and a full sample PR description. Rate your own diff for scope, consistency, tests and reversibility.

**Completion gate:** You can explain *why* a team should prefer one strategy and the consequences for review, attribution, debugging and rollback.
