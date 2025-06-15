

Here's a well-structured Python module to manage a list of tasks. This implementation provides basic task management capabilities such as adding, removing, listing, and marking tasks as complete.

---

### 🧩 `task_manager.py` — Task Manager Module

```python
class Task:
    def __init__(self, task_id, description, priority=1, done=False):
        self.id = task_id
        self.description = description
        self.priority = priority
        self.done = done

    def mark_as_done(self):
        self.done = True

    def __str__(self):
        status = "✓" if self.done else "✗"
        return f"ID: {self.id} | {status} | {self.description} (Priority: {self.priority})"


class TaskManager:
    def __init__(self):
        self.next_id = 1
        self.tasks = []

    def add_task(self, description, priority=1):
        task = Task(task_id=self.next_id, description=description, priority=priority)
        self.tasks.append(task)
        self.next_id += 1
        return task.id  # optional: useful for referencing the new task

    def get_task(self, task_id):
        return next((t for t in self.tasks if t.id == task_id), None)

    def remove_task(self, task_id):
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def mark_as_done(self, task_id):
        task = self.get_task(task_id)
        if task:
            task.mark_as_done()
            return True
        return False

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for task in self.tasks:
            print(task)

    def list_pending_tasks(self):
        pending = [t for t in self.tasks if not t.done]
        if not pending:
            print("No pending tasks.")
            return
        for task in pending:
            print(task)

    def list_completed_tasks(self):
        completed = [t for t in self.tasks if t.done]
        if not completed:
            print("No completed tasks.")
            return
        for task in completed:
            print(task)
```

---

### ✅ Example Usage

Here's how you might use this `TaskManager` in a script or interactive Python shell:

```python
from task_manager import TaskManager

# Create a task manager
tm = TaskManager()

# Add tasks
tm.add_task("Buy groceries", priority=2)
tm.add_task("Finish report", priority=1)
tm.add_task("Exercise", priority=3)

# Mark task as done
tm.mark_as_done(2)

# List all tasks
print("All Tasks:")
tm.list_tasks()

# List only pending tasks
print("\nPending Tasks:")
tm.list_pending_tasks()

# Remove a task
tm.remove_task(1)

# List updated tasks
print("\nTasks After Removal:")
tm.list_tasks()
```

---

### 📌 Notes

- **Tasks** are immutable by design — to change a task, you need to remove and re-add it (though this can be customized).
- The `TaskManager` class encapsulates all the logic related to tasks.
- You can easily extend this module to include deadlines, categories, persistence (e.g., saving to a file), or filtering based on priority.

Would you like to include support for saving and loading tasks to/from a file next?