Certainly! Below is an example of a Python module that manages a list of tasks. This module includes basic functionalities such as adding, removing, updating, and listing tasks.

```python
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the list."""
        if not task.strip():
            print("Task description cannot be empty.")
            return
        self.tasks.append(task)
        print(f"Task added: {task}")

    def remove_task(self, task_index):
        """Remove a task from the list by its index."""
        try:
            removed_task = self.tasks.pop(task_index)
            print(f"Task removed: {removed_task}")
        except IndexError:
            print("Invalid task index. Please try again.")

    def update_task(self, task_index, new_description):
        """Update the description of a task by its index."""
        try:
            if not new_description.strip():
                print("New task description cannot be empty.")
                return
            self.tasks[task_index] = new_description
            print(f"Task updated: {new_description}")
        except IndexError:
            print("Invalid task index. Please try again.")

    def list_tasks(self):
        """List all tasks with their indices."""
        if not self.tasks:
            print("No tasks to display.")
            return
        for index, task in enumerate(self.tasks):
            print(f"{index}: {task}")

# Example usage:
if __name__ == "__main__":
    manager = TaskManager()
    
    # Adding tasks
    manager.add_task("Read a book")
    manager.add_task("Write a report")
    
    # Listing tasks
    manager.list_tasks()
    
    # Updating a task
    manager.update_task(0, "Finish reading the book")
    
    # Removing a task
    manager.remove_task(1)
    
    # Listing tasks again to see changes
    manager.list_tasks()
```

### How to Use This Module:

1. **Add Task**: Use `add_task(task_description)` to add a new task.
2. **Remove Task**: Use `remove_task(index)` to remove a task by its index.
3. **Update Task**: Use `update_task(index, new_description)` to update the description of a task by its index.
4. **List Tasks**: Use `list_tasks()` to display all tasks with their indices.

### Example:

```python
manager = TaskManager()
manager.add_task("Buy groceries")
manager.add_task("Walk the dog")
manager.list_tasks()  # Output: 0: Buy groceries\n1: Walk the dog
manager.update_task(0, "Buy milk and eggs")
manager.remove_task(1)
manager.list_tasks()  # Output: 0: Buy milk and eggs
```

This module is simple yet functional. You can expand it by adding more features like task prioritization, deadlines, or saving/loading tasks from a file.