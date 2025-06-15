Creating a Python module to manage a list of tasks is a great exercise to practice object-oriented programming, file handling, and basic list operations. Below is a simple implementation of a task manager with features to add, remove, list, and save tasks to a file.

We'll create a single class called `TaskManager` to handle these operations:

```python
# task_manager.py

class TaskManager:
    def __init__(self, file_name="tasks.txt"):
        """Initialize the task manager with a list of tasks and specify a file for storage."""
        self.tasks = []
        self.file_name = file_name
        self.load_tasks()

    def add_task(self, task):
        """Add a task to the list."""
        if task not in self.tasks:
            self.tasks.append(task)
            print(f"Task '{task}' added.")
        else:
            print(f"Task '{task}' is already in the list.")

    def remove_task(self, task):
        """Remove a task from the list."""
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed.")
        else:
            print(f"Task '{task}' not found in the list.")
    
    def list_tasks(self):
        """List all tasks."""
        if self.tasks:
            print("Here are your tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks to show.")

    def save_tasks(self):
        """Save tasks to a file."""
        try:
            with open(self.file_name, 'w') as file:
                for task in self.tasks:
                    file.write(f"{task}\n")
            print(f"Tasks saved to {self.file_name}.")
        except Exception as e:
            print(f"An error occurred while saving tasks: {e}")

    def load_tasks(self):
        """Load tasks from a file."""
        try:
            with open(self.file_name, 'r') as file:
                self.tasks = [line.strip() for line in file.readlines()]
            print(f"Tasks loaded from {self.file_name}.")
        except FileNotFoundError:
            print(f"No existing task file found. Starting with an empty task list.")
        except Exception as e:
            print(f"An error occurred while loading tasks: {e}")

# Example of usage
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Finish writing report")
    manager.add_task("Email the client")
    manager.list_tasks()
    manager.save_tasks()
    manager.remove_task("Email the client")
    manager.list_tasks()
```

### Key Features
1. **Add Task**: Adds a unique task to the list.
2. **Remove Task**: Removes a task if it exists in the list.
3. **List Tasks**: Lists all current tasks in the task manager.
4. **Save Tasks**: Saves tasks to a `tasks.txt` file.
5. **Load Tasks**: Automatically loads tasks from a `tasks.txt` file when the `TaskManager` is initialized.

### How to Use
- Save this code in a file named `task_manager.py`.
- You can import and use the `TaskManager` class in other Python scripts.
- Run the script directly to test its functionality; the example usage at the bottom demonstrates how to use the class methods.

This implementation is simple and provides a good foundation for a task manager, which can be expanded with more features, such as setting priorities, due dates, or integrating with a database for persistent storage.