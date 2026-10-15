import tempfile
import unittest
from pathlib import Path
from task_manager import add_task, list_tasks, update_status, summarize, save_tasks

class TaskManagerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "tasks.csv"
        save_tasks(self.path, [
            {"task_id":"1","description":"A","priority":"low","status":"pending"},
            {"task_id":"2","description":"B","priority":"high","status":"completed"},
        ])
    def tearDown(self):
        self.tmp.cleanup()
    def test_add(self):
        t = add_task(self.path, "C", "medium")
        self.assertEqual(t["task_id"], "3")
        self.assertEqual(t["status"], "pending")
    def test_priority_filter_and_sort(self):
        self.assertEqual(list_tasks(self.path, "high")[0]["description"], "B")
        self.assertEqual(list_tasks(self.path)[0]["priority"], "high")
    def test_update_status(self):
        update_status(self.path, 1, "completed")
        self.assertEqual(summarize(self.path)["status"]["completed"], 2)
    def test_summary(self):
        s = summarize(self.path)
        self.assertEqual(s["status"]["pending"], 1)
        self.assertEqual(s["priority"]["high"], 1)
    def test_bad_priority(self):
        with self.assertRaises(ValueError):
            add_task(self.path, "X", "urgent")
if __name__ == "__main__":
    unittest.main()
