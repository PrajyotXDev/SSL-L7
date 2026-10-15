import csv
import tempfile
import unittest
from pathlib import Path
from grading import grade_for_marks, load_students, format_report

class GradingTests(unittest.TestCase):
    def test_boundaries(self):
        expected = {39:"F", 40:"C", 59:"C", 60:"B", 79:"B", 80:"A", 100:"A"}
        for marks, grade in expected.items():
            with self.subTest(marks=marks):
                self.assertEqual(grade_for_marks(marks), grade)

    def test_invalid_marks(self):
        for marks in (-1, 101, "abc", None):
            with self.subTest(marks=marks):
                with self.assertRaises(ValueError):
                    grade_for_marks(marks)

    def test_load_and_report(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "students.csv"
            p.write_text("name,marks\nAlice,80\nBob,39\n", encoding="utf-8")
            rows = load_students(p)
            self.assertEqual([r["grade"] for r in rows], ["A", "F"])
            self.assertIn("Alice", format_report(rows))

    def test_malformed_csv(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "students.csv"
            p.write_text("name,marks\nAlice,\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                load_students(p)

    def test_missing_headers(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "students.csv"
            p.write_text("student,score\nAlice,80\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                load_students(p)

if __name__ == "__main__":
    unittest.main()
