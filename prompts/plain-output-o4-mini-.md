Here’s a self-contained Python module (save as `task_manager.py`) that defines a `Task` object and a `TaskManager` to create, update, delete, list, mark complete, and persist your tasks to disk.

```python
import json
from datetime import datetime
from typing import List, Optional

class Task:
    """
    Represents a single to-do task.
    """
    def __init__(self,
                 title: str,
                 description: str = "",
                 due_date: Optional[datetime] = None,
                 priority: Optional[int] = None,
                 completed: bool = False):
        self.id = None  # will be set by TaskManager
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = completed
        self.created_at = datetime.now()

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        t = cls(
            title=data["title"],
            description=data.get("description", ""),
            due_date=datetime.fromisoformat(data["due_date"]) if data.get("due_date") else None,
            priority=data.get("priority"),
            completed=data.get("completed", False),
        )
        t.id = data.get("id")
        t.created_at = datetime.fromisoformat(data["created_at"])
        return t

    def __str__(self):
        status = "✓" if self.completed else "✗"
        due = self.due_date.strftime("%Y-%m-%d %H:%M") if self.due_date else "No due"
        prio = f"P{self.priority}" if self.priority is not None else ""
        return f"[{status}] {self.id}: {self.title} {prio} (due: {due})"

class TaskManager:
    """
    Manages a list of Task objects, supports add/remove/update/list/save/load.
    """
    def __init__(self, storage_file: str = "tasks.json"):
        self.storage_file = storage_file
        self.tasks: List[Task] = []
        self._next_id = 1
        self.load()

    def _reindex(self):
        # ensure unique incremental IDs
        self._next_id = 1
        for t in self.tasks:
            t.id = self._next_id
            self._next_id += 1

    def add_task(self,
                 title: str,
                 description: str = "",
                 due_date: Optional[datetime] = None,
                 priority: Optional[int] = None) -> Task:
        t = Task(title, description, due_date, priority)
        t.id = self._next_id
        self._next_id += 1
        self.tasks.append(t)
        return t

    def remove_task(self, task_id: int) -> bool:
        for i, t in enumerate(self.tasks):
            if t.id == task_id:
                del self.tasks[i]
                self._reindex()
                return True
        return False

    def get_task(self, task_id: int) -> Optional[Task]:
        return next((t for t in self.tasks if t.id == task_id), None)

    def mark_complete(self, task_id: int) -> bool:
        t = self.get_task(task_id)
        if t:
            t.completed = True
            return True
        return False

    def mark_incomplete(self, task_id: int) -> bool:
        t = self.get_task(task_id)
        if t:
            t.completed = False
            return True
        return False

    def list_tasks(self,
                   show_completed: bool = True,
                   sort_by: str = None) -> List[Task]:
        result = self.tasks
        if not show_completed:
            result = [t for t in result if not t.completed]
        if sort_by == "due":
            result = sorted(result, key=lambda t: (t.due_date or datetime.max))
        elif sort_by == "priority":
            result = sorted(result, key=lambda t: (t.priority or 0))
        return result

    def save(self):
        data = [t.to_dict() for t in self.tasks]
        with open(self.storage_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def load(self):
        try:
            with open(self.storage_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.tasks = [Task.from_dict(d) for d in data]
            # reset next id
            self._reindex()
        except (FileNotFoundError, json.JSONDecodeError):
            # start fresh
            self.tasks = []
            self._next_id = 1

if __name__ == "__main__":
    # Simple demo usage
    tm = TaskManager()

    # add some tasks
    t1 = tm.add_task("Buy milk", "2L of skim", priority=2)
    t2 = tm.add_task("Write report", due_date=datetime(2023,5,1,17,0), priority=1)
    tm.mark_complete(t1.id)

    # list all tasks
    print("All tasks:")
    for task in tm.list_tasks():
        print(" ", task)

    # list incomplete only, sorted by priority
    print("\nIncomplete tasks by priority:")
    for task in tm.list_tasks(show_completed=False, sort_by="priority"):
        print(" ", task)

    # save to disk
    tm.save()
    print("\nTasks saved to", tm.storage_file)
```

How to use:

1. Import in your code:
   ```python
   from task_manager import TaskManager
   ```
2. Create or load your manager:
   ```python
   tm = TaskManager("mytasks.json")
   ```
3. Add tasks:
   ```python
   tm.add_task("Do laundry", "Use cold water", priority=3)
   ```
4. Mark complete / remove / list:
   ```python
   tm.mark_complete(1)
   tm.remove_task(2)
   for t in tm.list_tasks(show_completed=False, sort_by="due"):
       print(t)
   ```
5. Don’t forget to `tm.save()` when you’re done!