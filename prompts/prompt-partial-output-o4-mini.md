Below is a small Python module `tasks.py` plus a suite of tests `test_tasks.py`.  
It follows the principles above (pure-function core in the `TaskManager`, data-only `@dataclass`, no hidden side-effects, executable spec via pytest).

─── tasks.py ───
```python
import uuid
from dataclasses import dataclass, replace
from typing import List, Optional


@dataclass(frozen=True)
class Task:
    """
    Immutable representation of a single task.
    """
    id: str
    title: str
    description: str
    completed: bool = False


class TaskManager:
    """
    In-memory manager for a list of Task objects.
    """

    def __init__(self, tasks: Optional[List[Task]] = None):
        # Always work on our own list
        self._tasks: List[Task] = list(tasks) if tasks else []

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Create a new task and append it.
        Returns the newly created Task.
        """
        new_task = Task(id=str(uuid.uuid4()), title=title, description=description, completed=False)
        self._tasks.append(new_task)
        return new_task

    def get_task(self, task_id: str) -> Task:
        """
        Retrieve a task by its ID. Raises KeyError if not found.
        """
        for t in self._tasks:
            if t.id == task_id:
                return t
        raise KeyError(f"Task with id {task_id!r} not found")

    def update_task(self, task_id: str, *, title: Optional[str] = None, description: Optional[str] = None) -> Task:
        """
        Update title and/or description of a task.
        Unchanged fields can be left as None.
        Returns the updated Task.
        """
        old = self.get_task(task_id)
        new = replace(
            old,
            title=title if title is not None else old.title,
            description=description if description is not None else old.description
        )
        self._replace(old, new)
        return new

    def complete_task(self, task_id: str) -> Task:
        """
        Mark a task as completed. Returns the updated Task.
        """
        old = self.get_task(task_id)
        if old.completed:
            return old
        new = replace(old, completed=True)
        self._replace(old, new)
        return new

    def delete_task(self, task_id: str) -> None:
        """
        Remove a task by ID. Raises KeyError if not found.
        """
        old = self.get_task(task_id)
        self._tasks.remove(old)

    def list_tasks(self, *, completed: Optional[bool] = None) -> List[Task]:
        """
        List all tasks. Optionally filter by completed status.
        """
        if completed is None:
            return list(self._tasks)
        return [t for t in self._tasks if t.completed is completed]

    def _replace(self, old: Task, new: Task) -> None:
        """
        Internal helper to swap one Task for another in-place.
        """
        idx = self._tasks.index(old)
        self._tasks[idx] = new
```

─── test_tasks.py ───
```python
import pytest
from tasks import TaskManager, Task


def test_add_and_list_tasks():
    mgr = TaskManager()
    t1 = mgr.add_task("Wash car")
    t2 = mgr.add_task("Write blog", "About Python")
    all_tasks = mgr.list_tasks()
    assert isinstance(t1, Task)
    assert t1.title == "Wash car"
    assert t1.description == ""
    assert not t1.completed
    # both tasks are present (order preserved)
    assert all_tasks == [t1, t2]


def test_get_task_not_found():
    mgr = TaskManager()
    with pytest.raises(KeyError):
        mgr.get_task("does-not-exist")


def test_update_task_title_and_description():
    mgr = TaskManager()
    t = mgr.add_task("A", "B")
    updated = mgr.update_task(t.id, title="New A", description="New B")
    assert updated.id == t.id
    assert updated.title == "New A"
    assert updated.description == "New B"


def test_update_task_partial():
    mgr = TaskManager()
    t = mgr.add_task("Old", "Desc")
    updated = mgr.update_task(t.id, title="Updated")
    assert updated.title == "Updated"
    assert updated.description == "Desc"


def test_complete_task():
    mgr = TaskManager()
    t = mgr.add_task("Task")
    comp = mgr.complete_task(t.id)
    assert comp.completed is True
    # idempotent
    comp2 = mgr.complete_task(t.id)
    assert comp2.completed is True


def test_delete_task():
    mgr = TaskManager()
    t = mgr.add_task("To be deleted")
    mgr.delete_task(t.id)
    with pytest.raises(KeyError):
        mgr.get_task(t.id)


def test_list_tasks_filtered():
    mgr = TaskManager()
    t1 = mgr.add_task("T1")
    t2 = mgr.add_task("T2")
    mgr.complete_task(t2.id)
    done = mgr.list_tasks(completed=True)
    not_done = mgr.list_tasks(completed=False)
    assert done == [mgr.get_task(t2.id)]
    assert not_done == [mgr.get_task(t1.id)]


def test_initial_tasks_passed_in():
    pre = [Task(id="1", title="X", description="Y", completed=False)]
    mgr = TaskManager(tasks=pre)
    assert mgr.list_tasks() == pre
```

How to run:

1. Save `tasks.py` and `test_tasks.py` in the same folder.
2. `pip install pytest`
3. `pytest`

All tests should pass.