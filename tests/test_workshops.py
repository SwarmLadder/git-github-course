"""Validate the enriched learning route and its human-graded workshop materials."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
WORKSHOPS = ROOT / "workshops"


class WorkshopTests(unittest.TestCase):
    def test_six_substantial_workshops(self):
        docs = sorted(WORKSHOPS.glob("[0-9][0-9]_*.md"))
        self.assertEqual(len(docs), 6)
        self.assertEqual([doc.name[:2] for doc in docs], [f"{n:02}" for n in range(1, 7)])
        for doc in docs:
            with self.subTest(doc=doc):
                body = doc.read_text(encoding="utf-8")
                self.assertGreaterEqual(len(body.split()), 320)
                self.assertIn("## Outcome", body)
                self.assertTrue("## Guided procedure" in body or "## Investigation phase" in body)
                self.assertIn("Completion gate", body)
                self.assertIn("Failure", body)
                self.assertIn("Labs:", body)
                self.assertNotIn("real production token", body.lower())

    def test_linked_local_content_exists(self):
        for file in [
            ROOT / "README.md", ROOT / "CURRICULUM.md",
            ROOT / "ASSESSMENT.md", ROOT / "practice" / "README.md",
            WORKSHOPS / "README.md", *WORKSHOPS.glob("[0-9][0-9]_*.md")
        ]:
            body = file.read_text(encoding="utf-8")
            for match in re.findall(r"\[[^\]]+\]\(([^)]+)\)", body):
                if "://" in match or match.startswith("#"):
                    continue
                target = (file.parent / match.split("#", 1)[0]).resolve()
                with self.subTest(source=file, link=match):
                    self.assertTrue(target.is_file(), f"{file}: broken link {match}")

    def test_route_covers_all_new_tasks(self):
        from json import loads
        tasks = loads((ROOT / "practice" / "tasks.json").read_text(encoding="utf-8"))
        self.assertEqual(len(tasks), 24)
        ids = {task["id"] for task in tasks}
        curriculum = (ROOT / "CURRICULUM.md").read_text(encoding="utf-8")
        self.assertEqual(ids, set(re.findall(r"\b(?:B|I|A)\d\d\b", curriculum)))
        mapping = {
            "B05": "basics/lessons/05_ignore_patterns_and_files.md",
            "B06": "basics/lessons/01_staging_diff_and_commits.md",
            "B07": "basics/lessons/08_undo_restore_revert_reset.md",
            "B08": "basics/lessons/06_remotes_fetch_push.md",
            "I05": "intermediate/lessons/03_interactive_rebase_and_commit_hygiene.md",
            "I06": "basics/lessons/09_stash_and_temporary_work.md",
            "I07": "intermediate/lessons/02_merge_squash_rebase_strategies.md",
            "I08": "intermediate/lessons/04_cherry_pick_and_revert.md",
            "A05": "advanced/lessons/00_objects_refs_and_plumbing.md",
            "A06": "advanced/lessons/04_rebase_onto_and_long_lived_branches.md",
            "A07": "advanced/lessons/06_monorepos_sparse_and_partial_clone.md",
            "A08": "advanced/lessons/07_submodules_subtrees_and_dependency_options.md",
        }
        for id, filename in mapping.items():
            with self.subTest(task=id):
                body = (ROOT / filename).read_text(encoding="utf-8")
                self.assertIn("Put this lesson into practice — " + id, body)

    def test_main_docs_current(self):
        for file in ("README.md", "CURRICULUM.md", "ASSESSMENT.md"):
            body = (ROOT / file).read_text(encoding="utf-8")
            with self.subTest(file=file):
                self.assertIn("24", body)
                self.assertIn("36", body)
        self.assertIn("six", (ROOT / "README.md").read_text(encoding="utf-8").lower())


if __name__ == "__main__":
    unittest.main()
