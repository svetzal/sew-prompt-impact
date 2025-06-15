Certainly! Here’s a simple Python module to manage a list of tasks. Each task can have a title, an optional description, and a status (pending or done).

Save this as `task_manager.py`:

```python
# task_manager.py

class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.done = False

    def mark_done(self):
        self.done = True

    def mark_pending(self):
        self.done = False

    def __repr__(self):
        status = "✓" if self.done else "✗"
        return f"[{status}] {self.title} : {self.description}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=""):
        task = Task(title, description)
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            return True
        return False

    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
            return True
        return False

    def mark_task_pending(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_pending()
            return True
        return False

    def list_tasks(self, show_done=True, show_pending=True):
        filtered = []
        for i, task in enumerate(self.tasks):
            if (task.done and show_done) or (not task.done and show_pending):
                filtered.append((i, task))
        return filtered

    def __repr__(self):
        return "\n".join(
            [f"{i}: {task}" for i, task in enumerate(self.tasks)]
        )

# Usage example (uncomment to test):
# if __name__ == "__main__":
#     tm = TaskManager()
#     tm.add_task("Buy milk")
#     tm.add_task("Complete assignment", "Due by Friday")
#     print("All tasks:")
#     print(tm)
#     tm.mark_task_done(0)
#     print("\nAfter marking first task as done:")
#     print(tm)
```

---

**How to use:**

```python
from task_manager import TaskManager

tm = TaskManager()
tm.add_task("Review PR")
tm.add_task("Write documentation", "Add usage examples")
print(tm)

tm.mark_task_done(0)
print(tm.list_tasks(show_pending=False))  # List only done tasks
```

Let me know if you want features like saving/loading to a file, or deadline support!