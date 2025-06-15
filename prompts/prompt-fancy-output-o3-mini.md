Below is an implementation of a Python module that manages a list of tasks. The module defines a pydantic‑based Task model for input validation and a TaskManager class with methods to add, update, complete, list, and remove tasks. The code is fully type‐annotated and includes example usage in a main block.

------------------------------------------------------------
File: task_manager.py
------------------------------------------------------------

#!/usr/bin/env python3
"""
A module to manage a list of tasks.

This module provides functionality for creating, updating, listing,
completing, and removing tasks. Each task is validated using pydantic.BaseModel.
"""

from typing import Dict, List, Optional

from pydantic import BaseModel


class Task(BaseModel):
    """Represents a single task."""

    id: int
    description: str
    completed: bool = False

    # No extra configuration is needed since
    # pydantic handles validation by default.

    # Note: if tasks are expected to be mutable, then we leave
    # the default settings. For immutability, we could set
    # `allow_mutation = False` in Config.
    class Config:
        # For clarity, explicitly allow mutation.
        allow_mutation = True


class TaskManager:
    """Manages a collection of tasks in-memory.

    The manager automatically assigns unique IDs to tasks.
    """

    def __init__(self) -> None:
        """Initializes the task manager with no tasks."""
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, description: str) -> Task:
        """Adds a new task to the manager.

        Args:
            description: A string describing the task.

        Returns:
            The newly created Task instance.
        """
        new_task = Task(id=self._next_id, description=description)
        self._tasks[self._next_id] = new_task
        self._next_id += 1
        return new_task

    def remove_task(self, task_id: int) -> bool:
        """Removes a task by its ID.

        Args:
            task_id: The unique identifier of the task to remove.

        Returns:
            True if the task was removed; False if no such task exists.
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def mark_task_complete(self, task_id: int) -> bool:
        """Marks a task as complete.

        Args:
            task_id: The unique identifier of the task to mark complete.

        Returns:
            True if the task was found and marked complete; otherwise False.
        """
        if task_id in self._tasks:
            # Using pydantic's copy to avoid in-place mutation,
            # thus revealing intent and keeping the model usage pure.
            task = self._tasks[task_id]
            updated_task = task.copy(update={"completed": True})
            self._tasks[task_id] = updated_task
            return True
        return False

    def update_task(self, task_id: int, description: Optional[str] = None) -> Optional[Task]:
        """Updates the description for a given task.

        Args:
            task_id: The unique identifier of the task to update.
            description: The new description for the task if provided.

        Returns:
            The updated Task instance if the task exists; otherwise None.
        """
        if task_id in self._tasks:
            current_task = self._tasks[task_id]
            task_data = current_task.dict()
            if description is not None:
                task_data["description"] = description
            updated_task = Task(**task_data)
            self._tasks[task_id] = updated_task
            return updated_task
        return None

    def get_task(self, task_id: int) -> Optional[Task]:
        """Retrieves a task by its ID.

        Args:
            task_id: The unique identifier of the task.

        Returns:
            The Task instance if found; otherwise None.
        """
        return self._tasks.get(task_id)

    def list_tasks(self) -> List[Task]:
        """Lists all tasks managed by the TaskManager.

        Returns:
            A list containing all Task instances.
        """
        return list(self._tasks.values())


def main() -> None:
    """Demonstrates basic usage of the TaskManager."""
    manager = TaskManager()

    # Add tasks.
    task1 = manager.add_task("Buy milk")
    task2 = manager.add_task("Write unit tests")
    print("Tasks after creation:")
    for task in manager.list_tasks():
        print(f"  [ID {task.id}] {task.description} (Completed: {task.completed})")

    # Mark task1 as complete.
    if manager.mark_task_complete(task1.id):
        print(f"\nTask {task1.id} marked as complete.")

    # Update task2 description.
    updated_task = manager.update_task(task2.id, description="Write comprehensive unit tests")
    if updated_task:
        print(f"\nTask {task2.id} updated. New description: {updated_task.description}")

    # Remove task1.
    if manager.remove_task(task1.id):
        print(f"\nTask {task1.id} removed.")

    # Final list of tasks.
    print("\nFinal list of tasks:")
    for task in manager.list_tasks():
        print(f"  [ID {task.id}] {task.description} (Completed: {task.completed})")


if __name__ == "__main__":
    main()

------------------------------------------------------------

Explanation:

1. The Task model (a subclass of pydantic.BaseModel) provides innate data validation and type checking.
2. The TaskManager class stores tasks in an internal dictionary keyed by their unique ID.
3. TaskManager methods provide functionality to add, update, mark complete, remove, and list tasks.
4. A main() function illustrates basic usage and can serve as a simple test harness.

This module adheres to code style guidelines by using snake_case, f‑strings where applicable (here mainly in prints), and comprehensive type annotations.