Certainly! Below is an example of a Python module named `task_manager.py` that provides functionality to manage a list of tasks. This module includes features such as adding tasks, removing tasks, listing all tasks, marking tasks as completed, and filtering tasks by their status.

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
            return
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

    def filter_tasks_by_status(self, completed=True):
        filtered_tasks = [task for task in self.tasks if task.completed == completed]
        if not filtered_tasks:
            status = "completed" if completed else "incomplete"
            print(f"No {status} tasks to display")
            return
        for i, task in enumerate(filtered_tasks):
            print(f"{i}: {task}")

# Example usage
if __name__ == "__main__":
    manager = TaskManager()
    
    # Adding tasks
    manager.add_task("Buy groceries")
    manager.add_task("Read a book")
    manager.add_task("Write a report")

    # Listing all tasks
    print("\nAll tasks:")
    manager.list_tasks()

    # Marking a task as completed
    manager.mark_task_as_completed(0)

    # Listing all tasks again
    print("\nAll tasks after marking one as completed:")
    manager.list_tasks()

    # Filtering completed tasks
    print("\nCompleted tasks:")
    manager.filter_tasks_by_status(completed=True)

    # Removing a task
    manager.remove_task(1)

    # Listing all tasks after removal
    print("\nAll tasks after removing one:")
    manager.list_tasks()
```

### Explanation

1. **Task Class**:
   - Represents a single task with a description and a completion status.
   - Methods to mark the task as completed or incomplete.

2. **TaskManager Class**:
   - Manages a list of `Task` objects.
   - Provides methods to add, remove, list, mark tasks as completed/incomplete, and filter tasks by their status.

3. **Example Usage**:
   - Demonstrates how to use the `TaskManager` class to manage tasks.

### How to Use

1. Save the code in a file named `task_manager.py`.
2. Run the script directly or import it into another Python script to use its functionality.

This module provides a basic structure for managing tasks and can be extended with additional features as needed.