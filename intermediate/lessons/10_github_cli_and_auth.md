# GitHub CLI, credentials, and pull request operations

**Intermediate · Lesson 10 · Study time: 75–110 minutes**

## Purpose
GitHub CLI (`gh`) provides a terminal interface to GitHub issues, PRs, and workflow runs. SSH and HTTPS authentication solve transport access; commit identity remains a separate setting.

## Concepts and guided examples
Examples may require a fork, a configured remote, an authenticated account or pre-existing files. Execute them only after confirming context.

### 1. Inspect available authentication
`gh auth status` displays authenticated account information and scopes without requiring you to print tokens. Prefer secure credential helpers, SSH keys, or supported device login over embedding secrets in URLs.

```bash
gh --version
gh auth status
git remote -v
git config --show-origin --get credential.helper
```

**Check:** This section requires `gh` installed and an authenticated account.

### 2. Create and inspect PRs
On a pushed feature branch, use `gh pr create` with a clear title and body. `gh pr view` and `gh pr checks` help review status without opening the browser.

```bash
git status -sb
# Requires a pushed feature branch:
# gh pr create --title "Fix setup guide" --body "Why, what, tests"
# gh pr view --web
# gh pr checks
```

**Check:** Review the branch diff and CI before publishing the PR.

### 3. Review and track issues
GitHub CLI can list issues and inspect details. Do not assume issue numbers or API permissions; always verify the repo you are operating on.

```bash
gh repo view
gh issue list --limit 10
# gh issue view <real-issue-number>
gh pr list --limit 10
```

**Check:** Commands operate on the current repository unless another is specified.

### 4. Inspect automation runs
`gh run list` and `gh run view` identify run status and logs. Use commands to investigate rather than blindly re-running jobs.

```bash
gh run list --limit 5
# gh run view <real-run-id>
# gh run view <real-run-id> --log-failed
```

**Check:** CI logs may contain sensitive values; avoid copying secrets into public bug reports.

## Practice
1. Explain the difference between Git identity, SSH auth, and gh auth.
2. Write a gh command sequence to inspect a PR's status and failing checks.
3. Describe how to use a personal access token safely without placing it in history.

## Interview prompts
- Does setting git user.email authenticate a GitHub push?
- Why should an API token never be hardcoded in an example repository?

**Done when:** You can explain decisions, show a reviewable change, and point to reproducible test evidence.
