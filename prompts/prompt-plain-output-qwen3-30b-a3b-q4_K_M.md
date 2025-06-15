

Here's a well-structured Python module for managing a list of tasks. It includes core functionality for adding, completing, viewing, and deleting tasks, along with sorting options.

```python
"""
task_manager.py

A module to manage a list of tasks with basic CRUD operations and sorting capabilities.
"""

class Task:
    """
    Represents a single task with a description, priority, completion status, and optional due date.
    
    Attributes:
        description (str): Description of the task.
        priority (int): Priority level (1 = high, 3 = low).
        completed (bool): Whether the task is completed.
        due_date (str, optional): Due date in "YYYY-MM-DD" format.
    """
    
    def __init__(self, description: str, priority: int = 2, completed: bool = False, due_date: str = None):
        self.description = description
        self.priority = priority
        self.completed = completed
        self.due_date = due_date

    def __str__(self):
        """Return a string representation of the task."""
        status = "✅" if self.completed else "❌"
        priority_str = "High" if self.priority == 1 else "Medium" if self.priority == 2 else "Low"
        return f"{status} {self.description} (Priority: {priority_str})"

    def mark_as_completed(self):
        """Mark the task as completed."""
        self.completed = True


class TaskManager:
    """
    Manages a collection of Task objects with methods to add, complete, list, and delete tasks.
    
    Attributes:
        tasks (list): List of Task objects.
    """
    
    def __init__(self):
        self.tasks = []

    def add_task(self, description: str, priority: int = 2, due_date: str = None):
        """
        Add a new task to the list.
        
        Args:
            description (str): Description of the task.
            priority (int): Priority level (1-3).
            due_date (str): Optional due date in "YYYY-MM-DD" format.
        """
        if not (1 <= priority <= 3):
            raise ValueError("Priority must be 1 (high), 2 (medium), or 3 (low).")
        
        task = Task(description, priority, due_date=due_date)
        self.tasks.append(task)

    def complete_task(self, task_index: int):
        """
        Mark a task as completed by its index.
        
        Args:
            task_index (int): Index of the task to mark as completed.
        """
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_completed()
        else:
            raise IndexError("Task index out of range.")

    def list_tasks(self, completed: bool = None, sort_by: str = "priority"):
        """
        List all tasks, optionally filtered by completion status and sorted.
        
        Args:
            completed (bool, optional): Filter by completion status (True = completed, False = incomplete).
            sort_by (str): Sort by "priority", "due_date", or "description".
        
        Returns:
            list: Filtered and sorted list of tasks.
        """
        filtered = self.tasks
        if completed is not None:
            filtered = [task for task in self.tasks if task.completed == completed]
        
        if sort_by == "priority":
            filtered.sort(key=lambda x: x.priority)
        elif sort_by == "due_date":
            filtered.sort(key=lambda x: x.due_date or "9999-12-31")  # Handle None values
        elif sort_by == "description":
            filtered.sort(key=lambda x: x.description)
        
        return filtered

    def delete_task(self, task_index: int):
        """
        Delete a task by its index.
        
        Args:
            task_index (int): Index of the task to delete.
        """
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)
        else:
            raise IndexError("Task index out of range.")


# Example usage
if __name__ == "__main__":
    manager = TaskManager()
    
    manager.add_task("Finish project report", priority=1, due_date="2023-10-25")
    manager.add_task("Submit time sheet", priority=2, due_date="2023-10-26")
    manager.add_task("Schedule meeting", priority=3, due_date="2023-10-27")
    
    print("All Tasks:")
    for task in manager.list_tasks():
        print(task)
    
    print("\nIncomplete Tasks (sorted by priority):")
    for task in manager.list_tasks(completed=False, sort_by="priority"):
        print(task)
    
    print("\nCompleted Tasks:")
    for task in manager.list_tasks(completed=True):
        print(task)
    
    manager.complete_task(0)
    print("\nAfter completing first task:")
    for task in manager.list_tasks(completed=False):
        print(task)
```

## Key Features:
- **Task Class**: Represents individual tasks with description, priority, completion status, and optional due date
- **TaskManager Class**: Provides:
  - Task creation with validation
  - Completion marking
  - Filtering by completion status
  - Sorting by priority, due date, or description
  - Task deletion
- **Flexible Interface**: Supports various sorting options and filtering
- **Error Handling**: Includes validation for priority levels and index ranges

## Example Usage:
```python
from task_manager import TaskManager

manager = TaskManager()
manager.add_task("Buy groceries", priority=2)
manager.add_task("Finish presentation", priority=1, due_date="2023-10-30")

# List all tasks
for task in manager.list_tasks():
    print(task)

# Complete a task
manager.complete_task(0)

# List incomplete tasks sorted by due date
for task in manager.list_tasks(completed=False, sort_by="due_date"):
    print(task)
```

This module provides a solid foundation that can be extended with additional features like task persistence, notifications, or GUI integration.