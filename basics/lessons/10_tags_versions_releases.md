# Tags, versioning, and releases

**Track:** Basics · **Lesson:** 10 · **Time:** 60–90 minutes

## Goal
Branches move as work progresses. A tag names a chosen commit; an annotated tag includes an additional tag object with message and metadata. GitHub releases attach notes and assets to tags.

## Worked walkthrough
Unless otherwise stated, run these commands in a **disposable practice repository**. Commands requiring a remote or live GitHub account are identified. Do not run destructive examples against important work.

### 1. Use annotated tags for milestones
Tag a verified commit after tests. Annotated tags help capture intent; Git does not enforce semantic versioning, and tags should generally be immutable once published.

```bash
git status -sb
git log -1 --oneline
git tag -a v0.1.0 -m "First course milestone"
git tag --list
git show v0.1.0 --no-patch
```

**Check:** Tags do not automatically publish to a remote.

### 2. Publish tags deliberately
`git push origin v0.1.0` pushes one specific tag. Avoid `--tags` when your repository has experiment tags you do not want to publish.

```bash
git remote -v
# Network + permission required:
# git push origin v0.1.0
git ls-remote --tags origin
```

**Check:** GitHub Releases are platform objects tied to tags; plain Git creates only tags.

### 3. Compare release versions
Git can diff two tags, show commits between them, and report changed paths. Use consistent, meaningful version labels and document breaking changes separately.

```bash
git tag --list
git log --oneline v0.1.0..HEAD
git diff --stat v0.1.0 HEAD
```

**Check:** This tells you what has changed since a chosen milestone.

### 4. Avoid moving published references
Changing an existing release tag after publication can confuse builds and consumers. Prefer a new tag or explicitly documented correction process.

```bash
git for-each-ref refs/tags --format='%(refname:short) %(objectname:short)'
git status -sb
```

**Check:** Review tag target before building or deploying from it.

## Exercises
1. Tag a tested commit and explain why annotated tags help.
2. Compare tag-to-HEAD changes.
3. Draft release notes including features, fixes, migration needs, and test evidence.

## Interview prompts
- Does `git tag` publish anything to GitHub?
- Why should released tags generally not be moved?

**Completion:** You can explain the intended history change and reproduce the workflow without disturbing another repository.
