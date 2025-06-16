```python
from typing import List, Optional

class Task:
    """Represents a task with an ID, description, and completion status."""
    
    def __init__(self, task_id: int, description: str):
        self.id = task_id
        self.description = description
        self.completed = False

    def __repr__(self):
        return f"Task(id={self.id}, description='{self.description}', completed={self.completed})"


class TaskManager:
    """
    Manages a collection of tasks, providing methods to add, remove, update, and filter tasks.
    """

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description: str) -> int:
        """
        Adds a new task with the given description.
        
        Returns:
            int: The ID of the newly created task.
        """
        task = Task(self.next_id, description)
        self.tasks.append(task)
        self.next_id += 1
        return task.id

    def remove_task(self, task_id: int) -> bool:
        """
        Removes a task by its ID.
        
        Args:
            task_id: The ID of the task to remove.
        
        Returns:
            bool: True if the task was removed, False if not found.
        """
        initial_length = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.id != task_id]
        return len(self.tasks) != initial_length

    def mark_complete(self, task_id: int) -> bool:
        """
        Marks a task as completed by its ID.
        
        Args:
            task_id: The ID of the task to mark as complete.
        
        Returns:
            bool: True if the task was found and updated, False otherwise.
        """
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                return True
        return False

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Retrieves a task by its ID.
        
        Args:
            task_id: The ID of the task to retrieve.
        
        Returns:
            Task: The task object if found, None otherwise.
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def list_tasks(self, filter_by: Optional[str] = None) -> List[Task]:
        """
        Lists tasks, optionally filtered by status.
        
        Args:
            filter_by: If 'completed', returns only completed tasks; if 'active', returns only uncompleted tasks. If None, returns all tasks.
        
        Returns:
            List[Task]: A list of tasks based on the filter.
        
        Raises:
            ValueError: If an invalid filter is provided.
        """
        if filter_by is None:
            return self.tasks
        elif filter_by == 'completed':
            return [task for task in self.tasks if task.completed]
        elif filter_by == 'active':
            return [task for task in self.tasks if not task.completed]
        else:
            raise ValueError("Invalid filter: must be 'completed', 'active', or None")


# Example Usage
if __name__ == "__main__":
    tm = TaskManager()
    task_id = tm.add_task("Buy groceries")
    print(f"Added task {task_id}: {tm.get_task(task_id)}")
    tm.mark_complete(task_id)
    print("Completed tasks:", tm.list_tasks("completed"))
    print("Active tasks:", tm.list_tasks("active"))
```

---

### ✅ Key Design Decisions

- **Task Abstraction**: A dedicated `Task` class encapsulates the data (ID, description, completion status), making the domain model clear and reusable.

- **Minimal Entities**: The `TaskManager` uses simple data structures (lists) to minimize complexity and avoid unnecessary indirection.

- **Reveals Intent**: Method names (`add_task`, `mark_complete`, `list_tasks`) clearly express their purpose.

- **Testable Interface**: The methods are side-effect-free (except for `add_task`, which must mutate state) and can be verified via unit tests.

- **Filtering Support**: The `list_tasks` method allows filtering by status, improving flexibility.

- **Robustness**: Error handling (e.g., checking if a task exists) ensures safe usage.

---

### 🧪 Test Suggestions (for future)

```python
def test_add_and_retrieve():
    tm = TaskManager()
    task_id = tm.add_task("Test task")
    assert tm.get_task(task_id).description == "Test task"

def test_mark_complete():
    tm = TaskManager()
    task_id = tm.add_task("Another task")
    tm.mark_complete(task_id)
    assert tm.get_task(task_id).completed is True

def test_remove_task():
    tm = TaskManager()
    task_id = tm.add_task("To be removed")
    assert tm.remove_task(task_id) is True
    assert tm.get_task(task_id) is None
```

This module is designed to be extensible (e.g., adding due dates, priority levels) while keeping the core functionality clear and maintainable.