# Git submodules, subtrees, and external code

**Advanced · Lesson 07 · Study time: 90–120 min**

## Goal
Choose a dependency strategy deliberately. Submodules pin another repository commit; subtree workflows copy content into a parent history; package managers may be preferable for versioned software dependencies.

## Worked technical sections
Practice in throwaway repositories. Commands with placeholders or commented examples require setup and judgment; do not paste them into a production repository.

### 1. Understand a submodule pointer
A superproject stores a gitlink pointing at a submodule commit, plus configuration of the URL. Cloning normally requires separate submodule initialization or a recursive clone.

```bash
git submodule status
git config --file .gitmodules --list
# If you have a trusted repo with submodules:
# git clone --recurse-submodules <trusted-url> sample
```

**Verify:** A submodule URL can point to untrusted code; review it before executing tools.

### 2. Update pinned dependencies
`git submodule update --init --recursive` checks out pinned commit versions. It does not automatically select the newest upstream branch commit.

```bash
git submodule update --init --recursive
git status -sb
git diff --submodule=log
```

**Verify:** The pinned gitlink commit must be available from the dependency remote.

### 3. Compare subtrees
`git subtree add` can incorporate external repository content under a prefix. This keeps a self-contained checkout but increases parent-repo history and complicates sync decisions.

```bash
# Conceptual subtree command (requires trusted remote):
# git subtree add --prefix=vendor/library <trusted-url> main --squash
git ls-tree HEAD
git log --oneline --all -6
```

**Verify:** Subtree contents are normal files in the parent tree.

### 4. Decide based on lifecycle
Use a package manager for released libraries, a submodule when separate repository identity matters, or subtree when consumers need a single checkout. Evaluate security review and dependency update processes.

```bash
# Decision questions:
# - Must the dependency be independently versioned?
# - Must offline checkout work after clone?
# - Who reviews updates to external code?
# - What is the rollback strategy?
```

**Verify:** Avoid including external code without a maintenance owner.

## Applied exercises
1. Create a submodule from a safe local repository and inspect the gitlink.
2. List trade-offs among submodule, subtree, and package dependency.
3. Explain what a fresh clone must do to obtain submodule files.

## Interview prompts
- Does updating the superproject automatically pull the newest submodule commit?
- How does subtree affect the clone experience?

**Completion:** Explain performance, security, and recovery trade-offs with reproducible evidence.
