```python
from typing import List, Optional
from pydantic import BaseModel


class Task(BaseModel):
    """
    Represents a task with a description and completion status.
    """
    id: int
    description: str
    completed: bool = False


class TaskManager:
    """
    Manages a list of tasks, allowing addition, removal, and status updates.
    """

    def __init__(self) -> None:
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def add_task(self, description: str) -> Task:
        """
        Adds a new task to the list with the given description.

        Args:
            description: The description of the task.

        Returns:
            The created Task object.
        """
        task = Task(id=self._next_id, description=description)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def remove_task(self, task_id: int) -> bool:
        """
        Removes a task by its ID.

        Args:
            task_id: The ID of the task to remove.

        Returns:
            True if removal was successful, False if task was not found.
        """
        for index, task in enumerate(self._tasks):
            if task.id == task_id:
                del self._tasks[index]
                return True
        return False

    def mark_task_completed(self, task_id: int) -> bool:
        """
        Marks the specified task as completed.

        Args:
            task_id: The ID of the task to mark as completed.

        Returns:
            True if the task was found and updated, False otherwise.
        """
        for index, task in enumerate(self._tasks):
            if task.id == task_id:
                updated_task = task.copy(update={"completed": True})
                self._tasks[index] = updated_task
                return True
        return False

    def list_tasks(self, include_completed: bool = True) -> List[Task]:
        """
        Returns a list of tasks, optionally filtering out completed ones.

        Args:
            include_completed: Whether to include completed tasks.

        Returns:
            A list of Task objects.
        """
        if include_completed:
            return self._tasks.copy()
        return [task for task in self._tasks if not task.completed]

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Retrieves a task by its ID.

        Args:
            task_id: The ID of the task.

        Returns:
            The Task object if found, None otherwise.
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None
```