# CS 202C — Software Systems Lab 7

**Repository:** SSL-L7  
**Student:** Prajyot Satarde  
**Roll Number:** MC25BT012  
**Branch:** Mathematics and Computing  
**Institute:** IIT Dharwad

This repository contains the source code, unit tests, documentation, and Git version-control exercises completed for Software Systems Lab Assignment 7.

## Repository Structure

```text
SSL-L7/
├── student-grading/
│   ├── grading.py
│   ├── students.csv
│   ├── test_grading.py
│   ├── README.md
│   └── .gitignore
├── calculator-library/
│   ├── calculator.py
│   ├── test_calculator.py
│   ├── README.md
│   └── .gitignore
├── task-manager/
│   ├── task_manager.py
│   ├── tasks.csv
│   ├── test_task_manager.py
│   ├── README.md
│   └── .gitignore
├── scripts/
│   ├── git-inspection-commands.sh
│   ├── upstream-inspection.sh
│   └── README.md
├── REPORT.md
├── TEST_RESULTS.txt
└── README.md
```

## Question 1 — Student Grading System

A Python program that reads student records from a CSV file, validates marks, assigns letter grades, and generates a formatted report.

### Features

- Reads student names and marks from CSV.
- Validates numeric marks and rejects values outside the range 0–100.
- Assigns grades according to the following scale:

| Marks | Grade |
|---|---|
| 80–100 | A |
| 60–less than 80 | B |
| 40–less than 60 | C |
| 0–less than 40 | F |

- Generates a formatted student report and grade-distribution summary.
- Handles malformed CSV records and invalid input.

### Run

```powershell
python student-grading/grading.py student-grading/students.csv
```

Generate the detailed report:

```powershell
python student-grading/grading.py student-grading/students.csv --report
```

Run tests:

```powershell
python -m unittest discover -s student-grading -p "test_*.py" -v
```

## Question 2 — Calculator Library

A reusable Python calculator library supporting common arithmetic operations.

### Features

- Addition
- Subtraction
- Multiplication
- Division with division-by-zero handling
- Squaring a number
- Numeric input validation

### Run

```powershell
python calculator-library/calculator.py
```

Run tests:

```powershell
python -m unittest discover -s calculator-library -p "test_*.py" -v
```

### Git Version-Control Exercise

The Git history preserves the deliberately introduced defect in the `square()` function and its subsequent correction.

| Commit | Description |
|---|---|
| `330e24f` | Introduced the deliberate bug in `square()` |
| `6d63f2a` | Fixed the square function implementation |

The annotated `v1.0` tag identifies the corrected calculator implementation.

Inspect the changes:

```powershell
git show 330e24f
git diff 330e24f~1 330e24f -- calculator-library/calculator.py
git show v1.0
```

## Question 3 — Task Manager

A CSV-backed command-line task manager for creating, listing, updating, and summarizing tasks.

### Features

- Add tasks with a description and priority.
- List tasks and filter by priority.
- Sort tasks by priority: high, medium, then low.
- Mark tasks as completed.
- Generate task summaries by status and priority.
- Persist tasks in a CSV file.

### Commands

List tasks:

```powershell
python task-manager/task_manager.py list
```

Add a high-priority task:

```powershell
python task-manager/task_manager.py add "Submit lab assignment" --priority high
```

Mark a task as completed:

```powershell
python task-manager/task_manager.py complete 1
```

Display a summary:

```powershell
python task-manager/task_manager.py summary
```

Run tests:

```powershell
python -m unittest discover -s task-manager -p "test_*.py" -v
```

## Git and Version-Control Exercises

The repository demonstrates practical Git workflows, including:

- Initial repository setup and commits.
- Feature branches and independent development.
- Merge-conflict creation and manual resolution.
- Merging feature branches into `main`.
- Inspecting commits and differences.
- Creating an annotated release tag.
- Pushing commits, branches, and tags to GitHub.

### Branches

- `feature-grading`
- `feature-report`
- `feature-priority`
- `feature-summary`

### Important Git Commands

View the commit graph:

```powershell
git --no-pager log --graph --oneline --decorate --all
```

Inspect branches:

```powershell
git branch -avv
```

Inspect repository status:

```powershell
git status
```

Inspect tags:

```powershell
git tag -n
```

## Test Results

The final local verification completed successfully:

| Test suite | Tests passed |
|---|---:|
| Student grading | 5/5 |
| Calculator library | 6/6 |
| Task manager | 5/5 |
| **Total** | **16/16** |

Run all three suites individually using the commands documented above.

## ⚙️ Requirements

- Python 3.10 or later recommended.
- Git.
- GitHub account for remote repository operations.

The Python programs use the standard library and do not require additional package installations.

## Clone the Repository

```powershell
git clone https://github.com/PrajyotXDev/SSL-L7.git
cd SSL-L7
```

## Author

**Prajyot Satarde**  
Mathematics and Computing  
IIT Dharwad

GitHub: [@PrajyotXDev](https://github.com/PrajyotXDev)

---

*Submitted as part of CS 202C — Software Systems Lab, Assignment 7.*
