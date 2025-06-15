Certainly! Below is a Python module that manages a list of tasks. It adheres to the conventions and principles outlined, including type hints, docstrings, and best practices for code clarity and maintainability.

### `task_manager.py`

```python
from typing import List, Optional
from pydantic import BaseModel

# Constants
MAX_TASKS = 100


class Task(BaseModel):
    """Represents a single task with an ID, title, description, and status."""
    
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False


class TaskManager:
    """A class to manage a list of tasks."""
    
    def __init__(self):
        """Initialize the task manager with an empty list of tasks."""
        self.tasks: List[Task] = []
        self.next_id: int = 1

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Add a new task to the list.

        Args:
            title (str): The title of the task.
            description (Optional[str], optional): A description of the task. Defaults to None.

        Returns:
            Task: The newly created task.
        """
        if len(self.tasks) >= MAX_TASKS:
            raise ValueError("Task limit exceeded")
        
        new_task = Task(id=self.next_id, title=title, description=description)
        self.tasks.append(new_task)
        self.next_id += 1
        return new_task

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Retrieve a task by its ID.

        Args:
            task_id (int): The ID of the task to retrieve.

        Returns:
            Optional[Task]: The task if found, otherwise None.
        """
        return next((task for task in self.tasks if task.id == task_id), None)

    def complete_task(self, task_id: int) -> bool:
        """
        Mark a task as completed by its ID.

        Args:
            task_id (int): The ID of the task to mark as completed.

        Returns:
            bool: True if the task was found and marked as completed, otherwise False.
        """
        task = self.get_task(task_id)
        if task is not None:
            task.completed = True
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id (int): The ID of the task to delete.

        Returns:
            bool: True if the task was found and deleted, otherwise False.
        """
        task = self.get_task(task_id)
        if task is not None:
            self.tasks.remove(task)
            return True
        return False

    def list_tasks(self) -> List[Task]:
        """
        List all tasks.

        Returns:
            List[Task]: A list of all tasks.
        """
        return self.tasks

# Example usage
if __name__ == "__main__":
    manager = TaskManager()
    task1 = manager.add_task("Buy groceries", "Milk, bread, eggs")
    task2 = manager.add_task("Finish report")

    print(f"Added task 1: {task1}")
    print(f"Added task 2: {task2}")

    manager.complete_task(task1.id)
    print(f"Completed task 1: {manager.get_task(task1.id)}")

    all_tasks = manager.list_tasks()
    for task in all_tasks:
        print(task)

    manager.delete_task(task2.id)
    print("Deleted task 2")
```

### Explanation

1. **Task Model**:
   - `Task` is a Pydantic model that represents a single task with an ID, title, description (optional), and completion status.

2. **Task Manager Class**:
   - `TaskManager` class manages a list of tasks.
   - `__init__`: Initializes the task manager with an empty list of tasks and sets the next available ID to 1.
   - `add_task`: Adds a new task to the list, ensuring the maximum number of tasks is not exceeded.
   - `get_task`: Retrieves a task by its ID.
   - `complete_task`: Marks a task as completed by its ID.
   - `delete_task`: Deletes a task by its ID.
   - `list_tasks`: Returns a list of all tasks.

3. **Example Usage**:
   - The example usage demonstrates how to create, complete, and delete tasks using the `TaskManager` class.

This module adheres to the principles of simple design, minimal entities, and clear communication through naming and docstrings. It also uses type hints and Pydantic for data validation, ensuring robustness and clarity in the code.