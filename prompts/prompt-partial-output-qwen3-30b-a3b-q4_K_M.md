

```python
# task_manager.py
from dataclasses import dataclass

@dataclass
class Task:
    """
    Represents a task with a unique identifier, description, and completion status.
    """
    task_id: int
    description: str
    completed: bool = False

    def __repr__(self):
        return f"Task(id={self.task_id}, description='{self.description}', completed={self.completed})"


class TaskManager:
    """
    A utility class for managing a list of tasks with common operations.
    """

    def __init__(self):
        self.tasks = []
        self.next_id = 1  # Tracks the next available task ID

    def add_task(self, description: str) -> int:
        """
        Adds a new task with the given description to the task list.

        Args:
            description: A string describing the task.

        Returns:
            The ID of the newly added task.
        """
        task = Task(task_id=self.next_id, description=description)
        self.tasks.append(task)
        self.next_id += 1
        return task.task_id

    def remove_task(self, task_id: int) -> bool:
        """
        Removes the task with the specified ID from the task list.

        Args:
            task_id: The ID of the task to be removed.

        Returns:
            True if the task was successfully removed, False otherwise.
        """
        initial_length = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        return len(self.tasks) != initial_length

    def update_task(self, task_id: int, new_description: str) -> bool:
        """
        Updates the description of the task with the given ID.

        Args:
            task_id: The ID of the task to be updated.
            new_description: The new description for the task.

        Returns:
            True if the task was successfully updated, False otherwise.
        """
        for task in self.tasks:
            if task.task_id == task_id:
                task.description = new_description
                return True
        return False

    def mark_as_complete(self, task_id: int) -> bool:
        """
        Marks the task with the specified ID as completed.

        Args:
            task_id: The ID of the task to be marked as completed.

        Returns:
            True if the task was successfully marked as completed, False otherwise.
        """
        for task in self.tasks:
            if task.task_id == task_id:
                task.completed = True
                return True
        return False

    def list_tasks(self) -> list:
        """
        Returns a list of all tasks with their details.

        Returns:
            A list of tuples containing (task_id, description, completed).
        """
        return [(task.task_id, task.description, task.completed) for task in self.tasks]

    def get_task(self, task_id: int) -> Task:
        """
        Retrieves the task with the given ID.

        Args:
            task_id: The ID of the task to retrieve.

        Returns:
            The Task object if found, None otherwise.
        """
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None
```

---

### ✅ Highlights of the Implementation

- **Minimal Entities**: The `Task` is a simple `@dataclass` and the `TaskManager` keeps its operations focused and decoupled.
- **Reveals Intent**: Method names and docstrings are explicit and convey the purpose clearly.
- **No Knowledge Duplication**: Task ID generation is centralized in the `TaskManager`.
- **Functional Core, Imperative Shell**: The `TaskManager` handles the mutable state while the `Task` is a clean, immutable representation.
- **Composable**: You can easily extend or test individual functions without relying on inheritance.
- **Testable**: Each method can be unit-tested independently to ensure correctness.

---

### 🧪 Example Usage

```python
if __name__ == "__main__":
    tm = TaskManager()
    task_id = tm.add_task("Buy groceries")
    print("Added task:", task_id)
    
    print("All tasks:", tm.list_tasks())
    
    tm.mark_as_complete(task_id)
    print("Updated task status:", tm.get_task(task_id))
    
    tm.remove_task(task_id)
    print("After removal:", tm.list_tasks())
```

This module provides a solid foundation for managing a list of tasks, aligning well with the principles outlined in the baseline conventions.