# Git & GitHub — 45 interview answers

Practice explaining each answer from a real repository example. Each level has 15 focused questions.

## Basics

1. **What does Git commit store?** A commit identifies a root tree, parent commits, and metadata. Trees point to files (blobs) and subtrees.

2. **What is the staging area?** The index holds the planned next snapshot. Staged content can differ from the latest working-tree edit.

3. **git diff versus git diff --cached?** git diff compares working tree to index; --cached compares index to HEAD.

4. **git add -p?** Selectively stages patch hunks, useful for splitting unrelated edits into separate commits.

5. **A branch is what?** A movable reference to a commit. It is not a separate full copy of the codebase.

6. **HEAD versus main?** HEAD denotes your current checkout; main is one branch ref. Detached HEAD points directly to a commit.

7. **What is a fast-forward?** Moving a branch ref forward to a descendant without creating a merge commit.

8. **Why do conflicts occur?** Git cannot safely combine overlapping changes or structural file operations. A human must choose a coherent result.

9. **How do you handle a conflict?** Inspect the state, understand both sides, edit the final file, stage the resolution, finish the merge/rebase, and run tests.

10. **Fetch versus pull?** Fetch updates local remote-tracking refs; pull fetches then integrates into the checked-out branch according to configured policy.

11. **What does origin/main mean?** Your last fetched local record of origin's main, not necessarily the remote's current live tip.

12. **How do you unstage safely?** Use git restore --staged path; it preserves working-tree edits.

13. **Revert versus reset?** Revert adds a reversing commit for shared history; reset moves a ref and may also alter index/worktree.

14. **Why doesn't .gitignore remove a committed secret?** It only affects tracking of untracked files. A committed secret remains in history and must be revoked/rotated.

15. **Do tags publish automatically?** No. `git tag` creates a local ref; push it explicitly and optionally create a GitHub Release.

## Intermediate

1. **What belongs in a good pull request?** Intent, scope, tests, risk, linked issue, and a reviewable diff; do not paste large unhelpful logs.

2. **Why should a reviewer inspect net diff?** A branch may contain multiple commits whose final combined effect differs from any single commit.

3. **Merge commit versus squash?** Merge preserves branch topology/commits; squash creates one new commit with the aggregate change and one parent.

4. **Does rebasing preserve commit hashes?** No. Replayed commits receive new identities, so rebasing shared history requires coordination.

5. **When use git cherry-pick?** To apply a specific change to another line of development, such as a backport. Test dependencies afterward.

6. **Can git revert undo a merge?** Yes, but it needs a chosen mainline parent and can affect how future merges treat the reverted changes.

7. **What does git rebase --abort do?** Aborts the active rebase and returns the branch to its pre-rebase state.

8. **Why can green CI be insufficient?** Only configured tests were checked. Missing scenarios, security flaws, and unstated requirements may remain.

9. **What is a GitHub Actions job?** A unit of workflow execution on a runner composed of steps; jobs can depend on other jobs.

10. **Why does pull_request_target need caution?** It runs in a privileged base-repository context; checking out and executing untrusted PR code with secrets can expose credentials.

11. **What should required checks verify?** Fast deterministic tests, static validation, packaging or other checks relevant to the protected branch.

12. **What is a GitHub fork?** A separate repository on GitHub, often used to propose changes upstream without source repo write access.

13. **gh auth versus git config user.email?** Git identity names commits; authentication grants access to GitHub APIs and Git transports.

14. **How do you respond to a code review defect?** Reproduce, change code/tests, explain the fix, and recheck CI before requesting another review.

15. **When is force-with-lease appropriate?** Only on a branch whose history you are authorized to rewrite, after fetching and coordinating. It isn't risk-free.

## Advanced

1. **Git blob, tree, and commit?** Blob holds content, tree holds path mappings, commit names a tree, parents, and metadata.

2. **Where does a reflog exist?** In a local repository, tracking ref movements; it is not automatically copied to another clone and may expire.

3. **How recover from a mistaken reset?** Inspect reflog, identify the old tip, create a recovery branch at its hash, and verify its content before further changes.

4. **What does git bisect find?** An earliest commit relative to a reliable good/bad test boundary that changes tested behavior; history/test assumptions matter.

5. **Why can bisect fail?** Flaky tests, incompatible scripts across revisions, or incorrect good/bad endpoints produce unreliable findings.

6. **Why use worktrees?** To maintain separate working directories/indices on branches while sharing one local object database.

7. **rebase --onto arguments?** `git rebase --onto NEWBASE UPSTREAM BRANCH` replays commits in BRANCH not reachable from UPSTREAM on NEWBASE.

8. **What is git range-diff?** Compares two commit sequences to detect patch/reordering differences after history rewriting.

9. **Are signed commits safe code?** No. A signature relates a key to a commit; it does not attest to code correctness or absence of malware.

10. **Sparse checkout versus shallow clone?** Sparse controls populated paths; shallow limits ancestry. Partial clone controls which objects are fetched.

11. **Submodule versus subtree?** Submodule pins a separate repository commit; subtree incorporates dependency files into the parent history.

12. **What does Git LFS store in Git?** Pointer text objects; large binary bytes reside in external LFS storage and require independent retrieval.

13. **What do you do first after a token leak?** Revoke/rotate the credential and assess exposure. History rewriting cannot retract downloaded copies.

14. **Why restrict release workflows?** Untrusted PR code should not access signing keys or production credentials; require reviewed branches and protected environments.

15. **How do you validate a hotfix release?** Reproduce the bug, find origin, add regression test, review fix, run CI, tag tested commit, document rollback.

## Interview evidence

Use a graded local lab, commit graph, PR, CI run, or reproduction script to support each answer. If you cannot demonstrate the behavior, repeat the relevant lesson.
