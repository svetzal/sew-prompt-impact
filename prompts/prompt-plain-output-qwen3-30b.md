

```python
class TaskManager:
    """
    A class to manage a list of tasks.

    Attributes:
        tasks (list): A list of dictionaries representing each task.
    """

    def __init__(self):
        """
        Initialize an empty list of tasks.
        """
        self.tasks = []

    def add_task(self, description):
        """
        Add a new task to the list.

        Args:
            description (str): The description of the task.
        """
        self.tasks.append({'description': description, 'completed': False})

    def remove_task(self, index):
        """
        Remove a task from the list by index.

        Args:
            index (int): The index of the task to remove.

        Raises:
            IndexError: If the index is out of range.
        """
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            raise IndexError("Task index out of range")

    def complete_task(self, index):
        """
        Mark a task as completed by index.

        Args:
            index (int): The index of the task to mark as completed.

        Raises:
            IndexError: If the index is out of range.
        """
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
        else:
            raise IndexError("Task index out of range")

    def list_tasks(self):
        """
        List all tasks with their status.
        """
        for i, task in enumerate(self.tasks):
            status = 'X' if task['completed'] else ' '
            print(f"{i}: [{status}] {task['description']}")
```

---

### ✅ Example Usage

You can use this module in your Python scripts like so:

```python
from task_manager import TaskManager

# Initialize the task manager
tm = TaskManager()

# Add some tasks
tm.add_task("Buy groceries")
tm.add_task("Finish project report")
tm.add_task("Call mom")

# List all tasks
print("Current Tasks:")
tm.list_tasks()

# Mark a task as completed
tm.complete_task(0)

# List tasks again
print("\nAfter completing one task:")
tm.list_tasks()

# Remove a task
tm.remove_task(1)

# Final list
print("\nAfter removing one task:")
tm.list_tasks()
```

---

### 🧩 Features

- **Add Tasks**: Easily add new tasks to the list.
- **Remove Tasks**: Remove a task by its index.
- **Mark as Completed**: Toggle the completion status of a task by its index.
- **List Tasks**: View the current list of tasks with their status (completed or pending).

This module provides a clean, reusable way to manage a list of tasks with simple and intuitive methods.