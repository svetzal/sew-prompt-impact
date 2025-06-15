Here’s a simple self-contained Python module, `tasks.py`, that lets you create, list, update, delete and persist a to-do list. It uses a `TaskManager` class and keeps tasks in JSON on disk.

```python
# tasks.py

import json
import os
from typing import List, Optional
from dataclasses import dataclass, asdict

@dataclass
class Task:
    id: int
    description: str
    done: bool = False

class TaskManager:
    def __init__(self, storage_path: str = "tasks.json"):
        self.storage_path = storage_path
        self.tasks: List[Task] = []
        self._next_id = 1
        self.load()

    def add_task(self, description: str) -> Task:
        """Add a new task."""
        task = Task(id=self._next_id, description=description, done=False)
        self.tasks.append(task)
        self._next_id += 1
        self.save()
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """Return the task with given id, or None."""
        return next((t for t in self.tasks if t.id == task_id), None)

    def list_tasks(self, show_done: bool = True) -> List[Task]:
        """Return all tasks; if show_done=False, only pending tasks."""
        if show_done:
            return list(self.tasks)
        return [t for t in self.tasks if not t.done]

    def mark_done(self, task_id: int) -> bool:
        """Mark the specified task as done. Returns True if successful."""
        t = self.get_task(task_id)
        if not t:
            return False
        t.done = True
        self.save()
        return True

    def delete_task(self, task_id: int) -> bool:
        """Delete the specified task. Returns True if successful."""
        t = self.get_task(task_id)
        if not t:
            return False
        self.tasks.remove(t)
        self.save()
        return True

    def save(self) -> None:
        """Persist the task list and next id to disk."""
        data = {
            "next_id": self._next_id,
            "tasks": [asdict(t) for t in self.tasks]
        }
        with open(self.storage_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def load(self) -> None:
        """Load tasks (and next_id) from disk, if file exists."""
        if not os.path.exists(self.storage_path):
            return
        try:
            with open(self.storage_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self._next_id = data.get("next_id", 1)
            self.tasks = [Task(**t) for t in data.get("tasks", [])]
        except (IOError, ValueError):
            # If file is corrupted, start fresh
            self.tasks = []
            self._next_id = 1

if __name__ == "__main__":
    # Simple CLI demo
    import argparse
    parser = argparse.ArgumentParser(description="Simple Task Manager")
    parser.add_argument("--add", "-a", help="Add a new task", metavar="DESC")
    parser.add_argument("--list", "-l", action="store_true", help="List tasks")
    parser.add_argument("--done", "-d", type=int, help="Mark task as done by ID")
    parser.add_argument("--delete", "-r", type=int, help="Remove task by ID")
    args = parser.parse_args()

    mgr = TaskManager()

    if args.add:
        task = mgr.add_task(args.add)
        print(f"Added task {task.id}: {task.description}")

    elif args.done is not None:
        if mgr.mark_done(args.done):
            print(f"Marked task {args.done} as done.")
        else:
            print(f"No task with ID {args.done} found.")

    elif args.delete is not None:
        if mgr.delete_task(args.delete):
            print(f"Deleted task {args.delete}.")
        else:
            print(f"No task with ID {args.delete} found.")

    elif args.list:
        tasks = mgr.list_tasks(show_done=True)
        if not tasks:
            print("No tasks.")
        else:
            for t in tasks:
                status = "[x]" if t.done else "[ ]"
                print(f"{t.id:3} {status} {t.description}")

    else:
        parser.print_help()
```

Usage example (interactive Python):

```python
from tasks import TaskManager
mgr = TaskManager("mytasks.json")

# Add tasks
mgr.add_task("Buy milk")
mgr.add_task("Write report")

# Mark task 1 done
mgr.mark_done(1)

# List pending only
for t in mgr.list_tasks(show_done=False):
    print(t)

# Delete a task
mgr.delete_task(2)
```

Or shell-style:

```
$ python tasks.py --add "Clean house"
$ python tasks.py --list
  1 [ ] Clean house
$ python tasks.py --done 1
$ python tasks.py --list
  1 [x] Clean house
```