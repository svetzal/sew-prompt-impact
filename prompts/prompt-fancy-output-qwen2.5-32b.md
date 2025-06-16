Sure! Let's create a Python module to manage a list of tasks. This will include adding, removing, and listing tasks. We'll also add tests to ensure our implementation is correct.

Here’s how the structure could look:
- `task_manager.py`: The main module where task management logic resides.
- `tests/test_task_manager.py`: Tests for verifying the functionality of the task manager.

### Step 1: Define the Task Manager

Let's start with defining a basic structure and functionalities:

```python
# task_manager.py

from typing import List, Optional


class TaskManager:
    def __init__(self):
        self.tasks: List[str] = []

    def add_task(self, task: str) -> None:
        """Adds a new task to the manager."""
        if not isinstance(task, str) or task.strip() == "":
            raise ValueError("Task must be a non-empty string.")
        self.tasks.append(task)

    def remove_task(self, task: str) -> Optional[str]:
        """Removes a specified task from the manager and returns it. If the task is not found, return None."""
        if task in self.tasks:
            self.tasks.remove(task)
            return task
        else:
            return None

    def list_tasks(self) -> List[str]:
        """Returns a list of all tasks managed by this instance."""
        return self.tasks[:]
```

### Step 2: Add Type Checks with mypy and Tests with pytest

Next, let's add tests to ensure our `TaskManager` behaves as expected:

```python
# tests/test_task_manager.py

from task_manager import TaskManager


def test_add_and_list_tasks():
    tm = TaskManager()
    tasks_to_add = ["Write blog post", "Fix bugs"]
    
    for task in tasks_to_add:
        tm.add_task(task)

    assert tm.list_tasks() == tasks_to_add
    assert len(tm.tasks) == 2

def test_remove_existing_task():
    tm = TaskManager()
    tm.add_task("Finish coding")
    tm.remove_task("Finish coding")

    assert "Finish coding" not in tm.tasks

def test_remove_nonexistent_task():
    tm = TaskManager()
    result = tm.remove_task("Read book")

    assert result is None
```

### Step 3: Setup `mypy` and Run Tests

To enforce type checking with mypy, add a configuration file `.mypy.ini`:

```ini
[mypy]
strict=True
plugins=task_manager.py
```

And to run the tests using `pytest`, you can install pytest (`pip install pytest`) if not already installed, then simply use:
```bash
pytest -v tests/
```

### Step 4: Formatting and Linting with black and flake8

Finally, ensure that your code is properly formatted and lints correctly by installing `black` and `flake8`:

```bash
pip install black flake8
```

Run the following commands to automatically format your files and check for lint issues:
```bash
black .
flake8 task_manager.py tests/test_task_manager.py
```

These steps will help ensure that your code follows good practices, is well-structured, and includes comprehensive testing.