

```python
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field

class Task(BaseModel):
    """Represents a task with a unique identifier, description, completion status, and creation timestamp."""
    id: Optional[int] = None
    description: str
    completed: bool = False
    created_at: datetime = Field(default_factory=datetime.now)

class TaskManager:
    """Manages a collection of tasks with CRUD operations."""
    def __init__(self):
        """Initialize an empty task list and an ID counter."""
        self.tasks: List[Task] = []
        self._next_id: int = 1

    def add_task(self, description: str, completed: bool = False) -> Task:
        """Add a new task to the manager.

        Args:
            description (str): Description of the task.
            completed (bool, optional): Whether the task is completed. Defaults to False.

        Returns:
            Task: The newly created task with an assigned ID.
        """
        task = Task(id=self._next_id, description=description, completed=completed)
        self._next_id += 1
        self.tasks.append(task)
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """Retrieve a task by its ID.

        Args:
            task_id (int): The unique identifier of the task.

        Returns:
            Optional[Task]: The task if found, otherwise None.
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, description: Optional[str] = None, completed: Optional[bool] = None) -> Optional[Task]:
        """Update a task's description or completion status.

        Args:
            task_id (int): The unique identifier of the task.
            description (Optional[str], optional): New description. Defaults to None.
            completed (Optional[bool], optional): New completion status. Defaults to None.

        Returns:
            Optional[Task]: The updated task if found, otherwise None.
        """
        task = self.get_task(task_id)
        if task:
            if description is not None:
                task.description = description
            if completed is not None:
                task.completed = completed
            return task
        return None

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by its ID.

        Args:
            task_id (int): The unique identifier of the task.

        Returns:
            bool: True if the task was deleted, False otherwise.
        """
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def list_tasks(self) -> List[Task]:
        """List all tasks managed by this instance.

        Returns:
            List[Task]: A list of all tasks.
        """
        return self.tasks
```