Below is an example of a Python module named task_manager.py. It provides a simple API for managing a list of tasks. Each task is represented by a Task instance, and a TaskManager class handles creating, listing, completing, and removing tasks. The module includes inline tests that serve as an executable specification.

------------------------------------------------------------
# task_manager.py

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Task:
    """
    Represents a single task.

    Attributes:
        id (int): Unique identifier for the task.
        description (str): A short description of the task.
        completed (bool): True if the task is completed; otherwise False.
    """
    id: int
    description: str
    completed: bool = False


class TaskManager:
    """
    Manages a list of tasks with basic operations such as adding,
    listing, completing, and removing tasks.
    """

    def __init__(self) -> None:
        # Stores tasks in order of insertion.
        self._tasks: List[Task] = []
        # A simple incremental id generator for new tasks.
        self._next_id: int = 1

    def add_task(self, description: str) -> int:
        """
        Adds a new task with the given description.

        Args:
            description (str): The description of the task.

        Returns:
            int: The unique id assigned to the new task.
        """
        task = Task(id=self._next_id, description=description)
        self._tasks.append(task)
        self._next_id += 1
        return task.id

    def list_tasks(self, include_completed: bool = True) -> List[Task]:
        """
        Returns a list of tasks.

        Args:
            include_completed (bool): If False, only active tasks are returned;
                                      otherwise, all tasks are returned.

        Returns:
            List[Task]: The list of tasks.
        """
        if include_completed:
            return self._tasks.copy()
        return [task for task in self._tasks if not task.completed]

    def complete_task(self, task_id: int) -> bool:
        """
        Marks the task with the given id as completed.

        Args:
            task_id (int): The unique id of the task to complete.

        Returns:
            bool: True if the task was found and marked complete;
                  False if no task with the given id exists.
        """
        task = self._find_task(task_id)
        if task:
            task.completed = True
            return True
        return False

    def remove_task(self, task_id: int) -> bool:
        """
        Removes the task with the given id from the manager.

        Args:
            task_id (int): The unique id of the task to remove.

        Returns:
            bool: True if the task was found and removed;
                  False if no task with the given id exists.
        """
        task = self._find_task(task_id)
        if task:
            self._tasks.remove(task)
            return True
        return False

    def _find_task(self, task_id: int) -> Optional[Task]:
        """
        Helper method to find a task by its id.

        Args:
            task_id (int): The unique id of the task.

        Returns:
            Optional[Task]: The task if found; otherwise None.
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None


# If this module is executed as a standalone script, run simple tests.
if __name__ == '__main__':
    # A simple test suite to verify that all functionality works as intended.
    import sys

    def main() -> None:
        manager = TaskManager()

        # Test: Add tasks
        task1_id = manager.add_task("Implement login feature")
        task2_id = manager.add_task("Write unit tests for task_manager")
        task3_id = manager.add_task("Design API endpoints")
        print("Added tasks:")
        for task in manager.list_tasks():
            print(f"  Task {task.id}: {task.description} (Completed: {task.completed})")

        # Test: Complete a task
        if manager.complete_task(task2_id):
            print(f"Task {task2_id} marked as complete.")
        else:
            print(f"Error: Task {task2_id} not found.", file=sys.stderr)

        # Test: List only active tasks
        print("Active tasks (excluding completed):")
        for task in manager.list_tasks(include_completed=False):
            print(f"  Task {task.id}: {task.description} (Completed: {task.completed})")

        # Test: Remove a task
        if manager.remove_task(task1_id):
            print(f"Task {task1_id} removed successfully.")
        else:
            print(f"Error: Task {task1_id} not found.", file=sys.stderr)

        # Final state of tasks
        print("Final list of tasks:")
        for task in manager.list_tasks():
            print(f"  Task {task.id}: {task.description} (Completed: {task.completed})")

    main()

------------------------------------------------------------

Design Notes:
• Each function is documented with clear docstrings, providing an executable specification of expected behavior.
• The code minimizes side‑effects within the core TaskManager class while the imperative shell (in the __main__ block) serves as a test harness.
• Simple, safe increments and clear naming ensure readability and maintainability.
• The _find_task helper encapsulates the logic for locating tasks and avoids duplicating code.
  
By following these design principles, this module aims to be simple to understand, modify, and extend.