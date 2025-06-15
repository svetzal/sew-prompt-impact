Certainly! Here is a simple Python module called `task_manager.py` that allows you to manage a list of tasks. It includes functionalities such as adding tasks, removing tasks, listing all tasks, and marking tasks as completed.

```python
# task_manager.py

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = '✓' if self.completed else '✗'
        return f"[{status}] {self.description}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Added task: {description}")

    def remove_task(self, index):
        try:
            removed_task = self.tasks.pop(index)
            print(f"Removed task: {removed_task.description}")
        except IndexError:
            print(f"Error: No task at index {index}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
            return
        for idx, task in enumerate(self.tasks):
            print(f"{idx}. {task}")

    def mark_task_completed(self, index):
        try:
            self.tasks[index].mark_completed()
            print(f"Marked task {index} as completed.")
        except IndexError:
            print(f"Error: No task at index {index}")

# Usage example (uncomment to test)
# if __name__ == "__main__":
#     tm = TaskManager()
#     tm.add_task("Buy groceries")
#     tm.add_task("Read a book")
#     tm.list_tasks()
#     tm.mark_task_completed(0)
#     tm.list_tasks()
#     tm.remove_task(1)
#     tm.list_tasks()
```

### How to use this module:
1. Save the code above in a file named `task_manager.py`.
2. In your Python code or interactive session, you can do:

```python
import task_manager

tm = task_manager.TaskManager()
tm.add_task("Finish homework")
tm.list_tasks()
tm.mark_task_completed(0)
tm.list_tasks()
tm.remove_task(0)
tm.list_tasks()
```

This will help you manage your tasks efficiently. Feel free to expand or modify it to suit your needs!