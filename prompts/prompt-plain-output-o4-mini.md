Below is a self‐contained Python module (`tasks.py`) which provides:

• A `Task` class (id, description, completed flag)  
• A `TaskManager` class (in‐memory list of tasks + add/remove/complete/list)  
• JSON persistence (`save`/`load`)  
• A simple CLI when run as a script  

Paste this into a file named `tasks.py` and you can both import it in your own code or drive it from the command‐line.

```python
#!/usr/bin/env python3
"""
tasks.py

A simple task management module + CLI.
"""

import json
import argparse
import sys
from typing import List, Optional, Dict


class Task:
    """
    Represents a single task.
    """
    def __init__(self, id: int, description: str, completed: bool = False):
        self.id = id
        self.description = description
        self.completed = completed

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "description": self.description,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, d: Dict) -> "Task":
        return cls(id=d["id"], description=d["description"], completed=d.get("completed", False))

    def __repr__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] ({self.id}) {self.description}"


class TaskManager:
    """
    Manages a list of Task objects in memory, with JSON persistence.
    """
    def __init__(self):
        self._tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, description: str) -> Task:
        """
        Create a new task with the next available ID.
        """
        task = Task(id=self._next_id, description=description)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def remove_task(self, task_id: int) -> bool:
        """
        Remove the task with the given ID. Returns True if removed.
        """
        for i, t in enumerate(self._tasks):
            if t.id == task_id:
                del self._tasks[i]
                return True
        return False

    def complete_task(self, task_id: int) -> bool:
        """
        Mark the task with the given ID as completed. Returns True if found.
        """
        for t in self._tasks:
            if t.id == task_id:
                t.completed = True
                return True
        return False

    def uncomplete_task(self, task_id: int) -> bool:
        """
        Mark the task with the given ID as not completed.
        """
        for t in self._tasks:
            if t.id == task_id:
                t.completed = False
                return True
        return False

    def list_tasks(self, show_completed: bool = True) -> List[Task]:
        """
        Return a list of tasks.  
        If show_completed is False, filter out completed tasks.
        """
        if show_completed:
            return list(self._tasks)
        else:
            return [t for t in self._tasks if not t.completed]

    def save(self, filepath: str) -> None:
        """
        Save all tasks to a JSON file.
        """
        data = {
            "next_id": self._next_id,
            "tasks": [t.to_dict() for t in self._tasks]
        }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def load(self, filepath: str) -> None:
        """
        Load tasks from a JSON file, replacing any in-memory tasks.
        """
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        self._tasks = [Task.from_dict(d) for d in data.get("tasks", [])]
        self._next_id = data.get("next_id", 1)


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Task Manager CLI")
    p.add_argument("--file", "-f", default="tasks.json",
                   help="Path to JSON file to load/save tasks")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list", help="List tasks").add_argument(
        "--show-completed", action="store_true", help="Also show completed tasks"
    )

    a = sub.add_parser("add", help="Add a new task")
    a.add_argument("description", nargs="+", help="Description of the task")

    r = sub.add_parser("remove", help="Remove a task by ID")
    r.add_argument("id", type=int, help="ID of the task to remove")

    c = sub.add_parser("complete", help="Mark a task completed")
    c.add_argument("id", type=int, help="ID of the task to complete")

    u = sub.add_parser("uncomplete", help="Mark a task as not completed")
    u.add_argument("id", type=int, help="ID of the task to un-complete")

    return p


def main():
    parser = _build_parser()
    args = parser.parse_args()

    mgr = TaskManager()
    # Load existing tasks if file exists
    try:
        mgr.load(args.file)
    except (IOError, json.JSONDecodeError):
        # no file yet or bad format → start fresh
        pass

    if args.cmd == "list":
        tasks = mgr.list_tasks(show_completed=args.show_completed)
        if not tasks:
            print("No tasks found.")
        else:
            for t in tasks:
                print(t)

    elif args.cmd == "add":
        desc = " ".join(args.description)
        t = mgr.add_task(desc)
        print(f"Added: {t}")

    elif args.cmd == "remove":
        success = mgr.remove_task(args.id)
        print("Removed." if success else "Task not found.")

    elif args.cmd == "complete":
        success = mgr.complete_task(args.id)
        print("Completed." if success else "Task not found.")

    elif args.cmd == "uncomplete":
        success = mgr.uncomplete_task(args.id)
        print("Marked as not completed." if success else "Task not found.")

    # Save back
    try:
        mgr.save(args.file)
    except IOError as e:
        print(f"Error saving tasks to {args.file}: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
```

How to use:

1. Save as `tasks.py` and make executable (`chmod +x tasks.py`)  
2. From the command line:

   • `./tasks.py add "Buy milk"`  
   • `./tasks.py list`  
   • `./tasks.py list --show-completed`  
   • `./tasks.py complete 1`  
   • `./tasks.py remove 1`  

3. By default it reads/writes `tasks.json` in the current directory. Change via `-f /path/to/file.json`.

4. In your own Python code, you can import:

```python
from tasks import TaskManager

mgr = TaskManager()
mgr.load("tasks.json")
mgr.add_task("Do the laundry")
mgr.complete_task(2)
mgr.save("tasks.json")
```

This should give you a lightweight, yet extendable, task manager you can build on!