Certainly! Here's a simple Python module named `task_manager.py` that allows you to manage a list of tasks. It includes functionalities to add, remove, list, and mark tasks as completed.

```python
# task_manager.py

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __repr__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Added task: {description}")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Removed task: {removed_task.description}")
        else:
            print("Invalid task index.")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            print(f"Marked task as completed: {self.tasks[index].description}")
        else:
            print("Invalid task index.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
        else:
            for idx, task in enumerate(self.tasks):
                print(f"{idx}. {task}")

# Example usage:
if __name__ == "__main__":
    tm = TaskManager()
    tm.add_task("Finish homework")
    tm.add_task("Read a book")
    tm.list_tasks()
    tm.mark_completed(0)
    tm.list_tasks()
    tm.remove_task(1)
    tm.list_tasks()
```

### Usage:
- To use this module, import and create an instance of `TaskManager`.
- Use `add_task(description)` to add new tasks.
- Use `remove_task(index)` to remove a task by its index.
- Use `mark_completed(index)` to mark a task as completed.
- Use `list_tasks()` to display all current tasks.

Feel free to customize this code further according to your needs!