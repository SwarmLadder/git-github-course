# Hands-on practice: 12 graded Git labs

Practice runs on **local disposable Git repositories only**. No GitHub login or network needed.

```bash
python tools/practice.py list
python tools/practice.py start B01
python tools/practice.py check B01
```

The start command creates `.practice/B01/repo` with a task-specific fixture. The check command **inspects Git state without running your scripts or altering history**. It shows a pass/fail reason. Starting an existing lab will not overwrite your work.

| Level | Labs |
|---|---|
| Basics | B01 first commit · B02 selective staging · B03 feature branch · B04 local push |
| Intermediate | I01 fast-forward · I02 merge conflict · I03 revert · I04 cherry-pick |
| Advanced | A01 reflog recovery · A02 bisect · A03 worktree · A04 annotated release tag |

Tasks: [practice/tasks.json](tasks.json).

**Reminder:** Labs grade concrete Git state and selected files; they cannot fully assess reasoning or review quality. Complete the written exercises too.
