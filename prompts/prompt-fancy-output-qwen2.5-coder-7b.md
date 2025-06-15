Sure! Below is a Python module named `task_manager.py` that manages a list of tasks. This module includes functionalities to add, update, remove, and list tasks. It also uses type hints and follows the best practices mentioned in your guidelines.

```python
# task_manager.py

from typing import List, Optional
from pydantic import BaseModel, validator
import uuid

class Task(BaseModel):
    id: str = None
    description: str
    completed: bool = False
    
    @validator('id', pre=True)
    def generate_id(cls, v):
        if not v:
            return str(uuid.uuid4())
        return v

def add_task(tasks: List[Task], description: str) -> List[Task]:
    """Add a new task to the list."""
    new_task = Task(description=description)
    tasks.append(new_task)
    return tasks

def update_task(tasks: List[Task], task_id: str, completed: Optional[bool] = None, description: Optional[str] = None) -> List[Task]:
    """Update an existing task."""
    for task in tasks:
        if task.id == task_id:
            if completed is not None:
                task.completed = completed
            if description is not None:
                task.description = description
            break
    return tasks

def remove_task(tasks: List[Task], task_id: str) -> List[Task]:
    """Remove a task by ID."""
    tasks = [task for task in tasks if task.id != task_id]
    return tasks

def list_tasks(tasks: List[Task]) -> None:
    """List all tasks."""
    print("Tasks:")
    for task in tasks:
        status = "Completed" if task.completed else "Pending"
        print(f"{task.id} - {task.description} ({status})")

# Example usage
if __name__ == "__main__":
    tasks: List[Task] = []

    tasks = add_task(tasks, description="Buy groceries")
    tasks = update_task(tasks, task_id=tasks[-1].id, completed=True)
    tasks = remove_task(tasks, task_id=tasks[-1].id)
    list_tasks(tasks)
```

### Explanation:

1. **Task Model**: The `Task` class uses Pydantic to define the structure of a task with validation for its fields. It includes an `id` which is auto-generated if not provided.

2. **Functions**:
   - `add_task`: Adds a new task to the list.
   - `update_task`: Updates the properties of an existing task by ID.
   - `remove_task`: Removes a task from the list by ID.
   - `list_tasks`: Prints all tasks in the list, showing their status.

3. **Example Usage**: The example usage at the bottom demonstrates how to use these functions.

### Testing:

To ensure correctness and maintainability, you can write tests for each function. Here's an example using `pytest`:

```python
# test_task_manager.py

from task_manager import Task, add_task, update_task, remove_task, list_tasks

def test_add_task():
    tasks = []
    tasks = add_task(tasks, description="Buy groceries")
    assert len(tasks) == 1
    assert tasks[0].description == "Buy groceries"
    assert tasks[0].completed == False

def test_update_task():
    tasks = [Task(description="Buy groceries")]
    tasks = update_task(tasks, task_id=tasks[0].id, completed=True)
    assert tasks[0].completed == True

def test_remove_task():
    tasks = [Task(description="Buy groceries")]
    tasks = remove_task(tasks, task_id=tasks[0].id)
    assert len(tasks) == 0

def test_list_tasks(capsys):
    tasks = [Task(description="Buy groceries"), Task(description="Clean the house", completed=True)]
    list_tasks(tasks)
    captured = capsys.readouterr()
    assert "Tasks:" in captured.out
    assert "Buy groceries" in captured.out
    assert "Clean the house (Completed)" in captured.out
```

### Running Tests:

You can run the tests using the following command:
```sh
pytest test_task_manager.py
```

This ensures that your code behaves as expected and follows the best practices outlined in the guidelines.