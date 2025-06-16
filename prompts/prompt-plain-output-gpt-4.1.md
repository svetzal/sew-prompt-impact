Certainly! Here’s a Python module called `task_manager.py` that provides an object-oriented way to manage a list of tasks. Each task can have a title, optional description, and a status indicating whether it’s completed. The module supports adding, removing, marking as done/undone, listing, and saving/loading tasks to a JSON file.

```python
# task_manager.py
import json

class Task:
    def __init__(self, title, description="", completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def mark_done(self):
        self.completed = True

    def mark_undone(self):
        self.completed = False

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data.get("title", ""),
            description=data.get("description", ""),
            completed=data.get("completed", False),
        )

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"[{status}] {self.title}: {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=""):
        self.tasks.append(Task(title, description))

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            raise IndexError("Task index out of range.")

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
        else:
            raise IndexError("Task index out of range.")

    def mark_undone(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_undone()
        else:
            raise IndexError("Task index out of range.")

    def list_tasks(self, show_completed=True):
        for i, task in enumerate(self.tasks):
            if not show_completed and task.completed:
                continue
            print(f"{i}. {task}")

    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=2)

    def load_from_file(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.tasks = [Task.from_dict(item) for item in data]

# Example usage (to be removed or put under if __name__ == "__main__"):
if __name__ == "__main__":
    tm = TaskManager()
    tm.add_task("Buy groceries", "Eggs, Milk, Bread")
    tm.add_task("Walk the dog")
    tm.list_tasks()
    tm.mark_done(0)
    tm.list_tasks(show_completed=False)
    tm.save_to_file("tasks.json")
```

---

**How to use:**

1. Save as `task_manager.py`
2. Import and use:

```python
from task_manager import TaskManager

tm = TaskManager()
tm.add_task("Do homework")
tm.add_task("Read book", "At least 30 minutes")
tm.mark_done(1)
tm.list_tasks()
tm.save_to_file("mytasks.json")
```

Let me know if you want CLI/shell interaction or more advanced features!