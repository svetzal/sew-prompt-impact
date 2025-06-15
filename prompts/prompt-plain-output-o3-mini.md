Below is an example Python module (for example, save it as task_manager.py) that defines a Task and TaskManager class. You can import this module into other programs or run it directly to test its functionality.

--------------------------------------------------
#!/usr/bin/env python3
"""
task_manager.py

A Python module for managing a list of tasks.
Each task has an id, a description, and a completed status.

Usage as a module:
  from task_manager import TaskManager
  tm = TaskManager()
  tm.add_task("Buy groceries")
  tm.list_tasks()
  
Usage as a script:
  python task_manager.py
"""

class Task:
    def __init__(self, task_id, description):
        self.id = task_id
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __repr__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.id}: {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add_task(self, description):
        """Adds a new task with the given description. Returns the Task object."""
        task = Task(self.next_id, description)
        self.tasks[self.next_id] = task
        self.next_id += 1
        print(f"Added task: {task}")
        return task

    def remove_task(self, task_id):
        """Removes the task with the given id."""
        if task_id in self.tasks:
            removed_task = self.tasks.pop(task_id)
            print(f"Removed task: {removed_task}")
        else:
            print(f"No task with id {task_id} found.")

    def mark_task_complete(self, task_id):
        """Marks the task with the given id as complete."""
        if task_id in self.tasks:
            self.tasks[task_id].mark_complete()
            print(f"Task {task_id} marked as complete.")
        else:
            print(f"No task with id {task_id} found.")

    def list_tasks(self, show_all=True):
        """
        Lists tasks.
        If show_all is True, lists all tasks.
        Otherwise, lists only incomplete tasks.
        """
        if not self.tasks:
            print("No tasks yet!")
            return

        for task in self.tasks.values():
            if show_all or not task.completed:
                print(task)

    def clear_completed(self):
        """Removes all tasks that are marked as completed."""
        completed_ids = [task_id for task_id, task in self.tasks.items() if task.completed]
        for task_id in completed_ids:
            self.remove_task(task_id)

# If run as a script, demonstrate basic usage.
if __name__ == '__main__':
    tm = TaskManager()

    print("=== Adding Tasks ===")
    tm.add_task("Buy groceries")
    tm.add_task("Write email to manager")
    tm.add_task("Read Python documentation")

    print("\n=== Listing All Tasks ===")
    tm.list_tasks()

    print("\n=== Marking Task 2 as Complete ===")
    tm.mark_task_complete(2)

    print("\n=== Listing Incomplete Tasks ===")
    tm.list_tasks(show_all=False)

    print("\n=== Removing Task 1 ===")
    tm.remove_task(1)

    print("\n=== Listing All Tasks ===")
    tm.list_tasks()
    
    print("\n=== Clearing Completed Tasks ===")
    tm.clear_completed()
    
    print("\n=== Final Task List ===")
    tm.list_tasks()
--------------------------------------------------

This module provides basic functionality:
• Adding new tasks
• Removing tasks by their ID
• Marking tasks as complete
• Listing tasks (all or only incomplete ones)
• Clearing all completed tasks

You can extend this module as needed—for example by adding persistence (saving to and reading from files) or more advanced task management features.