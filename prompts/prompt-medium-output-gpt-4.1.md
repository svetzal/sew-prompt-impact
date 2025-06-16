Of course! Below you'll find a **Python module** called `task_manager.py` implementing a minimal, easy-to-read Task Manager according to your **Baseline Conventions**.

## Features

- **Add tasks**
- **Mark tasks complete/incomplete**
- **List all tasks**
- **Remove tasks**
- **Pure data structures for core logic**  
- **No I/O in business logic** (imperative shell can be built around this if desired)
- **Simple, readable, tested**

---

```python
# task_manager.py
from dataclasses import dataclass, field
from typing import List, Optional
import itertools

@dataclass(frozen=True)
class Task:
    id: int
    description: str
    completed: bool = False

class TaskManager:
    def __init__(self):
        self._tasks: List[Task] = []
        self._id_counter = itertools.count(1)

    def add(self, description: str) -> Task:
        task = Task(id=next(self._id_counter), description=description)
        self._tasks.append(task)
        return task

    def list(self) -> List[Task]:
        return list(self._tasks)

    def get(self, task_id: int) -> Optional[Task]:
        return next((t for t in self._tasks if t.id == task_id), None)

    def complete(self, task_id: int) -> bool:
        idx = self._find_index(task_id)
        if idx is None:
            return False
        t = self._tasks[idx]
        if t.completed:
            return True
        self._tasks[idx] = Task(id=t.id, description=t.description, completed=True)
        return True

    def incomplete(self, task_id: int) -> bool:
        idx = self._find_index(task_id)
        if idx is None:
            return False
        t = self._tasks[idx]
        if not t.completed:
            return True
        self._tasks[idx] = Task(id=t.id, description=t.description, completed=False)
        return True

    def remove(self, task_id: int) -> bool:
        idx = self._find_index(task_id)
        if idx is None:
            return False
        del self._tasks[idx]
        return True

    def _find_index(self, task_id: int) -> Optional[int]:
        for i, task in enumerate(self._tasks):
            if task.id == task_id:
                return i
        return None

# Optional: minimal in-module tests (executable spec)

if __name__ == "__main__":
    tm = TaskManager()
    assert tm.list() == []
    t1 = tm.add("Write code")
    t2 = tm.add("Test code")
    assert [x.description for x in tm.list()] == ["Write code", "Test code"]
    assert not t1.completed
    assert tm.complete(t1.id)
    assert tm.get(t1.id).completed
    assert tm.incomplete(t1.id)
    assert not tm.get(t2.id).completed
    assert tm.remove(t2.id)
    assert len(tm.list()) == 1
    print("All tests passed.")
```

---

## Notes  
- **No I/O or CLI** in this file: All functions are pure except storage (`_tasks` list).
- **Logic is clear**: Adding new features or adapting storage to, e.g., a database, is easy.
- **Tests double as spec** and sanity check.
- **No knowledge duplication**: logic isn’t repeated.
- **Entities**: Only `Task` and `TaskManager`.

If you want a CLI or persistence, a small wrapper can be added—let me know if you need it!