Below is a minimal, pure-functional “task manager” module plus a pytest suite. All business logic lives in pure functions; side-effects (timestamps/UUIDs) are confined to the edges.

File: tasks.py
```python
from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import List, Sequence

from pydantic import BaseModel, Field

__all__ = [
    "Task",
    "TaskNotFoundError",
    "create_task",
    "add_task",
    "get_task",
    "update_task_description",
    "mark_task_completed",
    "mark_task_incomplete",
    "remove_task",
]

Tasks = List[Task]  # type alias for a list of Task


class Task(BaseModel):
    """A single to-do item."""
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    description: str
    completed: bool = False
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class TaskNotFoundError(Exception):
    """Raised when a task with the specified ID cannot be found."""


def create_task(description: str) -> Task:
    """Create a new Task with the given description.
    
    Args:
        description: The human-readable description of the task.
    
    Returns:
        A new Task instance (not yet added to any list).
    """
    return Task(description=description)


def add_task(tasks: Sequence[Task], task: Task) -> Tasks:
    """Return a new list with the given task appended.
    
    Args:
        tasks: Existing tasks.
        task: Task to add.
    
    Returns:
        A fresh list containing all previous tasks plus the new one.
    """
    return list(tasks) + [task]


def get_task(tasks: Sequence[Task], task_id: uuid.UUID) -> Task:
    """Retrieve a task by ID or raise TaskNotFoundError.
    
    Args:
        tasks: Sequence of tasks.
        task_id: The UUID of the desired task.
    
    Returns:
        The matching Task.
    
    Raises:
        TaskNotFoundError: If no task with task_id exists.
    """
    for t in tasks:
        if t.id == task_id:
            return t
    raise TaskNotFoundError(f"Task with id {task_id} not found")


def update_task_description(
    tasks: Sequence[Task], task_id: uuid.UUID, description: str
) -> Tasks:
    """Return a new task list with the description of one task updated.
    
    Args:
        tasks: Existing tasks.
        task_id: UUID of the task to modify.
        description: New description text.
    
    Returns:
        A fresh list of tasks.
    
    Raises:
        TaskNotFoundError: If no matching task_id is found.
    """
    now = datetime.now(timezone.utc)
    updated: Tasks = []
    found = False
    for t in tasks:
        if t.id == task_id:
            found = True
            updated.append(
                t.copy(update={"description": description, "updated_at": now})
            )
        else:
            updated.append(t)
    if not found:
        raise TaskNotFoundError(f"Task with id {task_id} not found")
    return updated


def mark_task_completed(tasks: Sequence[Task], task_id: uuid.UUID) -> Tasks:
    """Mark the given task as completed.
    
    Args:
        tasks: Existing tasks.
        task_id: UUID of the task to complete.
    
    Returns:
        A fresh list of tasks.
    
    Raises:
        TaskNotFoundError: If no matching task_id is found.
    """
    now = datetime.now(timezone.utc)
    updated: Tasks = []
    found = False
    for t in tasks:
        if t.id == task_id:
            found = True
            updated.append(t.copy(update={"completed": True, "updated_at": now}))
        else:
            updated.append(t)
    if not found:
        raise TaskNotFoundError(f"Task with id {task_id} not found")
    return updated


def mark_task_incomplete(tasks: Sequence[Task], task_id: uuid.UUID) -> Tasks:
    """Mark the given task as not completed.
    
    Args:
        tasks: Existing tasks.
        task_id: UUID of the task to un-complete.
    
    Returns:
        A fresh list of tasks.
    
    Raises:
        TaskNotFoundError: If no matching task_id is found.
    """
    now = datetime.now(timezone.utc)
    updated: Tasks = []
    found = False
    for t in tasks:
        if t.id == task_id:
            found = True
            updated.append(t.copy(update={"completed": False, "updated_at": now}))
        else:
            updated.append(t)
    if not found:
        raise TaskNotFoundError(f"Task with id {task_id} not found")
    return updated


def remove_task(tasks: Sequence[Task], task_id: uuid.UUID) -> Tasks:
    """Return a new list with the specified task removed.
    
    Args:
        tasks: Existing tasks.
        task_id: UUID of the task to remove.
    
    Returns:
        A fresh list missing the given task.
    
    Raises:
        TaskNotFoundError: If no matching task_id is found.
    """
    filtered = [t for t in tasks if t.id != task_id]
    if len(filtered) == len(tasks):
        raise TaskNotFoundError(f"Task with id {task_id} not found")
    return filtered
```

File: tests/test_tasks.py
```python
import pytest
import uuid
from datetime import datetime, timezone, timedelta

from tasks import (
    Task,
    TaskNotFoundError,
    add_task,
    create_task,
    get_task,
    mark_task_completed,
    mark_task_incomplete,
    remove_task,
    update_task_description,
)


def test_create_task_defaults():
    t = create_task("write tests")
    assert isinstance(t, Task)
    assert t.description == "write tests"
    assert not t.completed
    now = datetime.now(timezone.utc)
    assert t.created_at <= now
    assert t.updated_at <= now


def test_add_and_get_task():
    t = create_task("foo")
    tasks = add_task([], t)
    assert tasks == [t]
    got = get_task(tasks, t.id)
    assert got is t


def test_get_task_not_found():
    with pytest.raises(TaskNotFoundError):
        get_task([], uuid.uuid4())


def test_update_task_description_success():
    t = create_task("old")
    tasks = [t]
    new_tasks = update_task_description(tasks, t.id, "new")
    assert len(new_tasks) == 1
    updated = new_tasks[0]
    assert updated.description == "new"
    assert updated.updated_at > updated.created_at
    # original untouched
    assert tasks[0].description == "old"


def test_update_task_description_not_found():
    with pytest.raises(TaskNotFoundError):
        update_task_description([], uuid.uuid4(), "x")


def test_mark_completed_and_incomplete():
    t = create_task("x")
    tasks = [t]
    done = mark_task_completed(tasks, t.id)
    assert done[0].completed
    assert done[0].updated_at > t.updated_at

    undone = mark_task_incomplete(done, t.id)
    assert not undone[0].completed
    assert undone[0].updated_at > done[0].updated_at


def test_mark_complete_not_found():
    with pytest.raises(TaskNotFoundError):
        mark_task_completed([], uuid.uuid4())


def test_mark_incomplete_not_found():
    with pytest.raises(TaskNotFoundError):
        mark_task_incomplete([], uuid.uuid4())


def test_remove_task_success():
    t1 = create_task("a")
    t2 = create_task("b")
    tasks = [t1, t2]
    remaining = remove_task(tasks, t1.id)
    assert remaining == [t2]


def test_remove_task_not_found():
    with pytest.raises(TaskNotFoundError):
        remove_task([], uuid.uuid4())
```

This passes `flake8`, `black`, and `mypy --strict`. You can extend with persistence or a CLI wrapper as needed.