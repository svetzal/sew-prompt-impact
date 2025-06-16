Certainly! Below is a simple Python module designed to manage a list of tasks following the principles outlined in your baseline conventions. This module will include functions for adding, removing, and listing tasks, along with unit tests to ensure correctness.

### `task_manager.py`

```python
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: str) -> None:
        """Add a new task to the list."""
        if not task.strip():
            raise ValueError("Task cannot be empty or just whitespace.")
        self.tasks.append(task)

    def remove_task(self, task: str) -> bool:
        """
        Remove a task from the list.
        
        :return: True if the task was removed, False if it was not found.
        """
        try:
            self.tasks.remove(task)
            return True
        except ValueError:
            return False

    def list_tasks(self) -> list:
        """Return a copy of the current tasks."""
        return self.tasks.copy()

# Example usage:
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Read a book")
    manager.add_task("Write code")
    print(manager.list_tasks())
    manager.remove_task("Read a book")
    print(manager.list_tasks())
```

### `test_task_manager.py`

```python
import unittest
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task_successfully(self):
        self.manager.add_task("Write a report")
        self.assertIn("Write a report", self.manager.list_tasks())

    def test_add_empty_task_fails(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("")

    def test_remove_existing_task(self):
        self.manager.add_task("Take out the trash")
        result = self.manager.remove_task("Take out the trash")
        self.assertTrue(result)
        self.assertNotIn("Take out the trash", self.manager.list_tasks())

    def test_remove_nonexistent_task(self):
        result = self.manager.remove_task("Nonexistent task")
        self.assertFalse(result)

    def test_list_tasks_returns_copy(self):
        tasks = ["Do laundry", "Clean dishes"]
        for task in tasks:
            self.manager.add_task(task)
        listed_tasks = self.manager.list_tasks()
        self.assertEqual(tasks, listed_tasks)
        # Modifying the list returned by list_tasks should not affect the original list
        listed_tasks.append("This is a fake task")
        self.assertNotEqual(self.manager.tasks, listed_tasks)

if __name__ == "__main__":
    unittest.main()
```

### Key Points:
1. **Code Readability**: The code and comments are clear to understand.
2. **No Duplicate Knowledge**: There is no duplicated logic or decisions.
3. **Minimal Entities**: Only necessary classes and methods are used.
4. **Tests as Executable Spec**: Unit tests cover the expected behavior.
5. **Functional Core, Imperative Shell**: Business logic (task management) is separated from I/O operations (printing tasks).

### How to Use:
1. Save `task_manager.py` in your project directory.
2. Run `test_task_manager.py` to ensure all functionality works as expected.

This setup should meet the guidelines you provided and offer a simple, maintainable way to manage a list of tasks.