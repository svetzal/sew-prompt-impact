Certainly! Below is a Python module that manages a list of tasks following the provided conventions and principles. The module includes classes, functions, and type hints for data models using `pydantic.BaseModel`. Additionally, it includes unit tests to ensure correctness.

### `task_manager.py`

```python
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, validator

# Constants
DEFAULT_STATUS = 'pending'
MAX_TASKS = 100


class Task(BaseModel):
    """
    Represents a task with an ID, description, status, and due date.
    
    Attributes:
        id (int): Unique identifier for the task.
        description (str): Description of the task.
        status (str): Status of the task (e.g., 'pending', 'completed').
        due_date (Optional[datetime]): Due date of the task.
    """
    id: int
    description: str
    status: str = DEFAULT_STATUS
    due_date: Optional[datetime] = None

    @validator('status')
    def check_status(cls, v):
        if v not in ['pending', 'completed']:
            raise ValueError("Status must be either 'pending' or 'completed'")
        return v


class TaskManager(BaseModel):
    """
    Manages a list of tasks.
    
    Attributes:
        tasks (List[Task]): List of tasks managed by this instance.
    """
    tasks: List[Task] = []

    def add_task(self, description: str, due_date: Optional[datetime] = None) -> Task:
        """
        Adds a new task to the manager.

        Args:
            description (str): Description of the task.
            due_date (Optional[datetime]): Due date of the task. Defaults to None.

        Returns:
            Task: The newly added task.
        """
        if len(self.tasks) >= MAX_TASKS:
            raise ValueError("Cannot add more tasks, maximum limit reached.")
        
        new_id = max([task.id for task in self.tasks], default=0) + 1
        new_task = Task(id=new_id, description=description, due_date=due_date)
        self.tasks.append(new_task)
        return new_task

    def update_task(self, task_id: int, status: Optional[str] = None, description: Optional[str] = None,
                     due_date: Optional[datetime] = None) -> Task:
        """
        Updates an existing task in the manager.

        Args:
            task_id (int): ID of the task to update.
            status (Optional[str]): New status for the task. Defaults to None.
            description (Optional[str]): New description for the task. Defaults to None.
            due_date (Optional[datetime]): New due date for the task. Defaults to None.

        Returns:
            Task: The updated task.
        """
        task = self._find_task(task_id)
        if status is not None:
            task.status = status
        if description is not None:
            task.description = description
        if due_date is not None:
            task.due_date = due_date
        return task

    def delete_task(self, task_id: int) -> bool:
        """
        Deletes a task from the manager by its ID.

        Args:
            task_id (int): ID of the task to delete.

        Returns:
            bool: True if the task was deleted successfully, False otherwise.
        """
        task = self._find_task(task_id)
        self.tasks.remove(task)
        return True

    def get_tasks(self) -> List[Task]:
        """
        Retrieves all tasks managed by this instance.

        Returns:
            List[Task]: List of tasks.
        """
        return self.tasks

    def _find_task(self, task_id: int) -> Task:
        """
        Finds a task by its ID.

        Args:
            task_id (int): ID of the task to find.

        Returns:
            Task: The found task.

        Raises:
            ValueError: If no task with the given ID is found.
        """
        try:
            return next(task for task in self.tasks if task.id == task_id)
        except StopIteration:
            raise ValueError(f"No task found with ID {task_id}")


# Unit Tests
def test_task_manager():
    # Initialize a TaskManager
    manager = TaskManager()
    
    # Test adding tasks
    task1 = manager.add_task("Write code", datetime(2023, 12, 1))
    assert len(manager.get_tasks()) == 1
    assert task1.id == 1

    task2 = manager.add_task("Test code")
    assert len(manager.get_tasks()) == 2
    assert task2.id == 2

    # Test updating tasks
    updated_task1 = manager.update_task(task1.id, status="completed", due_date=datetime(2023, 12, 2))
    assert updated_task1.status == "completed"
    assert updated_task1.due_date == datetime(2023, 12, 2)

    # Test deleting tasks
    manager.delete_task(task1.id)
    assert len(manager.get_tasks()) == 1

    # Test finding task by ID
    found_task = manager._find_task(task2.id)
    assert found_task.description == "Test code"

    print("All tests passed!")


if __name__ == "__main__":
    test_task_manager()
```

### Explanation:

- **Task Class**: Represents a task with fields `id`, `description`, `status`, and `due_date`. The status is validated to be either 'pending' or 'completed'.
  
- **TaskManager Class**: Manages a list of tasks. It provides methods for adding, updating, deleting, and retrieving tasks.
  
- **Error Handling**: Includes error handling for tasks that do not exist when attempting updates or deletions.

- **Unit Tests**: The `test_task_manager` function includes tests to verify the functionality of the `TaskManager` class.

### How to Run:

1. Install necessary dependencies:
   ```sh
   pip install pydantic
   ```

2. Run the script:
   ```sh
   python task_manager.py
   ```

The output should print "All tests passed!" if everything works correctly. This module adheres to the principles of simplicity, readability, and testability as per your requirements.