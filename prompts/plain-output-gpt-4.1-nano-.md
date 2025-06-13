Sure! Here's a simple Python module called `task_manager.py` that allows you to manage a list of tasks. It supports adding tasks, removing tasks, listing all tasks, and saving/loading tasks to/from a file.

```python
# task_manager.py

import json
import os

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        """Add a new task to the list."""
        self.tasks.append(task)
        print(f"Added task: {task}")

    def remove_task(self, task):
        """Remove a task from the list."""
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Removed task: {task}")
        else:
            print(f"Task not found: {task}")

    def list_tasks(self):
        """Print all tasks."""
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Your tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def save_tasks(self):
        """Save tasks to a JSON file."""
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.tasks, f)
            print("Tasks saved.")
        except IOError as e:
            print(f"Error saving tasks: {e}")

    def load_tasks(self):
        """Load tasks from a JSON file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    self.tasks = json.load(f)
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error loading tasks: {e}")
                self.tasks = []
        else:
            self.tasks = []

# Example usage (uncomment for testing)
# if __name__ == "__main__":
#     tm = TaskManager()
#     tm.add_task("Buy groceries")
#     tm.add_task("Finish project")
#     tm.list_tasks()
#     tm.save_tasks()
```

### How to use the module:
1. Save this code in a file named `task_manager.py`.
2. In your Python script or interactive session, import the `TaskManager` class:
```python
from task_manager import TaskManager

tm = TaskManager()

# Add tasks
tm.add_task("Read a book")
tm.add_task("Exercise")

# List tasks
tm.list_tasks()

# Remove a task
tm.remove_task("Read a book")

# Save tasks to file
tm.save_tasks()
```

This module provides basic functionality to manage your tasks. Feel free to extend it with features like task prioritization, deadlines, or a CLI interface!