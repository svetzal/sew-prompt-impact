Sure! Below is a simple Python module named `task_manager.py` that can help you manage a list of tasks. This module includes functionalities to add, remove, view, and update tasks.

```python
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the list."""
        if task not in self.tasks:
            self.tasks.append(task)
            print(f"Task '{task}' added.")
        else:
            print(f"Task '{task}' already exists.")

    def remove_task(self, task):
        """Remove a task from the list."""
        try:
            self.tasks.remove(task)
            print(f"Task '{task}' removed.")
        except ValueError:
            print(f"Task '{task}' not found.")

    def update_task(self, old_task, new_task):
        """Update an existing task."""
        if old_task in self.tasks:
            index = self.tasks.index(old_task)
            self.tasks[index] = new_task
            print(f"Task '{old_task}' updated to '{new_task}'.")
        else:
            print(f"Task '{old_task}' not found.")

    def view_tasks(self):
        """View all tasks."""
        if self.tasks:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks to display.")

# Example usage
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Buy groceries")
    manager.add_task("Read a book")
    manager.view_tasks()
    manager.update_task("Read a book", "Finish the report")
    manager.remove_task("Buy groceries")
    manager.view_tasks()
```

### Explanation:

1. **Initialization**: The `TaskManager` class initializes with an empty list of tasks.
2. **Add Task**: The `add_task` method adds a new task to the list if it doesn't already exist.
3. **Remove Task**: The `remove_task` method removes a specified task from the list.
4. **Update Task**: The `update_task` method updates an existing task with a new one.
5. **View Tasks**: The `view_tasks` method prints all tasks in the list.

### Usage:

- To use this module, you can create an instance of `TaskManager` and call its methods to manage your tasks.
- The example usage at the bottom shows how to add, view, update, and remove tasks.

You can expand this module by adding more features such as saving tasks to a file, loading tasks from a file, or setting priorities for tasks.