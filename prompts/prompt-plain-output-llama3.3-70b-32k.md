**Task Manager Module**
=======================

### Overview

This Python module provides a simple task manager that allows you to create, read, update, and delete (CRUD) tasks.

### Installation

To use this module, save the following code in a file named `task_manager.py`. You can then import it into your Python scripts or programs.

### Code
```python
# task_manager.py

class Task:
    def __init__(self, title, description="", completed=False):
        """
        Initialize a new task.

        Args:
            title (str): The title of the task.
            description (str, optional): A brief description of the task. Defaults to "".
            completed (bool, optional): Whether the task is completed. Defaults to False.
        """
        self.title = title
        self.description = description
        self.completed = completed

    def mark_as_completed(self):
        """
        Mark the task as completed.
        """
        self.completed = True

    def mark_as_incomplete(self):
        """
        Mark the task as incomplete.
        """
        self.completed = False


class TaskManager:
    def __init__(self):
        """
        Initialize a new task manager with an empty list of tasks.
        """
        self.tasks = []

    def create_task(self, title, description=""):
        """
        Create a new task and add it to the list.

        Args:
            title (str): The title of the task.
            description (str, optional): A brief description of the task. Defaults to "".
        """
        new_task = Task(title, description)
        self.tasks.append(new_task)

    def read_tasks(self):
        """
        Return a list of all tasks.

        Returns:
            list: A list of Task objects.
        """
        return self.tasks

    def update_task(self, index, title=None, description=None):
        """
        Update an existing task.

        Args:
            index (int): The index of the task to update.
            title (str, optional): The new title of the task. Defaults to None.
            description (str, optional): The new description of the task. Defaults to None.
        """
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            if title:
                task.title = title
            if description:
                task.description = description

    def delete_task(self, index):
        """
        Delete a task from the list.

        Args:
            index (int): The index of the task to delete.
        """
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def display_tasks(self):
        """
        Print a list of all tasks.
        """
        for i, task in enumerate(self.tasks):
            status = "Completed" if task.completed else "Incomplete"
            print(f"{i+1}. {task.title} - {status}")
            if task.description:
                print(f"  Description: {task.description}")


def main():
    # Example usage
    manager = TaskManager()
    while True:
        print("\nTask Manager")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Display Tasks")
        print("6. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            manager.create_task(title, description)
        elif choice == "2":
            tasks = manager.read_tasks()
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task.title}")
        elif choice == "3":
            index = int(input("Enter task index: ")) - 1
            title = input("Enter new task title (optional): ")
            description = input("Enter new task description (optional): ")
            manager.update_task(index, title or None, description or None)
        elif choice == "4":
            index = int(input("Enter task index: ")) - 1
            manager.delete_task(index)
        elif choice == "5":
            manager.display_tasks()
        elif choice == "6":
            break


if __name__ == "__main__":
    main()
```

### Example Use Cases

*   Create a new task: `manager.create_task("Buy groceries", "Milk, eggs, and bread")`
*   Read all tasks: `tasks = manager.read_tasks()`
*   Update an existing task: `manager.update_task(0, title="New title")`
*   Delete a task: `manager.delete_task(0)`
*   Display all tasks: `manager.display_tasks()`