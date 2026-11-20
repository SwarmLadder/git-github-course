# Workshop 05 — Notes, sparse checkout and pinned dependencies

**Track:** Advanced · **After:** lessons 00, 03, 06 and 07 · **Labs:** A03, A05, A07, A08 · **Time:** 105–135 minutes

## Outcome

Understand Git objects, refs and special tree entries. Attach review commentary without changing a commit's identity; populate only selected working-tree paths; and pin a local library to a specific dependency commit.

## Three mechanisms

**Git notes** live in a notes ref (usually `refs/notes/commits`). A note attaches commentary without changing the target object's ID. Notes refs are not automatically distributed like ordinary branch refs; verify a team's explicit notes publication policy before relying on them as evidence.

**Sparse checkout** selects which tracked paths are populated in the working tree. It is not a shallow clone or a partial clone: commits still describe the original full tree.

**Submodules** store a gitlink entry (mode `160000`) that points at a commit in another repository. The superproject does not treat the dependency files as ordinary blobs. The `.gitmodules` file maps path and configured URL.

## Guided procedure

1. Start A05. Record `git rev-parse HEAD`. Run `git notes add -m "Reviewed for release: checks passed" HEAD`, followed by `git notes show HEAD` and `git rev-parse HEAD`. The commit hash must remain unchanged.
2. Start A07. Before enabling sparse checkout, inspect all committed paths with `git ls-tree -r --name-only HEAD`. Then run:

```bash
git sparse-checkout init --cone
git sparse-checkout set docs apps/api
git sparse-checkout list
git status -sb
```

Verify docs and apps/api are materialized, but assets and data are absent. `git ls-tree` still sees them, because sparse checkout does not delete history.

3. Start A08. The fixture supplies a sibling local repository at `.practice/A08/library`. From `.practice/A08/repo` run:

```bash
git -c protocol.file.allow=always submodule add ../library vendor/library
git status --short
git add .gitmodules vendor/library
git commit -m "Pin local library"
git ls-tree HEAD vendor/library
cat .gitmodules
```

The `protocol.file.allow=always` setting applies **only to this command** and this trusted local fixture. Do not set it globally or use untrusted repositories. Cloning another project with submodules often requires `git submodule update --init --recursive` with an appropriate access and trust policy.

## Failure clinic

**Library changes are not in the superproject.** The gitlink points at one dependency commit, not a moving branch. Review and test new dependency commits, stage the new gitlink, then commit deliberately.

**A note disappears in another clone.** Notes refs need explicit sharing. They also do not prove that the review really happened.

**Sparse checkout seems to delete files.** Sparse mode changes worktree population, not Git's stored commits. Inspect `git status` and `git sparse-checkout list`. Disable sparse checkout only after grading if you want all files restored.

## Evidence and reflection

Show unchanged HEAD hashes for A05/A07, the `160000 commit` tree entry for A08 and the path/URL in .gitmodules. Explain how gitlink pinning improves reproducibility and when a subtree or vendor folder may be simpler.

**Completion gate:** You can distinguish object storage, refs, worktree materialization and dependency pointers.
