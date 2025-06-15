

```python
class TaskManager:
    """
    A class to manage a list of tasks.
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

    def complete_task(self, index):
        """
        Mark a task as completed.

        Args:
            index (int): The index of the task to mark as completed.

        Raises:
            IndexError: If the index is out of range.
        """
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
        else:
            raise IndexError("Task index out of range")

    def delete_task(self, index):
        """
        Delete a task from the list.

        Args:
            index (int): The index of the task to delete.

        Raises:
            IndexError: If the index is out of range.
        """
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            raise IndexError("Task index out of range")

    def list_tasks(self):
        """
        List all tasks with their status.
        """
        for i, task in enumerate(self.tasks):
            status = "Done" if task['completed'] else "Pending"
            print(f"{i}: {task['description']} - {status}")

    def get_tasks(self):
        """
        Return the list of tasks.

        Returns:
            list: A list of dictionaries representing tasks.
        """
        return self.tasks
```

---

### ✅ Usage Example

You can use the `TaskManager` module like this:

```python
from task_manager import TaskManager

tm = TaskManager()
tm.add_task("Buy groceries")
tm.add_task("Walk the dog")
tm.list_tasks()

# Output:
# 0: Buy groceries - Pending
# 1: Walk the dog - Pending

tm.complete_task(0)
tm.list_tasks()

# Output:
# 0: Buy groceries - Done
# 1: Walk the dog - Pending

tm.delete_task(1)
tm.list_tasks()

# Output:
# 0: Buy groceries - Done
```

This module provides a clean and intuitive way to manage a list of tasks, with core operations like adding, completing, deleting, and viewing tasks.