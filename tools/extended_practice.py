"""Twelve additional, entirely local Git-state labs.

No network, GitHub token, user scripts, or production repository is involved.
This module uses the Git helpers supplied by tools/practice.py so all fixtures
share the same deliberately isolated identity/configuration and timeouts.
"""
from __future__ import annotations

from pathlib import Path
import subprocess


EXTRA_IDS = frozenset({
    "B05", "B06", "B07", "B08",
    "I05", "I06", "I07", "I08",
    "A05", "A06", "A07", "A08",
})


def setup(task_id, task, repo, metadata, git, make_commit, init_repo, git_env):
    """Populate a newly initialized .practice/<task>/repo."""
    if task_id == "B05":
        make_commit(repo, "README.md", "# Ignore rules lab\n", "Start project")
        (repo / ".env.local").write_text("DEMO_ONLY=not-a-real-secret\n", encoding="utf-8")
        (repo / "build").mkdir()
        (repo / "build" / "result.log").write_text("generated\n", encoding="utf-8")
        (repo / "important.log").write_text("keep this record\n", encoding="utf-8")
    elif task_id == "B06":
        original = [f"line-{n:02}\n" for n in range(1, 51)]
        make_commit(repo, "story.txt", "".join(original), "Write fifty-line story")
        original[2] = "line-03 staged change\n"
        original[46] = "line-47 worktree draft\n"
        (repo / "story.txt").write_text("".join(original), encoding="utf-8")
    elif task_id == "B07":
        metadata["base"] = make_commit(repo, "config.ini", "mode=stable\n", "Save stable configuration")
        (repo / "config.ini").write_text("mode=experimental\n", encoding="utf-8")
        (repo / "draft.txt").write_text("keep my notes\n", encoding="utf-8")
    elif task_id == "B08":
        metadata["base"] = make_commit(repo, "README.md", "# News\n", "Start news project")
        bare = task / "origin.git"
        result = subprocess.run(
            ["git", "init", "--bare", "-b", "main", str(bare)],
            capture_output=True, text=True, env=git_env(), timeout=20,
        )
        if result.returncode:
            raise RuntimeError(result.stderr.strip())
        git(repo, "remote", "add", "origin", str(bare))
        git(repo, "push", "-u", "origin", "main")
        publisher = task / "publisher"
        result = subprocess.run(
            ["git", "clone", "-b", "main", str(bare), str(publisher)],
            capture_output=True, text=True, env=git_env(), timeout=20,
        )
        if result.returncode:
            raise RuntimeError(result.stderr.strip())
        git(publisher, "config", "user.name", "Course Publisher")
        git(publisher, "config", "user.email", "publisher@example.test")
        metadata["remote_tip"] = make_commit(
            publisher, "NEWS.md", "published remotely\n", "Publish a new headline"
        )
        git(publisher, "push", "origin", "main")
        # The student's origin/main intentionally still points to base.
    elif task_id == "I05":
        make_commit(repo, "README.md", "# Reports\n", "Base")
        git(repo, "switch", "-c", "feature/reports")
        metadata["old_feature"] = make_commit(
            repo, "report.md", "Quarterly report\n", "Create report"
        )
        git(repo, "switch", "main")
        metadata["main_tip"] = make_commit(repo, "logging.conf", "verbose=no\n", "Improve logging")
        git(repo, "switch", "feature/reports")
    elif task_id == "I06":
        metadata["base"] = make_commit(repo, "README.md", "# Work in progress\n", "Baseline")
        (repo / "README.md").write_text("# Work in progress\nWIP line\n", encoding="utf-8")
        git(repo, "add", "README.md")
        (repo / "draft.md").write_text("future idea\n", encoding="utf-8")
    elif task_id == "I07":
        metadata["base"] = make_commit(repo, "README.md", "# Product\n", "Base")
        git(repo, "switch", "-c", "feature/promo")
        make_commit(repo, "promo.txt", "First draft\n", "Draft promotion")
        metadata["feature_tip"] = make_commit(
            repo, "promo.txt", "First draft\nPromotion ready\n", "Finish promotion"
        )
        git(repo, "switch", "main")
    elif task_id == "I08":
        make_commit(repo, "README.md", "# Notifications\n", "Base")
        git(repo, "switch", "-c", "feature/notify")
        make_commit(repo, "NOTICE.md", "New notification\n", "Add notification")
        git(repo, "switch", "main")
        make_commit(repo, "ROADMAP.md", "Keep the roadmap\n", "Document roadmap")
        git(repo, "merge", "--no-ff", "-m", "Merge notification feature", "feature/notify")
        metadata["merge_tip"] = git(repo, "rev-parse", "HEAD").stdout.strip()
    elif task_id == "A05":
        metadata["tip"] = make_commit(repo, "main.py", "print('ready')\n", "Prepare reviewed build")
    elif task_id == "A06":
        metadata["main_tip"] = make_commit(repo, "README.md", "# Search\n", "Base")
        git(repo, "switch", "-c", "feature/search")
        make_commit(repo, "search.txt", "first pass\n", "Prototype search")
        metadata["old_tip"] = make_commit(
            repo, "search.txt", "first pass\nsearch ready\n", "Finish search"
        )
    elif task_id == "A07":
        make_commit(repo, "docs/guide.md", "Use the API\n", "Documentation")
        make_commit(repo, "apps/api/README.md", "API service\n", "Add API")
        make_commit(repo, "assets/logo.txt", "binary placeholder\n", "Add asset")
        metadata["tip"] = make_commit(repo, "data/export.csv", "id,value\n1,2\n", "Add data")
    elif task_id == "A08":
        library = task / "library"
        init_repo(library)
        metadata["library_tip"] = make_commit(
            library, "lib.txt", "Local library v1\n", "Library baseline"
        )
        metadata["main_tip"] = make_commit(
            repo, "README.md", "# App with dependency\n", "App baseline"
        )
    else:
        raise AssertionError(f"Unsupported additional task {task_id}")


