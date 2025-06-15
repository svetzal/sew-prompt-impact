Creating a Python module to manage a list of tasks involves defining a class or set of functions that can add, remove, update, and display tasks. Below is a simple example of a Python module named `task_manager.py`:

```python
# task_manager.py

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        """Add a task to the task list."""
        task = {
            'description': description,
            'completed': False
        }
        self.tasks.append(task)
        print(f"Added task: {description}")

    def remove_task(self, index):
        """Remove a task from the task list by index."""
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Removed task: {removed_task['description']}")
        else:
            print(f"Task index {index} is out of range.")

    def update_task(self, index, description=None, completed=None):
        """Update a task's description or completed status."""
        if 0 <= index < len(self.tasks):
            if description is not None:
                self.tasks[index]['description'] = description
                print(f"Updated task description to: {description}")
            if completed is not None:
                self.tasks[index]['completed'] = completed
                print(f"Updated task completion status to: {completed}")
        else:
            print(f"Task index {index} is out of range.")

    def list_tasks(self):
        """List all tasks with their statuses."""
        if not self.tasks:
            print("No tasks available.")
            return

        for idx, task in enumerate(self.tasks, start=1):
            status = 'Completed' if task['completed'] else 'Pending'
            print(f"{idx}. {task['description']} - {status}")

    def complete_task(self, index):
        """Mark a specific task as completed."""
        self.update_task(index, completed=True)
```

### How to Use the Module

1. **Initialize the Task Manager:**

```python
from task_manager import TaskManager

tm = TaskManager()
```

2. **Add a Task:**

```python
tm.add_task("Buy groceries")
tm.add_task("Clean the house")
```

3. **List Tasks:**

```python
tm.list_tasks()
```

4. **Update a Task:**

```python
tm.update_task(0, description="Buy groceries and cook dinner")
```

5. **Complete a Task:**

```python
tm.complete_task(0)
```

6. **Remove a Task:**

```python
tm.remove_task(1)
```

### Notes

- The `tasks` list holds dictionaries, each representing a task with a `description` and `completed` status.
- The `index` for `remove_task`, `update_task`, and `complete_task` is zero-based internally, but can easily be adjusted if preferred.
- This module provides a basic framework and can be expanded with features such as task priorities, deadlines, or persistence through file operations or a database.