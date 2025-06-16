Here's a Python module that manages a list of tasks while adhering to the [Baseline Conventions](#baseline-conventions) you provided. The implementation follows functional principles for pure logic and uses a class for imperative state management, aligning with the **functional core, imperative shell** pattern.

---

### ✅ Features
- **Immutable core functions** for adding, removing, and marking tasks as completed.
- A **TaskManager** class for mutable state interaction.
- Clean API, with all code communicating clearly and avoiding unnecessary complexity.

---

### ✅ Key Design Choices
- **Task as Dataclass**: Makes `Task` objects self-documenting and easy to reason about.
- **Pure Functions**: Ensure no side effects for core logic.
- **TaskManager**: Provides an imperative interface to manage state, encapsulating mutable operations.
- **UUID-based Task IDs**: Avoid naming collisions and enforce task identity.
- **Minimal Entities**: Only the essential classes and functions are included.

---

### 📁 Module Structure: `task_manager.py`

```python
from dataclasses import dataclass
from uuid import uuid4
from typing import List, Optional

# ------------------------
# Core Data Structure
# ------------------------
@dataclass
class Task:
    id: str
    description: str
    completed: bool = False

# ------------------------
# Pure Functions (Functional Core)
# ------------------------
def create_task(description: str) -> Task:
    return Task(id=str(uuid4()), description=description, completed=False)

def add_task(tasks: List[Task], task: Task) -> List[Task]:
    return tasks + [task]

def remove_task(tasks: List[Task], task_id: str) -> List[Task]:
    return [task for task in tasks if task.id != task_id]

def mark_completed(tasks: List[Task], task_id: str) -> List[Task]:
    updated = []
    for task in tasks:
        if task.id == task_id:
            updated.append(Task(id=task.id, description=task.description, completed=True))
        else:
            updated.append(task)
    return updated

# ------------------------
# Imperative Shell
# ------------------------
class TaskManager:
    def __init__(self):
        self._tasks = []

    def add_task(self, description: str) -> None:
        """Add a new task with a unique ID."""
        new_task = create_task(description)
        self._tasks = add_task(self._tasks, new_task)

    def remove_task(self, task_id: str) -> None:
        """Remove task by ID."""
        self._tasks = remove_task(self._tasks, task_id)

    def mark_complete(self, task_id: str) -> None:
        """Mark task as completed by ID."""
        self._tasks = mark_completed(self._tasks, task_id)

    def list_tasks(self) -> List[Task]:
        """Retrieve all tasks."""
        return self._tasks.copy()  # Return a copy to avoid external modification

    def list_tasks_summary(self) -> str:
        """Human-readable summary of all tasks."""
        if not self._tasks:
            return "No tasks found."
        return "\n".join(
            f"[{'X' if t.completed else ' '}] {t.id[:8]}: {t.description}"
            for t in self._tasks
        )
```

---

### 📦 Usage Example

```python
# Import module
import task_manager

# Create task manager instance
tm = task_manager.TaskManager()

# Add tasks
tm.add_task("Write documentation")
tm.add_task("Refactor code")
tm.add_task("Write tests")

# Display all tasks
print("Initial Tasks:")
print(tm.list_tasks_summary())

# Mark one as complete
tm.mark_complete(tm._tasks[0].id)

# Remove one
tm.remove_task(tm._tasks[-1].id)

# Final state
print("\nUpdated Tasks:")
print(tm.list_tasks_summary())
```

---

### 🧪 Testable and Maintainable
- Pure functions can be directly unit tested.
- The `TaskManager` encapsulates mutability, isolating the side effect of managing a stateful list.
- All functions follow the **Single Responsibility Principle**, making them easy to read and extend.

---

### 🚀 Next Steps (Optional)
If needed, the module could be extended with:
- Persistence (e.g., JSON serialization).
- CLI or API integration for an external interface.
- Support for task priority or deadlines.

Let me know if you'd like help adding these features!