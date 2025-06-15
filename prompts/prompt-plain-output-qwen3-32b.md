

Here's a simple Python module to manage a list of tasks:

```python
"""
task_manager.py
A module to manage a list of tasks
"""

class TaskManager:
    """
    A class to manage a collection of tasks with features to add, remove,
    list, and mark tasks as done.
    """

    def __init__(self):
        """Initialize an empty list of tasks."""
        self.tasks = []

    def add_task(self, description, priority='medium', due_date=None):
        """
        Add a new task to the list.

        Parameters:
        - description (str): The task description
        - priority (str): Task priority (default: 'medium')
        - due_date (str, optional): Task due date in string format
        """
        task = {
            'description': description,
            'status': 'pending',
            'priority': priority,
            'due_date': due_date
        }
        self.tasks.append(task)

    def remove_task(self, index):
        """
        Remove a task by its index.

        Parameters:
        - index (int): The index of the task to remove
        """
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            raise ValueError("Invalid task index")

    def list_tasks(self, status=None):
        """
        List all tasks or filter by status.

        Parameters:
        - status (str, optional): Filter tasks by status ('pending' or 'completed')
        """
        filtered_tasks = [
            task for task in self.tasks 
            if status is None or task['status'] == status
        ]
        
        if not filtered_tasks:
            print(f"No {status if status else 'tasks'} found.")
            return

        for i, task in enumerate(filtered_tasks):
            due = task['due_date'] if task['due_date'] else 'No due date'
            print(
                f"{i}: {task['description']} "
                f"(Status: {task['status']}, "
                f"Priority: {task['priority']}, "
                f"Due: {due})"
            )

    def mark_done(self, index):
        """
        Mark a task as completed by its index.

        Parameters:
        - index (int): The index of the task to mark
        """
        if 0 <= index < len(self.tasks):
            self.tasks[index]['status'] = 'completed'
        else:
            raise ValueError("Invalid task index")
```

### Example Usage

```python
if __name__ == "__main__":
    tm = TaskManager()
    
    # Add tasks
    tm.add_task("Write document", priority="high", due_date="2023-10-15")
    tm.add_task("Review code")
    tm.add_task("Prepare meeting", priority="medium")
    
    # List all tasks
    print("All Tasks:")
    tm.list_tasks()
    
    # Mark a task as done
    tm.mark_done(1)
    
    # List pending tasks
    print("\nPending Tasks:")
    tm.list_tasks(status='pending')
    
    # List completed tasks
    print("\nCompleted Tasks:")
    tm.list_tasks(status='completed')
```

### Key Features

1. **Task Structure**:
   - Each task stores: `description`, `status`, `priority`, and `due_date`
   - Default status is always `pending` when created
   - Priority can be customized (default: `medium`)
   - Due date is optional

2. **Core Methods**:
   - `add_task()`: Create a new task with description and optional parameters
   - `remove_task()`: Remove tasks by index
   - `list_tasks()`: View all tasks or filter by status (`pending` or `completed`)
   - `mark_done()`: Mark a task as completed by index

3. **Error Handling**:
   - Invalid task indices raise `ValueError`
   - Clean output for empty task lists (especially after filtering)

### Notes

- No persistence across sessions - tasks are stored in memory
- The due date format is string-based for simplicity
- Tasks are ordered chronologically as they're added
- Can easily be extended with additional features like priority sorting, date validation, or file-based storage