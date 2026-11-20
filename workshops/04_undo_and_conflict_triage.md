# Workshop 04 — Stash, revert and conflict triage

**Track:** Intermediate · **After:** lessons 04, 05 and 09 · **Labs:** I02, I03, I06, I08 · **Time:** 90–120 minutes

## Outcome

Recover an interrupted session, stash staged and untracked changes, and reverse an unwanted two-parent merge *without deleting the merge from history*.

## A decision tree for a bad day

| State | Starting point | Avoid assuming |
|---|---|---|
| Work blocks branch switch | `git status`, targeted commit or `git stash push -u` | Plain stash saves untracked files |
| Merge in progress | `git status`, resolve or `git merge --abort` | Every conflict is identical |
| Bad commit already shared | `git revert <commit>` | Reset is safe on shared history |
| Bad merge already shared | `git show --summary HEAD`, consider `git revert -m 1 <merge>` | A merge has only one parent |
| Reset lost local work | `git reflog` and a recovery branch | Reflog exists on every clone |

## Guided procedure

1. Start I06 and inspect `git status --short`. The fixture contains a **staged** README edit and an **untracked** draft.md. Predict the result of plain `git stash push`: untracked files are normally excluded. Use `git stash push -u -m "Keep WIP for later"` to retain both.
2. Confirm `git status --short` is empty and inspect `git stash list`. Explore read-only examples: `git show stash@{0}:README.md` and `git show stash@{0}^3:draft.md`. The task grades retained stashed work; **do not pop the stash yet**.
3. Start I08 and draw the merge parents using `git log --graph --oneline --all`. Parent 1 is the mainline branch before the feature merged. Record the merge hash and its changes.
4. Run `git revert -m 1 --no-edit HEAD` on the disposable fixture. Confirm NOTICE.md is gone while ROADMAP.md remains. Inspect the ancestry to see that the merge remains part of history.

## Triage checklist

Before any destructive operation, answer: Is the change committed? Is it pushed? Which branch is checked out? Do collaborators depend on this commit? Are any files untracked or ignored? Is a merge or rebase already in progress? Can you create a recovery branch or backup?

Begin with `git status`, then inspect `git log --graph --decorate --oneline --all -12`, `git diff`, `git diff --cached` and `git reflog -10` as appropriate. Do not run these repair commands indiscriminately on valuable repositories.

## Failure clinic

**My stash omits the draft.** Plain stash normally excludes untracked files; `-u` includes them, but not ignored files. Stashes are local and may be lost through dropping/pruning. They are not durable backups.

**The revert wants -m.** Git needs a selected mainline parent for a merge revert. The wrong parent can remove unrelated work.

**Reverted code appears in a later merge.** Reverting a merge does not erase its ancestry. Future reintroduction may require reverting the revert or rebuilding the topic branch.

## Evidence and reflection

Include I06's staged/untracked stash proof; I08's before/after graph; a five-sentence incident report covering scope, action, tests, rationale and rollback; and an example where a private local reset would be appropriate.

**Completion gate:** You can reverse mistakes without silently rewriting shared history or losing unrelated changes.
