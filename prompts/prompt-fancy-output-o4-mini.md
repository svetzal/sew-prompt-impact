Below is a self-contained module and accompanying tests. It uses pydantic for the `Task` model, provides a `TaskManager` for in-memory task CRUD, and exercises everything with pytest. All code is mypy-strict-compatible.

tasks.py
---------
```python
from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class TaskNotFoundError(Exception):
    """Raised when a task with the given ID does not exist."""


class Task(BaseModel):
    """A single task with metadata and status."""

    id: UUID = Field(default_factory=uuid4)
    title: str
    description: Optional[str] = None
    completed: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    due_date: Optional[datetime] = None


class TaskManager:
    """Manage a collection of tasks in memory."""

    def __init__(self) -> None:
        self._tasks: Dict[UUID, Task] = {}

    def add_task(
        self, title: str, description: Optional[str] = None, due_date: Optional[datetime] = None
    ) -> Task:
        """Create a new task and store it."""
        task = Task(title=title, description=description, due_date=due_date)
        self._tasks[task.id] = task
        return task

    def get_task(self, task_id: UUID) -> Task:
        """Fetch a task by its ID, or raise TaskNotFoundError."""
        try:
            return self._tasks[task_id]
        except KeyError as e:
            raise TaskNotFoundError(f"Task {task_id} not found") from e

    def list_tasks(self, completed: Optional[bool] = None) -> List[Task]:
        """
        List tasks, optionally filtering by completion status.
        
        Args:
            completed: if True, only completed tasks; if False, only pending;
                       if None, all tasks.
        """
        tasks = list(self._tasks.values())
        if completed is None:
            return tasks
        return [t for t in tasks if t.completed is completed]

    def update_task(
        self,
        task_id: UUID,
        *,
        title: Optional[str] = None,
        description: Optional[str] = None,
        due_date: Optional[datetime] = None,
    ) -> Task:
        """
        Update mutable fields of a task.
        
        Only provided fields will be changed.
        """
        task = self.get_task(task_id)
        update_data = task.dict()
        if title is not None:
            update_data["title"] = title
        if description is not None:
            update_data["description"] = description
        if due_date is not None:
            update_data["due_date"] = due_date
        updated = Task(**update_data)
        self._tasks[task_id] = updated
        return updated

    def remove_task(self, task_id: UUID) -> None:
        """Delete a task, or raise TaskNotFoundError."""
        if task_id not in self._tasks:
            raise TaskNotFoundError(f"Task {task_id} not found")
        del self._tasks[task_id]

    def mark_completed(self, task_id: UUID) -> Task:
        """Mark the given task as completed."""
        task = self.get_task(task_id)
        if not task.completed:
            task = task.copy(update={"completed": True})
            self._tasks[task_id] = task
        return task

    def mark_incomplete(self, task_id: UUID) -> Task:
        """Mark the given task as not completed."""
        task = self.get_task(task_id)
        if task.completed:
            task = task.copy(update={"completed": False})
            self._tasks[task_id] = task
        return task
```

tests/test_tasks.py
-------------------
```python
import pytest
from datetime import datetime, timedelta
from uuid import UUID

from tasks import TaskManager, TaskNotFoundError


@pytest.fixture
def manager() -> TaskManager:
    return TaskManager()


def test_add_and_get_task(manager: TaskManager) -> None:
    t = manager.add_task("Write code", "Implement feature")
    fetched = manager.get_task(t.id)
    assert fetched.id == t.id
    assert fetched.title == "Write code"
    assert fetched.description == "Implement feature"
    assert not fetched.completed


def test_list_tasks_filters(manager: TaskManager) -> None:
    a = manager.add_task("A")
    b = manager.add_task("B")
    manager.mark_completed(b.id)
    all_tasks = manager.list_tasks()
    done = manager.list_tasks(completed=True)
    pending = manager.list_tasks(completed=False)
    assert set(t.id for t in all_tasks) == {a.id, b.id}
    assert [t.id for t in done] == [b.id]
    assert [t.id for t in pending] == [a.id]


def test_update_task(manager: TaskManager) -> None:
    t = manager.add_task("Old", None)
    new_due = datetime.utcnow() + timedelta(days=1)
    updated = manager.update_task(t.id, title="New", description="Desc", due_date=new_due)
    assert updated.title == "New"
    assert updated.description == "Desc"
    assert updated.due_date == new_due
    # other fields preserved
    assert updated.id == t.id
    assert not updated.completed


def test_remove_task(manager: TaskManager) -> None:
    t = manager.add_task("X")
    manager.remove_task(t.id)
    with pytest.raises(TaskNotFoundError):
        manager.get_task(t.id)


def test_mark_complete_and_incomplete(manager: TaskManager) -> None:
    t = manager.add_task("flip")
    c = manager.mark_completed(t.id)
    assert c.completed
    i = manager.mark_incomplete(t.id)
    assert not i.completed


def test_not_found_errors(manager: TaskManager) -> None:
    fake_id = UUID(int=0)
    with pytest.raises(TaskNotFoundError):
        manager.get_task(fake_id)
    with pytest.raises(TaskNotFoundError):
        manager.remove_task(fake_id)
    with pytest.raises(TaskNotFoundError):
        manager.mark_completed(fake_id)
    with pytest.raises(TaskNotFoundError):
        manager.update_task(fake_id, title="nope")
```

To run:

1. `pip install pydantic pytest`
2. `mypy --strict tasks.py`
3. `pytest --maxfail=1 --disable-warnings -q`

All tests should pass, and mypy should report no errors.