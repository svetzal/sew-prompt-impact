### Task Manager Module
#### Overview
This Python module provides a simple task management system. It allows users to create, read, update, and delete (CRUD) tasks.

#### Code

```python
# task_manager.py

class Task:
    """Represents a single task."""
    def __init__(self, title, description):
        """
        Initializes a Task object.

        Args:
            title (str): The title of the task.
            description (str): A brief description of the task.
        """
        self.title = title
        self.description = description

class TaskManager:
    """Manages a list of tasks."""
    def __init__(self):
        """Initializes an empty task list."""
        self.tasks = []

    def create_task(self, title, description):
        """
        Creates a new task and adds it to the task list.

        Args:
            title (str): The title of the task.
            description (str): A brief description of the task.
        """
        new_task = Task(title, description)
        self.tasks.append(new_task)

    def read_tasks(self):
        """Returns a list of all tasks."""
        return self.tasks

    def update_task(self, index, title=None, description=None):
        """
        Updates an existing task.

        Args:
            index (int): The index of the task to update.
            title (str, optional): The new title. Defaults to None.
            description (str, optional): The new description. Defaults to None.
        """
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Invalid task index")
        
        if title:
            self.tasks[index].title = title
        if description:
            self.tasks[index].description = description

    def delete_task(self, index):
        """
        Deletes a task from the task list.

        Args:
            index (int): The index of the task to delete.
        """
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Invalid task index")
        
        del self.tasks[index]

# Example usage
if __name__ == "__main__":
    manager = TaskManager()
    
    # Create tasks
    manager.create_task("Buy groceries", "Milk, eggs, and bread")
    manager.create_task("Finish project", "Meet the deadline")

    # Read tasks
    print("Tasks:")
    for i, task in enumerate(manager.read_tasks()):
        print(f"{i+1}. {task.title}: {task.description}")

    # Update task
    manager.update_task(0, title="Buy more groceries")
    
    # Delete task
    manager.delete_task(1)

    # Read tasks again
    print("\nUpdated Tasks:")
    for i, task in enumerate(manager.read_tasks()):
        print(f"{i+1}. {task.title}: {task.description}")
```

#### Tests

```python
# test_task_manager.py
import unittest
from task_manager import TaskManager, Task

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_create_task(self):
        self.manager.create_task("Test", "This is a test")
        self.assertEqual(len(self.manager.tasks), 1)

    def test_read_tasks(self):
        self.manager.create_task("Task 1", "Description 1")
        self.manager.create_task("Task 2", "Description 2")
        tasks = self.manager.read_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertIsInstance(tasks[0], Task)

    def test_update_task(self):
        self.manager.create_task("Test", "This is a test")
        self.manager.update_task(0, title="Updated Test")
        self.assertEqual(self.manager.tasks[0].title, "Updated Test")

    def test_delete_task(self):
        self.manager.create_task("Task 1", "Description 1")
        self.manager.create_task("Task 2", "Description 2")
        self.manager.delete_task(0)
        self.assertEqual(len(self.manager.tasks), 1)

if __name__ == "__main__":
    unittest.main()
```

#### Explanation
This implementation follows the baseline conventions outlined. The code is organized into two classes: `Task` and `TaskManager`. The `Task` class represents a single task with a title and description, while the `TaskManager` class manages a list of tasks.

The `TaskManager` class provides methods for creating, reading, updating, and deleting tasks. It also includes example usage in the `if __name__ == "__main__":` block.

The tests are written using the `unittest` framework and cover all the methods in the `TaskManager` class. They ensure that the implementation behaves as expected.