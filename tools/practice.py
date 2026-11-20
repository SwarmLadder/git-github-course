#!/usr/bin/env python3
"""Create and check 12 offline Git exercises in disposable local repositories.

This tool never executes student-authored scripts. It only calls Git to set up
or inspect repositories beneath .practice. Run from the course repository.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
TASKS_PATH = ROOT / "practice" / "tasks.json"
DEFAULT_WORKSPACE = ROOT / ".practice"


def all_tasks() -> dict[str, dict]:
    data = json.loads(TASKS_PATH.read_text(encoding="utf-8"))
    if len(data) != 12 or len({x["id"] for x in data}) != len(data):
        raise ValueError("The practice catalog must contain 12 unique tasks")
    return {x["id"]: x for x in data}


def git_env() -> dict[str, str]:
    env = dict(os.environ)
    env.update({
        "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_CONFIG_GLOBAL": os.devnull,
        "GIT_TERMINAL_PROMPT": "0",
        "GIT_EDITOR": "true",
        "GIT_SEQUENCE_EDITOR": "true",
    })
    return env


def git(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    p = subprocess.run(
        ["git", "-C", str(repo), *map(str, args)],
        text=True, capture_output=True, env=git_env(), check=False,
        timeout=20,
    )
    if check and p.returncode:
        raise RuntimeError(f"git {' '.join(args)}: {p.stderr.strip() or p.stdout.strip()}")
    return p


def make_commit(repo: Path, filename: str, content: str, message: str) -> str:
    file = repo / filename
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(content, encoding="utf-8")
    git(repo, "add", "--", filename)
    git(repo, "commit", "-m", message)
    return git(repo, "rev-parse", "HEAD").stdout.strip()


def init_repo(path: Path) -> None:
    result = subprocess.run(
        ["git", "init", "-b", "main", str(path)],
        text=True, capture_output=True, env=git_env(), check=False, timeout=20,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip())
    git(path, "config", "user.name", "Course Learner")
    git(path, "config", "user.email", "learner@example.test")
    git(path, "config", "core.autocrlf", "false")


def start_task(task_id: str, workspace: Path = DEFAULT_WORKSPACE) -> Path:
    if task_id not in all_tasks():
        raise ValueError("Unknown practice task")
    task = workspace / task_id
    # Refuse to overwrite existing work (even a partial task directory).
    task.mkdir(parents=True, exist_ok=False)
    repo = task / "repo"
    init_repo(repo)
    meta: dict[str, str] = {}

    if task_id == "B01":
        pass
    elif task_id == "B02":
        make_commit(repo, "notes.txt", "original\n", "Add notes")
        make_commit(repo, "config.txt", "default\n", "Add config")
        (repo / "notes.txt").write_text("original\nmore notes\n", encoding="utf-8")
        (repo / "config.txt").write_text("default\nlocal override\n", encoding="utf-8")
    elif task_id == "B03":
        make_commit(repo, "README.md", "# Demo\n", "Add README")
    elif task_id == "B04":
        make_commit(repo, "README.md", "# Local remote lab\n", "Initialize")
        bare = task / "origin.git"
        result = subprocess.run(
            ["git", "init", "--bare", str(bare)],
            capture_output=True, text=True, env=git_env(), timeout=20,
        )
        if result.returncode:
            raise RuntimeError(result.stderr.strip())
        git(repo, "remote", "add", "origin", str(bare))
    elif task_id == "I01":
        make_commit(repo, "README.md", "# Collaboration\n", "Base")
        git(repo, "switch", "-c", "feature/checklist")
        make_commit(repo, "CHECKLIST.md", "# Check before merge\n", "Add checklist")
        git(repo, "switch", "main")
    elif task_id == "I02":
        make_commit(repo, "settings.txt", "color=blue\n", "Base settings")
        git(repo, "switch", "-c", "feature/red")
        make_commit(repo, "settings.txt", "color=red\n", "Select red")
        git(repo, "switch", "main")
        make_commit(repo, "settings.txt", "color=green\n", "Select green")
    elif task_id == "I03":
        make_commit(repo, "status.txt", "healthy\n", "Working baseline")
        meta["broken"] = make_commit(repo, "status.txt", "broken\n", "Introduce regression")
    elif task_id == "I04":
        make_commit(repo, "README.md", "# Maintenance\n", "Create baseline")
        git(repo, "branch", "maintenance")
        meta["fix"] = make_commit(repo, "bugfix.txt", "validation fixed\n", "Fix validation")
        git(repo, "switch", "maintenance")
    elif task_id == "A01":
        make_commit(repo, "chapter.txt", "v1\n", "First revision")
        meta["lost"] = make_commit(repo, "chapter.txt", "v2\n", "Important second revision")
        git(repo, "reset", "--hard", "HEAD~1")
    elif task_id == "A02":
        make_commit(repo, "program.py", "def result():\n    return 'ok'\n", "Working program")
        make_commit(repo, "check.py", "from program import result\nassert result() == 'ok'\n", "Add regression test")
        meta["good"] = git(repo, "rev-parse", "HEAD").stdout.strip()
        for n in range(2):
            make_commit(repo, "change.txt", f"good-{n}\n", f"Unrelated good change {n}")
        meta["bad"] = make_commit(repo, "program.py", "def result():\n    return 'broken'\n", "Introduce regression")
        for n in range(3):
            make_commit(repo, "change.txt", f"later-{n}\n", f"Later change {n}")
    elif task_id == "A03":
        make_commit(repo, "README.md", "# Worktree demo\n", "Base")
    elif task_id == "A04":
        make_commit(repo, "version.txt", "0.8.0\n", "Begin development")
        make_commit(repo, "version.txt", "0.9.0\n", "Prepare release candidate")
        make_commit(repo, "version.txt", "1.0.0\n", "Prepare release")
    else:
        raise AssertionError("Unhandled task")
    (task / "metadata.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    return task


def assert_task(task_id: str, workspace: Path = DEFAULT_WORKSPACE) -> None:
    if task_id not in all_tasks():
        raise ValueError("Unknown practice task")
    path = workspace / task_id
    repo = path / "repo"
    if not (repo / ".git").exists():
        raise AssertionError("Start the task before checking it")
    metadata = json.loads((path / "metadata.json").read_text(encoding="utf-8"))
    out = lambda *args: git(repo, *args).stdout.strip()

    if task_id == "B01":
        assert out("branch", "--show-current") == "main", "Commit on main"
        assert out("show", "HEAD:notes.txt").strip() == "learning Git", "Commit notes.txt with exact line"
    elif task_id == "B02":
        staged = out("diff", "--cached", "--name-only").splitlines()
        unstaged = out("diff", "--name-only").splitlines()
        assert staged == ["notes.txt"], "Only notes.txt should be staged"
        assert "config.txt" in unstaged and "config.txt" not in staged, "Keep config.txt unstaged"
        assert "more notes" in out("show", ":notes.txt"), "Stage the edited notes content"
    elif task_id == "B03":
        target = out("rev-parse", "refs/heads/feature/readme")
        main = out("rev-parse", "refs/heads/main")
        assert target != main, "Feature branch must have a new commit"
        assert "## Usage" in out("show", "feature/readme:README.md"), "Commit Usage heading"
        assert "## Usage" not in out("show", "main:README.md"), "Keep main unchanged"
        assert git(repo, "merge-base", "--is-ancestor", main, target, check=False).returncode == 0
    elif task_id == "B04":
        main = out("rev-parse", "refs/heads/main")
        remote = git(path / "origin.git", "rev-parse", "refs/heads/main", check=False)
        assert remote.returncode == 0 and remote.stdout.strip() == main, "Push main to local origin"
    elif task_id == "I01":
        main = out("rev-parse", "refs/heads/main")
        feature = out("rev-parse", "refs/heads/feature/checklist")
        assert main == feature, "Fast-forward main to feature/checklist"
        assert out("show", "main:CHECKLIST.md") == "# Check before merge", "Include checklist"
    elif task_id == "I02":
        assert out("branch", "--show-current") == "main", "Complete merge on main"
        parents = out("rev-list", "--parents", "-n", "1", "HEAD").split()
        assert len(parents) == 3, "Finish a two-parent merge commit"
        assert out("show", "HEAD:settings.txt") == "color=purple", "Resolve to color=purple"
        assert not out("ls-files", "-u"), "Resolve every unmerged index path"
    elif task_id == "I03":
        current = out("rev-parse", "HEAD")
        assert current != metadata["broken"], "Make a new revert commit"
        assert out("show", "HEAD:status.txt") == "healthy", "Restore healthy status"
        assert git(repo, "merge-base", "--is-ancestor", metadata["broken"], "HEAD", check=False).returncode == 0, "Preserve published bad commit in ancestry"
        assert out("log", "-1", "--format=%s").startswith("Revert"), "Use git revert, not reset"
    elif task_id == "I04":
        current = out("rev-parse", "refs/heads/maintenance")
        assert current != metadata["fix"], "Cherry-pick creates a new commit hash"
        assert out("show", "maintenance:bugfix.txt") == "validation fixed", "Bring fix to maintenance"
        assert out("rev-parse", "refs/heads/main") == metadata["fix"], "Leave main unchanged"
    elif task_id == "A01":
        assert out("rev-parse", "refs/heads/recovered-work") == metadata["lost"], "Recover lost hash on recovered-work"
        assert out("show", "recovered-work:chapter.txt") == "v2", "Recovered commit has v2"
    elif task_id == "A02":
        finding = (repo / "finding.txt")
        assert finding.is_file(), "Write the first-bad-commit hash to finding.txt"
        assert finding.read_text(encoding="utf-8").strip() == metadata["bad"], "Identify the original first bad commit, not HEAD"
        assert out("branch", "--show-current") == "main", "Run git bisect reset"
    elif task_id == "A03":
        linked = path / "hotfix"
        assert (linked / ".git").exists(), "Create linked worktree at .practice/A03/hotfix"
        assert git(linked, "branch", "--show-current").stdout.strip() == "hotfix", "Use branch hotfix"
        assert git(linked, "show", "HEAD:FIX.txt").stdout.strip() == "hotfix ready", "Commit FIX.txt"
        assert git(repo, "show", "main:FIX.txt", check=False).returncode != 0, "Keep main unchanged"
    elif task_id == "A04":
        assert out("cat-file", "-t", "refs/tags/v1.0.0") == "tag", "Use an annotated, not lightweight tag"
        assert out("rev-parse", "v1.0.0^{commit}") == out("rev-parse", "main"), "Tag current release commit"
        assert "Release" in out("cat-file", "-p", "refs/tags/v1.0.0"), "Include release message"
    else:
        raise AssertionError("Unhandled task")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="action", required=True)
    commands.add_parser("list")
    for command in ("start", "check"):
        p = commands.add_parser(command)
        p.add_argument("task_id", choices=sorted(all_tasks()))
    args = parser.parse_args()
    tasks = all_tasks()
    if args.action == "list":
        for task_id, task in sorted(tasks.items()):
            print(f"{task_id} | {task['level']:<12} | {task['title']}")
        return 0
    task_id = args.task_id
    try:
        if args.action == "start":
            folder = start_task(task_id)
            print(f"Started {task_id}: {tasks[task_id]['title']}")
            print(f"Repository: {folder / 'repo'}")
            print(f"Goal: {tasks[task_id]['goal']}")
            print(f"Hint: {tasks[task_id]['hint']}")
            print(f"Check with: python tools/practice.py check {task_id}")
        else:
            assert_task(task_id)
            print(f"PASS {task_id}: {tasks[task_id]['title']}")
        return 0
    except (AssertionError, OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as exc:
        print(f"FAIL {task_id}: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
