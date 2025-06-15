**Task Manager Module**
========================

### Overview

This Python module provides a simple task management system. It allows users to create, read, update, and delete (CRUD) tasks.

### Installation

To use this module, simply copy the code into a file named `task_manager.py` and import it in your Python script.

### Code
```python
# task_manager.py

class Task:
    def __init__(self, id, title, description, due_date=None):
        """
        Initialize a new task.

        Args:
            id (int): Unique task ID.
            title (str): Task title.
            description (str): Task description.
            due_date (str, optional): Task due date. Defaults to None.
        """
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date

class TaskManager:
    def __init__(self):
        """
        Initialize the task manager with an empty list of tasks.
        """
        self.tasks = []
        self.next_id = 1

    def create_task(self, title, description, due_date=None):
        """
        Create a new task and add it to the list.

        Args:
            title (str): Task title.
            description (str): Task description.
            due_date (str, optional): Task due date. Defaults to None.

        Returns:
            Task: The newly created task.
        """
        task = Task(self.next_id, title, description, due_date)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_task(self, id):
        """
        Get a task by its ID.

        Args:
            id (int): Task ID.

        Returns:
            Task: The task with the matching ID, or None if not found.
        """
        for task in self.tasks:
            if task.id == id:
                return task
        return None

    def update_task(self, id, title=None, description=None, due_date=None):
        """
        Update a task's details.

        Args:
            id (int): Task ID.
            title (str, optional): New task title. Defaults to None.
            description (str, optional): New task description. Defaults to None.
            due_date (str, optional): New task due date. Defaults to None.

        Returns:
            bool: True if the task was updated successfully, False otherwise.
        """
        task = self.get_task(id)
        if task is not None:
            if title:
                task.title = title
            if description:
                task.description = description
            if due_date:
                task.due_date = due_date
            return True
        return False

    def delete_task(self, id):
        """
        Delete a task by its ID.

        Args:
            id (int): Task ID.

        Returns:
            bool: True if the task was deleted successfully, False otherwise.
        """
        for i, task in enumerate(self.tasks):
            if task.id == id:
                del self.tasks[i]
                return True
        return False

    def list_tasks(self):
        """
        Get a list of all tasks.

        Returns:
            list[Task]: The list of tasks.
        """
        return self.tasks

# Example usage
if __name__ == "__main__":
    task_manager = TaskManager()

    # Create some tasks
    task1 = task_manager.create_task("Buy milk", "Get 2 liters of milk")
    task2 = task_manager.create_task("Walk the dog", "Take the dog for a 30-minute walk")

    # Print the list of tasks
    print("Tasks:")
    for task in task_manager.list_tasks():
        print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}")

    # Update a task
    task_manager.update_task(task1.id, description="Get 3 liters of milk")
    print("\nUpdated task:")
    print(f"ID: {task1.id}, Title: {task1.title}, Description: {task1.description}")

    # Delete a task
    task_manager.delete_task(task2.id)
    print("\nTasks after deletion:")
    for task in task_manager.list_tasks():
        print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}")
```
### API Documentation

* `Task`: Represents a single task with an ID, title, description, and due date.
	+ `__init__(id, title, description, due_date=None)`: Initialize a new task.
* `TaskManager`: Manages a list of tasks.
	+ `__init__()`: Initialize the task manager with an empty list of tasks.
	+ `create_task(title, description, due_date=None)`: Create a new task and add it to the list.
	+ `get_task(id)`: Get a task by its ID.
	+ `update_task(id, title=None, description=None, due_date=None)`: Update a task's details.
	+ `delete_task(id)`: Delete a task by its ID.
	+ `list_tasks()`: Get a list of all tasks.

### Usage

1. Import the module: `import task_manager`
2. Create a new task manager instance: `task_manager = task_manager.TaskManager()`
3. Create tasks using the `create_task` method: `task1 = task_manager.create_task("Buy milk", "Get 2 liters of milk")`
4. Update tasks using the `update_task` method: `task_manager.update_task(task1.id, description="Get 3 liters of milk")`
5. Delete tasks using the `delete_task` method: `task_manager.delete_task(task2.id)`
6. List all tasks using the `list_tasks` method: `tasks = task_manager.list_tasks()`