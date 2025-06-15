Sure! Below is a simple Python module for managing a list of tasks. This module provides basic functionalities such as adding, removing, and listing tasks.

```python
# task_manager.py

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the list."""
        if task not in self.tasks:
            self.tasks.append(task)
            print(f"Task added: {task}")
        else:
            print("Task already exists.")

    def remove_task(self, task):
        """Remove a task from the list."""
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task removed: {task}")
        else:
            print("Task not found.")

    def list_tasks(self):
        """List all tasks."""
        if self.tasks:
            print("Tasks:")
            for index, task in enumerate(self.tasks, 1):
                print(f"{index}. {task}")
        else:
            print("No tasks to display.")

# Example usage
if __name__ == "__main__":
    manager = TaskManager()
    
    while True:
        print("\nTask Manager")
        print("1. Add task")
        print("2. Remove task")
        print("3. List tasks")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter the task to add: ")
            manager.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            manager.remove_task(task)
        elif choice == '3':
            manager.list_tasks()
        elif choice == '4':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")
```

### How to Use This Module

1. **Save the Code**: Save the above code in a file named `task_manager.py`.
2. **Run the Example Usage**:
   - You can run the example usage directly from the command line by executing:
     ```sh
     python task_manager.py
     ```
   - This will open a simple command-line interface where you can add, remove, and list tasks.

### Explanation

- **TaskManager Class**: 
  - `__init__`: Initializes an empty list to store tasks.
  - `add_task`: Adds a new task if it doesn't already exist in the list.
  - `remove_task`: Removes a task from the list if it exists.
  - `list_tasks`: Lists all the tasks currently stored.

- **Example Usage**:
  - A simple CLI loop that allows you to interact with the `TaskManager` class by selecting options and providing inputs.

This module is basic and can be extended with more features such as saving tasks to a file, loading tasks from a file, prioritizing tasks, etc.