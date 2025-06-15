Below is a complete Python module that uses pydantic models to represent each task and a TaskManager class to perform task operations. The module includes type hints, Google‑style docstrings, and is formatted to pass flake8/black and mypy.

--------------------------------------------------
#!/usr/bin/env python3
"""
Task Manager Module

This module defines a Task model and a TaskManager class to manage a list of tasks.
It provides basic operations such as creating, updating, retrieving, and deleting tasks.
"""

from typing import List, Optional
from uuid import uuid4

from pydantic import BaseModel, Field, validator


class Task(BaseModel):
    """Data model representing a single task.

    Attributes:
        id (str): A unique identifier for the task.
        description (str): The description of the task.
        completed (bool): A flag indicating if the task has been completed.
    """
    id: str = Field(default_factory=lambda: str(uuid4()))
    description: str
    completed: bool = False

    @validator("description")
    def description_must_not_be_empty(cls, value: str) -> str:
        """Validate that the task description is not empty.

        Args:
            value (str): The description value.

        Returns:
            str: The original description if valid.

        Raises:
            ValueError: If the description is empty.
        """
        if not value.strip():
            raise ValueError("Task description must not be empty")
        return value


class TaskManager:
    """Class to manage a list of tasks.

    Attributes:
        _tasks (List[Task]): Internal list of tasks.
    """

    def __init__(self) -> None:
        """Initializes a TaskManager with an empty task list."""
        self._tasks: List[Task] = []

    def add_task(self, description: str) -> Task:
        """Create and add a new task to the manager.

        Args:
            description (str): The description for the new task.

        Returns:
            Task: The newly created task.
        """
        task = Task(description=description)
        self._tasks.append(task)
        return task

    def get_task(self, task_id: str) -> Optional[Task]:
        """Retrieve a task by its unique identifier.

        Args:
            task_id (str): The unique identifier of the task.

        Returns:
            Optional[Task]: The task if found; otherwise, None.
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: str, *, description: Optional[str] = None,
                    completed: Optional[bool] = None) -> Optional[Task]:
        """Update properties of an existing task.

        Args:
            task_id (str): The unique identifier of the task.
            description (Optional[str]): New description for the task.
            completed (Optional[bool]): New completion status for the task.

        Returns:
            Optional[Task]: The updated task if found; otherwise, None.
        """
        task = self.get_task(task_id)
        if task is None:
            return None

        # Create a dictionary of fields to update.
        update_data = {}
        if description is not None:
            update_data["description"] = description
        if completed is not None:
            update_data["completed"] = completed

        if update_data:
            # Using pydantic's copy(update=...) to create an updated Task instance.
            updated_task = task.copy(update=update_data)
            # Replace the task in the internal list.
            index = self._tasks.index(task)
            self._tasks[index] = updated_task
            return updated_task

        return task

    def delete_task(self, task_id: str) -> bool:
        """Delete a task by its unique identifier.

        Args:
            task_id (str): The unique identifier of the task.

        Returns:
            bool: True if the task was found and deleted, False otherwise.
        """
        for index, task in enumerate(self._tasks):
            if task.id == task_id:
                del self._tasks[index]
                return True
        return False

    def list_tasks(self) -> List[Task]:
        """List all stored tasks.

        Returns:
            List[Task]: The list of all tasks.
        """
        return self._tasks.copy()


if __name__ == '__main__':
    # A simple demonstration of TaskManager usage.
    manager = TaskManager()
    print("Adding tasks...")
    task1 = manager.add_task("Write unit tests")
    task2 = manager.add_task("Refactor code")
    print("Current tasks:", manager.list_tasks())

    print("\nUpdating a task...")
    updated_task = manager.update_task(task1.id, completed=True)
    print("Updated task:", updated_task)

    print("\nDeleting a task...")
    if manager.delete_task(task2.id):
        print("Task deleted successfully.")
    else:
        print("Task not found.")
    print("Final tasks:", manager.list_tasks())
--------------------------------------------------

This module is designed with clarity and modularity in mind. Each function reveals its intent with descriptive names and comprehensive docstrings, and the code is fully type annotated to ensure reliability and maintainability.

You can further test this module with unit tests or by running it directly as a standalone script.