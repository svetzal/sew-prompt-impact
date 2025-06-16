Below is a complete Python module that manages a list of tasks. Each task is represented using a Pydantic model for validation, and the TaskManager class provides methods for common operations such as adding, removing, listing, and marking tasks as complete or incomplete.

------------------------------------------------------------
# tasks_manager.py

------------------------------------------------------------
#!/usr/bin/env python3
"""
A module to manage a list of tasks.

Each task is defined using a Pydantic model for data validation.
The TaskManager class provides a simple interface to add, remove,
query, and update tasks.

Usage:
    manager = TaskManager()
    task = manager.add_task("Buy groceries", "Milk, Eggs, Bread")
    manager.mark_completed(task.id)
    all_tasks = manager.list_tasks()
"""

import uuid
from typing import List, Optional

from pydantic import BaseModel, Field


class Task(BaseModel):
    """Represents a task with a unique id, title, description, and completion status."""
    id: str
    title: str = Field(..., min_length=1)
    description: Optional[str] = None
    completed: bool = False

    @classmethod
    def create(cls, title: str, description: Optional[str] = None) -> "Task":
        """Factory method to create a new task with a unique identifier.

        Args:
            title (str): The title of the task.
            description (Optional[str], optional): A description of the task.
                Defaults to None.

        Returns:
            Task: A new Task instance.
        """
        return cls(
            id=str(uuid.uuid4()),
            title=title,
            description=description,
            completed=False,
        )


class TaskManager:
    """Manages a list of tasks with operations to add, list, update, and remove tasks."""

    def __init__(self) -> None:
        """Initialize the TaskManager with an empty list of tasks."""
        self.tasks: List[Task] = []

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """Add a new task to the list.

        Args:
            title (str): The title of the task.
            description (Optional[str], optional): The description of the task.
                Defaults to None.

        Returns:
            Task: The newly created task.
        """
        task = Task.create(title, description)
        self.tasks.append(task)
        return task

    def get_task(self, task_id: str) -> Optional[Task]:
        """Retrieve a task by its unique id.

        Args:
            task_id (str): The ID of the task.

        Returns:
            Optional[Task]: The task if found; otherwise, None.
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def remove_task(self, task_id: str) -> bool:
        """Remove a task based on its id.

        Args:
            task_id (str): The ID of the task to remove.

        Returns:
            bool: True if the task was removed; False if not found.
        """
        for index, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[index]
                return True
        return False

    def list_tasks(self, completed: Optional[bool] = None) -> List[Task]:
        """List all tasks filtered by completion status if provided.

        Args:
            completed (Optional[bool], optional): If provided, filters tasks that are
                either completed (True) or incomplete (False). Defaults to None.

        Returns:
            List[Task]: A list of tasks that match the filter criteria.
        """
        if completed is None:
            return self.tasks.copy()
        return [task for task in self.tasks if task.completed == completed]

    def mark_completed(self, task_id: str) -> bool:
        """Mark a specific task as completed.

        Args:
            task_id (str): The ID of the task to mark as completed.

        Returns:
            bool: True if the task was found and marked; False otherwise.
        """
        task = self.get_task(task_id)
        if task:
            task.completed = True
            return True
        return False

    def mark_incomplete(self, task_id: str) -> bool:
        """Mark a specific task as incomplete.

        Args:
            task_id (str): The ID of the task to mark as incomplete.

        Returns:
            bool: True if the task was found and marked; False otherwise.
        """
        task = self.get_task(task_id)
        if task:
            task.completed = False
            return True
        return False

    def clear_completed(self) -> int:
        """Remove all tasks that are marked as completed.

        Returns:
            int: The number of tasks that were removed.
        """
        completed_tasks = [task for task in self.tasks if task.completed]
        self.tasks = [task for task in self.tasks if not task.completed]
        return len(completed_tasks)


# Example usage when running this module directly.
if __name__ == "__main__":
    manager = TaskManager()
    print("Adding tasks...")
    task1 = manager.add_task("Write documentation", "Document the task manager module")
    task2 = manager.add_task("Fix bugs", "Resolve issue #42")
    print("Listing all tasks:", manager.list_tasks())

    print("Marking the first task as completed...")
    manager.mark_completed(task1.id)
    print("Completed tasks:", manager.list_tasks(completed=True))
    print("Incomplete tasks:", manager.list_tasks(completed=False))

    print("Clearing completed tasks...")
    cleared_count = manager.clear_completed()
    print(f"Cleared {cleared_count} task(s).")
    print("Remaining tasks:", manager.list_tasks())
    
    print("Removing remaining tasks...")
    manager.remove_task(task2.id)
    print("Remaining tasks after removal:", manager.list_tasks())
    
    print("Done.")
------------------------------------------------------------

This module adheres to the provided guidelines:
• It uses clear, descriptive naming and docstrings.
• It covers basic task management operations.
• It utilizes Pydantic for task validation.
• It includes type hints and is formatted for readability.

You can further extend this module with additional features or integrate it into a larger project as needed.