def verify(task_id, path, repo, metadata, git):
    """Inspect only Git state and files; never execute learner-authored code."""
    out = lambda *args: git(repo, *args).stdout.strip()
    ok = lambda *args: git(repo, *args, check=False).returncode == 0

    if task_id == "B05":
        assert ok("cat-file", "-e", "HEAD:.gitignore"), "Commit a .gitignore file"
        assert out("show", "HEAD:important.log") == "keep this record", "Track important.log"
        for file in (".env.local", "build/result.log"):
            assert ok("check-ignore", "--no-index", "-q", file), f"Ignore {file}"
            assert not ok("ls-files", "--error-unmatch", "--", file), f"Do not track {file}"
        assert not ok("check-ignore", "--no-index", "-q", "important.log"), "Allow important.log"
    elif task_id == "B06":
        head = out("show", "HEAD:story.txt").splitlines()
        staged = out("show", ":story.txt").splitlines()
        worktree = (repo / "story.txt").read_text(encoding="utf-8").splitlines()
        assert staged[2] == "line-03 staged change", "Stage the first hunk"
        assert staged[46] == head[46] == "line-47", "Do not stage the second hunk"
        assert worktree[46] == "line-47 worktree draft", "Keep second hunk unstaged"
        assert out("diff", "--cached", "--name-only") == "story.txt", "Stage only story.txt"
        assert out("diff", "--name-only") == "story.txt", "Second hunk must remain unstaged"
    elif task_id == "B07":
        assert out("rev-parse", "HEAD") == metadata["base"], "Do not create a new commit"
        assert out("show", "HEAD:config.ini") == "mode=stable", "Keep original commit"
        assert (repo / "config.ini").read_text(encoding="utf-8") == "mode=stable\n", "Restore config.ini"
        assert (repo / "draft.txt").read_text(encoding="utf-8") == "keep my notes\n", "Preserve untracked draft"
        assert not out("diff", "--name-only"), "There must be no unstaged tracked-file changes"
    elif task_id == "B08":
        assert out("rev-parse", "main") == metadata["base"], "Do not merge into main"
        assert out("rev-parse", "refs/remotes/origin/main") == metadata["remote_tip"], "Fetch updated origin/main"
        assert out("show", "refs/remotes/origin/main:NEWS.md") == "published remotely", "Fetch latest remote commit"
        assert not ok("cat-file", "-e", "main:NEWS.md"), "Do not incorporate the new commit into main"
    elif task_id == "I05":
        assert out("branch", "--show-current") == "feature/reports", "Rebase the feature branch"
        assert out("rev-parse", "main") == metadata["main_tip"], "Leave main unchanged"
        assert out("merge-base", "main", "feature/reports") == metadata["main_tip"], "Move feature onto latest main"
        assert out("rev-list", "--count", "main..feature/reports") == "1", "Keep one focused feature commit"
        assert out("rev-parse", "feature/reports") != metadata["old_feature"], "Replay the feature commit"
        assert out("show", "feature/reports:report.md") == "Quarterly report", "Preserve report"
        assert out("show", "feature/reports:logging.conf") == "verbose=no", "Include updated main"
    elif task_id == "I06":
        assert not out("status", "--porcelain"), "Stash both staged and untracked work"
        assert out("rev-parse", "HEAD") == metadata["base"], "Keep branch history unchanged"
        assert "WIP line" in out("show", "stash@{0}:README.md"), "Stash the staged README"
        assert out("show", "stash@{0}^3:draft.md") == "future idea", "Use stash -u to include untracked draft"
    elif task_id == "I07":
        assert out("branch", "--show-current") == "main", "Finish on main"
        assert out("rev-parse", "feature/promo") == metadata["feature_tip"], "Do not rewrite the feature"
        assert out("rev-list", "--count", f"{metadata['base']}..main") == "1", "Squash into exactly one commit"
        assert out("rev-list", "--parents", "-n", "1", "main").split()[1:] == [metadata["base"]], "Single-parent squash"
        assert out("show", "main:promo.txt") == "First draft\nPromotion ready", "Include complete feature"
        assert not ok("merge-base", "--is-ancestor", metadata["feature_tip"], "main"), "Do not merge feature history"
    elif task_id == "I08":
        assert out("branch", "--show-current") == "main", "Revert on main"
        assert out("rev-parse", "HEAD^") == metadata["merge_tip"], "Add a new revert commit"
        assert out("log", "-1", "--format=%s").startswith("Revert"), "Use git revert -m 1"
        assert not ok("cat-file", "-e", "HEAD:NOTICE.md"), "Undo the merge's feature changes"
        assert out("show", "HEAD:ROADMAP.md") == "Keep the roadmap", "Keep mainline changes"
    elif task_id == "A05":
        assert out("rev-parse", "HEAD") == metadata["tip"], "Do not amend history"
        assert "Reviewed for release: checks passed" in out("notes", "show", metadata["tip"]), "Attach a Git note with release-review evidence"
        assert out("show", "HEAD:main.py") == "print('ready')", "Keep source unchanged"
    elif task_id == "A06":
        assert out("branch", "--show-current") == "feature/search", "Stay on the feature branch"
        assert out("rev-parse", "main") == metadata["main_tip"], "Do not change main"
        assert out("rev-list", "--count", "main..feature/search") == "1", "Squash two commits to one"
        assert out("rev-parse", "HEAD") != metadata["old_tip"], "Rewrite only local feature history"
        assert out("show", "HEAD:search.txt") == "first pass\nsearch ready", "Preserve full work"
    elif task_id == "A07":
        assert out("rev-parse", "HEAD") == metadata["tip"], "Keep commit history unchanged"
        listed = set(out("sparse-checkout", "list").splitlines())
        assert {"docs", "apps/api"} <= listed, "Select docs and apps/api with cone-mode sparse checkout"
        assert (repo / "docs" / "guide.md").is_file(), "Populate docs"
        assert (repo / "apps" / "api" / "README.md").is_file(), "Populate apps/api"
        assert not (repo / "assets" / "logo.txt").exists(), "Omit assets"
        assert not (repo / "data" / "export.csv").exists(), "Omit data"
    elif task_id == "A08":
        assert out("branch", "--show-current") == "main", "Commit on main"
        assert out("rev-parse", "HEAD^") == metadata["main_tip"], "Create a new commit, preserving main"
        sub = out("ls-tree", "HEAD", "vendor/library")
        assert sub.startswith("160000 commit " + metadata["library_tip"]), "Commit a Git submodule gitlink"
        modules = out("show", "HEAD:.gitmodules")
        assert "path = vendor/library" in modules, "Record submodule path in .gitmodules"
        assert "url = ../library" in modules, "Use the supplied local library repository"
        assert (repo / "vendor" / "library" / ".git").exists(), "Keep an initialized linked submodule checkout"
    else:
        raise AssertionError(f"Unsupported additional task {task_id}")
