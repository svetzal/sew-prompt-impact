```python
from typing import List
from pydantic import BaseModel, ValidationError


class Task(BaseModel):
    """Represents a single task with a description and completion status."""
    description: str
    completed: bool = False


class TaskManager:
    """Manages a list of tasks, allowing adding, removing, and toggling."""
    
    def __init__(self) -> None:
        """Initialize an empty list of tasks."""
        self._tasks: List[Task] = []

    def add_task(self, description: str) -> None:
        """Add a new task with the given description."""
        task = Task(description=description)
        self._tasks.append(task)

    def remove_task(self, index: int) -> None:
        """Remove a task by its index."""
        if 0 <= index < len(self._tasks):
            del self._tasks[index]
        else:
            raise IndexError(f"Task index {index} is out of range.")

    def toggle_task(self, index: int) -> None:
        """Toggle the completion status of a task by its index."""
        if 0 <= index < len(self._tasks):
            task = self._tasks[index]
            self._tasks[index] = Task(
                description=task.description,
                completed=not task.completed
            )
        else:
            raise IndexError(f"Task index {index} is out of range.")

    def list_tasks(self) -> List[Task]:
        """Return a list of all tasks."""
        return self._tasks.copy()
```