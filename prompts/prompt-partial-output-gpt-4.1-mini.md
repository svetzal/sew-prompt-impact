Here's a Python module implementing a simple but clear task manager following the baseline conventions described. It uses pure functions for core logic, minimal classes, and keeps side effects at the boundaries (in this case, printing or data persistence can be added externally).

```python
"""
task_manager.py

Provides functions to manage a list of tasks.

A task is represented as a dictionary with keys:
  - id: int
  - description: str
  - done: bool
"""

from typing import List, Dict, Optional

Task = Dict[str, object]


def add_task(tasks: List[Task], description: str) -> List[Task]:
    """
    Returns a new task list with the new task added.

    New task IDs start at 1 and increment by 1 from the max existing ID.

    Args:
        tasks: Current list of tasks.
        description: Description of the new task.

    Returns:
        New list of tasks including the new task.
    """
    next_id = 1 + max((task['id'] for task in tasks), default=0)
    new_task = {'id': next_id, 'description': description, 'done': False}
    return tasks + [new_task]


def remove_task(tasks: List[Task], task_id: int) -> List[Task]:
    """
    Returns a new task list with the task of given ID removed.

    If no task with task_id exists, returns tasks unchanged.

    Args:
        tasks: Current list of tasks.
        task_id: ID of the task to remove.

    Returns:
        New list of tasks excluding the removed task.
    """
    return [task for task in tasks if task['id'] != task_id]


def mark_done(tasks: List[Task], task_id: int) -> List[Task]:
    """
    Returns a new task list with the task marked as done.

    If no task with task_id exists, returns tasks unchanged.

    Args:
        tasks: Current list of tasks.
        task_id: ID of the task to mark done.

    Returns:
        New list of tasks with task marked done.
    """
    def mark_task_done(task: Task) -> Task:
        if task['id'] == task_id:
            return {**task, 'done': True}
        else:
            return task

    return [mark_task_done(task) for task in tasks]


def mark_undone(tasks: List[Task], task_id: int) -> List[Task]:
    """
    Returns a new task list with the task marked as not done.

    If no task with task_id exists, returns tasks unchanged.

    Args:
        tasks: Current list of tasks.
        task_id: ID of the task to mark undone.

    Returns:
        New list of tasks with task marked undone.
    """
    def mark_task_undone(task: Task) -> Task:
        if task['id'] == task_id:
            return {**task, 'done': False}
        else:
            return task

    return [mark_task_undone(task) for task in tasks]


def find_task(tasks: List[Task], task_id: int) -> Optional[Task]:
    """
    Finds and returns the task with the given ID.

    Returns None if no such task exists.

    Args:
        tasks: Current list of tasks.
        task_id: ID to find.

    Returns:
        Task dictionary or None.
    """
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None


def list_tasks(tasks: List[Task], done: Optional[bool] = None) -> List[Task]:
    """
    Returns tasks optionally filtered by done status.

    Args:
        tasks: Current list of tasks.
        done: If None, return all tasks; if True or False, filter by done.

    Returns:
        Filtered list of tasks.
    """
    if done is None:
        return list(tasks)
    return [task for task in tasks if task['done'] == done]
```

---

If you want I can add usage examples or tests next.