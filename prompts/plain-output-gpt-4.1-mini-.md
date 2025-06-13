Sure! Here's a simple Python module named `task_manager.py` that you can use to manage a list of tasks. It includes basic functionalities such as adding tasks, removing tasks, listing all tasks, and marking tasks as completed.

```python
# task_manager.py

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, description):
        """Add a new task with the given description."""
        task = {"description": description, "completed": False}
        self.tasks.append(task)
        print(f"Task added: '{description}'")
    
    def remove_task(self, index):
        """Remove a task by its index (0-based)."""
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"Removed task: '{removed['description']}'")
        else:
            print(f"Error: No task found at index {index}.")
    
    def complete_task(self, index):
        """Mark a task as completed by its index (0-based)."""
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print(f"Task completed: '{self.tasks[index]['description']}'")
        else:
            print(f"Error: No task found at index {index}.")
    
    def list_tasks(self):
        """Print all tasks with their status."""
        if not self.tasks:
            print("No tasks available.")
            return
        
        for i, task in enumerate(self.tasks):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. [{status}] {task['description']}")
    
    def get_tasks(self):
        """Return the list of tasks."""
        return self.tasks
```

### How to use

Example usage after importing:

```python
from task_manager import TaskManager

tm = TaskManager()
tm.add_task("Write unit tests")
tm.add_task("Review pull requests")
tm.list_tasks()

tm.complete_task(0)
tm.list_tasks()

tm.remove_task(1)
tm.list_tasks()
```

Let me know if you'd like the module to support saving/loading tasks from a file or other features!