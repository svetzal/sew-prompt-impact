```python
from typing import List, Optional
from pydantic import BaseModel, Field


class Task(BaseModel):
    """Task item with an id, description, and completion status."""

    id: int
    description: str = Field(min_length=1)
    done: bool = False


class TaskManager:
    """Manage a list of tasks with add, remove, list, and update operations."""

    def __init__(self) -> None:
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def add_task(self, description: str) -> Task:
        """Add a new task with the given description.

        Args:
            description: The task's description, must be non-empty.

        Returns:
            The created Task object.
        """
        task = Task(id=self._next_id, description=description)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """Get a task by its id.

        Args:
            task_id: The id of the task.

        Returns:
            The Task if found, else None.
        """
        return next((task for task in self._tasks if task.id == task_id), None)

    def remove_task(self, task_id: int) -> bool:
        """Remove a task by its id.

        Args:
            task_id: The id of the task to remove.

        Returns:
            True if a task was removed, False if not found.
        """
        for i, task in enumerate(self._tasks):
            if task.id == task_id:
                del self._tasks[i]
                return True
        return False

    def mark_done(self, task_id: int) -> bool:
        """Mark the task as done.

        Args:
            task_id: The task id to mark done.

        Returns:
            True if task was found and marked, False otherwise.
        """
        task = self.get_task(task_id)
        if task is None or task.done:
            return False
        # mutate the task in place (pydantic BaseModel is immutable by default,
        # but default is mutable unless frozen=True)
        task.done = True
        return True

    def list_tasks(self, done: Optional[bool] = None) -> List[Task]:
        """List tasks, optionally filtered by completion status.

        Args:
            done: If set, filters tasks by their 'done' status.

        Returns:
            List of tasks, filtered if done is set.
        """
        if done is None:
            return list(self._tasks)
        return [task for task in self._tasks if task.done is done]
```