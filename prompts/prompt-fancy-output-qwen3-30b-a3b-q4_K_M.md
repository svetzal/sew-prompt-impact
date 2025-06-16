```python
import uuid
from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional

class Task(BaseModel):
    """
    Represents a task with a unique identifier, description, completion status, and creation timestamp.

    Attributes:
        id (str): Unique identifier for the task.
        description (str): Description of the task.
        done (bool): Indicates if the task is completed.
        created_at (datetime): Timestamp when the task was created.
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    description: str
    done: bool = False
    created_at: datetime = Field(default_factory=datetime.now)

class TaskManager:
    """
    Manages a collection of tasks with functionality to add, retrieve, update, delete, and filter tasks.

    Methods:
        add_task(description: str) -> Task
        get_task(task_id: str) -> Optional[Task]
        update_task(task_id: str, description: str = None, done: bool = None) -> Optional[Task]
        delete_task(task_id: str) -> bool
        list_tasks(filter_by: str = None) -> List[Task]
    """

    def __init__(self):
        """
        Initializes an empty list of tasks.
        """
        self.tasks: List[Task] = []

    def add_task(self, description: str) -> Task:
        """
        Adds a new task with the specified description.

        Args:
            description (str): The task's description.

        Returns:
            Task: The newly created task.
        """
        task = Task(description=description)
        self.tasks.append(task)
        return task

    def get_task(self, task_id: str) -> Optional[Task]:
        """
        Retrieves a task by its ID.

        Args:
            task_id (str): Unique identifier of the task.

        Returns:
            Optional[Task]: The task if found, otherwise None.
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: str, description: str = None, done: bool = None) -> Optional[Task]:
        """
        Updates a task's description or completion status.

        Args:
            task_id (str): Unique identifier of the task.
            description (str, optional): New description for the task.
            done (bool, optional): New completion status for the task.

        Returns:
            Optional[Task]: The updated task if found, otherwise None.
        """
        task = self.get_task(task_id)
        if not task:
            return None
        if description is not None:
            task.description = description
        if done is not None:
            task.done = done
        return task

    def delete_task(self, task_id: str) -> bool:
        """
        Deletes a task by its ID.

        Args:
            task_id (str): Unique identifier of the task.

        Returns:
            bool: True if the task was successfully deleted, False otherwise.
        """
        task = self.get_task(task_id)
        if not task:
            return False
        self.tasks.remove(task)
        return True

    def list_tasks(self, filter_by: str = None) -> List[Task]:
        """
        Lists tasks, optionally filtered by their completion status.

        Args:
            filter_by (str, optional): 'done' or 'pending' to filter the tasks.

        Returns:
            List[Task]: A list of tasks, filtered if specified.
        """
        if filter_by is None:
            return self.tasks
        if filter_by == 'done':
            return [task for task in self.tasks if task.done]
        elif filter_by == 'pending':
            return [task for task in self.tasks if not task.done]
        else:
            return self.tasks
```

---

### 📌 Notes on Compliance with Conventions

- **Code as Communication**: Methods and attributes are named to clearly communicate their purpose.
- **Simple Design**: The module uses minimal entities, focusing on the core logic without unnecessary abstraction.
- **Tests as the Executable Spec**: While not included here, the module is structured to support writing unit tests easily.
- **Type Hints**: All types are annotated for clarity and correctness.
- **Docstrings**: Follow Google format, explaining what each method does without repeating obvious details.
- **Functional Core, Imperative Shell**: The `TaskManager` handles state changes (imperative), while the `Task` model represents the pure data structure.

This module is ready to be used in a larger application or to build upon with additional features.