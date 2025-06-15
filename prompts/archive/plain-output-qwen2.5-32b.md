Certainly! Below is an example of a simple Python module named `task_manager` which you can use to manage a list of tasks. This module will include functionalities to add, remove, and list tasks.

### task_manager.py

```python
class TaskManager:
    def __init__(self):
        """Initialize the task manager with an empty list."""
        self.tasks = []

    def add_task(self, task_description: str) -> None:
        """
        Add a new task to the task list.
        
        :param task_description: Description of the task.
        """
        if not task_description.strip():
            raise ValueError("Task description cannot be empty or just whitespace.")
        
        self.tasks.append(task_description)
        print(f"Added task: {task_description}")

    def remove_task(self, task_index: int) -> None:
        """
        Remove a task from the task list by its index.
        
        :param task_index: Index of the task to be removed.
        """
        if not 0 <= task_index < len(self.tasks):
            raise IndexError("Task index out of range.")
        
        print(f"Removed task: {self.tasks[task_index]}")
        self.tasks.pop(task_index)

    def list_tasks(self) -> None:
        """List all tasks in the task manager."""
        if not self.tasks:
            print("No tasks to display.")
            return
        
        for index, task in enumerate(self.tasks):
            print(f"{index}: {task}")
```

### How to Use the Module

To use this module, you can import it into your Python script or interactive session.

```python
# Import the TaskManager class from the task_manager module
from task_manager import TaskManager

# Create an instance of TaskManager
tm = TaskManager()

# Add some tasks
tm.add_task("Learn Python")
tm.add_task("Do laundry")
tm.add_task("Walk the dog")

# List all tasks
print("\nAll tasks:")
tm.list_tasks()

# Remove a specific task by its index
try:
    tm.remove_task(1)  # Removes "Do laundry" (the second task)
except IndexError as e:
    print(e)

# List remaining tasks after removal
print("\nTasks after removal:")
tm.list_tasks()
```

### Notes

- The `add_task` method checks that the task description is not empty or just whitespace.
- When removing a task with `remove_task`, ensure you provide a valid index. It starts from 0, so if you have three tasks, indices are 0, 1, and 2.
- The module can be extended to include functionalities like marking tasks as completed or filtering tasks by completion status.

This is a very basic example of task management in Python. Depending on your needs, the module could be expanded with more features such as persistence (saving/loading tasks), priority management, etc.