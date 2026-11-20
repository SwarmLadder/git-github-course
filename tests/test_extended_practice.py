"""Exercise the twelve expanded Git labs against real disposable Git repositories."""
from __future__ import annotations

import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from extended_practice import EXTRA_IDS
from practice import all_tasks, assert_task, git, make_commit, start_task


class ExtendedPracticeTests(unittest.TestCase):
    def test_all_extended_tasks_exist(self):
        all_ids = all_tasks()
        self.assertEqual(len(EXTRA_IDS), 12)
        self.assertTrue(EXTRA_IDS <= set(all_ids))
        self.assertEqual(len(all_ids), 24)
        for prefix in ("B", "I", "A"):
            self.assertEqual(len([i for i in EXTRA_IDS if i.startswith(prefix)]), 4)

    def test_fixtures_start_incomplete_and_refuse_overwrite(self):
        with TemporaryDirectory() as tmp:
            base = Path(tmp)
            for task_id in sorted(EXTRA_IDS):
                with self.subTest(task=task_id):
                    start_task(task_id, base)
                    with self.assertRaises((AssertionError, RuntimeError)):
                        assert_task(task_id, base)
                    with self.assertRaises(FileExistsError):
                        start_task(task_id, base)

    def test_real_git_solution_paths(self):
        with TemporaryDirectory() as tmp:
            base = Path(tmp)
            for task_id in sorted(EXTRA_IDS):
                with self.subTest(task=task_id):
                    task = start_task(task_id, base)
                    repo = task / "repo"
                    meta = json.loads((task / "metadata.json").read_text(encoding="utf-8"))
                    if task_id == "B05":
                        (repo / ".gitignore").write_text(
                            ".env.local\nbuild/\n*.log\n!important.log\n", encoding="utf-8"
                        )
                        git(repo, "add", ".gitignore", "important.log")
                        git(repo, "commit", "-m", "Ignore generated files safely")
                    elif task_id == "B06":
                        # Stage exactly one hunk while the worktree keeps both.
                        original = git(repo, "show", "HEAD:story.txt").stdout.splitlines(keepends=True)
                        original[2] = "line-03 staged change\n"
                        (repo / "story.txt").write_text("".join(original), encoding="utf-8")
                        git(repo, "add", "story.txt")
                        original[46] = "line-47 worktree draft\n"
                        (repo / "story.txt").write_text("".join(original), encoding="utf-8")
                    elif task_id == "B07":
                        git(repo, "restore", "--", "config.ini")
                    elif task_id == "B08":
                        git(repo, "fetch", "origin")
                    elif task_id == "I05":
                        git(repo, "rebase", "main")
                    elif task_id == "I06":
                        git(repo, "stash", "push", "-u", "-m", "Keep WIP for later")
                    elif task_id == "I07":
                        git(repo, "merge", "--squash", "feature/promo")
                        git(repo, "commit", "-m", "Add promotion")
                    elif task_id == "I08":
                        git(repo, "revert", "-m", "1", "--no-edit", "HEAD")
                    elif task_id == "A05":
                        git(repo, "notes", "add", "-m", "Reviewed for release: checks passed", "HEAD")
                    elif task_id == "A06":
                        git(repo, "reset", "--soft", "main")
                        git(repo, "commit", "-m", "Implement complete search")
                    elif task_id == "A07":
                        git(repo, "sparse-checkout", "init", "--cone")
                        git(repo, "sparse-checkout", "set", "docs", "apps/api")
                    elif task_id == "A08":
                        git(repo, "-c", "protocol.file.allow=always", "submodule",
                            "add", "../library", "vendor/library")
                        git(repo, "add", ".gitmodules", "vendor/library")
                        git(repo, "commit", "-m", "Pin local library")
                    else:
                        self.fail(f"Missing solution path {task_id}")
                    assert_task(task_id, base)

    def test_shortcuts_do_not_fake_success(self):
        with TemporaryDirectory() as tmp:
            base = Path(tmp)

            start_task("B08", base)
            # origin/main is deliberately stale before fetch.
            with self.assertRaises((AssertionError, RuntimeError)):
                assert_task("B08", base)

            task = start_task("I06", base)
            git(task / "repo", "stash", "push", "-m", "Missed untracked draft")
            with self.assertRaises((AssertionError, RuntimeError)):
                assert_task("I06", base)

            task = start_task("I07", base)
            git(task / "repo", "merge", "--no-ff", "-m", "Merge feature", "feature/promo")
            with self.assertRaises((AssertionError, RuntimeError)):
                assert_task("I07", base)

            task = start_task("A08", base)
            repo = task / "repo"
            make_commit(repo, "vendor/library/lib.txt", "Local library v1\n", "Copy dependency")
            with self.assertRaises((AssertionError, RuntimeError)):
                assert_task("A08", base)


if __name__ == "__main__":
    unittest.main()
