Below is an example of a Python module (which you might save as task_manager.py) that defines two classes—Task and TaskManager—to help you add, list, remove, and mark tasks as complete.

------------------------------------------------------------
# File: task_manager.py

class Task:
    def __init__(self, title, description=""):
        """
        Initialize a new Task.
        
        Args:
            title (str): The title or name of the task.
            description (str): Optional description of the task.
        """
        self.title = title
        self.description = description
        self.done = False

    def mark_done(self):
        """Mark the task as completed."""
        self.done = True

    def __str__(self):
        """Return a string representation of the task info."""
        status = "Done" if self.done else "Pending"
        return f"Task: {self.title} | Status: {status} | Description: {self.description}"


class TaskManager:
    def __init__(self):
        """Initialize an empty list of tasks."""
        self.tasks = []

    def add_task(self, task):
        """
        Add a new task to the list.
        
        Args:
            task (Task): The task object to add.
        """
        if not isinstance(task, Task):
            raise TypeError("Only Task instances can be added.")
        self.tasks.append(task)

    def remove_task(self, title):
        """
        Remove a task based on its title.
        
        Args:
            title (str): The title of the task to remove.
        """
        for i, task in enumerate(self.tasks):
            if task.title == title:
                del self.tasks[i]
                print(f"Removed task: {title}")
                return
        print(f"Task '{title}' not found.")

    def mark_task_done(self, title):
        """
        Mark a task as done based on its title.
        
        Args:
            title (str): The title of the task to mark as complete.
        """
        for task in self.tasks:
            if task.title == title:
                task.mark_done()
                print(f"Marked task '{title}' as done.")
                return
        print(f"Task '{title}' not found.")

    def list_tasks(self):
        """List all tasks with their status."""
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            print(task)


# Optional: simple demonstration when running this module directly.
if __name__ == "__main__":
    tm = TaskManager()
    
    # Create some tasks
    t1 = Task("Buy groceries", "Milk, Eggs, Bread")
    t2 = Task("Call Alice", "Discuss the project details")
    t3 = Task("Read book", "Finish reading Chapter 5")
    
    # Add tasks to the manager
    tm.add_task(t1)
    tm.add_task(t2)
    tm.add_task(t3)
    
    # List tasks
    print("Current tasks:")
    tm.list_tasks()
    
    # Mark a task as done
    tm.mark_task_done("Buy groceries")
    
    # List tasks again to see the update
    print("\nUpdated tasks:")
    tm.list_tasks()
    
    # Remove a task
    tm.remove_task("Call Alice")
    
    # List tasks again to see the update
    print("\nTasks after removal:")
    tm.list_tasks()

------------------------------------------------------------

Usage:

• You can import this module into another Python script using:

    from task_manager import Task, TaskManager

• Then create a TaskManager instance, and manage your Task objects.

This module provides a simple example of task management but can be expanded further—such as by adding due dates, priorities, persistent storage (e.g., saving to a file), or a richer interface—depending on your requirements.