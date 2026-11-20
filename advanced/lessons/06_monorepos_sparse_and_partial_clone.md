# Monorepos: sparse checkout and partial clone

**Advanced · Lesson 06 · Study time: 90–120 min**

## Goal
Large repositories create operational costs. Sparse checkout controls files present in a working tree; partial clone can defer object downloads; neither is a security boundary.

## Worked technical sections
Practice in throwaway repositories. Commands with placeholders or commented examples require setup and judgment; do not paste them into a production repository.

### 1. Use sparse checkout
Cone mode can check out selected directories along with necessary root paths. Start with a fresh clone and inspect which tracked files are included before changing patterns.

```bash
git sparse-checkout init --cone
git sparse-checkout set docs tools
git sparse-checkout list
git status -sb
```

**Verify:** Only use directory paths that actually exist in the practice repository.

### 2. Understand partial clone filters
`git clone --filter=blob:none` asks a capable server to omit blobs until needed. Filters depend on server support and fetching; not all hosting setups honor them.

```bash
# For a remote supporting partial clone:
# git clone --filter=blob:none <repository-url> large-repo
git config --get extensions.partialClone
git count-objects -v
```

**Verify:** Partial clone is an optimization, not an access-control mechanism.

### 3. Compare shallow clone
`--depth` limits history received and creates shallow boundaries. Shallow clones can break history analysis such as bisect, blame, and comparisons to older tags.

```bash
git rev-parse --is-shallow-repository
git log --oneline -6
# In a throwaway clone needing old history:
# git fetch --unshallow origin
```

**Verify:** Shallow history and missing blobs are different limitations.

### 4. Plan monorepo CI scopes
Path filters can avoid unnecessary jobs, but dependency graphs matter: changing shared libraries may require broader test sets. Required checks should not be skipped unintentionally.

```bash
# Example GitHub Actions filter:
# on:
#   pull_request:
#     paths:
#       - 'services/api/**'
#       - 'libs/common/**'
```

**Verify:** A path-only rule cannot prove impacted dependencies are fully covered.

## Applied exercises
1. Apply sparse checkout to a disposable repo with services/api and docs folders.
2. Explain partial clone versus shallow clone versus sparse checkout.
3. Design path-based CI rules that also test shared dependency changes.

## Interview prompts
- Can sparse checkout stop an authorized user from fetching other repository content?
- Why can shallow clones obstruct git bisect?

**Completion:** Explain performance, security, and recovery trade-offs with reproducible evidence.

## Put this lesson into practice — A07

Populate only docs and apps/api using cone-mode sparse checkout. Verify that assets and data are absent on disk while git ls-tree still sees every committed path.

From the **course root**, run `python tools/practice.py start A07`, work inside `.practice/A07/repo`, then run `python tools/practice.py check A07`. Save the before/after Git state in your evidence journal. Continue with the [guided workshop](../../workshops/05_internals_and_dependencies.md).
