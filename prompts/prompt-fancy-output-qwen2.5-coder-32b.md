Certainly! Below is a Python module designed to manage a list of tasks. This module adheres to the principles and conventions you've specified, including naming conventions, type hints, docstrings, and more.

```python
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, validator

# Data model for a task using Pydantic for validation
class Task(BaseModel):
    id: int
    title: str
    description: str = ""
    due_date: Optional[datetime] = None
    completed: bool = False

    @validator('id')
    def check_id(cls, v):
        if v < 0:
            raise ValueError('ID must be a non-negative integer.')
        return v


class TaskManager(BaseModel):
    tasks: List[Task] = []

    def add_task(self, title: str, description: str = "", due_date: Optional[datetime] = None) -> None:
        """
        Adds a new task to the list.

        Args:
            title (str): The title of the task.
            description (str): A detailed description of the task. Defaults to an empty string.
            due_date (Optional[datetime]): The due date for the task. Defaults to None.
        """
        if not self.tasks:
            new_id = 0
        else:
            new_id = max(task.id for task in self.tasks) + 1

        new_task = Task(id=new_id, title=title, description=description, due_date=due_date)
        self.tasks.append(new_task)

    def complete_task(self, task_id: int) -> None:
        """
        Marks a task as completed.

        Args:
            task_id (int): The ID of the task to mark as completed.
        """
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                return

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Retrieves a task by its ID.

        Args:
            task_id (int): The ID of the task to retrieve.

        Returns:
            Optional[Task]: The Task object if found; otherwise, None.
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def list_tasks(self) -> List[Task]:
        """
        Lists all tasks.

        Returns:
            List[Task]: A list of all tasks.
        """
        return self.tasks

    def remove_task(self, task_id: int) -> None:
        """
        Removes a task from the list by its ID.

        Args:
            task_id (int): The ID of the task to remove.
        """
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                return

    def __str__(self) -> str:
        """
        Returns a string representation of all tasks.

        Returns:
            str: A formatted string of all tasks.
        """
        tasks_str = "\n".join(str(task) for task in self.tasks)
        return f"TaskManager:\n{tasks_str}"
```

### Explanation:

1. **Task Model**:
   - The `Task` class is a Pydantic model with fields: `id`, `title`, `description`, `due_date`, and `completed`.
   - Validation is ensured using the `@validator` decorator for the `id` field to ensure it's non-negative.

2. **TaskManager Class**:
   - This class manages a list of tasks.
   - Methods provided include: 
     - `add_task`: Adds a new task with an auto-generated ID.
     - `complete_task`: Marks a task as completed using its ID.
     - `get_task`: Retrieves a task by its ID.
     - `list_tasks`: Returns all tasks.
     - `remove_task`: Removes a task by its ID.
     - `__str__`: Provides a string representation of the manager's tasks.

### Usage Example:

```python
# Create a TaskManager instance
task_manager = TaskManager()

# Add some tasks
task_manager.add_task(title="Read a book", description="Finish reading 'Python Programming'.")
task_manager.add_task(title="Write a report", due_date=datetime(2023, 12, 31))

# List all tasks
print(task_manager)

# Complete a task
task_manager.complete_task(task_id=0)

# Print the updated list of tasks
print(task_manager)
```

### Notes:
- The module adheres to the principles mentioned: code readability, simplicity, and testability.
- Type hints are used extensively for clarity and validation with `mypy`.
- No magic numbers or duplicate code are present.

You can run this code in a Python environment that supports Pydantic. If you need more features like persistence or integration with other systems, let me know!