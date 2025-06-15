Below is a simple self-contained Python module (`tasks.py`) that lets you create and manage an in-memory list of tasks, with optional persistence to JSON. You can import `TaskManager` in your own scripts or extend it as needed.

```python
# tasks.py
from __future__ import annotations
import json
import uuid
from dataclasses import dataclass, field, asdict
from datetime import datetime, date
from typing import List, Optional, Dict


@dataclass
class Task:
    """
    A simple Task record.
    """
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str = field(default="")
    description: str = field(default="")
    due_date: Optional[date] = field(default=None)
    created_at: datetime = field(default_factory=datetime.now)
    completed: bool = field(default=False)

    def to_dict(self) -> Dict:
        """
        Convert to JSON-serializable dict.
        """
        d = asdict(self)
        # serialize dates/times to isoformat
        d["created_at"] = self.created_at.isoformat()
        d["due_date"] = self.due_date.isoformat() if self.due_date else None
        return d

    @staticmethod
    def from_dict(d: Dict) -> Task:
        """
        Reconstruct a Task from dict (as produced by to_dict).
        """
        td = date.fromisoformat(d["due_date"]) if d.get("due_date") else None
        ca = datetime.fromisoformat(d["created_at"])
        return Task(
            id=d["id"],
            title=d["title"],
            description=d.get("description", ""),
            due_date=td,
            created_at=ca,
            completed=d.get("completed", False),
        )


class TaskManager:
    """
    In-memory manager for a list of Task objects.
    """

    def __init__(self) -> None:
        self._tasks: List[Task] = []

    def add_task(
        self,
        title: str,
        description: str = "",
        due_date: Optional[date] = None,
    ) -> Task:
        """
        Create a new task and add it to the list.
        """
        task = Task(title=title, description=description, due_date=due_date)
        self._tasks.append(task)
        return task

    def get_task(self, task_id: str) -> Optional[Task]:
        """
        Return the Task with the given id, or None if not found.
        """
        for t in self._tasks:
            if t.id == task_id:
                return t
        return None

    def list_tasks(self, *, show_completed: Optional[bool] = None) -> List[Task]:
        """
        Return all tasks, or filter by completion status.
        - show_completed=True  → only completed tasks
        - show_completed=False → only uncompleted tasks
        - show_completed=None  → all tasks
        """
        if show_completed is None:
            return list(self._tasks)
        return [t for t in self._tasks if t.completed is show_completed]

    def remove_task(self, task_id: str) -> bool:
        """
        Remove a task by id. Returns True if removed, False if not found.
        """
        task = self.get_task(task_id)
        if task:
            self._tasks.remove(task)
            return True
        return False

    def mark_completed(self, task_id: str) -> bool:
        """
        Mark the given task as completed. Returns True on success.
        """
        task = self.get_task(task_id)
        if task and not task.completed:
            task.completed = True
            return True
        return False

    def mark_uncompleted(self, task_id: str) -> bool:
        """
        Mark the given task as uncompleted. Returns True on success.
        """
        task = self.get_task(task_id)
        if task and task.completed:
            task.completed = False
            return True
        return False

    def save_to_file(self, file_path: str) -> None:
        """
        Save all tasks to a JSON file.
        """
        with open(file_path, "w", encoding="utf-8") as f:
            data = [t.to_dict() for t in self._tasks]
            json.dump(data, f, indent=2)

    def load_from_file(self, file_path: str) -> None:
        """
        Load tasks from a JSON file, replacing any in-memory tasks.
        """
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self._tasks = [Task.from_dict(item) for item in data]
```

Usage example:

```python
# example_usage.py
from datetime import date
from tasks import TaskManager

tm = TaskManager()

# add some tasks
t1 = tm.add_task("Buy groceries", "Milk, eggs, bread", due_date=date(2024, 7, 1))
t2 = tm.add_task("Finish report", "Annual finance report")

# list all
for t in tm.list_tasks():
    print(f"{t.id[:8]} | {t.title:20} | done={t.completed}")

# mark one completed
tm.mark_completed(t1.id)

# save to disk
tm.save_to_file("my_tasks.json")

# later or in another script
tm2 = TaskManager()
tm2.load_from_file("my_tasks.json")
print("Loaded tasks:", tm2.list_tasks())
```

Feel free to extend it with CLI hooks, database backends, priority levels, etc.