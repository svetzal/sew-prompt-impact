Here is a well-documented Python module designed to manage a list of tasks, including features such as adding, completing, deleting, listing, and persisting tasks to a JSON file.

---

### ✅ Module: `task_manager.py`

```python
import json

class TaskManager:
    """
    A class to manage a list of tasks.

    Attributes:
        tasks (list): A list of task dictionaries, each with 'description' and 'completed' keys.
    """

    def __init__(self):
        """
        Initializes an empty list of tasks.
        """
        self.tasks = []

    def add_task(self, description):
        """
        Adds a new task to the list.

        Args:
            description (str): A string describing the task.
        """
        self.tasks.append({'description': description, 'completed': False})

    def complete_task(self, index):
        """
        Marks the task at the specified index as completed.

        Args:
            index (int): The index of the task to mark as completed.
        """
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
        else:
            print("Invalid index")

    def delete_task(self, index):
        """
        Deletes the task at the specified index.

        Args:
            index (int): The index of the task to delete.
        """
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid index")

    def list_tasks(self):
        """
        Prints all tasks with their current status and indexes.
        """
        for i, task in enumerate(self.tasks):
            status = 'Completed' if task['completed'] else 'Pending'
            print(f"{i}: {task['description']} - {status}")

    def save_to_file(self, filename):
        """
        Saves the current tasks to a JSON file.

        Args:
            filename (str): The path to the file where tasks will be saved.
        """
        with open(filename, 'w') as f:
            json.dump([{'description': t['description'], 'completed': t['completed']} for t in self.tasks], f)

    def load_from_file(self, filename):
        """
        Loads tasks from a JSON file.

        Args:
            filename (str): The path to the file from which tasks will be loaded.
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.tasks = [{'description': d['description'], 'completed': d['completed']} for d in data]
        except FileNotFoundError:
            print("File not found. No tasks loaded.")
        except json.JSONDecodeError:
            print("Invalid JSON format. No tasks loaded.")
```

---

### 📁 Usage Example

You can use the module in your project like this:

```python
from task_manager import TaskManager

# Create a task manager instance
task_manager = TaskManager()

# Add tasks
task_manager.add_task("Buy groceries")
task_manager.add_task("Clean room")

# List all tasks
task_manager.list_tasks()

# Complete a task
task_manager.complete_task(0)

# Delete a task
task_manager.delete_task(1)

# Save tasks to a file
task_manager.save_to_file("tasks.json")

# Load tasks from a file
task_manager.load_from_file("tasks.json")

# List tasks again
task_manager.list_tasks()
```

---

### 📦 Notes

- The module uses the built-in `json` module for file I/O.
- Error handling is included for invalid indexes and malformed JSON files.
- The module can be extended with additional features such as task priorities, deadlines, or filters.

This is a complete and flexible tool for task management in Python, suitable for both learning and small-scale applications.