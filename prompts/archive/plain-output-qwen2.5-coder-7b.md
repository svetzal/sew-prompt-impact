Sure! Below is an example of a Python module to manage a list of tasks. This module includes functionalities like adding a task, removing a task, updating a task, listing all tasks, and marking a task as completed.

```python
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, due_date=None, description=None):
        """
        Adds a new task to the list.

        :param task_name: Name of the task (str)
        :param due_date: Due date for the task (str), optional
        :param description: Description of the task (str), optional
        """
        task = {
            'task_name': task_name,
            'due_date': due_date,
            'description': description,
            'completed': False
        }
        self.tasks.append(task)

    def remove_task(self, task_name):
        """
        Removes a task from the list.

        :param task_name: Name of the task (str)
        """
        for i, task in enumerate(self.tasks):
            if task['task_name'] == task_name:
                del self.tasks[i]
                break
        else:
            print(f"Task '{task_name}' not found.")

    def update_task(self, task_name, new_due_date=None, new_description=None):
        """
        Updates a task's details.

        :param task_name: Name of the task (str)
        :param new_due_date: New due date for the task (str), optional
        :param new_description: New description of the task (str), optional
        """
        for task in self.tasks:
            if task['task_name'] == task_name:
                if new_due_date is not None:
                    task['due_date'] = new_due_date
                if new_description is not None:
                    task['description'] = new_description
                break
        else:
            print(f"Task '{task_name}' not found.")

    def mark_task_as_completed(self, task_name):
        """
        Marks a task as completed.

        :param task_name: Name of the task (str)
        """
        for task in self.tasks:
            if task['task_name'] == task_name:
                task['completed'] = True
                break
        else:
            print(f"Task '{task_name}' not found.")

    def list_tasks(self):
        """
        Lists all tasks.
        """
        if not self.tasks:
            print("No tasks available.")
            return

        for task in self.tasks:
            status = "Completed" if task['completed'] else "Pending"
            print(f"Task: {task['task_name']}, Due Date: {task['due_date']}, Description: {task['description']}, Status: {status}")

# Example usage
if __name__ == "__main__":
    task_manager = TaskManager()

    # Add tasks
    task_manager.add_task("Complete assignment", "2023-10-01", "Math homework")
    task_manager.add_task("Read a book", "2023-10-05")

    # List tasks
    print("\nCurrent Tasks:")
    task_manager.list_tasks()

    # Update a task
    task_manager.update_task("Complete assignment", new_due_date="2023-10-02")
    print("\nUpdated Tasks:")
    task_manager.list_tasks()

    # Mark a task as completed
    task_manager.mark_task_as_completed("Read a book")
    print("\nTasks after marking one as completed:")
    task_manager.list_tasks()

    # Remove a task
    task_manager.remove_task("Complete assignment")
    print("\nTasks after removal:")
    task_manager.list_tasks()
```

You can save this code in a file named `task_manager.py` and use it in your Python scripts. The example usage at the bottom demonstrates how to use the `TaskManager` class to manage tasks.

To run the example, simply execute the script:

```sh
python task_manager.py
```

This will create a new `TaskManager` instance, add tasks, update them, mark one as completed, remove a task, and list all tasks.