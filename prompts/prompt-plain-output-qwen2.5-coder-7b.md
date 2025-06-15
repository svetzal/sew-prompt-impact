Sure! Below is a simple Python module for managing a list of tasks. This module includes basic functionalities such as adding tasks, removing tasks, and listing all tasks.

```python
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description):
        """
        Adds a new task to the list.
        
        :param task_description: str, description of the task
        """
        if not task_description.strip():
            raise ValueError("Task description cannot be empty")
        self.tasks.append(task_description)
        print(f"Task added: {task_description}")

    def remove_task(self, task_index):
        """
        Removes a task from the list by its index.
        
        :param task_index: int, index of the task to remove
        """
        if not self.tasks:
            raise ValueError("No tasks to remove")
        if task_index < 0 or task_index >= len(self.tasks):
            raise IndexError("Invalid task index")
        removed_task = self.tasks.pop(task_index)
        print(f"Task removed: {removed_task}")

    def list_tasks(self):
        """
        Lists all the tasks.
        
        :return: list, list of all tasks
        """
        if not self.tasks:
            return []
        for index, task in enumerate(self.tasks):
            print(f"{index}: {task}")
        return self.tasks

# Example usage:
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Read a book")
    manager.add_task("Go for a run")
    manager.list_tasks()
    manager.remove_task(0)
    manager.list_tasks()
```

### Explanation:

1. **TaskManager Class**:
   - `__init__`: Initializes an empty list to store tasks.
   - `add_task`: Adds a new task to the list after validating that the description is not empty.
   - `remove_task`: Removes a task by its index, ensuring the index is valid.
   - `list_tasks`: Lists all tasks and returns them as a list.

2. **Example Usage**:
   - Demonstrates adding, listing, and removing tasks using the `TaskManager` class.

You can further extend this module by adding features such as updating tasks, marking tasks as completed, or saving/loading tasks from a file.