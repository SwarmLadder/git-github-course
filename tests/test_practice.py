"""Exercise all twelve Git practice fixtures with real local Git."""
from __future__ import annotations

import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from practice import all_tasks, assert_task, git, make_commit, start_task

LEGACY_IDS = [f'{level}{i:02}' for level in ('B', 'I', 'A') for i in range(1, 5)]


class PracticeTests(unittest.TestCase):
    def test_task_catalog(self):
        tasks = all_tasks()
        self.assertEqual(len(tasks), 24)
        for level in ("basics", "intermediate", "advanced"):
            self.assertEqual(sum(t["level"] == level for t in tasks.values()), 8)

    def test_fixtures_are_incomplete_and_not_overwritten(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            for task_id in LEGACY_IDS:
                with self.subTest(task_id=task_id):
                    start_task(task_id, root)
                    with self.assertRaises((AssertionError, RuntimeError)):
                        assert_task(task_id, root)
                    with self.assertRaises(FileExistsError):
                        start_task(task_id, root)

    def test_all_twelve_valid_completion_paths(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            for task_id in LEGACY_IDS:
                with self.subTest(task_id=task_id):
                    folder = start_task(task_id, root)
                    repo = folder / "repo"
                    meta = json.loads((folder / "metadata.json").read_text(encoding="utf-8"))
                    if task_id == "B01":
                        make_commit(repo, "notes.txt", "learning Git\n", "Start learning")
                    elif task_id == "B02":
                        git(repo, "add", "notes.txt")
                    elif task_id == "B03":
                        git(repo, "switch", "-c", "feature/readme")
                        make_commit(repo, "README.md", "# Demo\n\n## Usage\n", "Explain usage")
                    elif task_id == "B04":
                        git(repo, "push", "-u", "origin", "main")
                    elif task_id == "I01":
                        git(repo, "merge", "--ff-only", "feature/checklist")
                    elif task_id == "I02":
                        conflict = git(repo, "merge", "feature/red", check=False)
                        self.assertNotEqual(conflict.returncode, 0)
                        (repo / "settings.txt").write_text("color=purple\n", encoding="utf-8")
                        git(repo, "add", "settings.txt")
                        git(repo, "commit", "-m", "Resolve color choice")
                    elif task_id == "I03":
                        git(repo, "revert", "--no-edit", "HEAD")
                    elif task_id == "I04":
                        git(repo, "cherry-pick", "main")
                    elif task_id == "A01":
                        git(repo, "branch", "recovered-work", meta["lost"])
                    elif task_id == "A02":
                        git(repo, "bisect", "start")
                        git(repo, "bisect", "bad", "HEAD")
                        git(repo, "bisect", "good", meta["good"])
                        found = git(repo, "bisect", "run", sys.executable, "check.py")
                        self.assertIn(meta["bad"], found.stdout)
                        git(repo, "bisect", "reset")
                        (repo / "finding.txt").write_text(meta["bad"] + "\n", encoding="utf-8")
                    elif task_id == "A03":
                        linked = folder / "hotfix"
                        git(repo, "worktree", "add", "-b", "hotfix", str(linked), "HEAD")
                        make_commit(linked, "FIX.txt", "hotfix ready\n", "Prepare hotfix")
                    elif task_id == "A04":
                        git(repo, "tag", "-a", "v1.0.0", "-m", "Release 1.0.0")
                    assert_task(task_id, root)

    def test_wrong_first_commit_fails(self):
        with TemporaryDirectory() as temp:
            folder = start_task("B01", Path(temp))
            make_commit(folder / "repo", "other.txt", "wrong\n", "Wrong file")
            with self.assertRaises((AssertionError, RuntimeError)):
                assert_task("B01", Path(temp))


if __name__ == "__main__":
    unittest.main()
