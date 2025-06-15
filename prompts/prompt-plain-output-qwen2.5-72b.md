Certainly! Below is a simple Python module called `task_manager` that allows you to manage a list of tasks. This module includes functions to add, remove, list, and mark tasks as completed.

### task_manager.py

```python
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def mark_as_incomplete(self):
        self.completed = False

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Task added: {description}")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Task removed: {removed_task}")
        else:
            print("Invalid task index")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks to display")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i}: {task}")

    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()
            print(f"Task marked as completed: {self.tasks[index]}")
        else:
            print("Invalid task index")

    def mark_task_as_incomplete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_incomplete()
            print(f"Task marked as incomplete: {self.tasks[index]}")
        else:
            print("Invalid task index")


# Example usage
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Buy groceries")
    manager.add_task("Do laundry")
    manager.list_tasks()
    manager.mark_task_as_completed(0)
    manager.list_tasks()
    manager.remove_task(1)
    manager.list_tasks()
```

### Explanation

1. **Task Class**:
   - `__init__(self, description)`: Initializes a task with a description and sets it as incomplete.
   - `mark_as_completed(self)`: Marks the task as completed.
   - `mark_as_incomplete(self)`: Marks the task as incomplete.
   - `__str__(self)`: Returns a string representation of the task.

2. **TaskManager Class**:
   - `__init__(self)`: Initializes an empty list to store tasks.
   - `add_task(self, description)`: Adds a new task with the given description.
   - `remove_task(self, index)`: Removes the task at the specified index.
   - `list_tasks(self)`: Lists all tasks with their status (completed or not).
   - `mark_task_as_completed(self, index)`: Marks the task at the specified index as completed.
   - `mark_task_as_incomplete(self, index)`: Marks the task at the specified index as incomplete.

### Example Usage

When you run the script directly (i.e., `python task_manager.py`), it demonstrates how to use the `TaskManager` class by adding tasks, listing them, marking one as completed, and removing another.

Feel free to expand or modify this module to suit your specific needs!