Creating a simple Python module to manage a list of tasks is a great way to incorporate the baseline conventions you've outlined. Below is a basic implementation that adheres to these engineering principles.

```python
from typing import List, Optional


class Task:
    def __init__(self, description: str, completed: bool = False):
        self.description = description
        self.completed = completed

    def __str__(self):
        return f'[{"x" if self.completed else " "}] {self.description}'

    def mark_completed(self):
        """Mark this task as completed."""
        self.completed = True


class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, description: str):
        """Add a new task to the list."""
        if not description:
            raise ValueError("Task description cannot be empty")
        self.tasks.append(Task(description))

    def remove_task(self, index: int) -> Optional[str]:
        """Remove a task by its index and return its description, or none if the index is invalid."""
        if 0 <= index < len(self.tasks):
            return self.tasks.pop(index).description
        return None

    def mark_task_completed(self, index: int):
        """Mark a task as completed if the index is valid."""
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()

    def list_tasks(self) -> List[str]:
        """Return a list of task descriptions."""
        return [str(task) for task in self.tasks]


def main():
    manager = TaskManager()

    # Add example tasks
    manager.add_task("Write unit tests")
    manager.add_task("Document code")
    manager.add_task("Review pull requests")

    # Mark the second task as completed
    manager.mark_task_completed(1)

    # List all tasks
    for idx, task in enumerate(manager.list_tasks()):
        print(f"{idx}: {task}")

    # Remove a task
    removed_task = manager.remove_task(2)
    if removed_task:
        print(f"Removed task: {removed_task}")
    else:
        print("Task not found")


if __name__ == "__main__":
    main()
```

### Key Implementation Details:

1. **Code is communication**: Comments and method names aim to make the code self-explanatory.
2. **Simple Design Heuristics**:
   - All tests pass: Though tests aren't included here, it's assumed they would be implemented in a separate test suite.
   - Reveals intent: The methods and class are named to reflect their intentions clearly.
   - No knowledge duplication: Avoided by centralizing task-related operations within the `Task` and `TaskManager` classes.
   - Minimal entities: Only essential classes (`Task` and `TaskManager`) and methods are included.
3. **Compose over inherit**: Used composition with a list of `Task` objects.
4. **Functional core, imperative shell**: Business logic handled by methods, minimal I/O in the `main` function.
5. **Version-control etiquette**: If integrating into a larger project, maintain structured commits and follow branching strategies.

This module provides basic operations to manage tasks, aligning with the outlined engineering principles. Further expansion could include adding persistence (e.g., saving/loading tasks to/from a file), refining CLI inputs, or extending with more features while keeping in mind psychological safety and best practices.