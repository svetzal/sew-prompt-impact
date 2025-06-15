Sure! I'll create a Python module for you that can help manage a list of tasks. This module will include functions to add, remove, and display tasks. Let's name this module `task_manager.py`.

Here’s the content of `task_manager.py`:

```python
# task_manager.py

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description):
        """Add a new task to the list."""
        if not task_description:
            return "Task cannot be empty."
        
        # Ensure no duplicate tasks are added.
        for existing_task in self.tasks:
            if existing_task['description'] == task_description:
                return f"Task '{task_description}' already exists."

        task = {'description': task_description, 'completed': False}
        self.tasks.append(task)
        return "Task added successfully!"

    def remove_task(self, task_index):
        """Remove a specific task from the list."""
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            return f"Removed: {removed_task['description']}"
        else:
            return "Invalid index. Task not found."

    def complete_task(self, task_index):
        """Mark a specific task as completed."""
        if 0 <= task_index < len(self.tasks) and not self.tasks[task_index]['completed']:
            self.tasks[task_index]['completed'] = True
            return f"Task '{self.tasks[task_index]['description']}' marked as complete."
        else:
            return "Invalid index or already completed."

    def list_tasks(self):
        """List all tasks, indicating which ones are completed."""
        if not self.tasks:
            return "No tasks found!"
        
        task_list = []
        for i, task in enumerate(self.tasks):
            status = "[x]" if task['completed'] else "[ ]"
            task_list.append(f"{i}. {status} {task['description']}")
        
        return '\n'.join(task_list)


# Example usage:
if __name__ == "__main__":
    tm = TaskManager()
    
    print(tm.add_task("Buy groceries"))
    print(tm.add_task("Finish homework"))
    print(tm.list_tasks())
    print(tm.complete_task(0))
    print(tm.remove_task(1))
    print(tm.list_tasks())
```

To use the module, you can import it into another Python script or run this script directly. Here's an example of how to interact with the `TaskManager` class:

```python
from task_manager import TaskManager

# Initialize a TaskManager instance.
tm = TaskManager()

# Adding tasks
print(tm.add_task("Learn Python"))
print(tm.add_task("Read a book"))

# Displaying all tasks
print("\nCurrent Tasks:")
print(tm.list_tasks())

# Marking a task as completed
print(tm.complete_task(0))

# Removing a task
print(tm.remove_task(1))

# Final display of tasks after completing and removing some tasks.
print("\nFinal Tasks:")
print(tm.list_tasks())
```

This module provides a simple yet effective way to manage tasks. You can expand it further based on your needs, such as adding features for editing tasks or saving/loading task lists from files.