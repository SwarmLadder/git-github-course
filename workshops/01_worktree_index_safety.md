# Workshop 01 — Worktree, index, history and safe undo

**Track:** Basics · **Recommended after:** lessons 01, 05 and 08 · **Labs:** B02, B05, B06, B07 · **Time:** 90–120 minutes

## Outcome

Create a reviewable commit from deliberately mixed edits. Explain why `HEAD`, the index and the working tree may contain three different versions of the same file. Preserve an important log while ignoring generated data, then discard *only* one mistaken worktree edit.

## Mental model before touching files

The working tree is what you see in the editor. The index (also called the staging area) is the exact snapshot planned for the next commit. `HEAD` is the commit currently checked out. The key comparisons are:

| Question | Command |
|---|---|
| What is different from the planned commit? | `git diff -- path` |
| What will the next commit record? | `git diff --cached -- path` |
| What did the last commit record? | `git show HEAD:path` |
| What content is in the index now? | `git show :path` |
| What paths are untracked or modified? | `git status --short` |

**Prediction:** If you stage a file and then edit it again, the next commit records the staged content—not the latest disk content. Prove the prediction in B06.

## Guided procedure

1. Start B05 from the course checkout. In its generated repository, inspect `git status --short --ignored` before editing. Compare a directory pattern like `build/` with a file pattern like `*.log`. An ignore rule does not stop a *tracked* file from being updated; using `.gitignore` is not a way to erase a secret already committed.
2. Use a narrow exception (`!important.log`) to keep one log file tracked. Verify both `git check-ignore --no-index -v build/result.log` and `git check-ignore --no-index -v important.log`. The second should show the negation rule, not an ordinary ignore outcome.
3. Start B06. Before staging, run `git diff -- story.txt`. Use `git add -p story.txt` to select only the first hunk; inspect both diff commands. Do not commit yet—this exercise is about demonstrating two simultaneous file versions.
4. Start B07. Confirm your untracked `draft.txt` contains notes. Run `git diff -- config.ini` and inspect the actual value being discarded. Only then use `git restore -- config.ini`. Confirm draft.txt still exists and `HEAD` is unchanged.

## Failure clinic

**My entire story was staged.** An unconditional `git add story.txt` stages both hunks. Use `git restore --staged -- story.txt` to unstage the file without deleting your work, then select hunks intentionally.

**The log was ignored despite an exception.** Pattern order matters; later rules may override earlier rules. Also confirm parent directories are not excluded in a way that prevents re-inclusion.

**I lost the edited config.** `git restore -- config.ini` is destructive for uncommitted tracked edits. Git history may contain earlier committed values, but it generally does **not** back up unsaved, untracked or never-committed content.

## Evidence to submit

Capture: (a) index/worktree difference for story.txt, (b) ignore/exception result, (c) before-and-after status for the discarded tracked edit, (d) a short explanation of why `git reset --hard` would be overkill for the requested fix. The four practice checks should pass.

## Reflection

What would change if `important.log` had already been committed before you added the ignore rule? Can `git diff` show a newly created untracked file? Why is `git diff --cached` a better pre-commit review than simply trusting `git status`?

**Completion gate:** You can predict the effect on HEAD, index and disk *before* running a Git command.
