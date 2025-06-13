Certainly! Below is a simple Python module that manages a list of tasks. This module will allow you to add tasks, mark them as completed, remove tasks, and list all tasks.

### `task_manager.py`

```python
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description):
        """Add a new task to the list."""
        task = {
            'description': task_description,
            'completed': False
        }
        self.tasks.append(task)
        return f"Task added: {task_description}"

    def mark_completed(self, index):
        """Mark a task as completed by its index."""
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
            return f"Task marked as completed: {self.tasks[index]['description']}"
        else:
            return "Invalid task index"

    def remove_task(self, index):
        """Remove a task by its index."""
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            return f"Task removed: {removed_task['description']}"
        else:
            return "Invalid task index"

    def list_tasks(self):
        """List all tasks with their status."""
        if not self.tasks:
            return "No tasks available"
        
        task_list = []
        for i, task in enumerate(self.tasks):
            status = "Completed" if task['completed'] else "Not Completed"
            task_list.append(f"{i}: {task['description']} - {status}")
        
        return "\n".join(task_list)

# Example usage
if __name__ == "__main__":
    manager = TaskManager()
    
    print(manager.add_task("Buy groceries"))
    print(manager.add_task("Read a book"))
    print(manager.add_task("Write a report"))
    
    print("\nList of tasks:")
    print(manager.list_tasks())
    
    print("\nMarking task 1 as completed")
    print(manager.mark_completed(1))
    
    print("\nList of tasks after marking one as completed:")
    print(manager.list_tasks())
    
    print("\nRemoving task 0")
    print(manager.remove_task(0))
    
    print("\nFinal list of tasks:")
    print(manager.list_tasks())
```

### Explanation:

- **TaskManager Class**: This class manages the list of tasks.
  - `__init__`: Initializes an empty list to store tasks.
  - `add_task`: Adds a new task with a description and sets it as not completed by default.
  - `mark_completed`: Marks a task as completed based on its index.
  - `remove_task`: Removes a task based on its index.
  - `list_tasks`: Lists all tasks along with their completion status.

### Example Usage:

When you run the script, it will create a `TaskManager` instance and demonstrate adding tasks, marking them as completed, removing tasks, and listing all tasks.

You can save this code in a file named `task_manager.py` and import it into other Python scripts or use it directly as shown in the example usage.