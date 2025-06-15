

```python
class Task:
    """
    Represents a single task with a description, priority, and completion status.
    
    Attributes:
        description (str): A brief description of the task.
        priority (int): Priority level (lower numbers mean higher priority).
        completed (bool): Whether the task has been completed.
    """

    def __init__(self, description, priority=1, completed=False):
        self.description = description
        self.priority = priority
        self.completed = completed

    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True

    def mark_incomplete(self):
        """Mark the task as not completed."""
        self.completed = False

    def __str__(self):
        return f"{self.description} (Priority: {self.priority}, Completed: {self.completed})"


class TaskManager:
    """
    Manages a collection of tasks, allowing for addition, removal, updating, and filtering.
    """

    def __init__(self):
        """Initialize an empty list of tasks."""
        self.tasks = []

    def add_task(self, description, priority=1):
        """
        Add a new task with the given description and priority.
        
        Args:
            description (str): Description of the task.
            priority (int): Priority level (default is 1).
        
        Returns:
            Task: The newly created task.
        """
        task = Task(description, priority)
        self.tasks.append(task)
        return task

    def remove_task(self, index):
        """
        Remove a task at the specified index.
        
        Args:
            index (int): Index of the task to be removed.
        
        Raises:
            IndexError: If the index is out of range.
        """
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            raise IndexError("Task index out of range")

    def update_task(self, index, description=None, priority=None, completed=None):
        """
        Update an existing task at the specified index.
        
        Args:
            index (int): Index of the task to be updated.
            description (str, optional): New description for the task.
            priority (int, optional): New priority for the task.
            completed (bool, optional): Update the completion status.
        
        Raises:
            IndexError: If the index is out of range.
        """
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            if description is not None:
                task.description = description
            if priority is not None:
                task.priority = priority
            if completed is not None:
                task.completed = completed
        else:
            raise IndexError("Task index out of range")

    def get_tasks(self, completed=None, priority=None):
        """
        Retrieve a filtered list of tasks.
        
        Args:
            completed (bool, optional): Filter tasks by completion status.
            priority (int, optional): Filter tasks by priority level.
        
        Returns:
            list: A list of tasks matching the criteria.
        """
        filtered = self.tasks
        if completed is not None:
            filtered = [task for task in filtered if task.completed == completed]
        if priority is not None:
            filtered = [task for task in filtered if task.priority == priority]
        return filtered

    def __str__(self):
        """Return a string representation of all tasks."""
        return "\n".join(str(task) for task in self.tasks)
```

---

### 🧩 Example Usage

```python
from task_manager import TaskManager

# Create a task manager
tm = TaskManager()

# Add tasks
tm.add_task("Buy groceries", 2)
tm.add_task("Walk the dog", 1)
tm.add_task("Finish project", 3)

# Print all tasks
print("All Tasks:")
print(tm)

# Mark a task as complete
tm.update_task(0, completed=True)

# Get and print only completed tasks
print("\nCompleted Tasks:")
print(tm.get_tasks(completed=True))

# Remove a task by index
tm.remove_task(1)

# Print the updated list
print("\nAfter Removal:")
print(tm)
```

---

This module provides a clean, object-oriented way to manage a collection of tasks with support for prioritization, completion status tracking, and filtering. It’s easy to extend or integrate into larger applications.