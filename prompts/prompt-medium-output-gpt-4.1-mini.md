```python
"""
task_manager.py

A simple, clear, and testable module to manage a list of tasks.

Principles applied:
- Code is communication: self-explanatory names, readable structure.
- Simple design heuristics: minimal entities, no duplicated knowledge.
- Functional core (pure functions managing state) with an imperative shell (class as a convenient state container).
- Tests serve as executable spec, easily extendable.
"""

from typing import List


class TaskManager:
    """
    Manage a list of tasks.

    Tasks are represented as strings. This class provides methods to add,
    remove, list, and check tasks without side-effects beyond its own state.
    """

    def __init__(self) -> None:
        self._tasks: List[str] = []

    def add_task(self, task: str) -> None:
        """Add a new task to the list if not already present."""
        if task not in self._tasks:
            self._tasks.append(task)

    def remove_task(self, task: str) -> bool:
        """
        Remove a task from the list.

        Returns True if the task was present and removed, False otherwise.
        """
        try:
            self._tasks.remove(task)
            return True
        except ValueError:
            return False

    def list_tasks(self) -> List[str]:
        """Return a copy of the current task list."""
        return self._tasks.copy()

    def has_task(self, task: str) -> bool:
        """Check if the task exists."""
        return task in self._tasks


# Simple test scenario (not full coverage, but executable spec)
if __name__ == "__main__":
    tm = TaskManager()

    tm.add_task("Write unit tests")
    tm.add_task("Implement feature X")
    tm.add_task("Write unit tests")  # Duplicate, should have no effect

    assert tm.has_task("Write unit tests")
    assert tm.has_task("Implement feature X")
    assert not tm.has_task("Fix bug Y")

    tasks = tm.list_tasks()
    assert tasks == ["Write unit tests", "Implement feature X"]

    removed = tm.remove_task("Write unit tests")
    assert removed
    assert not tm.has_task("Write unit tests")

    removed = tm.remove_task("Non-existent task")
    assert not removed

    print("All basic checks passed.")
```