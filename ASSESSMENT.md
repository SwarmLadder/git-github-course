# Final assessment — Git & GitHub engineering

**What is assessed:** Correct Git state, technical explanation, recovery decisions, collaboration quality and security judgment. Complete three portfolio projects and six workshops, or provide clearly labeled local simulations for tasks that would otherwise need an online GitHub account. The automated checker covers **24 offline Git labs** but does not replace human review.

## Mandatory evidence pack

Your submission should contain:

1. **Git fundamentals** — a screenshot or text capture of `git status -sb`, staged vs unstaged diffs, a selective commit and a branch graph.
2. **Collaboration** — a review-ready PR description, a meaningful diff summary, response to at least two imagined review comments and a traceable merge/squash decision.
3. **Recovery** — a valid revert, a lost-commit recovery using a newly created ref, and a deterministic bisect identifying the first-bad commit.
4. **Automation and security** — minimum permissions for pull-request jobs, a separate trusted release path, a plan for leaked credentials, and an explanation of untrusted-code boundaries.
5. **Release** — an annotated tag pointing at a tested commit, concise release notes, rollback plan and truthful test evidence.
6. **Dependencies and scale** — evidence for a sparse checkout and a gitlink-pinned submodule, including a reproducibility explanation.

Every claim must identify exact commands and results, or be explicitly labeled **simulated**.

## Scoring rubric (100 points)

| Category | Points | What a strong answer shows |
|---|---:|---|
| Git fundamentals | 20 | Clean commits, correct index/worktree state, safe branch and remote handling |
| Collaboration | 20 | Focused diff, clear review request, appropriate merge strategy |
| Recovery | 20 | Revert/reflog/bisect with preserved history and reproducible evidence |
| CI and security | 20 | Minimal token permissions, protected release paths, no exposed secrets |
| Release engineering | 10 | Meaningful annotated tag, validated source and rollback notes |
| Documentation | 10 | Precise reproduction, assumptions, failure/decision rationale |

**Pass:** at least **80/100**, plus each mandatory safety gate.

## Safety gates (required)

- No real secret, private key, credential or token is committed or pasted into work products.
- No destructive reset or force push against a shared or non-disposable branch.
- No claim of a successful online PR, verified signature, production deploy or security approval without actual evidence.
- No untrusted PR code is knowingly executed with deployment credentials or elevated repository write permissions.
- All 24 offline labs pass (`python tools/practice.py check <ID>`) before the course is considered complete.

## Verification interview

Use the [45 interview prompts](interview/QUESTIONS.md). Explain at least 36 without notes. For five randomly selected questions demonstrate a Git command, commit graph or security decision. If a command fails, explain why, then show a safe recovery path.

## Capstone checkpoints

### Project 1 — Local collaboration
Demonstrate branches, fast-forward or merge behavior, local bare remote and fetch without implicit integration. Record why `origin/main` can differ from `main`.

### Project 2 — Review and CI
Present a reviewable PR plan and CI trust-boundary review. Include a concrete discussion of rebase vs squash and how you would handle a failing check. A real GitHub PR is optional; never mislabel a simulation.

### Project 3 — Regression to release
Identify first-bad commit using bisect; recover a lost commit with reflog; repair on a topic branch; verify tests; document an annotated release tag and rollback strategy.

## Instructor moderation

Evaluate what the learner **actually did**, not only whether the final file exists. Ask for the before/after HEAD hash, index state, and graph where appropriate. Challenge unsafe shortcuts, assess explanations independently of the automatic checker, and allow different valid Git command paths yielding equivalent states.

For more scaffolded preparation see [six workshops](workshops/README.md) and the [eight-week plan](CURRICULUM.md).
