Certainly! Based on the Baseline Conventions and Universal Engineering Principles, I'll create a Python module that manages a list of tasks with clean, simple, and testable code.

Here's the plan:
- Define a `Task` data class.
- Create a `TaskManager` class for managing tasks.
- Include functions for adding, removing, listing tasks.
- Write tests to verify behavior.

Let's start with the core module:

```python
# tasks.py

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Task:
    id: int
    description: str
    completed: bool = False


class TaskManager:
    def __init__(self):
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def add_task(self, description: str) -> Task:
        new_task = Task(id=self._next_id, description=description)
        self._tasks.append(new_task)
        self._next_id += 1
        return new_task

    def remove_task(self, task_id: int) -> bool:
        for i, task in enumerate(self._tasks):
            if task.id == task_id:
                del self._tasks[i]
                return True
        return False

    def list_tasks(self, include_completed: bool = True) -> List[Task]:
        if include_completed:
            return list(self._tasks)
        return [task for task in self._tasks if not task.completed]

    def mark_complete(self, task_id: int) -> bool:
        for task in self._tasks:
            if task.id == task_id:
                task.completed = True
                return True
        return False

    def get_task(self, task_id: int) -> Optional[Task]:
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None
```

Next, write some tests to serve as executable specifications:

```python
# test_tasks.py

import unittest
from tasks import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Write unit tests")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Write unit tests")
        self.assertFalse(task.completed)

    def test_list_tasks(self):
        self.manager.add_task("Task 1")
        self.manager.add_task("Task 2")
        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 2)

    def test_mark_complete(self):
        task = self.manager.add_task("Complete this task")
        result = self.manager.mark_complete(task.id)
        self.assertTrue(result)
        self.assertTrue(self.manager.get_task(task.id).completed)

    def test_remove_task(self):
        task = self.manager.add_task("Task to remove")
        result = self.manager.remove_task(task.id)
        self.assertTrue(result)
        self.assertIsNone(self.manager.get_task(task.id))
        # Removing non-existent task
        self.assertFalse(self.manager.remove_task(999))

    def test_list_tasks_excludes_completed(self):
        t1 = self.manager.add_task("Active task")
        t2 = self.manager.add_task("Completed task")
        self.manager.mark_complete(t2.id)
        tasks = self.manager.list_tasks(include_completed=False)
        self.assertIn(t1, tasks)
        self.assertNotIn(t2, tasks)

if __name__ == "__main__":
    unittest.main()
```

This code:
- Is simple and clear, demonstrating intent.
- Avoids duplication by reusing methods.
- Follows incremental development: easy to extend and modify.
- Uses tests as an executable specification to ensure correctness.

Would you like me to package this as a module with an entry point or provide usage examples?