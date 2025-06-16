### Task Manager Module
#### Description
A Python module to manage a list of tasks. This module follows the principles outlined in the Baseline Conventions document, emphasizing simplicity, testability, and maintainability.

#### Code
```python
# task_manager.py

class Task:
    """Represents a single task with a description and status."""
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        """Marks the task as completed."""
        self.completed = True

    def mark_incomplete(self):
        """Marks the task as incomplete."""
        self.completed = False


class TaskManager:
    """Manages a list of tasks."""
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        """Adds a new task to the list."""
        task = Task(description)
        self.tasks.append(task)

    def remove_task(self, index):
        """Removes a task from the list by its index."""
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            raise IndexError("Task index out of range")

    def get_tasks(self):
        """Returns a list of all tasks."""
        return self.tasks

    def complete_task(self, index):
        """Marks a task as completed by its index."""
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
        else:
            raise IndexError("Task index out of range")

    def incomplete_task(self, index):
        """Marks a task as incomplete by its index."""
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_incomplete()
        else:
            raise IndexError("Task index out of range")


# Example usage
if __name__ == "__main__":
    task_manager = TaskManager()

    # Add tasks
    task_manager.add_task("Buy milk")
    task_manager.add_task("Walk the dog")

    # Print all tasks
    print("Tasks:")
    for i, task in enumerate(task_manager.get_tasks()):
        status = "Completed" if task.completed else "Not completed"
        print(f"{i}: {task.description} - {status}")

    # Complete a task
    task_manager.complete_task(0)

    # Print all tasks again
    print("\nTasks after completing the first task:")
    for i, task in enumerate(task_manager.get_tasks()):
        status = "Completed" if task.completed else "Not completed"
        print(f"{i}: {task.description} - {status}")
```

#### Tests
```python
# test_task_manager.py

import unittest
from task_manager import Task, TaskManager

class TestTask(unittest.TestCase):
    def test_mark_completed(self):
        task = Task("Buy milk")
        self.assertFalse(task.completed)
        task.mark_completed()
        self.assertTrue(task.completed)

    def test_mark_incomplete(self):
        task = Task("Walk the dog")
        task.mark_completed()
        self.assertTrue(task.completed)
        task.mark_incomplete()
        self.assertFalse(task.completed)


class TestTaskManager(unittest.TestCase):
    def test_add_task(self):
        task_manager = TaskManager()
        task_manager.add_task("Buy milk")
        self.assertEqual(len(task_manager.get_tasks()), 1)

    def test_remove_task(self):
        task_manager = TaskManager()
        task_manager.add_task("Buy milk")
        task_manager.remove_task(0)
        self.assertEqual(len(task_manager.get_tasks()), 0)

    def test_get_tasks(self):
        task_manager = TaskManager()
        task_manager.add_task("Buy milk")
        task_manager.add_task("Walk the dog")
        tasks = task_manager.get_tasks()
        self.assertEqual(len(tasks), 2)

    def test_complete_task(self):
        task_manager = TaskManager()
        task_manager.add_task("Buy milk")
        task_manager.complete_task(0)
        self.assertTrue(task_manager.get_tasks()[0].completed)

    def test_incomplete_task(self):
        task_manager = TaskManager()
        task_manager.add_task("Walk the dog")
        task_manager.complete_task(0)
        task_manager.incomplete_task(0)
        self.assertFalse(task_manager.get_tasks()[0].completed)


if __name__ == "__main__":
    unittest.main()
```
This code defines two classes: `Task` and `TaskManager`. The `Task` class represents a single task with a description and status, while the `TaskManager` class manages a list of tasks. The example usage demonstrates how to create a `TaskManager`, add tasks, print all tasks, complete a task, and print all tasks again after completing the first task.

The tests cover various scenarios for both classes, ensuring that the code behaves as expected. They check the status of tasks, adding and removing tasks from the list, retrieving the list of tasks, and marking tasks as completed or incomplete.