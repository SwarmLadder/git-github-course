"""Check substantive lessons, course structure, and linked projects."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ContentTests(unittest.TestCase):
    def test_thirty_six_substantial_lessons(self):
        for level in ("basics", "intermediate", "advanced"):
            lessons = sorted((ROOT / level / "lessons").glob("*.md"))
            self.assertEqual(len(lessons), 12, level)
            self.assertEqual([p.name[:2] for p in lessons], [f"{n:02}" for n in range(12)])
            for path in lessons:
                with self.subTest(path=path):
                    text = path.read_text(encoding="utf-8")
                    self.assertGreaterEqual(len(text.split()), 280)
                    self.assertEqual(len(re.findall(r"(?m)^### [1-4]\. ", text)), 4)
                    self.assertIn(chr(96)*3 + "bash", text)
                    self.assertIn("Interview", text)

    def test_three_projects(self):
        self.assertEqual(len(list((ROOT / "projects").glob("[0-9][0-9]_*.md"))), 3)

    def test_syllabi_and_references(self):
        for rel in ("README.md", "CHEATSHEET.md", "GLOSSARY.md",
                    "CURRICULUM.md", "practice/README.md", "interview/README.md"):
            with self.subTest(path=rel):
                self.assertTrue((ROOT / rel).is_file())


if __name__ == "__main__":
    unittest.main()
