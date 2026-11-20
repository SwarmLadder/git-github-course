# Intermediate capstone: issue → PR → CI → review

**Intermediate · Lesson 11 · Study time: 75–110 minutes**

## Purpose
Deliver a small change through a realistic collaboration flow. You should be able to demonstrate both the local Git history and the GitHub review process.

## Concepts and guided examples
Examples may require a fork, a configured remote, an authenticated account or pre-existing files. Execute them only after confirming context.

### 1. Specify a small issue
Choose an isolated improvement such as adding input validation to a Python CLI. Define two acceptance cases: valid input produces expected output, and invalid input gives a useful error and nonzero exit.

```bash
# Issue acceptance criteria:
# - Success path documented
# - Invalid input tested
# - Backward compatibility explained
# - No secrets or external network needed
```

**Check:** The issue is complete enough that another contributor could implement it.

### 2. Implement on a topic branch
Start from current main, make one focused change, add regression tests, and verify the diff. Avoid mixing unrelated formatting changes.

```bash
git switch main
git pull --ff-only
git switch -c fix/validate-input
# Edit code and tests.
git status --short
git diff --check
python -m unittest discover -s tests -v
git add -- path/to/code.py tests/
git commit -m "Validate CLI input before processing"
```

**Check:** Paths and commands must correspond to the real practice project.

### 3. Create a PR and respond to review
Push, open a PR, and collect feedback. Provide rationale and evidence. Update the same branch with a follow-up fix, preserving reviewer context; use rebase or squash only when agreed.

```bash
git push -u origin fix/validate-input
# gh pr create --title "Validate input" --body "Why, what, tests"
# gh pr checks
git log --oneline main..HEAD
git diff --stat main...HEAD
```

**Check:** Required checks and review approvals should pass before merge.

### 4. Verify integration and follow-up
After merge, pull main and confirm the issue's behavior in a clean environment. Document whether the merge was squash, merge commit, or rebase.

```bash
git switch main
git pull --ff-only
git log --oneline --decorate -5
git status -sb
```

**Check:** Evidence includes PR link, checks, merged commit, and passing tests.

## Practice
1. Perform the flow using a fork or private sandbox repository.
2. Create a review checklist and apply it to your own PR.
3. Write a one-paragraph delivery summary with test evidence and residual risk.

## Interview prompts
- Why are CI and code review complementary?
- What should happen if tests pass but a blocking review finding remains?

**Done when:** You can explain decisions, show a reviewable change, and point to reproducible test evidence.
