

Here's a well-structured Python module to manage a list of tasks. It provides basic functionality such as adding, marking as complete, deleting, listing, and persisting tasks to a file.

---

### ✅ Features
- Add tasks with description and optional due date
- Mark tasks as completed
- Delete tasks
- List all tasks or filter by completion status
- Save tasks to a file (JSON format)
- Load tasks from a file

---

### 📦 Module: `task_manager.py`

```python
import json
from datetime import datetime

class Task:
    def __init__(self, description: str, due_date: str = None):
        self.description = description
        self.due_date = self._parse_date(due_date) if due_date else None
        self.completed = False

    def _parse_date(self, date_str: str) -> datetime:
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Invalid date format. Use 'YYYY-MM-DD' for: {date_str}")

    def mark_as_complete(self):
        self.completed = True

    def __str__(self):
        status = "✅" if self.completed else "❌"
        date_str = self.due_date.strftime("%Y-%m-%d") if self.due_date else "No due date"
        return f"{status} {self.description} (Due: {date_str})"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description: str, due_date: str = None):
        task = Task(description, due_date)
        self.tasks.append(task)
        print(f"Task added: {description}")

    def mark_as_complete(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_complete()
            print(f"Marked task {index} as complete.")
        else:
            print("Invalid task index.")

    def delete_task(self, index: int):
        if 0 <= index < len(self.tasks):
            task = self.tasks.pop(index)
            print(f"Deleted task: {task.description}")
        else:
            print("Invalid task index.")

    def list_tasks(self, completed: bool = None):
        if not self.tasks:
            print("No tasks available.")
            return

        filtered_tasks = self.tasks
        if completed is not None:
            filtered_tasks = [t for t in self.tasks if t.completed == completed]

        for i, task in enumerate(filtered_tasks):
            print(f"{i}: {task}")

    def save_to_file(self, filename: str):
        task_list = []
        for task in self.tasks:
            task_data = {
                "description": task.description,
                "due_date": task.due_date.strftime("%Y-%m-%d") if task.due_date else None,
                "completed": task.completed
            }
            task_list.append(task_data)

        with open(filename, 'w') as f:
            json.dump(task_list, f, indent=4)
        print(f"Tasks saved to {filename}.")

    def load_from_file(self, filename: str):
        try:
            with open(filename, 'r') as f:
                task_data = json.load(f)

            self.tasks = []
            for data in task_data:
                task = Task(data["description"], data["due_date"])
                task.completed = data["completed"]
                self.tasks.append(task)
            print(f"Tasks loaded from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except json.JSONDecodeError:
            print(f"Invalid JSON format in {filename}.")

```

---

### 🧪 Example Usage

```python
from task_manager import TaskManager

def main():
    manager = TaskManager()

    manager.add_task("Buy groceries", "2025-04-10")
    manager.add_task("Finish project", "2025-04-15")
    manager.add_task("Walk the dog")

    print("\nAll tasks:")
    manager.list_tasks()

    print("\nIncomplete tasks:")
    manager.list_tasks(completed=False)

    print("\nComplete tasks:")
    manager.list_tasks(completed=True)

    manager.mark_as_complete(0)
    print("\nAfter marking task 0 as complete:")
    manager.list_tasks()

    manager.delete_task(1)
    print("\nAfter deleting task 1:")
    manager.list_tasks()

    manager.save_to_file("tasks.json")
    manager.load_from_file("tasks.json")
    print("\nLoaded tasks:")
    manager.list_tasks()

if __name__ == "__main__":
    main()
```

---

### 📝 Notes

- This module is designed for basic to intermediate task management.
- You can enhance it with more features like:
  - Priority levels
  - Due date reminders
  - Command-line interface
  - GUI interface using `tkinter` or `PyQt`

Let me know if you'd like to expand this with additional features!