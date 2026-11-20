# Branch protection, rulesets, and deployment environments

**Advanced · Lesson 10 · Study time: 90–120 min**

## Goal
Repository governance combines review requirements, CI checks, allowed merge methods, and restricted release credentials. These controls vary with GitHub plan and repository policy.

## Worked technical sections
Practice in throwaway repositories. Commands with placeholders or commented examples require setup and judgment; do not paste them into a production repository.

### 1. Design protected integration
Protect critical branches through appropriate GitHub rulesets or branch protection. Require checks and reviews where supported, and limit bypass permission to accountable maintainers.

```bash
# Policy example (configure in GitHub settings):
# main:
#   required_checks: unit-test, security-scan
#   approvals: 1 or more
#   force_pushes: disallowed
#   deployments: require review
```

**Verify:** Settings aren't stored as Git commands and may require admin access.

### 2. Use protected environments
Deployment credentials should be bound to trusted environments with approval rules. Favor short-lived credentials (e.g. OIDC) where supported and audit access regularly.

```bash
# Trust-boundary checklist:
# - CI PR job: read-only token, no secrets
# - Build job: source and dependency verification
# - Deploy job: protected environment and scoped credentials
# - Incident rollback: documented procedure
```

**Verify:** Untrusted pull requests must not gain deployment authority.

### 3. Handle required checks
Match required check names to actual workflow job names; renamed or skipped jobs may block merges. Design checks so necessary statuses are reliably reported.

```bash
# Workflow conceptual example:
# jobs:
#   tests:
#     runs-on: ubuntu-latest
#     steps:
#       - run: python -m unittest discover -s tests
```

**Verify:** A protection rule must refer to checks emitted by the current workflow.

### 4. Review merge and audit policy
Squash, merge commits, or rebase merges should reflect a documented history policy. Avoid bypassing rules to save time; update rules through normal review when requirements change.

```bash
git log --first-parent --oneline -10
git branch -avv
git remote -v
```

**Verify:** Release notes and approvals should link to the exact tested commit.

## Applied exercises
1. Draft a branch-rules policy for a five-person backend team.
2. Separate PR CI permissions from production deploy permissions.
3. Explain how a required check name change could interrupt merges.

## Interview prompts
- Can code review replace restrictive token permissions?
- Why should release credentials be unavailable to untrusted PR jobs?

**Completion:** Explain performance, security, and recovery trade-offs with reproducible evidence.
