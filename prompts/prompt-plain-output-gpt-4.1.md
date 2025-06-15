Here’s a Python module named `task_manager.py` that allows you to manage a list of tasks. Tasks can be added, removed, marked as completed, and you can list all tasks or pending tasks. It uses a simple in-memory list. If you want, the module can be extended for saving to files or other persistence.

**task_manager.py**:

```python
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        """Add a new task by description."""
        task = Task(description)
        self.tasks.append(task)
        return task

    def remove_task(self, index):
        """Remove task by its index."""
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            return removed
        raise IndexError("No task at the specified index.")

    def complete_task(self, index):
        """Mark a task as complete by index."""
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            return self.tasks[index]
        raise IndexError("No task at the specified index.")

    def list_tasks(self, show_completed=True):
        """Return all tasks. If show_completed is False, only incomplete tasks are returned."""
        if show_completed:
            return list(enumerate(self.tasks))
        else:
            return [(i, task) for i, task in enumerate(self.tasks) if not task.completed]

    def __repr__(self):
        lines = []
        for idx, task in enumerate(self.tasks):
            lines.append(f"{idx}. {task}")
        return "\n".join(lines) if lines else "No tasks."


# Example usage
if __name__ == "__main__":
    tm = TaskManager()
    tm.add_task("Buy groceries")
    tm.add_task("Write report")
    tm.complete_task(0)
    print("All tasks:")
    print(tm)
    print("\nIncomplete tasks:")
    for idx, task in tm.list_tasks(show_completed=False):
        print(f"{idx}. {task}")
```

---

**How to use:**

1. **Save as `task_manager.py`**
2. **Import and use in your other scripts:**

```python
from task_manager import TaskManager

tm = TaskManager()
tm.add_task("Do homework")
tm.add_task("Clean room")
tm.complete_task(1)
print(tm)
```

Let me know if you want file saving/loading support or other features!