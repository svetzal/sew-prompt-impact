Sure! Here's a simple Python module that can manage a list of tasks. It supports adding, removing, listing, and marking tasks as completed.

You can save this as `task_manager.py` and then use it in your projects.

```python
from typing import List, Optional

class Task:
    def __init__(self, description: str):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, description: str):
        task = Task(description)
        self.tasks.append(task)
        print(f"Added task: {description}")

    def remove_task(self, index: int) -> bool:
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"Removed task: {removed.description}")
            return True
        else:
            print("Error: Task index out of range.")
            return False

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for i, task in enumerate(self.tasks):
            print(f"{i}: {task}")

    def mark_task_completed(self, index: int) -> bool:
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print(f"Marked task {index} as completed.")
            return True
        else:
            print("Error: Task index out of range.")
            return False

    def get_tasks(self) -> List[Task]:
        return self.tasks.copy()
```

### Example usage:

```python
if __name__ == "__main__":
    tm = TaskManager()
    tm.add_task("Write report")
    tm.add_task("Do laundry")
    tm.list_tasks()
    tm.mark_task_completed(0)
    tm.list_tasks()
    tm.remove_task(1)
    tm.list_tasks()
```

Let me know if you want me to include saving/loading tasks to a file or any other features!