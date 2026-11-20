# Commit signing, verification, and provenance

**Advanced · Lesson 05 · Study: 90–120 minutes**

## What you will learn
Signatures help verify that a commit was signed using an associated key. They do not establish that code is safe, and the trust model depends on identity/key management and platform verification.

## Technical walkthrough
Unless marked otherwise, use a disposable local practice repository. Read command comments: example placeholders and risky operations are intentionally not executable.

### 1. Distinguish author, committer, and signer
Git commit metadata can include author and committer identities and an optional cryptographic signature. `git log --show-signature` reports verification when the relevant key is available.

```bash
git log -1 --format=fuller
git log -1 --show-signature
git config --show-origin --get commit.gpgsign
git config --show-origin --get gpg.format
```

**Verification:** A name/email is not cryptographic evidence of ownership.

### 2. Understand signing choices
Git supports signing through compatible GPG, SSH, and other configured methods depending on Git version. Keys should be protected, rotated, and connected to an appropriate trust policy.

```bash
# Inspect current settings without changing global config:
git config --local --get user.signingkey
git config --local --get commit.gpgsign
git config --local --get gpg.format
```

**Verification:** Do not put private keys into tracked files or CI logs.

### 3. Check verification without assuming trust
GitHub may show verified commit status when the signature and account/key context satisfy its rules. Review the verified signer's identity and key hygiene; a green badge is not a substitute for code review.

```bash
git log --format='%h %G? %s' -10
git show --show-signature --no-patch HEAD
git status -sb
```

**Verification:** Signature verification says something about a key, not software correctness.

### 4. Preserve audit and release evidence
A high-assurance release may combine signed commits/tags, CI evidence, branch protections, and immutable artifacts. Specify which risk each control mitigates.

```bash
git tag --list
git log --format='%h %an <%ae> %G? %s' -5
git show --format=fuller --no-patch HEAD
```

**Verification:** Release integrity needs more than one control.

## Applied exercises
1. Compare an unsigned commit with a signed commit in a practice repo where signing is configured.
2. Describe how a stolen private signing key affects trust.
3. Design a release verification checklist using commits, tags, and CI evidence.

## Interview checks
- Can a signed commit contain malicious code?
- What should you do if a signing key is compromised?

**Pass condition:** Explain the state transition, failure path, and safeguards before running advanced commands.
