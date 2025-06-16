Below is an example Python module named task_manager.py that implements a simple task management system. Each task is stored as a dictionary with an ID, description, and a status (pending or completed). You can add, remove, update, and list tasks using the TaskManager class.

---------------
# task_manager.py

import itertools

class TaskManager:
    def __init__(self):
        """
        Initializes a new TaskManager with an empty task list and an ID counter.
        """
        self._tasks = {}
        self._id_counter = itertools.count(1)
    
    def add_task(self, description):
        """
        Adds a new task with the given description.
        
        Parameters:
            description (str): A description of the task.
            
        Returns:
            int: The id of the newly added task.
        """
        task_id = next(self._id_counter)
        self._tasks[task_id] = {
            'id': task_id,
            'description': description,
            'completed': False
        }
        return task_id

    def remove_task(self, task_id):
        """
        Removes the task with the specified id.
        
        Parameters:
            task_id (int): The id of the task to remove.
            
        Raises:
            KeyError: If the task id does not exist.
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
        else:
            raise KeyError(f"Task with id {task_id} not found.")
    
    def mark_completed(self, task_id):
        """
        Marks the task with the specified id as completed.
        
        Parameters:
            task_id (int): The id of the task to mark as completed.
        
        Raises:
            KeyError: If the task id does not exist.
        """
        if task_id in self._tasks:
            self._tasks[task_id]['completed'] = True
        else:
            raise KeyError(f"Task with id {task_id} not found.")
    
    def list_tasks(self, show_all=True):
        """
        Lists tasks.
        
        Parameters:
            show_all (bool): If True, all tasks are returned. If False, only pending tasks are returned.
        
        Returns:
            list: A list of tasks (each task is a dictionary).
        """
        if show_all:
            return list(self._tasks.values())
        else:
            return [task for task in self._tasks.values() if not task['completed']]
    
    def get_task(self, task_id):
        """
        Gets the task with the specified id.
        
        Parameters:
            task_id (int): The id of the task to retrieve.
        
        Returns:
            dict: The task dictionary.
        
        Raises:
            KeyError: If the task id does not exist.
        """
        if task_id in self._tasks:
            return self._tasks[task_id]
        else:
            raise KeyError(f"Task with id {task_id} not found.")

# Example usage (for testing the module functionality)
if __name__ == '__main__':
    manager = TaskManager()

    # Adding tasks
    task1_id = manager.add_task("Buy groceries")
    task2_id = manager.add_task("Read a book")
    
    print("All Tasks:")
    for task in manager.list_tasks():
        print(task)
    
    # Mark task1 as completed
    manager.mark_completed(task1_id)
    
    print("\nPending Tasks:")
    for task in manager.list_tasks(show_all=False):
        print(task)
    
    # Remove task2 and show remaining tasks
    manager.remove_task(task2_id)
    
    print("\nAll Tasks after removal:")
    for task in manager.list_tasks():
        print(task)
    
    # Retrieve individual task
    try:
        task = manager.get_task(task1_id)
        print("\nRetrieved Task:", task)
    except KeyError as e:
        print(e)

---------------

Explanation:

• The TaskManager class initializes with an empty dictionary to store tasks and an ID generator using itertools.count.
• The add_task method creates a new task with a unique id and marks it initially as not completed.
• The remove_task, mark_completed, and get_task methods provide ways to modify and access the tasks.
• The list_tasks method returns either all tasks or only the pending ones, based on the show_all parameter.
• The bottom section under if __name__ == '__main__' demonstrates basic usage and testing of the module functionality.

You can now import task_manager.py into your projects and use the TaskManager class to manage a list of tasks.