Certainly! Below is a Python module that manages a list of tasks, adhering to the principles and conventions you've outlined. This module includes type hints, docstrings, and follows best practices for readability, simplicity, and maintainability.

### `task_manager.py`

```python
from typing import List, Optional, Dict
from pydantic import BaseModel, Field

class Task(BaseModel):
    """Represents a single task."""
    id: int = Field(..., description="Unique identifier for the task.")
    title: str = Field(..., description="Title of the task.")
    description: Optional[str] = Field(None, description="Detailed description of the task.")
    completed: bool = Field(False, description="Indicates whether the task is completed.")

class TaskManager:
    """Manages a list of tasks."""
    
    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id: int = 1

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Adds a new task to the task list.
        
        Args:
            title (str): Title of the task.
            description (Optional[str]): Detailed description of the task. Defaults to None.
        
        Returns:
            Task: The newly created task.
        """
        task = Task(id=self.next_id, title=title, description=description)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Retrieves a task by its ID.
        
        Args:
            task_id (int): The ID of the task to retrieve.
        
        Returns:
            Optional[Task]: The task with the given ID, or None if not found.
        """
        return next((task for task in self.tasks if task.id == task_id), None)

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None, completed: Optional[bool] = None) -> bool:
        """
        Updates an existing task.
        
        Args:
            task_id (int): The ID of the task to update.
            title (Optional[str]): New title for the task. Defaults to None.
            description (Optional[str]): New detailed description for the task. Defaults to None.
            completed (Optional[bool]): New completion status for the task. Defaults to None.
        
        Returns:
            bool: True if the task was updated, False otherwise.
        """
        task = self.get_task(task_id)
        if not task:
            return False

        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if completed is not None:
            task.completed = completed

        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Deletes a task by its ID.
        
        Args:
            task_id (int): The ID of the task to delete.
        
        Returns:
            bool: True if the task was deleted, False otherwise.
        """
        task = self.get_task(task_id)
        if not task:
            return False

        self.tasks.remove(task)
        return True

    def list_tasks(self) -> List[Task]:
        """
        Lists all tasks.
        
        Returns:
            List[Task]: A list of all tasks.
        """
        return self.tasks

# Example usage
if __name__ == "__main__":
    manager = TaskManager()
    task1 = manager.add_task(title="Buy groceries", description="Milk, bread, eggs")
    task2 = manager.add_task(title="Read a book")

    print(f"Added tasks: {task1}, {task2}")

    updated = manager.update_task(task_id=1, completed=True)
    print(f"Updated task 1: {updated}")

    deleted = manager.delete_task(task_id=2)
    print(f"Deleted task 2: {deleted}")

    all_tasks = manager.list_tasks()
    print(f"All tasks: {all_tasks}")
```

### Explanation

1. **Task Model**: The `Task` class is a Pydantic model that represents a single task. It includes fields for the task's ID, title, description, and completion status.
2. **Task Manager**: The `TaskManager` class manages a list of tasks. It provides methods to add, retrieve, update, delete, and list tasks.
3. **Type Hints and Docstrings**: All methods have type hints and docstrings in Google format, ensuring clarity and completeness.
4. **Validation**: Pydantic is used for data validation, ensuring that tasks are created with the correct types and values.
5. **Example Usage**: An example usage section demonstrates how to use the `TaskManager` class.

This module adheres to the principles of simple design, readability, and maintainability while providing a robust foundation for managing tasks.