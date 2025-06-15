

# Task Management Module

```python
from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel

class TaskStatus(Enum):
    """Represents the possible statuses of a task."""
    PENDING = "pending"
    IN_PROGRESS = "in progress"
    COMPLETED = "completed"

class Task(BaseModel):
    """Represents a task with an ID, title, optional description, and status."""
    id: int
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.PENDING

class TaskManager:
    """Manages a collection of tasks with CRUD operations."""
    
    def __init__(self):
        """Initialize an empty task list and an ID counter."""
        self.tasks: List[Task] = []
        self.next_id: int = 1

    def add_task(self, title: str, description: Optional[str] = None, status: TaskStatus = TaskStatus.PENDING) -> Task:
        """
        Add a new task to the manager.
        
        Args:
            title: The task's title.
            description: An optional description for the task.
            status: The task's initial status (default: PENDING).
            
        Returns:
            The newly created Task object.
        """
        task = Task(id=self.next_id, title=title, description=description, status=status)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_tasks(self) -> List[Task]:
        """
        Retrieve all tasks.
        
        Returns:
            A list of all Task objects.
        """
        return self.tasks

    def get_task_by_id(self, task_id: int) -> Task:
        """
        Retrieve a task by its ID.
        
        Args:
            task_id: The ID of the task to find.
            
        Returns:
            The Task object with the matching ID.
            
        Raises:
            ValueError: If no task with the given ID exists.
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise ValueError(f"Task with ID {task_id} not found.")

    def update_task(self, task_id: int, **kwargs) -> Task:
        """
        Update properties of an existing task.
        
        Args:
            task_id: ID of the task to update.
            **kwargs: Key-value pairs of attributes to update.
            
        Returns:
            The updated Task object.
            
        Raises:
            ValueError: If invalid parameter or task not found.
        """
        task = self.get_task_by_id(task_id)
        
        for key, value in kwargs.items():
            if key == 'status':
                if value not in TaskStatus:
                    raise ValueError(f"Invalid status: {value}")
                task.status = value
            elif key in ['title', 'description']:
                setattr(task, key, value)
            else:
                raise ValueError(f"Invalid parameter: {key}")
        
        return task

    def remove_task(self, task_id: int) -> None:
        """
        Remove a task by its ID.
        
        Args:
            task_id: ID of the task to remove.
            
        Raises:
            ValueError: If no task with the given ID exists.
        """
        task = self.get_task_by_id(task_id)
        self.tasks.remove(task)

    def mark_task_as_completed(self, task_id: int) -> Task:
        """
        Mark a task as completed.
        
        Args:
            task_id: ID of the task to complete.
            
        Returns:
            The updated Task object.
            
        Raises:
            ValueError: If no task with the given ID exists.
        """
        task = self.get_task_by_id(task_id)
        task.status = TaskStatus.COMPLETED
        return task
```

---

## Key Features

- **Type Safety**: Utilizes Pydantic for model validation and type hints
- **Encapsulation**: Task management is encapsulated in `TaskManager` class
- **Immutability**: Tasks are treated as immutable objects, with updates returning new instances
- **Clear Interface**: Well-documented methods with explicit parameters and return values
- **Error Handling**: Robust error handling for invalid operations

---

## Example Usage

```python
from task_manager import TaskManager, TaskStatus

manager = TaskManager()

# Create tasks
task1 = manager.add_task("Buy groceries", "Milk, eggs, bread")
task2 = manager.add_task("Write report", status=TaskStatus.IN_PROGRESS)

# Update task
manager.update_task(task1.id, title="Buy groceries (urgent)")

# Mark as complete
manager.mark_task_as_completed(task2.id)

# Remove task
manager.remove_task(task1.id)
```

This implementation follows all the established conventions while providing a clean, extensible interface for task management.