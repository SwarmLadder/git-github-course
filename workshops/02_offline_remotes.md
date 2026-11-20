# Workshop 02 — Remotes and collaboration without internet access

**Track:** Basics · **Recommended after:** lessons 06 and 07 · **Labs:** B03, B04, B08 · **Time:** 75–105 minutes

## Outcome

Distinguish your local branch `main`, the local remote-tracking reference `origin/main`, and the real tip of a separate bare repository. Fetch another contributor's work without integrating or overwriting your own branch.

## The three places that matter

A Git repository has its own refs. Adding a remote does not merge content. A remote-tracking reference such as `refs/remotes/origin/main` is stored **locally**, and reflects what you last learned from the remote. It is not a live subscription.

| Action | Your main | Your origin/main | Local bare origin |
|---|---|---|---|
| Add remote | unchanged | may not exist | unchanged |
| Fetch new commit | unchanged | advances | unchanged |
| Merge (fast-forward possible) | advances | unchanged | unchanged |
| Push your main | unchanged | normally updated | advances |

## Guided procedure

1. Complete B04 to experience a remote that is a local directory. Use `git remote -v` to see its path. The push should not require credentials or internet access.
2. Start B08. The fixture contains a student checkout (`repo/`), a bare repository (`origin.git/`) and a second checkout (`publisher/`). The publisher has already pushed a new commit; the student's remote-tracking ref has not been updated.
3. From `.practice/B08/repo`, inspect:

```bash
git status -sb
git remote -v
git log --all --oneline --decorate -6
git rev-parse main
git rev-parse origin/main
```

4. Write down the predicted state after a fetch. Then use `git fetch origin`. Check `git log --oneline main..origin/main` to see the change you have learned about. Inspect `git show origin/main:NEWS.md` without merging.
5. Explain why `git pull` would be a different operation: it fetches **and** integrates according to branch configuration. For deterministic behavior when you explicitly want fast-forward only, prefer `git merge --ff-only origin/main` after reviewing changes—**but do not run that command in B08**, because this exercise requires main to remain unchanged.

## Failure clinic

**The file appears in origin/main but not on disk.** Fetch updates refs and objects; it does not update your currently checked-out branch's working tree. This is correct.

**I cannot see the publisher's work.** Confirm you are in the student's repository. The publisher has its own working tree; the bare remote has no normal checkout.

**I accidentally merged.** In this disposable exercise only, inspect `git reflog` before any recovery. Do not use `git reset --hard` automatically on a real shared branch. Recreate the fixture if you need a clean attempt.

## Evidence to submit

Provide the before/after `git rev-parse main` and `git rev-parse origin/main` values. Explain why one changes and the other does not. Include one `git log main..origin/main` output and a three-sentence description of the difference between clone, fetch, pull and push.

**Completion gate:** You can review remote changes without changing your worktree or accidentally publishing local commits.
