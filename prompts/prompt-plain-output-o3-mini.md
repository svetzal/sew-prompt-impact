Below is an example Python module named task_manager.py that implements a simple task management system. This module defines a Task class to represent individual tasks and a TaskManager class to add, remove, list, and mark tasks as completed.

────────────────────────────
# Begin task_manager.py

class Task:
    def __init__(self, task_id, description, completed=False):
        """
        Initialize a new task.

        Args:
            task_id (int): A unique identifier for the task.
            description (str): A text description of the task.
            completed (bool): Task completion status. Defaults to False.
        """
        self.task_id = task_id
        self.description = description
        self.completed = completed

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True

    def __str__(self):
        status = 'Done' if self.completed else 'Pending'
        return f"[{self.task_id}] {self.description} - {status}"


class TaskManager:
    def __init__(self):
        """Initialize the Task Manager with an empty list of tasks."""
        self.tasks = []
        self.next_id = 1

    def add_task(self, description):
        """
        Add a new task.

        Args:
            description (str): Task description.

        Returns:
            Task: The newly created task.
        """
        task = Task(self.next_id, description)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_task(self, task_id):
        """
        Retrieve a task by its ID.

        Args:
            task_id (int): The ID of the task to retrieve.

        Returns:
            Task or None: The task with the specified id, or None if not found.
        """
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def remove_task(self, task_id):
        """
        Remove a task by its ID.

        Args:
            task_id (int): The ID of the task to remove.

        Returns:
            bool: True if a task was removed, False if not found.
        """
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def mark_task_completed(self, task_id):
        """
        Mark a specific task as completed.

        Args:
            task_id (int): The ID of the task to mark completed.

        Returns:
            bool: True if the task was found and marked, False otherwise.
        """
        task = self.get_task(task_id)
        if task:
            task.mark_completed()
            return True
        return False

    def list_tasks(self, completed=None):
        """
        List tasks with an optional filter on completion status.

        Args:
            completed (bool, optional): If provided, filter tasks by completed status.

        Returns:
            list: A list of tasks that match the criteria.
        """
        if completed is None:
            return self.tasks
        else:
            return [task for task in self.tasks if task.completed == completed]

    def __str__(self):
        if not self.tasks:
            return "No tasks available."
        result = "\n".join(str(task) for task in self.tasks)
        return result


# If this module is run as the main program, demonstrate its functionality.
if __name__ == "__main__":
    tm = TaskManager()

    # Adding tasks
    tm.add_task("Buy groceries")
    tm.add_task("Call Alice")
    tm.add_task("Prepare presentation")

    print("All Tasks:")
    print(tm)
    print()

    # Mark the second task as completed
    tm.mark_task_completed(2)

    print("Tasks after marking task 2 as completed:")
    print(tm)
    print()

    # List only pending tasks
    pending_tasks = tm.list_tasks(completed=False)
    print("Pending Tasks:")
    for task in pending_tasks:
        print(task)

    # Remove a task
    tm.remove_task(1)
    print("\nTasks after removing task 1:")
    print(tm)

# End task_manager.py
────────────────────────────

Explanation:

1. The Task class represents a single task with an ID, a description, and a flag indicating whether it’s completed.
2. The TaskManager class maintains a list of Task objects. It includes methods to add a new task (automatically assigning an incrementing ID), get a task, remove a task, mark a task as completed, and list tasks (with an optional filter based on completion status).
3. At the bottom of the module, a basic demonstration is provided which runs if the module is executed as the main program.
4. You can import this module into other Python scripts to manage tasks programmatically.

This module can be extended further based on your needs, such as saving tasks to a file or integrating with a GUI.