Certainly! Below is a simple Python module called `task_manager.py` that allows you to manage a list of tasks. This module provides basic functionalities such as adding, removing, listing, and marking tasks as completed.

### `task_manager.py`

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
        status = "Completed" if self.completed else "Incomplete"
        return f"{self.description} - {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Task added: {task}")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Task removed: {removed_task}")
        else:
            print("Invalid task index")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks to display")
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
    manager.add_task("Call mom")

    manager.list_tasks()

    manager.mark_task_as_completed(1)

    manager.list_tasks()

    manager.remove_task(2)

    manager.list_tasks()
```

### Explanation

1. **Task Class**:
   - `__init__(self, description)`: Initializes a task with a description and sets its status to incomplete.
   - `mark_as_completed(self)`: Marks the task as completed.
   - `mark_as_incomplete(self)`: Marks the task as incomplete.
   - `__str__(self)`: Returns a string representation of the task.

2. **TaskManager Class**:
   - `__init__(self)`: Initializes an empty list to store tasks.
   - `add_task(self, description)`: Adds a new task to the list.
   - `remove_task(self, index)`: Removes a task from the list based on its index.
   - `list_tasks(self)`: Lists all tasks with their status.
   - `mark_task_as_completed(self, index)`: Marks a task as completed based on its index.
   - `mark_task_as_incomplete(self, index)`: Marks a task as incomplete based on its index.

### Example Usage

When you run the module directly (i.e., `python task_manager.py`), it demonstrates how to use the `TaskManager` class by adding, listing, marking, and removing tasks.

Feel free to expand this module with additional features or modify it to suit your needs!