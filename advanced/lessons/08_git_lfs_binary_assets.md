# Git LFS and large binary files

**Advanced · Lesson 08 · Study time: 90–120 min**

## Goal
Binary artifacts often diff poorly and inflate repository history. Git LFS uses pointer files plus external object storage for supported hosts; it introduces availability, quota, and access constraints.

## Worked technical sections
Practice in throwaway repositories. Commands with placeholders or commented examples require setup and judgment; do not paste them into a production repository.

### 1. Know what normal Git stores
Large files included in history remain in older commits even after deletion. Git delta compression may help some formats but not already-compressed binaries such as images or archives.

```bash
git count-objects -vH
git ls-tree -r -l HEAD
git status --short
```

**Verify:** Identify unusually large tracked assets before adding more.

### 2. Track assets with LFS rules
Where Git LFS is installed and allowed, `git lfs track` sets attributes for file patterns. LFS availability depends on both client installation and remote hosting.

```bash
# Only if Git LFS is installed:
# git lfs install
# git lfs track "*.bin"
# git add .gitattributes
# git lfs ls-files
```

**Verify:** Track patterns before committing large assets; validate host quotas.

### 3. Understand pointers
A Git LFS pointer is a small text object containing the external asset's identifier and size. A clone may have pointers without fully downloaded binaries if LFS retrieval is skipped.

```bash
git check-attr -a -- example.bin
git ls-files .gitattributes
git status -sb
```

**Verify:** Pointer files are not the full binary contents.

### 4. Avoid artifact misuse
Generated build outputs are typically better in release artifacts, package registries, or object storage than in Git. Evaluate data retention, reproducibility, and access controls.

```bash
# Decision checklist:
# - Is it source input or derived output?
# - Can a build reproduce it?
# - Is storage private or public?
# - Will every clone need the bytes?
```

**Verify:** Do not use Git LFS as a universal backup system.

## Applied exercises
1. Inspect an asset policy for a repo with model weights and generated reports.
2. Demonstrate .gitattributes using a disposable small binary file (if LFS available).
3. Explain how restoring a repository differs from restoring LFS-hosted objects.

## Interview prompts
- Does removing a huge file from HEAD erase its history storage?
- Can a clone work offline if required LFS objects are unavailable?

**Completion:** Explain performance, security, and recovery trade-offs with reproducible evidence.
