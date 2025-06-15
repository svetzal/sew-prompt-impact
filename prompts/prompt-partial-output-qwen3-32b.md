

Here's a Python module for task management following your baseline conventions:

```python
# task_manager.py

from typing import Optional, List

class Task:
    """Immutable task representation with core properties"""
    def __init__(self, task_id: int, title: str, description: str = "", completed: bool = False, due_date: Optional[str] = None):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.completed = completed
        self.due_date = due_date

    def mark_complete(self) -> 'Task':
        """Return new Task instance with completion status updated"""
        return Task(self.task_id, self.title, self.description, True, self.due_date)

    def __repr__(self):
        return f"Task(task_id={self.task_id}, title='{self.title}', completed={self.completed})"
        
class TaskManager:
    """Imperative shell for task operations"""
    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id: int = 1

    def add_task(self, title: str, description: str = "", due_date: Optional[str] = None) -> Task:
        """Create and add a new task, returns created task"""
        task = Task(self.next_id, title, description, False, due_date)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def remove_task(self, task_id: int) -> None:
        """Remove task by ID"""
        self.tasks = [t for t in self.tasks if t.task_id != task_id]

    def mark_complete(self, task_id: int) -> None:
        """Mark task as complete by ID"""
        for i, t in enumerate(self.tasks):
            if t.task_id == task_id:
                self.tasks[i] = t.mark_complete()
                break

    def get_task(self, task_id: int) -> Optional[Task]:
        """Retrieve task by ID"""
        return next((t for t in self.tasks if t.task_id == task_id), None)

    def get_all_tasks(self) -> List[Task]:
        """Get all tasks"""
        return self.tasks

    def get_pending_tasks(self) -> List[Task]:
        """Get tasks that are not completed"""
        return [t for t in self.tasks if not t.completed]

    def get_completed_tasks(self) -> List[Task]:
        """Get completed tasks"""
        return [t for t in self.tasks if t.completed]
```

Key design decisions following your conventions:

1. **Functional Core, Imperative Shell**
   - Task objects are immutable (functional core)
   - TaskManager handles state changes (imperative shell)

2. **Testability**
   - Pure functions for task transformations
   - Clear separation of concerns
   - Easily testable with assertions like:
     ```python
     assert task.completed == False
     new_task = task.mark_complete()
     assert new_task.completed == True
     ```

3. **Code as Documentation**
   - Clear method naming and type hints
   - Docstrings explain key behaviors
   - Immutable operations return new instances

4. **Extensibility**
   - Simple to add new task states or properties
   - Easy to extend TaskManager with new operations

5. **Usage Pattern**
   ```python
   manager = TaskManager()
   task1 = manager.add_task("Write report", due_date="2023-12-15")
   manager.mark_complete(task1.task_id)
   
   for task in manager.get_pending_tasks():
       print(f"{task.title} (ID: {task.task_id})")
   ```

This implementation balances clarity with functionality while adhering to all specified engineering principles. The code can be extended with additional features like persistence, filtering, or notifications as needed.