**Task Manager Module**
========================

Below is an example implementation of a Python module to manage a list of tasks.

```python
# task_manager.py

class Task:
    """Represents a single task with a title and description."""
    
    def __init__(self, title: str, description: str):
        """
        Initializes a new task.
        
        Args:
        - title (str): The title of the task.
        - description (str): A brief description of the task.
        """
        self.title = title
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        """Marks the task as completed."""
        self.completed = True

    def mark_as_incomplete(self):
        """Marks the task as incomplete."""
        self.completed = False


class TaskManager:
    """Manages a list of tasks."""
    
    def __init__(self):
        """
        Initializes an empty task manager.
        """
        self.tasks = []

    def add_task(self, title: str, description: str):
        """
        Adds a new task to the task manager.
        
        Args:
        - title (str): The title of the task.
        - description (str): A brief description of the task.
        """
        task = Task(title, description)
        self.tasks.append(task)

    def view_tasks(self):
        """
        Prints out all tasks in the task manager.
        """
        for i, task in enumerate(self.tasks):
            status = "Completed" if task.completed else "Not Completed"
            print(f"{i+1}. {task.title} - {status}")
            print(f"Description: {task.description}")
            print()

    def delete_task(self, index: int):
        """
        Deletes a task at the specified index.
        
        Args:
        - index (int): The zero-based index of the task to delete.
        """
        try:
            del self.tasks[index]
        except IndexError:
            print("Invalid task index.")

    def update_task_status(self, index: int, status: str):
        """
        Updates the completion status of a task at the specified index.
        
        Args:
        - index (int): The zero-based index of the task to update.
        - status (str): The new status ("Completed" or "Not Completed").
        """
        try:
            if status.lower() == "completed":
                self.tasks[index].mark_as_completed()
            elif status.lower() == "not completed":
                self.tasks[index].mark_as_incomplete()
            else:
                print("Invalid task status.")
        except IndexError:
            print("Invalid task index.")


def main():
    # Example usage
    task_manager = TaskManager()

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Update Task Status")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_manager.add_task(title, description)
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            index = int(input("Enter the task index to delete: ")) - 1
            task_manager.delete_task(index)
        elif choice == "4":
            index = int(input("Enter the task index to update: ")) - 1
            status = input("Enter the new status (Completed/Not Completed): ")
            task_manager.update_task_status(index, status)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

### Features

*   **Task Class**: Represents a single task with a title and description.
*   **Task Manager Class**: Manages a list of tasks, allowing you to add, view, delete, and update tasks.
*   **Main Function**: Provides an example usage of the Task Manager class through a simple command-line interface.

### Example Usage

1.  Run the script using Python (e.g., `python task_manager.py`).
2.  Follow the on-screen instructions to interact with the task manager:
    *   Add tasks by entering their title and description.
    *   View all tasks, including their completion status.
    *   Delete tasks by specifying their index.
    *   Update the completion status of tasks by specifying their index and new status.
3.  Exit the program when finished.

Note that this implementation provides a basic task management system. You can extend it to include additional features such as due dates, priorities, or tags as needed.