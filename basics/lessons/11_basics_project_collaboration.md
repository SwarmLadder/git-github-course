# Basics capstone: a team feature workflow

**Track:** Basics · **Lesson:** 11 · **Time:** 60–90 minutes

## Goal
Bring together commits, branches, merges, remotes, and safe recovery. The deliverable is a repository with a reviewable feature history—not a list of command screenshots.

## Worked walkthrough
Unless otherwise stated, run these commands in a **disposable practice repository**. Commands requiring a remote or live GitHub account are identified. Do not run destructive examples against important work.

### 1. Create a reproducible work area
Use a new repo and a local bare remote so the entire exercise works offline. Initialize identity locally and produce an initial commit.

```bash
mkdir -p team-capstone && cd team-capstone
git init -b main
git config user.name "Course Learner"
git config user.email "learner@example.test"
printf "# Team project\n" > README.md
git add README.md && git commit -m "Initialize team project"
git init --bare ../team-remote.git
git remote add origin ../team-remote.git
git push -u origin main
```

**Check:** The bare repo stands in for GitHub without requiring credentials.

### 2. Create a small focused change
Add a feature file and use a descriptive branch. Commit only the paths that belong to this feature, inspect the patch, and push.

```bash
git switch -c feature/checklist
printf "## Checklist\n- Test before merging\n" > CHECKLIST.md
git diff --check
git add CHECKLIST.md
git diff --cached
git commit -m "Add contributor checklist"
git push -u origin feature/checklist
```

**Check:** The feature commit exists on a separate branch with an upstream.

### 3. Review and merge
Before merging, compare your branch to main and decide whether to use fast-forward or a merge commit. For this simple case, fast-forward is sufficient.

```bash
git switch main
git fetch origin
git log --oneline main..origin/feature/checklist
git diff --stat main...origin/feature/checklist
git merge --ff-only origin/feature/checklist
git push origin main
```

**Check:** History should contain the feature commit reachable from main.

### 4. Verify and clean up
Use status, logs, and remotes to check the repository. Delete local feature branches only after confirming integration; pruning remote references is separate from deleting server branches.

```bash
git status -sb
git log --graph --oneline --all -8
git branch --merged
git branch -d feature/checklist
git remote -v
```

**Check:** All expected changes remain on main and no accidental files are staged.

## Exercises
1. Rebuild the capstone from zero without copying a script blindly.
2. Make a conflicting feature branch and resolve it after explaining both intents.
3. Produce a short contribution report: branch, commits, checks, merge strategy.

## Interview prompts
- When is a fast-forward merge preferable?
- How can a reviewer verify no unrelated files entered a commit?

**Completion:** You can explain the intended history change and reproduce the workflow without disturbing another repository.
