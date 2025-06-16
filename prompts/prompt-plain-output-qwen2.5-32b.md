Sure! I'll create a simple Python module to help you manage a list of tasks. This module will allow you to add tasks, remove them by name or index, mark tasks as complete, and display the current list of tasks.

Let's get started:

1. Create a new file named `task_manager.py`.

2. Define functions in this file to handle adding tasks, removing tasks, marking tasks as completed, and displaying all tasks.

3. Save it in your desired directory.

Here is the content for `task_manager.py`:

```python
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        """Adds a new task to the list."""
        if not isinstance(task_name, str) or task_name.strip() == "":
            raise ValueError("Task name must be a non-empty string.")
        
        if any(t["name"] == task_name for t in self.tasks):
            print(f"Warning: Task '{task_name}' already exists.")
        else:
            self.tasks.append({"name": task_name, "completed": False})
            print(f"Task added: {task_name}")

    def remove_task(self, task_id=None, task_name=None):
        """Removes a task by its index or name."""
        if task_id is not None and 0 <= task_id < len(self.tasks):
            removed_task = self.tasks.pop(task_id)
            print(f"Task removed: {removed_task['name']}")
        elif task_name:
            for idx, task in enumerate(self.tasks):
                if task["name"] == task_name:
                    removed_task = self.tasks.pop(idx)
                    print(f"Task removed: {task_name}")
                    break
            else:
                print(f"Task '{task_name}' not found.")
        else:
            print("Invalid index or name provided.")

    def mark_completed(self, task_id=None, task_name=None):
        """Marks a task as completed by its index or name."""
        if task_id is not None and 0 <= task_id < len(self.tasks):
            self.tasks[task_id]["completed"] = True
            print(f"Marked as completed: {self.tasks[task_id]['name']}")
        elif task_name:
            for task in self.tasks:
                if task["name"] == task_name:
                    task["completed"] = True
                    print(f"Marked as completed: {task_name}")
                    break
            else:
                print(f"Task '{task_name}' not found.")
        else:
            print("Invalid index or name provided.")

    def list_tasks(self):
        """Lists all tasks in the manager."""
        if not self.tasks:
            print("No tasks to show.")
        for idx, task in enumerate(self.tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{idx}. {task['name']} - {status}")

# Example usage
if __name__ == "__main__":
    manager = TaskManager()
    
    # Add tasks
    manager.add_task("Buy groceries")
    manager.add_task("Read a book")

    # List tasks
    manager.list_tasks()

    # Mark a task as completed by name
    manager.mark_completed(task_name="Buy groceries")

    # Remove a task by index
    manager.remove_task(task_id=1)

    # List tasks again
    manager.list_tasks()
```

To use this module in another Python script or interactive session, you can import it and create an instance of `TaskManager`, then call its methods to manage your tasks.

Example:

```python
from task_manager import TaskManager

manager = TaskManager()
manager.add_task("Finish the project")
manager.mark_completed(task_id=0)
manager.list_tasks()
```

This module is quite basic but provides a good foundation for managing tasks. You can extend it further with more features or customizations as needed!