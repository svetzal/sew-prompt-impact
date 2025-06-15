Certainly! Here’s a simple Python module for managing a list of tasks, following the specified engineering principles and conventions.

```python
# tasks.py

from dataclasses import dataclass, field
from typing import List, Optional
import uuid

@dataclass(frozen=True)
class Task:
    id: str
    description: str
    completed: bool = False

def _generate_id() -> str:
    return str(uuid.uuid4())

class TaskManager:
    def __init__(self):
        self._tasks: List[Task] = []
    
    def add(self, description: str) -> Task:
        """Add a new task with the provided description."""
        new_task = Task(id=_generate_id(), description=description)
        self._tasks.append(new_task)
        return new_task

    def list(self, show_completed: Optional[bool]=None) -> List[Task]:
        """
        Return all tasks, optionally filtering by completion status.
        :param show_completed: If set to True or False, returns only tasks with that completed status.
        """
        if show_completed is None:
            return list(self._tasks)
        return [task for task in self._tasks if task.completed == show_completed]

    def complete(self, task_id: str) -> bool:
        """Mark a task as completed. Returns True if successful, False if not found."""
        for idx, task in enumerate(self._tasks):
            if task.id == task_id and not task.completed:
                self._tasks[idx] = Task(id=task.id, description=task.description, completed=True)
                return True
        return False

    def delete(self, task_id: str) -> bool:
        """Delete a task by its ID. Returns True if successful, False if not found."""
        for idx, task in enumerate(self._tasks):
            if task.id == task_id:
                del self._tasks[idx]
                return True
        return False
    
    def clear(self):
        """Remove all tasks."""
        self._tasks.clear()
```

## Example usage:

```python
if __name__ == '__main__':
    mgr = TaskManager()
    t = mgr.add("Write documentation")
    print(mgr.list())
    mgr.complete(t.id)
    print(mgr.list(show_completed=True))
    mgr.delete(t.id)
    print(mgr.list())
```

---

**Notes:**
- The `Task` dataclass is immutable for safety.
- No global state, simple interface: `add`, `list`, `complete`, `delete`, `clear`.
- No I/O in core logic—side effects (like printing) happen outside.
- All changes made in-place are safe, in small increments.
- To test, mock or replace the I/O/context at the boundaries.  
- Designed for easy extension (e.g., persistence, search).  

Let me know if you’d like tests, CLI, or other extensions!