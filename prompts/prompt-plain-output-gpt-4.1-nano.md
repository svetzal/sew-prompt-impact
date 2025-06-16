Certainly! Here's a simple Python module named `task_manager.py` that allows you to manage a list of tasks. It includes functionalities to add, remove, list, and mark tasks as completed.

```python
# task_manager.py

from typing import List, Dict

class Task:
    def __init__(self, description: str):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"

class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, description: str):
        """Add a new task to the list."""
        self.tasks.append(Task(description))
        print(f"Added task: '{description}'")

    def remove_task(self, index: int):
        """Remove a task by its index (0-based)."""
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Removed task: '{removed_task.description}'")
        else:
            print("Invalid task index.")

    def list_tasks(self):
        """Display all tasks with their status."""
        if not self.tasks:
            print("No tasks to display.")
            return
        for idx, task in enumerate(self.tasks):
            print(f"{idx}. {task}")

    def complete_task(self, index: int):
        """Mark a task as completed."""
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print(f"Marked task {index} as completed.")
        else:
            print("Invalid task index.")

# Example usage:
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Write unit tests")
    manager.add_task("Update documentation")
    manager.list_tasks()
    manager.complete_task(0)
    manager.list_tasks()
    manager.remove_task(1)
    manager.list_tasks()
```

### How to use this module:

1. Save the code above in a file named `task_manager.py`.
2. You can run it directly to see example usage, or import the `TaskManager` class into other scripts.

### Example in a separate script:

```python
from task_manager import TaskManager

manager = TaskManager()
manager.add_task("Finish project report")
manager.add_task("Call Alice")
manager.list_tasks()
manager.complete_task(1)
manager.list_tasks()
```

Feel free to extend features such as saving/loading tasks from a file, assigning priorities, or adding due dates!