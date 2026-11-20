# GitHub Actions: workflows, jobs, and tests

**Intermediate · Lesson 08 · Study time: 75–110 minutes**

## Purpose
GitHub Actions automates checks triggered by repository events. A workflow is YAML in .github/workflows, jobs run on runners, and steps execute within jobs.

## Concepts and guided examples
Examples may require a fork, a configured remote, an authenticated account or pre-existing files. Execute them only after confirming context.

### 1. Read a minimal CI workflow
Use a stable workflow name, appropriate triggers, a bounded environment, and clear commands. Actions are code dependencies; pin trusted versions or SHAs per security policy.

```bash
# .github/workflows/tests.yml
name: Tests
on: [push, pull_request]
permissions:
  contents: read
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: python --version
      - run: python -m unittest discover -s tests -v
```

**Check:** Workflow only runs when pushed to a supported GitHub repository.

### 2. Understand context and event differences
A pull_request workflow tests proposed changes under event-specific permissions. push runs on a pushed ref. Workflow filters can reduce unnecessary jobs, but do not accidentally skip required checks.

```bash
# Optional event filter in a workflow:
# on:
#   pull_request:
#     branches: [main]
#   push:
#     branches: [main]
```

**Check:** Identify which events trigger required branch checks.

### 3. Know artifact and dependency boundaries
CI runners are temporary; test setup should be reproducible from committed files. Use setup actions for runtime versions and avoid relying on local uncommitted files.

```bash
# Typical steps:
# - uses: actions/setup-python@v5
#   with:
#     python-version: "3.12"
# - run: python -m pip install -r requirements.txt
# - run: python -m unittest discover -s tests -v
```

**Check:** Versions and dependencies must match the tested project.

### 4. Debug failures without disabling gates
Find the failing step and first meaningful error in the run logs. Reproduce locally and push a targeted fix rather than skipping the test or removing rules.

```bash
git status -sb
git show --stat HEAD
git diff --check
python -m unittest discover -s tests -v
```

**Check:** A green workflow is evidence of configured checks, not proof of every behavior.

## Practice
1. Write a two-job workflow separating lint from unit tests.
2. Explain why CI should run for pull requests before merge.
3. Debug a failing test output and propose a focused fix.

## Interview prompts
- Where must a GitHub Actions workflow file live?
- What is the difference between a job and a step?

**Done when:** You can explain decisions, show a reviewable change, and point to reproducible test evidence.
