# CS 202C Software Systems Lab — Assignment 7

**Student:** Prajyot Satarde  
**Roll No.:** MC25BT012  
**Branch:** Mathematics and Computing, IIT Dharwad  
**Topic:** Version management and Git commands

## Package structure
- `student-grading/`: CSV grading, formatted report, boundary/malformed-input tests.
- `calculator-library/`: calculator API, validation, test suite, and instructions for the deliberate-bug/history exercise.
- `task-manager/`: independent CSV task manager with priority filtering/sorting and summaries.
- `scripts/`: repeatable Git command sequences and inspection commands.

## Grading rules
A: 80–100; B: 60–<80; C: 40–<60; F: 0–<40. Values below 0 or above 100 are rejected. Boundary tests cover 39, 40, 59, 60, 79, 80, and 100; invalid tests cover -1 and 101, malformed numeric values, missing values, and invalid headers.

## Run verification
From the package root:
```bash
python -m unittest discover -s student-grading -p 'test_*.py' -v
python -m unittest discover -s calculator-library -p 'test_*.py' -v
python -m unittest discover -s task-manager -p 'test_*.py' -v
```

## Git evidence to collect in your terminal
```bash
git status --short --branch
git branch -avv
git log --graph --oneline --decorate --all
git show --stat --oneline HEAD
git diff <old-commit> <new-commit>
git tag -n
git status --porcelain
```

## Merge-conflict explanation (student grading)
The two feature branches originate from the same initial commit and modify overlapping lines in the shared grading function. Git cannot safely choose which implementation to keep, so the merge pauses with conflict markers. Resolve by retaining range validation and the report-related processing, remove all conflict markers, run tests, stage the resolved file, and complete the merge commit. Verify the merge graph and test suite afterward.

## Calculator bug audit
A faulty `square` implementation should be introduced and committed only as a deliberate intermediate exercise. Use `git log --oneline`, `git show <bug-commit>`, and `git diff <bug-commit>^ <bug-commit>` to identify the faulty change. Fix it in a new commit rather than rewriting history, then create an annotated `v1.0` tag on the corrected commit. This preserves an auditable record of the defect and correction.

## Upstream inspection
The assignment-provided upstream URL is `https://github.com/octocat/Hello-World.git`. Clone it into `upstream-inspection/` and inspect only; do not modify or push to the upstream repository.
