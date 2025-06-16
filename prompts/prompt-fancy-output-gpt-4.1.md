Certainly! Let's deliver a simple, type-safe **tasks module** that:

- Provides a `Task` data model (with validation via [pydantic](https://docs.pydantic.dev/))
- Offers a `TaskManager` class to add, remove, and list tasks, and mark them as done
- Separates core logic from I/O (imperative shell)
- Follows your conventions (flake8/black, type hints, docstrings, etc.)
- 100% testable: no CLI or persistence included—functional core only

Let’s implement that:

```python
# tasks.py

from typing import List, Optional
from pydantic import BaseModel, Field, validator


class Task(BaseModel):
    """A task item with a name, status and optional description."""

    name: str = Field(..., min_length=1)
    description: Optional[str] = None
    completed: bool = False

    @validator("name")
    def name_cannot_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("name cannot be blank")
        return value


class TaskManager:
    """Manages a collection of tasks."""

    def __init__(self) -> None:
        """Initialise an empty task list."""
        self._tasks: List[Task] = []

    def add_task(self, name: str, description: Optional[str] = None) -> Task:
        """
        Add a new task.

        Args:
            name: Task title.
            description: Details about the task.

        Returns:
            Task: The task created.
        """
        task = Task(name=name, description=description)
        self._tasks.append(task)
        return task

    def remove_task(self, name: str) -> None:
        """
        Remove a task by name.

        Args:
            name: Exact name of the task to remove.

        Raises:
            ValueError: If no task with given name exists.
        """
        index = self._find_task_index(name)
        self._tasks.pop(index)

    def list_tasks(self, completed: Optional[bool] = None) -> List[Task]:
        """
        List tasks, optionally filtering by completion.

        Args:
            completed: If set, filter by completed/incomplete.

        Returns:
            List[Task]: Matching tasks.
        """
        if completed is None:
            return list(self._tasks)
        return [task for task in self._tasks if task.completed == completed]

    def mark_done(self, name: str) -> Task:
        """
        Mark a task as completed.

        Args:
            name: Exact name of the task.

        Returns:
            Task: Updated task.

        Raises:
            ValueError: If no such task found.
        """
        index = self._find_task_index(name)
        self._tasks[index].completed = True
        return self._tasks[index]

    def _find_task_index(self, name: str) -> int:
        """
        Find the index of a task by name.

        Args:
            name: Exact name to match.

        Returns:
            int: Index in the list.

        Raises:
            ValueError: If not found.
        """
        for i, task in enumerate(self._tasks):
            if task.name == name:
                return i
        raise ValueError(f"No task found with name: {name!r}")
```

---

**Next steps (if you want):**

- Would you like some unit tests for this module?
- Do you need persistence (saving/loading)?
- Or a basic CLI or API shell?