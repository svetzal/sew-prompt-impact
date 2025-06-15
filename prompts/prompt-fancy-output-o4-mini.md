Below is a self-contained Python module `tasks.py` plus accompanying tests under `tests/test_tasks.py`. It follows your conventions: 

- 100% type hints (mypy‐strict clean)  
- pydantic models for data  
- pure “core” functions that return new lists  
- an imperative shell (`TaskManager`) that wraps those functions  
- Google-style docstrings  
- ready for pytest, flake8, black  

---

File: tasks.py
```python
from typing import List, Optional, Sequence

from pydantic import BaseModel, Field


class Task(BaseModel):
    """A single task with an auto-assigned ID and completion flag."""

    id: int
    title: str = Field(..., min_length=1)
    description: Optional[str] = None
    completed: bool = False


def _next_id(tasks: Sequence[Task]) -> int:
    """Return the next available task ID."""
    if not tasks:
        return 1
    return max(task.id for task in tasks) + 1


def add_task(
    tasks: Sequence[Task], title: str, description: Optional[str] = None
) -> List[Task]:
    """Return a new list with an added task."""
    new = Task(id=_next_id(tasks), title=title, description=description)
    return list(tasks) + [new]


def remove_task(tasks: Sequence[Task], task_id: int) -> List[Task]:
    """Return a new list with the task of given ID removed.

    Raises:
        ValueError: If no task with `task_id` exists.
    """
    if not any(t.id == task_id for t in tasks):
        raise ValueError(f"No task with id={task_id!r}")
    return [t for t in tasks if t.id != task_id]


def mark_completed(tasks: Sequence[Task], task_id: int) -> List[Task]:
    """Return a new list where the given task is marked completed.

    Raises:
        ValueError: If no task with `task_id` exists.
    """
    found = False
    new_tasks: List[Task] = []
    for t in tasks:
        if t.id == task_id:
            found = True
            new_tasks.append(t.copy(update={"completed": True}))
        else:
            new_tasks.append(t)
    if not found:
        raise ValueError(f"No task with id={task_id!r}")
    return new_tasks


def get_task(tasks: Sequence[Task], task_id: int) -> Task:
    """Retrieve a single task by ID.

    Raises:
        ValueError: If no task with `task_id` exists.
    """
    for t in tasks:
        if t.id == task_id:
            return t
    raise ValueError(f"No task with id={task_id!r}")


def list_tasks(tasks: Sequence[Task]) -> List[Task]:
    """Return tasks in insertion order."""
    return list(tasks)


class TaskManager:
    """Imperative shell around the pure task-list functions."""

    def __init__(self) -> None:
        self._tasks: List[Task] = []

    def add(self, title: str, description: Optional[str] = None) -> Task:
        """Create and store a new task, returning it."""
        self._tasks = add_task(self._tasks, title, description)
        return self._tasks[-1]

    def remove(self, task_id: int) -> None:
        """Remove a task by ID."""
        self._tasks = remove_task(self._tasks, task_id)

    def complete(self, task_id: int) -> Task:
        """Mark a task completed and return its updated version."""
        self._tasks = mark_completed(self._tasks, task_id)
        return get_task(self._tasks, task_id)

    def get(self, task_id: int) -> Task:
        """Retrieve a task by ID."""
        return get_task(self._tasks, task_id)

    def all(self) -> List[Task]:
        """List all tasks."""
        return list_tasks(self._tasks)
```

File: tests/test_tasks.py
```python
import pytest

from tasks import (
    Task,
    TaskManager,
    add_task,
    get_task,
    list_tasks,
    mark_completed,
    remove_task,
)


def test_add_and_list_tasks() -> None:
    tasks: list[Task] = []
    tasks = add_task(tasks, title="Write tests", description="for task manager")
    tasks = add_task(tasks, title="Review code")
    assert len(tasks) == 2
    assert list_tasks(tasks)[0].id == 1
    assert list_tasks(tasks)[1].id == 2


def test_get_task_success_and_failure() -> None:
    tasks = add_task([], title="One")
    t = get_task(tasks, 1)
    assert t.title == "One"
    with pytest.raises(ValueError):
        get_task(tasks, 999)


def test_remove_task() -> None:
    tasks = []
    tasks = add_task(tasks, title="A")
    tasks = add_task(tasks, title="B")
    tasks2 = remove_task(tasks, 1)
    assert len(tasks2) == 1
    assert tasks2[0].id == 2
    with pytest.raises(ValueError):
        remove_task(tasks2, 999)


def test_mark_completed() -> None:
    tasks = []
    tasks = add_task(tasks, title="X")
    assert not tasks[0].completed
    tasks2 = mark_completed(tasks, 1)
    assert tasks2[0].completed is True
    with pytest.raises(ValueError):
        mark_completed(tasks, 999)


def test_task_manager_integration() -> None:
    tm = TaskManager()
    t1 = tm.add("Task1")
    t2 = tm.add("Task2", "desc")
    assert tm.all() == [t1, t2]
    tm.complete(t1.id)
    assert tm.get(t1.id).completed
    tm.remove(t2.id)
    assert [t.id for t in tm.all()] == [t1.id]
```

To run:

1. `pip install pydantic pytest mypy flake8 black`
2. `black . && flake8`
3. `mypy --strict tasks.py tests/test_tasks.py`
4. `pytest`

All tests should pass.