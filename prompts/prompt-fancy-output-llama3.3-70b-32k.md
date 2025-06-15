**Task Manager Module**
========================

### Overview

This module provides a simple task management system, allowing users to create, read, update, and delete (CRUD) tasks.

### Installation

To use this module, you'll need Python 3.8 or later installed on your system. Additionally, you'll need to install the `pydantic` library for data validation. You can do this using pip:

```bash
pip install pydantic
```

### Code

**tasks.py**
```python
from pydantic import BaseModel
from typing import List, Optional
import uuid

class Task(BaseModel):
    """Represents a single task."""
    id: str = None
    title: str
    description: Optional[str] = None
    completed: bool = False

    def __init__(self, **kwargs):
        if not kwargs.get('id'):
            kwargs['id'] = str(uuid.uuid4())
        super().__init__(**kwargs)

class TaskManager:
    """Manages a list of tasks."""
    def __init__(self):
        self.tasks: List[Task] = []

    def create_task(self, title: str, description: Optional[str] = None) -> Task:
        """Creates a new task and adds it to the list."""
        task = Task(title=title, description=description)
        self.tasks.append(task)
        return task

    def get_tasks(self) -> List[Task]:
        """Returns the list of tasks."""
        return self.tasks

    def get_task(self, id: str) -> Optional[Task]:
        """Returns a task by its ID, or None if not found."""
        for task in self.tasks:
            if task.id == id:
                return task
        return None

    def update_task(self, id: str, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """Updates a task by its ID. Returns True if updated, False if not found."""
        for task in self.tasks:
            if task.id == id:
                if title:
                    task.title = title
                if description is not None:
                    task.description = description
                return True
        return False

    def delete_task(self, id: str) -> bool:
        """Deletes a task by its ID. Returns True if deleted, False if not found."""
        for i, task in enumerate(self.tasks):
            if task.id == id:
                del self.tasks[i]
                return True
        return False

def main():
    # Example usage:
    manager = TaskManager()
    task1 = manager.create_task("Buy milk")
    print(task1)
    tasks = manager.get_tasks()
    for task in tasks:
        print(task)

if __name__ == "__main__":
    main()
```

### Usage

To use this module, simply import the `TaskManager` class and create an instance. You can then use the various methods to manage your list of tasks.

**Example:**

```python
from tasks import TaskManager

manager = TaskManager()
task1 = manager.create_task("Buy milk")
print(task1)
tasks = manager.get_tasks()
for task in tasks:
    print(task)
```

This will create a new task, add it to the list, and then print out all tasks in the list.

### Tests

To ensure this module is working correctly, you can write tests using the `unittest` framework. Here's an example:

**tests.py**
```python
import unittest
from tasks import TaskManager, Task

class TestTaskManager(unittest.TestCase):
    def test_create_task(self):
        manager = TaskManager()
        task = manager.create_task("Buy milk")
        self.assertIsInstance(task, Task)
        self.assertEqual(task.title, "Buy milk")

    def test_get_tasks(self):
        manager = TaskManager()
        task1 = manager.create_task("Buy milk")
        task2 = manager.create_task("Walk dog")
        tasks = manager.get_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertIn(task1, tasks)
        self.assertIn(task2, tasks)

    def test_get_task(self):
        manager = TaskManager()
        task = manager.create_task("Buy milk")
        retrieved_task = manager.get_task(task.id)
        self.assertEqual(retrieved_task, task)

if __name__ == "__main__":
    unittest.main()
```

You can run these tests using the `unittest` command:

```bash
python -m unittest discover -s . -p 'tests.py'
```