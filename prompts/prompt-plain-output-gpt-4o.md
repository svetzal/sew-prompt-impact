Creating a Python module to manage a list of tasks is a great project to practice managing data within a program. Below is an example of a simple task manager, implemented as a class, which allows you to add, remove, view, and mark tasks as completed.

First, we'll define the `Task` class, then the `TaskManager` class. Finally, I’ll show you how to use this module in practice.

### Step 1: Define the Task class

```python
class Task:
    def __init__(self, title, description=''):
        """
        Initialize a Task object.

        Parameters:
        title (str): The title of the task.
        description (str): A short description of the task (optional).
        """
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        """Marks the task as completed."""
        self.completed = True

    def __str__(self):
        """Returns a string representation of the task."""
        status = 'Completed' if self.completed else 'Pending'
        return f"Title: {self.title}, Description: {self.description}, Status: {status}"
```

### Step 2: Define the TaskManager class

```python
class TaskManager:
    def __init__(self):
        """Initialize the TaskManager with an empty list of tasks."""
        self.tasks = []

    def add_task(self, title, description=''):
        """
        Add a new task.

        Parameters:
        title (str): The title of the task.
        description (str): A description of the task (optional).
        """
        task = Task(title, description)
        self.tasks.append(task)
        print(f"Added task: '{title}'")

    def remove_task(self, title):
        """
        Remove a task by its title.

        Parameters:
        title (str): The title of the task to remove.
        """
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Removed task: '{title}'")
                return
        print(f"Task '{title}' not found.")

    def mark_task_completed(self, title):
        """
        Mark a task as completed by its title.

        Parameters:
        title (str): The title of the task to mark as completed.
        """
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                print(f"Task '{title}' marked as completed.")
                return
        print(f"Task '{title}' not found.")

    def list_tasks(self):
        """List all tasks with their status."""
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            print(task)
```

### Step 3: How to use the module

Here's how you might use this module in practice:

```python
if __name__ == '__main__':
    manager = TaskManager()
    manager.add_task("Buy groceries", "Milk, Eggs, Bread")
    manager.add_task("Submit report", "Due by end of the week")

    print("\nCurrent Tasks:")
    manager.list_tasks()

    manager.mark_task_completed("Buy groceries")

    print("\nTasks After Completion:")
    manager.list_tasks()

    manager.remove_task("Submit report")

    print("\nTasks After Removal:")
    manager.list_tasks()
```

This module starts simple but can be extended with more features such as prioritization, deadlines, and persistence to a file or database.