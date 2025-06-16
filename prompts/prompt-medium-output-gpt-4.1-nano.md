Certainly! Based on the Baseline Conventions you've shared, I'll create a Python module that manages a list of tasks with a focus on clarity, simplicity, and testability. I'll structure the code with a pure functional core and minimal side-effects, include clear function names, and write accompanying tests.

Here's the plan:

- A `Task` data class to represent individual tasks.
- Pure functions to add, remove, toggle, and list tasks.
- An in-memory list as the task storage.
- Tests to serve as executable specifications.

Let's proceed step-by-step.

---

### Tasks Module (`tasks.py`)

```python
from dataclasses import dataclass
from typing import List, Tuple

@dataclass(frozen=True)
class Task:
    id: int
    description: str
    completed: bool = False

def add_task(tasks: List[Task], description: str, next_id: int) -> Tuple[List[Task], int]:
    """
    Add a new task to the task list.
    Returns the new list and the next task ID.
    """
    new_task = Task(id=next_id, description=description)
    return tasks + [new_task], next_id + 1

def remove_task(tasks: List[Task], task_id: int) -> List[Task]:
    """
    Remove a task by ID.
    """
    return [task for task in tasks if task.id != task_id]

def toggle_task_completion(tasks: List[Task], task_id: int) -> List[Task]:
    """
    Toggle the completion status of a task.
    """
    def toggle(task: Task) -> Task:
        if task.id == task_id:
            return Task(id=task.id, description=task.description, completed=not task.completed)
        return task

    return [toggle(task) for task in tasks]

def list_tasks(tasks: List[Task]) -> List[Task]:
    """
    Return the current list of tasks.
    """
    return tasks
```

---

### Tests (`test_tasks.py`)

```python
import unittest
from tasks import Task, add_task, remove_task, toggle_task_completion, list_tasks

class TestTaskFunctions(unittest.TestCase):
    def setUp(self):
        # Initial task list and ID
        self.tasks = []
        self.next_id = 1

    def test_add_task(self):
        tasks, next_id = add_task(self.tasks, "Write tests", self.next_id)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].description, "Write tests")
        self.assertFalse(tasks[0].completed)
        self.assertEqual(next_id, 2)

    def test_remove_task(self):
        tasks, next_id = add_task(self.tasks, "Write tests", self.next_id)
        tasks = add_task(tasks, "Fix bugs", next_id)[0]
        tasks = remove_task(tasks, task_id=1)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].description, "Fix bugs")
        self.assertEqual(tasks[0].id, 2)

    def test_toggle_task_completion(self):
        tasks, next_id = add_task(self.tasks, "Write code", self.next_id)
        tasks = toggle_task_completion(tasks, task_id=1)
        self.assertTrue(tasks[0].completed)
        tasks = toggle_task_completion(tasks, task_id=1)
        self.assertFalse(tasks[0].completed)

    def test_list_tasks(self):
        tasks, next_id = add_task(self.tasks, "Task 1", self.next_id)
        result = list_tasks(tasks)
        self.assertEqual(result, tasks)

if __name__ == '__main__':
    unittest.main()
```

---

### Summary

- The **production code** maintains a pure functional style with immutable `Task` instances.
- The **test code** explicitly tests each operation, serving as an executable spec.
- We're following the conventions: simple, clear, testable, and focused on readability.

Would you like me to package this into a ready-to-run directory structure or extend functionality further?