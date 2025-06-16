Certainly! Below is an example of how you might create a simple Python module to manage a list of tasks.

```python
# task_manager.py

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task."""
        self.tasks.append(task)
        print(f"Task added: {task}")

    def remove_task(self, task_id):
        """Remove a task by its index (0-based)."""
        if 0 <= task_id < len(self.tasks):
            removed_task = self.tasks.pop(task_id)
            print(f"Task removed: {removed_task}")
        else:
            print("Invalid task ID")

    def get_all_tasks(self):
        """Return all tasks."""
        return self.tasks

    def mark_task_as_completed(self, task_id):
        """Mark a task as completed (replace with task description and 'completed')."""
        if 0 <= task_id < len(self.tasks):
            self.tasks[task_id] = f"{self.tasks[task_id]} - Completed"
            print(f"Task marked as completed: {self.tasks[task_id]}")
        else:
            print("Invalid task ID")

    def display_tasks(self):
        """Display all tasks with their status."""
        for index, task in enumerate(self.tasks):
            status = "Completed" if "- Completed" in task else "Pending"
            print(f"{index}: {task} ({status})")


# Usage example
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Read a book")
    manager.add_task("Write code")
    manager.display_tasks()
    manager.mark_task_as_completed(1)
    manager.display_tasks()
```

### Explanation:

- `TaskManager` is a class that manages the list of tasks.
- **`__init__()`**: Initializes an empty list to store tasks.
- **`add_task(task)`**: Adds a new task to the list and prints confirmation.
- **`remove_task(task_id)`**: Removes a task by its index and prints confirmation. If the task ID is invalid, it informs the user.
- **`get_all_tasks()`**: Returns all tasks in the list.
- **`mark_task_as_completed(task_id)`**: Marks a task as completed by replacing the task description with "task - Completed".
- **`display_tasks()`**: Displays all tasks along with their status (completed or pending).

### Usage:
You can use this module in your Python script like this:

```python
from task_manager import TaskManager

manager = TaskManager()
manager.add_task("Read a book")
manager.add_task("Write code")
manager.display_tasks()
manager.mark_task_as_completed(1)
manager.display_tasks()
```

This example shows how to create, manipulate, and display tasks in the `TaskManager` class. You can expand this module based on your needs, such as adding task prioritization, filtering tasks by status, or storing tasks persistently using databases like SQLite.