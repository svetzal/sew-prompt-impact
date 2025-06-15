```python
from typing import List
from pydantic import BaseModel, Field


class Task(BaseModel):
    """Represents a single task item."""

    id: int = Field(..., ge=1, description="Unique identifier for the task")
    title: str = Field(..., min_length=1, description="Title of the task")
    completed: bool = Field(False, description="Completion status")


class TaskManager:
    """Manages a list of tasks with add, remove, update, and query operations."""

    def __init__(self) -> None:
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def list_tasks(self, *, completed: bool | None = None) -> List[Task]:
        """Return all tasks optionally filtered by completion status.

        Args:
            completed: If specified, filter tasks by completion status.

        Returns:
            List of tasks matching the filter.
        """
        if completed is None:
            return self._tasks.copy()
        return [task for task in self._tasks if task.completed is completed]

    def add_task(self, title: str) -> Task:
        """Create a new task with the given title, uncompleted by default.

        Args:
            title: Title of the task.

        Returns:
            The created Task.
        """
        task = Task(id=self._next_id, title=title)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def remove_task(self, task_id: int) -> bool:
        """Remove a task by its id.

        Args:
            task_id: Identifier of the task to remove.

        Returns:
            True if the task was found and removed, otherwise False.
        """
        for i, task in enumerate(self._tasks):
            if task.id == task_id:
                del self._tasks[i]
                return True
        return False

    def update_task(self, task_id: int, *, title: str | None = None, completed: bool | None = None) -> bool:
        """Update fields of a task by id.

        Args:
            task_id: Identifier of the task to update.
            title: New title, if updating.
            completed: New completion status, if updating.

        Returns:
            True if the task was found and updated, otherwise False.
        """
        for i, task in enumerate(self._tasks):
            if task.id == task_id:
                updated = task.copy(update={k: v for k, v in (("title", title), ("completed", completed)) if v is not None})
                self._tasks[i] = updated
                return True
        return False
```
