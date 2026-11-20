# Workflow permissions, secrets, and supply-chain safety

**Intermediate · Lesson 09 · Study time: 75–110 minutes**

## Purpose
CI jobs may run code from contributors, so treat them as an execution boundary. Minimize token permissions, avoid exposing credentials to untrusted changes, and review third-party actions.

## Concepts and guided examples
Examples may require a fork, a configured remote, an authenticated account or pre-existing files. Execute them only after confirming context.

### 1. Apply least privilege
Explicit permissions such as contents: read reduce the default GITHUB_TOKEN scope. A job that publishes a release may need different permissions and should be separated from untrusted PR tests.

```bash
# Example workflow header:
# permissions:
#   contents: read
#
# jobs:
#   test:
#     runs-on: ubuntu-latest
#     steps:
#       - uses: actions/checkout@v4
```

**Check:** Test jobs normally should not need permission to push code.

### 2. Keep secrets out of PR test paths
Do not print tokens or pass secrets to jobs executing untrusted PR code. `pull_request_target` has special security implications because it executes in the base repository context; never blindly checkout and run untrusted PR code with elevated permissions.

```bash
# Anti-pattern (DO NOT USE):
# on: pull_request_target
# steps:
#   - checkout untrusted PR HEAD
#   - run PR-provided scripts with secrets
#
# Prefer least-privileged pull_request checks.
```

**Check:** External contributors must not be able to exfiltrate repository credentials.

### 3. Pin trusted actions and dependencies
Review third-party action source and policy; SHA pinning can reduce mutable-version risk. Validate dependencies and lockfiles as relevant to the language. Do not assume a name from the marketplace implies trust.

```bash
# Conceptual SHA-pin pattern:
# - uses: organization/action@<reviewed-full-commit-sha>
# Never paste a made-up SHA into a real workflow.
#
# Prefer known first-party actions or reviewed dependencies.
```

**Check:** A pinned action still needs maintenance and vulnerability review.

### 4. Separate tests from deployments
Use protected environments, explicit approvals, and scoped deploy credentials for release jobs. PR checks should be independently safe and should not assume secrets are available.

```bash
# Deployment review questions:
# - Is target environment protected?
# - Is deployment limited to trusted branches?
# - Does test job work without credentials?
# - Can release artifacts be traced to a commit?
```

**Check:** Test and release trust boundaries should not be merged casually.

## Practice
1. Review a workflow that exposes a token to PR code and propose a safer design.
2. Create a CI permission table for test and release jobs.
3. Explain risks of running a third-party action at a mutable ref.

## Interview prompts
- Why is pull_request_target potentially risky?
- Does SHA pinning eliminate supply-chain risk?

**Done when:** You can explain decisions, show a reviewable change, and point to reproducible test evidence.
