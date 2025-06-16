Certainly! Below is a Python module named `task_manager.py` that can manage a list of tasks. This module follows the baseline conventions you provided, ensuring code clarity, simplicity, and maintainability.

### task_manager.py

```python
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Task:
    """Represents a single task."""
    id: int
    description: str
    completed: bool = False

class TaskManager:
    """Manages a list of tasks."""

    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1

    def add_task(self, description: str) -> None:
        """Adds a new task to the list."""
        new_task = Task(id=self.next_id, description=description)
        self.tasks.append(new_task)
        self.next_id += 1

    def complete_task(self, task_id: int) -> Optional[Task]:
        """Marks a task as completed by its ID."""
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                return task
        return None

    def remove_task(self, task_id: int) -> bool:
        """Removes a task from the list by its ID."""
        for index, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[index]
                return True
        return False

    def list_tasks(self) -> List[Task]:
        """Returns a list of all tasks."""
        return self.tasks

    def list_incomplete_tasks(self) -> List[Task]:
        """Returns a list of incomplete tasks."""
        return [task for task in self.tasks if not task.completed]

    def list_completed_tasks(self) -> List[Task]:
        """Returns a list of completed tasks."""
        return [task for task in self.tasks if task.completed]

# Example usage
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Buy groceries")
    manager.add_task("Pay bills")
    print("All tasks:", [t.description for t in manager.list_tasks()])
    
    completed_task = manager.complete_task(1)
    if completed_task:
        print(f"Completed task: {completed_task.description}")
    
    print("Incomplete tasks:", [t.description for t in manager.list_incomplete_tasks()])
    print("Completed tasks:", [t.description for t in manager.list_completed_tasks()])

    removed = manager.remove_task(2)
    if removed:
        print("Task removed successfully")
    else:
        print("Task not found")

    print("All tasks after removal:", [t.description for t in manager.list_tasks()])
```

### Explanation

1. **Data Class `Task`**:
   - Represents a single task with an ID, description, and completion status.
   - Uses the `dataclass` decorator to automatically generate special methods like `__init__`, `__repr__`, etc.

2. **Class `TaskManager`**:
   - Manages a list of tasks.
   - Methods:
     - `add_task(description: str)`: Adds a new task with a unique ID.
     - `complete_task(task_id: int)`: Marks a task as completed by its ID.
     - `remove_task(task_id: int)`: Removes a task from the list by its ID.
     - `list_tasks()`: Returns a list of all tasks.
     - `list_incomplete_tasks()`: Returns a list of incomplete tasks.
     - `list_completed_tasks()`: Returns a list of completed tasks.

3. **Example Usage**:
   - Demonstrates how to use the `TaskManager` class to add, complete, remove, and list tasks.

### Testing

To ensure all tests pass, you can write unit tests using a testing framework like `unittest`.

```python
import unittest
from task_manager import TaskManager, Task

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()
        self.manager.add_task("Buy groceries")
        self.manager.add_task("Pay bills")

    def test_add_task(self):
        self.assertEqual(len(self.manager.list_tasks()), 2)

    def test_complete_task(self):
        completed_task = self.manager.complete_task(1)
        self.assertTrue(completed_task.completed)

    def test_remove_task(self):
        removed = self.manager.remove_task(2)
        self.assertTrue(removed)
        self.assertEqual(len(self.manager.list_tasks()), 1)

    def test_list_incomplete_tasks(self):
        incomplete_tasks = self.manager.list_incomplete_tasks()
        self.assertEqual(len(incomplete_tasks), 2)

    def test_list_completed_tasks(self):
        completed_tasks = self.manager.list_completed_tasks()
        self.assertEqual(len(completed_tasks), 0)
        self.manager.complete_task(1)
        completed_tasks = self.manager.list_completed_tasks()
        self.assertEqual(len(completed_tasks), 1)

if __name__ == "__main__":
    unittest.main()
```

### Version Control

- **Commit Messages**: Use descriptive commit messages that explain what was changed and why.
- **Branching**: Branch from `main` for new features or bug fixes.
- **Pull Requests**: Ensure PRs have green CI before merging.

This module follows the principles of simplicity, clarity, and maintainability, making it easy to understand and extend.