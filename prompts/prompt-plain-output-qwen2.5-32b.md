Certainly! Below is an example of how you might create a simple Python module to manage a list of tasks. This module will allow adding, removing, and listing tasks.

### File: `task_manager.py`

```python
class TaskManager:
    def __init__(self):
        # Initialize the task list
        self.tasks = []

    def add_task(self, task_description):
        """
        Add a new task to the list.
        
        :param task_description: Description of the task.
        """
        if not isinstance(task_description, str) or len(task_description.strip()) == 0:
            raise ValueError("Task description must be a non-empty string.")
        self.tasks.append({"description": task_description, "completed": False})

    def list_tasks(self):
        """
        List all tasks with their status.
        
        :return: A formatted string containing the details of each task and its completion status.
        """
        if not self.tasks:
            return "No tasks in the list."
        output = ["Task List:"]
        for index, task in enumerate(self.tasks, start=1):
            status = 'Completed' if task['completed'] else 'Pending'
            output.append(f"{index}. [{status}] {task['description']}")
        return "\n".join(output)

    def mark_task_completed(self, task_index):
        """
        Mark a specific task as completed.
        
        :param task_index: Index of the task (1-based index).
        :return: True if task was found and marked as completed, False otherwise.
        """
        try:
            self.tasks[task_index - 1]['completed'] = True
            return True
        except IndexError:
            return False

    def remove_task(self, task_index):
        """
        Remove a specific task from the list by its index.
        
        :param task_index: Index of the task (1-based index).
        :return: True if task was found and removed, False otherwise.
        """
        try:
            del self.tasks[task_index - 1]
            return True
        except IndexError:
            return False


def main():
    manager = TaskManager()
    
    # Example usage of the TaskManager class
    print("Adding Tasks...")
    manager.add_task("Buy groceries")
    manager.add_task("Do laundry")
    manager.add_task("Go to gym")

    print("\nCurrent tasks:")
    print(manager.list_tasks())

    print("\nMarking first task as completed...")
    manager.mark_task_completed(1)

    print("\nUpdated task list:")
    print(manager.list_tasks())

    print("\nRemoving second task...")
    if manager.remove_task(2):
        print("Task removed successfully.")
    else:
        print("Failed to remove task.")

    print("\nFinal task list:")
    print(manager.list_tasks())


if __name__ == '__main__':
    main()
```

### Explanation:

- **`add_task()`**: Adds a new task to the list with its description and sets its completion status as `False`.
- **`list_tasks()`**: Returns a formatted string listing all tasks along with their status (whether they are completed or not).
- **`mark_task_completed()`**: Takes an index of a task and marks it as completed.
- **`remove_task()`**: Takes the index of a task to remove from the list.

### Usage:

You can use this module in another Python script by importing `TaskManager` class. For example, you can create an instance of `TaskManager`, add tasks, mark them as completed or remove them as per your requirements.

```python
from task_manager import TaskManager

# Initialize a TaskManager object
manager = TaskManager()

# Add some tasks
manager.add_task("Clean the kitchen")
manager.add_task("Pay bills")

# List current tasks
print(manager.list_tasks())

# Mark first task as completed
manager.mark_task_completed(1)

# List updated tasks
print(manager.list_tasks())
```

This is a very basic implementation and can be expanded with features such as due dates, priorities, or saving/loading from files.