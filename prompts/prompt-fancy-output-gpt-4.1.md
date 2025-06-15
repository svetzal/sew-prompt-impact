Certainly! Below is a Python module that manages a list of tasks. It uses `pydantic.BaseModel` for data validation, includes type hints, and is structured for simple extension and testability. CRUD (Create, Read, Update, Delete) operations are included. Task storage is in-memory, suitable for simple apps or as a starting point for further development.  

If you need persistence, let me know.

---

```python
from typing import List, Optional, Dict
from uuid import UUID, uuid4
from pydantic import BaseModel, Field, validator


class Task(BaseModel):
    """A single task in the task list."""
    id: UUID = Field(default_factory=uuid4)
    title: str
    description: Optional[str] = None
    completed: bool = False

    @validator('title')
    def title_must_not_be_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError('Title must not be blank')
        return v


class TaskManager:
    """
    Manages a collection of tasks in memory.
    """

    def __init__(self) -> None:
        self._tasks: Dict[UUID, Task] = {}

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Adds a new task.

        Args:
            title: Title of the task.
            description: Optional detailed description.

        Returns:
            The created Task object.
        """
        task = Task(title=title, description=description)
        self._tasks[task.id] = task
        return task

    def get_task(self, task_id: UUID) -> Optional[Task]:
        """
        Retrieves a task by ID.

        Args:
            task_id: UUID of the task.

        Returns:
            The Task object if found, else None.
        """
        return self._tasks.get(task_id)

    def list_tasks(self, completed: Optional[bool] = None) -> List[Task]:
        """
        Lists all tasks, optionally filtering by completion.

        Args:
            completed: If set, filter tasks by completion status.

        Returns:
            List of Task objects.
        """
        tasks = list(self._tasks.values())
        if completed is not None:
            tasks = [task for task in tasks if task.completed == completed]
        return tasks

    def update_task(
        self,
        task_id: UUID,
        *,
        title: Optional[str] = None,
        description: Optional[str] = None,
        completed: Optional[bool] = None
    ) -> Optional[Task]:
        """
        Updates fields of a task.

        Args:
            task_id: UUID of the task.
            title: New title, if updating.
            description: New description, if updating.
            completed: New completion state, if updating.

        Returns:
            The updated Task, or None if not found.
        """
        task = self._tasks.get(task_id)
        if not task:
            return None
        update_data = {}
        if title is not None:
            update_data['title'] = title
        if description is not None:
            update_data['description'] = description
        if completed is not None:
            update_data['completed'] = completed
        updated = task.copy(update=update_data)
        self._tasks[task_id] = updated
        return updated

    def delete_task(self, task_id: UUID) -> bool:
        """
        Deletes a task by ID.

        Args:
            task_id: UUID of the task to delete.

        Returns:
            True if the task was deleted, False if not found.
        """
        return self._tasks.pop(task_id, None) is not None
```

---

### Example Usage

```python
if __name__ == "__main__":
    tm = TaskManager()
    t1 = tm.add_task(title="Write docs", description="Complete user documentation")
    t2 = tm.add_task(title="Fix bug #42")
    tm.update_task(t1.id, completed=True)
    all_tasks = tm.list_tasks()
    completed_tasks = tm.list_tasks(completed=True)
    tm.delete_task(t2.id)
```

---

Let me know if you want CLI, file/database save, or tests!