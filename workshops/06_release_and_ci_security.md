# Workshop 06 — Release governance and CI security review

**Track:** Advanced · **After:** Intermediate 08–11 and Advanced 05, 09–11 · **Labs:** A02, A04, A05, A06 · **Time:** 120–150 minutes

## Outcome

Investigate a regression, prepare a traceable release, and review a GitHub Actions design for trust-boundary mistakes without any production credentials. This is an **offline Git exercise plus architecture review**, not an actual GitHub deployment.

## Scenario

A service has a known-good tag; a regression entered main; an external contributor proposes a fix. The team wants reproducible tests, review evidence and a verifiable release. An engineer suggests providing a deployment token to PR test jobs for convenience. Explain why that is unsafe.

## Investigation phase

1. Run A02: use a deterministic `git bisect` test to find the first bad commit, record its full hash, and exit bisect mode.
2. Explain why flaky tests, untestable old commits and mistaken good/bad boundaries can invalidate bisect findings.
3. Run A06: squash **private local feature** history into one reviewed change. Explain why rewriting already-shared main is not an appropriate fix.
4. Run A04: create an annotated release tag on a verified commit. Describe how an annotated tag differs from a lightweight tag and a hosted GitHub Release.

## CI security design

Consider this **anti-pattern only; do not install or deploy**:

```yaml
# UNSAFE CONCEPT — DO NOT USE
on: pull_request_target
jobs:
  test:
    permissions:
      contents: write
    steps:
      # checkout and execute untrusted PR code with secrets: NOT SAFE
```

The risk is executing untrusted contribution code in a privileged base-repository context. Safer designs isolate low-privilege PR checks from protected, trusted release jobs. Use minimal token permissions, reviewed action dependencies, restricted deployment environments and explicit approvals.

### Review questions

- Which jobs run untrusted PR code? Are secrets or write permissions truly necessary?
- Which reviewed commit does a release build? Can a mutable artifact change after approval?
- Which environments require approval? Can a feature branch deploy directly?
- Are third-party actions reviewed and pinned to verified immutable SHAs where feasible?
- Are credentials scoped and rotated? After a leak, were they revoked **before** history cleanup?
- Can CI evidence be tied to the release tag and final binary/artifact?

## Release evidence pack

Write this report outside the main codebase, labeling **simulated evidence** as simulated:

```markdown
# Release investigation
Regression: first-bad commit hash and reproduction command
Fix: minimal reviewed patch and reasoning
Verification: exact tests and results, CI run if one exists
Provenance: tag target and signing policy, if applicable
Security: PR trust boundary and credential review
Rollout: staging, monitoring and rollback plan
```

Do not invent approvals, successful builds, signatures, credentials or deployments.

## Score (100 points)

| Dimension | Points |
|---|---:|
| Deterministic root-cause investigation | 20 |
| Branch/ref strategy and rollback plan | 20 |
| Tests and traceable release evidence | 20 |
| Least-privilege CI and untrusted-PR separation | 25 |
| Clear release/incident communication | 15 |

Pass at 80+, with no serious credential handling mistake. Green CI means only that the configured checks passed; signatures do not guarantee code correctness; rewriting history cannot revoke leaked secrets.

**Completion gate:** You can present an evidence-backed release recommendation without granting untrusted code deployment authority.
