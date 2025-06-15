```python
from typing import List, Optional
from pydantic import BaseModel


class Task(BaseModel):
    """
    Represents a single task.

    Attributes:
        id: Unique identifier for the task.
        description: Description of the task.
        is_completed: Completion status of the task.
    """
    id: int
    description: str
    is_completed: bool = False


class TaskManager:
    """
    Manages a list of tasks, providing operations to add, remove, and update tasks.
    """

    def __init__(self):
        """
        Initializes an empty task list and internal ID counter.
        """
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def add_task(self, description: str) -> Task:
        """
        Adds a new task with the given description.

        Args:
            description: Text describing the task.

        Returns:
            The created Task instance.
        """
        task = Task(id=self._next_id, description=description)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def remove_task(self, task_id: int) -> bool:
        """
        Removes a task by its ID.

        Args:
            task_id: The ID of the task to remove.

        Returns:
            True if a task was removed, False otherwise.
        """
        for index, task in enumerate(self._tasks):
            if task.id == task_id:
                del self._tasks[index]
                return True
        return False

    def toggle_task_completion(self, task_id: int) -> bool:
        """
        Toggles the completion status of a task.

        Args:
            task_id: The ID of the task to toggle.

        Returns:
            True if the task was found and toggled, False otherwise.
        """
        for index, task in enumerate(self._tasks):
            if task.id == task_id:
                updated_task = task.copy(update={'is_completed': not task.is_completed})
                self._tasks[index] = updated_task
                return True
        return False

    def get_tasks(self, completed: Optional[bool] = None) -> List[Task]:
        """
        Retrieves tasks, optionally filtered by completion status.

        Args:
            completed: If specified, filters tasks by their completion status.

        Returns:
            List of tasks matching the filter.
        """
        if completed is None:
            return list(self._tasks)
        return [task for task in self._tasks if task.is_completed == completed]
```