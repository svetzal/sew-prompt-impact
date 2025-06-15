

```python
from enum import Enum
from typing import List, Optional

class TaskStatus(Enum):
    PENDING = "pending"
    DONE = "done"

class Task:
    def __init__(self, description: str):
        self.description = description
        self.status = TaskStatus.PENDING

    def mark_as_done(self):
        self.status = TaskStatus.DONE

    def __repr__(self):
        return f"Task(description={self.description!r}, status={self.status.value})"

class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, description: str) -> Task:
        task = Task(description)
        self.tasks.append(task)
        return task

    def complete_task(self, task: Task) -> None:
        task.mark_as_done()

    def remove_task(self, task: Task) -> None:
        self.tasks.remove(task)

    def get_tasks(self) -> List[Task]:
        return self.tasks

    def get_pending_tasks(self) -> List[Task]:
        return [task for task in self.tasks if task.status == TaskStatus.PENDING]

    def get_done_tasks(self) -> List[Task]:
        return [task for task in self.tasks if task.status == TaskStatus.DONE]
```

---

### 📦 Module Description

This Python module provides a clean and maintainable way to manage a list of tasks. It includes:

- **`Task` class**: Represents an individual task with a description and a status (`pending` or `done`).
- **`TaskManager` class**: Manages the collection of tasks, allowing for adding, completing, removing, and filtering of tasks.

---

### ✅ Key Features

- **Type safety**: Uses `Enum` for task statuses and `List` typing for clarity and correctness.
- **Behavioral methods**: `mark_as_done()` on a task and `complete_task()` in the manager.
- **Flexible querying**:
  - `get_tasks()` for all tasks.
  - `get_pending_tasks()` and `get_done_tasks()` for filtering by status.
- **Simple and readable API**: Each method has a clear purpose, and the `__repr__` method aids debugging.

---

### 🧪 Example Usage

```python
manager = TaskManager()
task1 = manager.add_task("Buy groceries")
task2 = manager.add_task("Walk the dog")

print(manager.get_tasks())  # [Task(description='Buy groceries', status='pending'), Task(description='Walk the dog', status='pending')]

manager.complete_task(task1)
print(task1.status)  # TaskStatus.DONE

print(manager.get_pending_tasks())  # [Task(description='Walk the dog', status='pending')]
print(manager.get_done_tasks())    # [Task(description='Buy groceries', status='done')]
```

---

### 🧩 Design Principles

- **Code is communication**: Clean method names and structure make the intent clear.
- **Minimal entities**: Only necessary classes and methods are defined.
- **No knowledge duplication**: Logic for filtering and managing tasks is centralized in `TaskManager`.
- **Tests as specs**: While not included here, this design enables easy testing with `pytest` or `unittest`.

This module adheres to the principles of functional core, imperative shell, and test-driven design. It’s ready for extension (e.g., adding task IDs or persistence) without compromising clarity or correctness.