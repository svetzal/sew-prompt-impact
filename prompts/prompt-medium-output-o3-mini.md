Below is a complete Python module that manages a list of tasks. Each task has an auto‑generated ID, a description, and a completed (boolean) status. The module is designed so that its business logic is contained within a pure Python class (TaskManager), which you can import and use from another module or run directly to execute the tests. The tests at the bottom serve as an executable specification of the module's behaviour.

────────────────────────────────────────────
# tasks.py
────────────────────────────────────────────
#!/usr/bin/env python3
"""
A simple task manager module.

This module provides a Task and a TaskManager to create, update, remove,
and list tasks. The design obeys principles like:
 • Code is communication: clear names and comments explain intent.
 • Minimal entities: keep data structures simple.
 • Tests are the executable spec: see __main__ for usage examples/tests.
"""

from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Task:
    """
    A task with a unique id, a description, and a completed flag.
    """
    id: int
    description: str
    completed: bool = field(default=False)

    def __str__(self) -> str:
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.id}: {self.description}"


class TaskManager:
    """
    Manage a list of tasks.

    This class supports adding tasks, removing tasks, marking tasks as completed,
    and listing tasks. The interface clearly reveals intent, and each method
    focuses on a single responsibility.
    """

    def __init__(self) -> None:
        # List to store tasks and a counter for unique ids.
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def add_task(self, description: str) -> Task:
        """
        Add a new task with the given description.
        Returns the created Task.
        """
        task = Task(id=self._next_id, description=description)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def list_tasks(self) -> List[Task]:
        """
        Return a list of all tasks.
        """
        # Return a copy to prevent accidental external modifications.
        return list(self._tasks)

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Retrieve a task by its id.
        Returns the Task if found, otherwise None.
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def remove_task(self, task_id: int) -> bool:
        """
        Remove a task by its id.
        Returns True if a task was removed, else False.
        """
        for index, task in enumerate(self._tasks):
            if task.id == task_id:
                del self._tasks[index]
                return True
        return False

    def complete_task(self, task_id: int) -> bool:
        """
        Mark the task with the given id as completed.
        Returns True if the task was found and marked, else False.
        """
        task = self.get_task(task_id)
        if task is not None:
            task.completed = True
            return True
        return False


# Executable tests: these are the red/green tests that serve as the executable spec
if __name__ == '__main__':
    # Define a simple function to print test results.
    def assert_true(condition: bool, message: str) -> None:
        if not condition:
            raise AssertionError(message)

    print("Running TaskManager tests...")

    # Test 1: Adding tasks
    tm = TaskManager()
    t1 = tm.add_task("Write unit tests")
    t2 = tm.add_task("Commit code")
    tasks = tm.list_tasks()
    assert_true(len(tasks) == 2, "Should have two tasks after adding.")
    assert_true(t1.description == "Write unit tests", "Task 1 description should match.")
    assert_true(t2.id == t1.id + 1, "Task 2 id should be one greater than task 1 id.")

    # Test 2: Completing tasks
    result = tm.complete_task(t1.id)
    assert_true(result, "Completing a valid task should return True.")
    task = tm.get_task(t1.id)
    assert_true(task is not None and task.completed, "Task should be marked as completed.")

    # Test 3: Removing tasks
    removed = tm.remove_task(t1.id)
    assert_true(removed, "Removing an existing task should return True.")
    task = tm.get_task(t1.id)
    assert_true(task is None, "Removed task should not be found.")

    # Test 4: Trying to complete a non-existent task
    result = tm.complete_task(9999)
    assert_true(result is False, "Completing a non-existent task should return False.")

    print("All tests passed!")
    
# End of module
────────────────────────────────────────────

Guidelines followed:
 • The code is simple, minimal and easy to read (reveals intent).
 • Tests at the bottom act as an executable specification.
 • There is no unnecessary duplication and side‑effects are contained.
 • Changes are incremental and individually verifiable.

You can run this module directly (python tasks.py) to verify its correctness,
or import TaskManager and Task into another module for further use.