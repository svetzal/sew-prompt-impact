Certainly! Below is a simple Python module to manage a list of tasks. This module provides functionality to add, remove, update, and list tasks. 

Let's create a file named `task_manager.py`:

```python
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description):
        """Add a new task to the list."""
        if not task_description:
            raise ValueError("Task description cannot be empty.")
        task_id = len(self.tasks) + 1
        self.tasks.append({'id': task_id, 'description': task_description})
        print(f"Task added: {task_description}")

    def remove_task(self, task_id):
        """Remove a task from the list by its ID."""
        for index, task in enumerate(self.tasks):
            if task['id'] == task_id:
                removed_task = self.tasks.pop(index)
                print(f"Task removed: {removed_task['description']}")
                return
        raise ValueError("Task ID not found.")

    def update_task(self, task_id, new_description):
        """Update the description of a task by its ID."""
        for task in self.tasks:
            if task['id'] == task_id:
                task['description'] = new_description
                print(f"Task updated. New description: {new_description}")
                return
        raise ValueError("Task ID not found.")

    def list_tasks(self):
        """List all tasks with their IDs."""
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(f"ID: {task['id']}, Description: {task['description']}")

# Example usage
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Buy groceries")
    manager.add_task("Read a book")
    manager.list_tasks()
    manager.update_task(1, "Buy groceries and cook dinner")
    manager.remove_task(2)
    manager.list_tasks()
```

### Explanation:

- **TaskManager Class**: This class manages the tasks. It has an internal list `tasks` to store task data.
  
- **add_task(task_description)**: Adds a new task with a given description.

- **remove_task(task_id)**: Removes a task based on its ID.

- **update_task(task_id, new_description)**: Updates the description of a task specified by its ID.

- **list_tasks()**: Lists all tasks currently in the manager along with their IDs.

### Example Usage:

When you run this module directly (`python task_manager.py`), it demonstrates how to use the `TaskManager` class. You can add tasks, list them, update an existing task, and remove a task.

Feel free to modify or extend this module as per your requirements!