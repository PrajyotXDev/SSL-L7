
import csv
from pathlib import Path


def grade_for_marks(marks):
    """Validate marks and return a letter grade."""
    try:
        marks = float(marks)
    except (TypeError, ValueError):
        raise ValueError("Marks must be numeric")

    if not 0 <= marks <= 100:
        raise ValueError("Marks must be between 0 and 100")

    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    return "F"


def load_students(csv_path):
    """Load student records from a CSV file."""
    students = []

    with Path(csv_path).open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        if not reader.fieldnames or not {
            "name", "marks"
        }.issubset(set(reader.fieldnames)):
            raise ValueError("CSV must contain name and marks columns")

        for line_no, row in enumerate(reader, start=2):
            name = (row.get("name") or "").strip()
            raw_marks = (row.get("marks") or "").strip()

            if not name or not raw_marks:
                raise ValueError(
                    f"Malformed CSV record at line {line_no}"
                )

            try:
                marks = float(raw_marks)
                grade = grade_for_marks(marks)
            except ValueError as exc:
                raise ValueError(
                    f"Invalid record at line {line_no}: {exc}"
                ) from exc

            students.append({
                "name": name,
                "marks": marks,
                "grade": grade
            })

    return students


def format_report(students):
    """Display student grades and a grade distribution summary."""
    lines = [
        "Student Grading Report",
        "=" * 40,
        f"{'Name':<20} {'Marks':>7} {'Grade':>7}",
        "-" * 40
    ]

    counts = {"A": 0, "B": 0, "C": 0, "F": 0}

    for student in students:
        lines.append(
            f"{student['name']:<20} "
            f"{student['marks']:>7g} "
            f"{student['grade']:>7}"
        )
        counts[student["grade"]] += 1

    lines.extend(["-" * 40, "Grade Summary"])

    for grade, count in counts.items():
        lines.append(f"Grade {grade}: {count} student(s)")

    return "\n".join(lines)


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Grade students from a CSV file"
    )
    parser.add_argument("csv_file", nargs="?", default="students.csv")
    parser.add_argument(
        "--report",
        action="store_true",
        help="print a formatted report"
    )
    args = parser.parse_args()

    students = load_students(args.csv_file)

    if args.report:
        print(format_report(students))
    else:
        for student in students:
            print(
                f"{student['name']}: "
                f"{student['marks']:g} -> {student['grade']}"
            )


if __name__ == "__main__":
    main()
