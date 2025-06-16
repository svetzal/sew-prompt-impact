Here is a well-structured Python module that manages a list of tasks, designed with clarity, maintainability, and the principles of good software engineering in mind.

---

### ✅ Features

- **Task Management** – Create, retrieve, update, and delete tasks
- **Task Status** – Each task has a status (`'pending'` or `'completed'`)
- **Task ID** – Unique ID assigned automatically
- **Filtering** – Retrieve tasks based on their status
- **Immutability & Clean Design** – The internal state is encapsulated within a class
- **Docstrings** – Each method is well-documented

---

### 📁 `task_manager.py`

```python
from typing import List, Dict, Optional, Union

class TaskManager:
    """
    Manages a list of tasks with support for adding, retrieving, updating, and deleting tasks.
    Each task is uniquely identified by an ID, and has a title and a status ('pending' or 'completed').
    """

    def __init__(self):
        """
        Initializes an empty list of tasks and a counter for task IDs.
        """
        self.tasks = []
        self.next_id = 1

    def add_task(self, title: str) -> int:
        """
        Adds a new task with the given title and returns its unique ID.

        :param title: Title of the task
        :return: ID of the newly added task
        """
        task = {
            'id': self.next_id,
            'title': title,
            'status': 'pending'
        }
        self.tasks.append(task)
        self.next_id += 1
        return task['id']

    def get_tasks(self, status: Optional[str] = None) -> List[Dict]:
        """
        Retrieves all tasks, optionally filtered by their status.

        :param status: Status to filter by ('pending' or 'completed'), or None for all
        :return: List of tasks
        """
        if status:
            return [task for task in self.tasks if task['status'] == status]
        return self.tasks

    def get_task(self, task_id: int) -> Optional[Dict]:
        """
        Retrieves a specific task by its ID.

        :param task_id: Unique identifier of the task
        :return: Task dictionary or None if not found
        """
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return None

    def update_task(self, task_id: int, updates: Dict[str, Union[str, int]]) -> bool:
        """
        Updates a task's attributes by ID.

        :param task_id: Unique identifier of the task
        :param updates: Dictionary of key-value pairs to update
        :return: True if the task was successfully updated, False otherwise
        """
        task = self.get_task(task_id)
        if not task:
            return False
        task.update(updates)
        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Deletes a task by ID.

        :param task_id: Unique identifier of the task
        :return: True if the task was successfully deleted, False otherwise
        """
        task = self.get_task(task_id)
        if not task:
            return False
        self.tasks.remove(task)
        return True

    def mark_as_complete(self, task_id: int) -> bool:
        """
        Marks a task as completed by updating its status.

        :param task_id: Unique identifier of the task
        :return: True if the task was successfully marked as complete, False otherwise
        """
        return self.update_task(task_id, {'status': 'completed'})
```

---

### 🧪 Example Usage

```python
tm = TaskManager()
task_id_1 = tm.add_task("Finish the project")
task_id_2 = tm.add_task("Write documentation")

print(tm.get_tasks())  # Get all tasks
print(tm.get_task(task_id_1))  # Get specific task
tm.mark_as_complete(task_id_1)
print(tm.get_tasks("completed"))  # Get completed tasks
tm.delete_task(task_id_2)
```

---

### 📝 Notes

- The design follows the principle of **"Functional Core, Imperative Shell"**, by isolating mutable state within the class.
- The `update_task` method allows for flexible modification of task attributes.
- All operations return a clear boolean to indicate success or failure.
- You may extend this module in the future by adding features like due dates, tags, or persisting tasks to disk.

---

This module provides a clean, intuitive, and extendable interface for managing tasks in a Python project.