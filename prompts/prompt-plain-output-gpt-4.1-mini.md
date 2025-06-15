Sure! Here's a Python module called `task_manager.py` that can manage a list of tasks. It provides functionality to add, remove, update, list, and find tasks.

```python
# task_manager.py

from typing import List, Optional


class Task:
    def __init__(self, id: int, description: str, completed: bool = False):
        self.id = id
        self.description = description
        self.completed = completed

    def __repr__(self):
        status = "✔" if self.completed else "✘"
        return f"Task(id={self.id}, description='{self.description}', completed={status})"

    def to_dict(self):
        return {"id": self.id, "description": self.description, "completed": self.completed}


class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, description: str) -> Task:
        task = Task(self._next_id, description)
        self.tasks.append(task)
        self._next_id += 1
        return task

    def remove_task(self, task_id: int) -> bool:
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                return True
        return False

    def update_task(self, task_id: int, description: Optional[str] = None, completed: Optional[bool] = None) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                if description is not None:
                    task.description = description
                if completed is not None:
                    task.completed = completed
                return True
        return False

    def list_tasks(self, completed: Optional[bool] = None) -> List[Task]:
        if completed is None:
            return self.tasks[:]
        return [task for task in self.tasks if task.completed == completed]

    def find_task(self, task_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None


# Example usage:
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Buy groceries")
    manager.add_task("Finish project")
    manager.update_task(2, completed=True)

    print("All tasks:")
    for task in manager.list_tasks():
        print(task)

    print("\nCompleted tasks:")
    for task in manager.list_tasks(completed=True):
        print(task)
```

### Features:
- Add a task by description.
- Remove a task by its unique ID.
- Update a task's description and/or completion status.
- List all tasks or filter by completion status.
- Find a task by ID.

Would you like me to add persistence (saving/loading to a file) or more advanced features?