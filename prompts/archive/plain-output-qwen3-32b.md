

Here's a Python module for task management that supports common operations like creating, updating, removing, and listing tasks, along with error handling and user-friendly behavior:

```python
class Task:
    """Represents a single task item"""
    def __init__(self, description: str, task_id: int, priority: int = 1, status: str = 'pending'):
        self.description = description.strip()
        self.task_id = task_id
        self.priority = priority
        self.status = status

    def mark_complete(self) -> None:
        """Marks the task as completed"""
        self.status = 'completed'

    def __str__(self):
        return f"[Task ID: {self.task_id}] {self.description} " \
               f"(Priority: {self.priority}, Status: {self.status})"
    
    def __repr__(self):
        return self.__str__()


class TaskManager:
    """Manages a collection of tasks with ID-based operations"""
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add_task(self, description: str, priority: int = 1) -> int:
        """
        Creates a new task and returns its ID
        Raises ValueError for invalid input
        """
        if not description or not description.strip():
            raise ValueError("Task description cannot be empty or whitespace")
        
        task = Task(description, self.next_id, priority)
        self.tasks[self.next_id] = task
        task_id = self.next_id
        self.next_id += 1
        return task_id

    def remove_task(self, task_id: int) -> bool:
        """Removes a task by ID and returns success status"""
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def update_description(self, task_id: int, new_description: str) -> bool:
        """
        Updates task description and returns success status
        Raises ValueError for invalid input
        """
        if not new_description.strip():
            raise ValueError("Description cannot be empty or whitespace")
            
        task = self.tasks.get(task_id)
        if task:
            task.description = new_description.strip()
            return True
        return False

    def update_priority(self, task_id: int, new_priority: int) -> bool:
        """Updates task priority and returns success status"""
        task = self.tasks.get(task_id)
        if task:
            task.priority = new_priority
            return True
        return False

    def mark_complete(self, task_id: int) -> bool:
        """Marks a task as completed and returns success status"""
        task = self.tasks.get(task_id)
        if task:
            task.mark_complete()
            return True
        return False

    def list_tasks(self, status: str = None) -> list:
        """
        Returns all tasks (filtered by status if provided)
        Valid status values: 'pending', 'completed'
        """
        if status:
            return [task for task in self.tasks.values() 
                   if task.status.lower() == status.lower()]
        return list(self.tasks.values())

    def get_task(self, task_id: int):
        """Returns a specific task by ID or None if not found"""
        return self.tasks.get(task_id)
```

### Example Usage:

```python
# Create task manager
tm = TaskManager()

# Add tasks and get their IDs
task1_id = tm.add_task("Buy groceries", priority=2)
task2_id = tm.add_task("Finish report", priority=1)

# List all pending tasks
print("Pending Tasks:")
for task in tm.list_tasks("pending"):
    print(task)

# Update a task
tm.update_description(task2_id, "Urgent report completion")
tm.mark_complete(task2_id)

# Remove a task
tm.remove_task(task1_id)

# Final task list
print("\nAll Tasks:")
for task in tm.list_tasks():
    print(task)
```

### Key Features:
- Unique ID generation for tasks
- Task status tracking (pending/completed)
- Priority levels for task sorting
- Robust error handling for invalid inputs
- Clean and modular class design
- Supports filtering by task status

### Usage Notes:
1. Task IDs are sequential and automatically generated
2. Task descriptions must be non-empty and trimmed of whitespace
3. All operations return boolean status for success tracking
4. Tasks are stored in memory (for persistent storage you'd need to add file/db saving)

This module provides a solid foundation for a task management system and can be extended with additional features like sorting by priority or implementing persistence.