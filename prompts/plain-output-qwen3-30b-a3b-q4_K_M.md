

Here's a well-structured Python module that allows you to manage a list of tasks with the following features:

- Add tasks
- Mark tasks as completed
- Remove tasks
- View all tasks
- Save tasks to a JSON file
- Load tasks from a JSON file

---

### 📁 `task_manager.py`

```python
import json

class TaskManager:
    """
    A class to manage a list of tasks.

    Attributes:
        tasks (list): A list of task dictionaries, each containing:
                      - 'description': str
                      - 'completed': bool
        filename (str): The filename to save/load tasks from.
    """

    def __init__(self, filename=None):
        """
        Initialize a new TaskManager instance.

        Args:
            filename (str, optional): The name of the file to load tasks from.
        """
        self.tasks = []
        self.filename = filename
        if self.filename:
            self.load_from_file()

    def add_task(self, description):
        """
        Add a new task to the task list.

        Args:
            description (str): A brief description of the task.
        """
        self.tasks.append({
            'description': description,
            'completed': False
        })

    def mark_as_done(self, index):
        """
        Mark a task as completed.

        Args:
            index (int): The 0-based index of the task to mark as done.
        """
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
        else:
            print("Invalid task index.")

    def remove_task(self, index):
        """
        Remove a task from the list.

        Args:
            index (int): The 0-based index of the task to remove.
        """
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid task index.")

    def view_tasks(self):
        """
        Display all tasks with their current status.
        """
        if not self.tasks:
            print("No tasks available.")
            return

        for i, task in enumerate(self.tasks):
            status = 'Done' if task['completed'] else 'Pending'
            print(f"{i}: {task['description']} - {status}")

    def save_to_file(self, filename=None):
        """
        Save the current tasks to a JSON file.

        Args:
            filename (str, optional): The name of the file to save to.
        """
        if filename:
            self.filename = filename
        if self.filename:
            try:
                with open(self.filename, 'w') as f:
                    json.dump(self.tasks, f, indent=4)
                print(f"Tasks saved to {self.filename}.")
            except Exception as e:
                print(f"Failed to save tasks: {e}")
        else:
            print("No filename specified.")

    def load_from_file(self, filename=None):
        """
        Load tasks from a JSON file.

        Args:
            filename (str, optional): The name of the file to load from.
        """
        if filename:
            self.filename = filename
        if self.filename:
            try:
                with open(self.filename, 'r') as f:
                    self.tasks = json.load(f)
                print(f"Tasks loaded from {self.filename}.")
            except FileNotFoundError:
                print(f"File {self.filename} not found. Starting with an empty task list.")
            except Exception as e:
                print(f"Failed to load tasks: {e}")
        else:
            print("No filename specified.")
```

---

### ✅ Example Usage

```python
from task_manager import TaskManager

# Create a task manager with a file
tm = TaskManager("tasks.json")

# Add tasks
tm.add_task("Buy groceries")
tm.add_task("Finish report")

# View tasks
tm.view_tasks()

# Mark first task as done
tm.mark_as_done(0)

# View updated tasks
tm.view_tasks()

# Save tasks
tm.save_to_file()

# Load tasks (if the file exists)
tm2 = TaskManager("tasks.json")
tm2.view_tasks()
```

---

### 📝 Notes

- The module uses the `json` module for persistence.
- It handles invalid indices and file errors gracefully.
- Tasks are stored as a list of dictionaries, making them easily extendable for additional features (like priority or due dates).
- The methods `save_to_file()` and `load_from_file()` allow flexibility in specifying or changing filenames at runtime.