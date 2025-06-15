Sure! Here's a simple Python module for managing a list of tasks. It provides functionalities to add, remove, update, list, and mark tasks as done.

```python
# task_manager.py

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_done(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            raise IndexError("Task index out of range")

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
        else:
            raise IndexError("Task index out of range")

    def update_task(self, index, new_description):
        if 0 <= index < len(self.tasks):
            self.tasks[index].description = new_description
        else:
            raise IndexError("Task index out of range")

    def list_tasks(self):
        return [str(task) for task in self.tasks]

    def __len__(self):
        return len(self.tasks)


if __name__ == "__main__":
    # demo usage
    manager = TaskManager()
    manager.add_task("Buy groceries")
    manager.add_task("Prepare presentation")
    manager.mark_done(0)
    manager.update_task(1, "Prepare presentation slides")

    for i, task_str in enumerate(manager.list_tasks()):
        print(f"{i}. {task_str}")
```

Save this as `task_manager.py`. You can then import and use it like this:

```python
from task_manager import TaskManager

manager = TaskManager()
manager.add_task("Write report")
manager.add_task("Attend meeting")
manager.mark_done(0)

for idx, task in enumerate(manager.list_tasks()):
    print(f"{idx}: {task}")

manager.remove_task(1)
```

Let me know if you want me to add persistence, due dates, priorities, or other features!