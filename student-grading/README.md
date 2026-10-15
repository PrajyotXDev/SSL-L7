# Student Grading System

Reads `name,marks` records from CSV and assigns grades: A for 80–100, B for 60–<80, C for 40–<60, and F for 0–<40. Marks outside 0–100 and malformed records are rejected.

```bash
python grading.py students.csv
python grading.py students.csv --report
python -m unittest -v
```

The assignment's feature branches and merge-conflict evidence are documented in the top-level `REPORT.md`. Use `git log --graph --oneline --decorate --all` to inspect history.
