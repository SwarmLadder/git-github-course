# Git & GitHub terms

| Term | Meaning |
|---|---|
| Blob | Git object holding file content |
| Tree | Object mapping filenames to other objects |
| Commit | Snapshot reference plus metadata and parent commit IDs |
| HEAD | Current checkout reference, usually symbolic to a branch |
| Index/staging area | Snapshot planned for the next commit |
| Working tree | Files you edit locally |
| Branch | Movable reference to a commit |
| Remote | Named URL or path for another Git repository |
| Remote-tracking branch | Local record of a remote branch after fetching |
| Merge base | Best common ancestor used for comparisons/merging |
| Fast-forward | Move a branch tip forward without a merge commit |
| Merge commit | Commit recording two or more parents |
| Rebase | Replay commits on a different base, changing their IDs |
| Revert | Commit that undoes another commit's changes |
| Reset | Move a branch/HEAD, optionally resetting index and worktree |
| Reflog | Local log of reference movement |
| Cherry-pick | Apply changes from one commit onto another branch |
| Stash | Local stack-like storage for unfinished changes |
| Tag | Named reference for a commit or annotated tag object |
| Pull request | GitHub review/proposal interface for merging changes |
| Workflow | GitHub Actions automation defined in a YAML file |
| Runner | Machine/environment executing workflow jobs |
| Worktree | Checkout sharing one repository object database |
| Git LFS | Extension storing external large-file data and Git pointers |
| Shallow clone | Clone with limited commit ancestry |
| Sparse checkout | Controls what paths populate the worktree |
| Partial clone | Defers fetching selected Git objects |
| Protected branch | Branch constrained by GitHub policy/rules |


## Additional applied terms

| Term | Meaning |
|---|---|
| Gitlink | Tree entry with mode `160000` pointing at a submodule commit |
| `.gitmodules` | Versioned mapping of submodule paths to their configured URLs |
| Git note | Metadata stored on a notes ref without modifying the annotated commit |
| Squash merge | Apply a feature's net changes as one new commit without preserving feature ancestry |
| Mainline parent | Parent chosen to determine the side retained when reverting a merge |
| Cone-mode sparse checkout | Efficient directory-based selection of materialized tracked paths |
| Protected environment | Deployment target with configured restrictions or approval requirements |
| Least-privilege token | Credential whose scope is limited to the operations a job must perform |
| `pull_request_target` | GitHub Actions event with base-repository trust context; must not blindly run untrusted PR code with privileged credentials |
| Evidence pack | Reproducible commands, refs, test results, review rationale and rollback notes supporting an engineering decision |

Apply these concepts in [six guided workshops](workshops/README.md) and the [24 checked tasks](practice/README.md).
