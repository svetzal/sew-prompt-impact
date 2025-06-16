Below is a minimal “functional‐core” Python module plus a pytest suite.  
It manages an in‐memory list of tasks (each task is a frozen dataclass), and exposes pure functions for add/remove/complete/list/clear.  

File: tasks.py  
```python
from dataclasses import dataclass
from typing import List, Optional

@dataclass(frozen=True)
class Task:
    """
    Immutable representation of a single task.
    """
    id: int
    description: str
    completed: bool = False


def add_task(tasks: List[Task], description: str) -> List[Task]:
    """
    Return a new list with a fresh Task appended.
    IDs are assigned incrementally starting at 1.
    """
    next_id = max((t.id for t in tasks), default=0) + 1
    new_task = Task(id=next_id, description=description)
    return tasks + [new_task]


def remove_task(tasks: List[Task], task_id: int) -> List[Task]:
    """
    Return a new list without the Task whose id == task_id.
    """
    return [t for t in tasks if t.id != task_id]


def complete_task(tasks: List[Task], task_id: int) -> List[Task]:
    """
    Return a new list where the matching Task.completed is set to True.
    """
    def _mark(t: Task) -> Task:
        if t.id == task_id:
            return Task(id=t.id, description=t.description, completed=True)
        return t

    return [_mark(t) for t in tasks]


def list_tasks(tasks: List[Task], completed: Optional[bool] = None) -> List[Task]:
    """
    If completed is None, return all tasks.
    Otherwise filter by t.completed == completed.
    """
    if completed is None:
        return tasks[:]
    return [t for t in tasks if t.completed == completed]


def clear_completed(tasks: List[Task]) -> List[Task]:
    """
    Remove all tasks that are already completed.
    """
    return [t for t in tasks if not t.completed]
```

File: test_tasks.py  
```python
import pytest
from tasks import Task, add_task, remove_task, complete_task, list_tasks, clear_completed

@pytest.fixture
def empty_list():
    return []

def test_add_single(empty_list):
    tasks = add_task(empty_list, "Write code")
    assert len(tasks) == 1
    assert tasks[0].id == 1
    assert tasks[0].description == "Write code"
    assert not tasks[0].completed

def test_add_multiple(empty_list):
    t1 = add_task(empty_list, "Task A")
    t2 = add_task(t1, "Task B")
    assert [t.id for t in t2] == [1, 2]

def test_remove_existing():
    tasks = [Task(1, "A"), Task(2, "B")]
    after = remove_task(tasks, 1)
    assert len(after) == 1
    assert after[0].id == 2

def test_remove_nonexistent():
    tasks = [Task(1, "A")]
    # removing a non‐existent id should be a no-op
    assert remove_task(tasks, 42) == tasks

def test_complete_task():
    tasks = [Task(1, "A"), Task(2, "B")]
    updated = complete_task(tasks, 2)
    assert updated[0].completed is False
    assert updated[1].completed is True

def test_list_filtering():
    tasks = [
        Task(1, "A", completed=False),
        Task(2, "B", completed=True),
        Task(3, "C", completed=False),
    ]
    assert list_tasks(tasks) == tasks
    assert [t.id for t in list_tasks(tasks, completed=False)] == [1, 3]
    assert [t.id for t in list_tasks(tasks, completed=True)] == [2]

def test_clear_completed():
    tasks = [
        Task(1, "A", completed=True),
        Task(2, "B", completed=False),
    ]
    cleaned = clear_completed(tasks)
    assert len(cleaned) == 1
    assert cleaned[0].id == 2

def test_id_monotonicity_after_clear():
    # clearing does not reset IDs
    ts = []
    ts = add_task(ts, "A")  # id=1
    ts = add_task(ts, "B")  # id=2
    ts = complete_task(ts, 1)
    ts = clear_completed(ts)
    ts = add_task(ts, "C")
    assert [t.id for t in ts] == [2, 3]
```

To run the tests:

```bash
pip install pytest
pytest -q
```

All tests should pass. You now have a small, pure‐function core for task management; you can wrap it in an I/O layer (e.g. CLI or web) as needed.