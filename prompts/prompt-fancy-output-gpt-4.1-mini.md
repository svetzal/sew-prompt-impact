```python
from typing import List
from pydantic import BaseModel, Field


class Task(BaseModel):
    """A task with a description and completion status."""

    description: str = Field(..., min_length=1)
    completed: bool = False


class TaskManager:
    """Manage a list of tasks."""

    def __init__(self) -> None:
        self._tasks: List[Task] = []

    def add_task(self, description: str) -> None:
        """Add a new task with the given description.

        Args:
            description: The task description, must be non-empty.
        """
        self._tasks.append(Task(description=description))

    def complete_task(self, index: int) -> None:
        """Mark the task at index as completed.

        Args:
            index: Index of the task to mark complete.

        Raises:
            IndexError: If the index is out of bounds.
        """
        task = self._tasks[index]
        self._tasks[index] = task.copy(update={"completed": True})

    def delete_task(self, index: int) -> None:
        """Delete the task at index.

        Args:
            index: Index of the task to delete.

        Raises:
            IndexError: If the index is out of bounds.
        """
        del self._tasks[index]

    def list_tasks(self, *, completed: bool | None = None) -> List[Task]:
        """List tasks, optionally filtering by completion status.

        Args:
            completed: If True, only return completed tasks; if False,
                only incomplete tasks; if None, return all tasks.

        Returns:
            List of tasks matching filter.
        """
        if completed is None:
            return list(self._tasks)
        return [t for t in self._tasks if t.completed == completed]
```
