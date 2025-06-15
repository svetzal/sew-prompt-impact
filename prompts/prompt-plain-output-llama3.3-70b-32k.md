**Task Manager Module**
=======================

Below is a Python module named `task_manager.py` that provides functionality to manage a list of tasks.

```python
# task_manager.py

class Task:
    """Represents a single task."""
    
    def __init__(self, title, description, due_date=None):
        """
        Initializes a new Task instance.
        
        Args:
            title (str): The title of the task.
            description (str): A brief description of the task.
            due_date (str, optional): The due date for the task. Defaults to None.
        """
        self.title = title
        self.description = description
        self.due_date = due_date

    def __str__(self):
        """Returns a string representation of the Task."""
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}"


class TaskManager:
    """Manages a list of tasks."""
    
    def __init__(self):
        """
        Initializes an empty TaskManager instance.
        """
        self.tasks = []

    def add_task(self, title, description, due_date=None):
        """
        Adds a new task to the task list.
        
        Args:
            title (str): The title of the task.
            description (str): A brief description of the task.
            due_date (str, optional): The due date for the task. Defaults to None.
        """
        new_task = Task(title, description, due_date)
        self.tasks.append(new_task)

    def view_tasks(self):
        """Displays all tasks in the task list."""
        if not self.tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"Task {i}:")
                print(task)
                print("-" * 30)

    def delete_task(self, task_index):
        """
        Removes a task from the task list by its index.
        
        Args:
            task_index (int): The zero-based index of the task to remove.
        """
        try:
            del self.tasks[task_index]
            print(f"Task {task_index + 1} deleted successfully.")
        except IndexError:
            print("Invalid task index.")

    def update_task(self, task_index, title=None, description=None, due_date=None):
        """
        Updates an existing task in the task list.
        
        Args:
            task_index (int): The zero-based index of the task to update.
            title (str, optional): The new title for the task. Defaults to None.
            description (str, optional): A new brief description for the task. Defaults to None.
            due_date (str, optional): The new due date for the task. Defaults to None.
        """
        try:
            if title:
                self.tasks[task_index].title = title
            if description:
                self.tasks[task_index].description = description
            if due_date:
                self.tasks[task_index].due_date = due_date
            print(f"Task {task_index + 1} updated successfully.")
        except IndexError:
            print("Invalid task index.")


# Example usage
if __name__ == "__main__":
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Update task")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter task due date (optional): ") or None
            task_manager.add_task(title, description, due_date)
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            task_index = int(input("Enter the task index to delete: ")) - 1
            task_manager.delete_task(task_index)
        elif choice == "4":
            task_index = int(input("Enter the task index to update: ")) - 1
            title = input("Enter new task title (optional): ") or None
            description = input("Enter new task description (optional): ") or None
            due_date = input("Enter new task due date (optional): ") or None
            task_manager.update_task(task_index, title, description, due_date)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")
```

**Module Functionality:**

*   **Task Class:** Represents a single task with attributes for `title`, `description`, and `due_date`.
*   **TaskManager Class:** Manages a list of tasks, providing methods to add, view, delete, and update tasks.
*   **Example Usage:** The module includes an example usage section demonstrating how to interact with the TaskManager instance.

**How to Use:**

1.  Create an instance of the `TaskManager` class.
2.  Use the provided methods to manage your tasks:
    *   `add_task(title, description, due_date=None)`: Adds a new task to the list.
    *   `view_tasks()`: Displays all tasks in the list.
    *   `delete_task(task_index)`: Removes a task from the list by its index (zero-based).
    *   `update_task(task_index, title=None, description=None, due_date=None)`: Updates an existing task's details.