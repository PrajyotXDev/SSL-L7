"""CSV-backed command-line task manager."""
import argparse
import csv
from pathlib import Path

FIELDS = ["task_id", "description", "priority", "status"]
PRIORITIES = {"low", "medium", "high"}
STATUSES = {"pending", "completed"}

def load_tasks(path):
    p = Path(path)
    if not p.exists():
        return []
    with p.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != FIELDS:
            raise ValueError(f"CSV headers must be: {','.join(FIELDS)}")
        tasks = []
        for row in reader:
            if row["priority"] not in PRIORITIES or row["status"] not in STATUSES:
                raise ValueError(f"Invalid task record: {row}")
            tasks.append(row)
        return tasks

def save_tasks(path, tasks):
    with Path(path).open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(tasks)

def add_task(path, description, priority="medium"):
    if priority not in PRIORITIES:
        raise ValueError("Priority must be low, medium, or high")
    tasks = load_tasks(path)
    next_id = max((int(t["task_id"]) for t in tasks), default=0) + 1
    task = {"task_id": str(next_id), "description": description,
            "priority": priority, "status": "pending"}
    tasks.append(task)
    save_tasks(path, tasks)
    return task

def list_tasks(path, priority=None):
    tasks = load_tasks(path)

    if priority is not None:
        if priority not in PRIORITIES:
            raise ValueError("Priority must be low, medium, or high")
        tasks = [t for t in tasks if t["priority"] == priority]

    priority_order = {"high": 0, "medium": 1, "low": 2}
    return sorted(
        tasks,
        key=lambda t: (
            priority_order[t["priority"]],
            int(t["task_id"])
        )
    )

def update_status(path, task_id, status):
    if status not in STATUSES:
        raise ValueError("Status must be pending or completed")
    tasks = load_tasks(path)
    for task in tasks:
        if task["task_id"] == str(task_id):
            task["status"] = status
            save_tasks(path, tasks)
            return task
    raise KeyError(f"No task with ID {task_id}")

def summarize(path):
    tasks = load_tasks(path)

    return {
        "total": len(tasks),
        "status": {
            status: sum(t["status"] == status for t in tasks)
            for status in sorted(STATUSES)
        },
        "priority": {
            priority: sum(t["priority"] == priority for t in tasks)
            for priority in ("high", "medium", "low")
        }
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", default="tasks.csv")
    sub = parser.add_subparsers(dest="command", required=True)
    a = sub.add_parser("add"); a.add_argument("description"); a.add_argument("--priority", choices=sorted(PRIORITIES), default="medium")
    l = sub.add_parser("list"); l.add_argument("--priority", choices=sorted(PRIORITIES))
    u = sub.add_parser("complete"); u.add_argument("task_id")
    s = sub.add_parser("summary")
    args = parser.parse_args()
    if args.command == "add":
        print(add_task(args.file, args.description, args.priority))
    elif args.command == "list":
        for t in list_tasks(args.file, args.priority): print(t)
    elif args.command == "complete":
        print(update_status(args.file, args.task_id, "completed"))
    elif args.command == "summary":
        print(summarize(args.file))

if __name__ == "__main__":
    main()
