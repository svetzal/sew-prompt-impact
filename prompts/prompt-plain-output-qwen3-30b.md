```python
import json

class Task:
    """
    Represents a single task with a description and a completion status.
    """
    def __init__(self, description):
        self.description = description
        self.done = False

    def __str__(self):
        return f"{self.description} - {'Done' if self.done else 'Pending'}"


class TaskManager:
    """
    Manages a list of tasks. Provides methods to add, mark, delete, view, and persist tasks.
    """
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        """
        Adds a new task to the task list.
        """
        task = Task(description)
        self.tasks.append(task)

    def mark_as_done(self, index):
        """
        Marks the task at the given index as done.
        """
        if 0 <= index < len(self.tasks):
            self.tasks[index].done = True
        else:
            print("Invalid index. Please provide a valid task index.")

    def view_tasks(self):
        """
        Displays all tasks with their descriptions and status.
        """
        if not self.tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i}: {task}")

    def delete_task(self, index):
        """
        Deletes the task at the given index.
        """
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid index. Please provide a valid task index.")

    def clear_all(self):
        """
        Clears all tasks from the list.
        """
        self.tasks.clear()

    def save_to_file(self, filename):
        """
        Saves the current task list to a JSON file.
        """
        with open(filename, 'w') as f:
            json.dump([{'description': t.description, 'done': t.done} for t in self.tasks], f)
        print(f"Tasks saved to {filename}")

    def load_from_file(self, filename):
        """
        Loads tasks from a JSON file into the task list.
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.tasks = [Task(item['description']) for item in data]
                for task, item in zip(self.tasks, data):
                    task.done = item['done']
            print(f"Tasks loaded from {filename}")
        except FileNotFoundError:
            print(f"File '{filename}' not found. No tasks loaded.")


# Example usage (uncomment to test):
# if __name__ == "__main__":
#     tm = TaskManager()
#     tm.add_task("Complete Python module")
#     tm.add_task("Write documentation")
#     tm.view_tasks()
#     tm.mark_as_done(0)
#     tm.view_tasks()
#     tm.save_to_file("tasks.json")
#     tm.clear_all()
#     tm.load_from_file("tasks.json")
#     tm.view_tasks()
```

### Key Features:
- **Task Class**: Manages individual tasks with a description and completion status.
- **TaskManager Class**: 
  - Adds, marks, deletes, and clears tasks.
  - Provides methods to persist tasks to a file and load them back.
  - Includes input validation to handle invalid indices.
- **File Operations**: Uses JSON for easy-to-read storage and retrieval of tasks.
- **User-Friendly Output**: Displays task status clearly, and provides feedback on operations.