

```python
import uuid
from enum import Enum
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class Status(Enum):
    """Represents the possible statuses of a task."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class Task(BaseModel):
    """A task with description, status, and creation time."""
    id: str
    description: str
    status: Status
    created_at: datetime

class TaskManager:
    """Manages a list of tasks with CRUD operations."""
    
    def __init__(self):
        """Initialize an empty list of tasks."""
        self.tasks: List[Task] = []
    
    def add_task(self, description: str, status: Status = Status.PENDING) -> Task:
        """Add a new task with the given description and status.
        
        Args:
            description: The task description.
            status: The task status, default is PENDING.
        
        Returns:
            The newly created task.
        """
        task_id = str(uuid.uuid4())
        task = Task(
            id=task_id,
            description=description,
            status=status,
            created_at=datetime.now()
        )
        self.tasks.append(task)
        return task

    def get_task(self, task_id: str) -> Optional[Task]:
        """Retrieve a task by its ID.
        
        Args:
            task_id: The ID of the task to retrieve.
        
        Returns:
            The task if found, else None.
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: str, description: Optional[str] = None, status: Optional[Status] = None) -> bool:
        """Update a task's description and/or status.
        
        Args:
            task_id: The ID of the task to update.
            description: New description (optional).
            status: New status (optional).
        
        Returns:
            True if the task was found and updated, else False.
        """
        for task in self.tasks:
            if task.id == task_id:
                if description:
                    task.description = description
                if status:
                    task.status = status
                return True
        return False

    def delete_task(self, task_id: str) -> bool:
        """Delete a task by its ID.
        
        Args:
            task_id: The ID of the task to delete.
        
        Returns:
            True if the task was deleted, else False.
        """
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                return True
        return False

    def list_tasks(self, status_filter: Optional[Status] = None) -> List[Task]:
        """List all tasks, optionally filtered by status.
        
        Args:
            status_filter: Status to filter by (optional).
        
        Returns:
            A list of tasks matching the filter, or all if none.
        """
        if status_filter:
            return [task for task in self.tasks if task.status == status_filter]
        return self.tasks
```

---

### ✅ Key Features

- **Clean Architecture**: Follows "Functional Core, Imperative Shell" by separating the data model (`Task`) from the imperative logic (`TaskManager`).
- **Strong Typing**: Uses `pydantic.BaseModel` for data validation and `enum.Enum` for status consistency.
- **Testability**: Methods return boolean or task objects, making them easy to verify in unit tests.
- **Minimalism**: Avoids unnecessary abstractions. Each class and method has a single responsibility.

---

### 🧪 Example Usage

```python
manager = TaskManager()
task = manager.add_task("Write documentation")
print(task)
# Output: id='...' description='Write documentation' status='PENDING' created_at='...'
```

---

### 🧠 Design Rationale

- **UUIDs for IDs**: Ensures uniqueness and avoids collisions.
- **Task as a Data Model**: Encapsulates all properties and validation in `Task`, making the system more robust.
- **Imperative Shell**: `TaskManager` handles side-effects (list mutations), while `Task` remains a pure data structure.
- **Docstrings**: Follows Google format, explaining each method's purpose without redundancy.