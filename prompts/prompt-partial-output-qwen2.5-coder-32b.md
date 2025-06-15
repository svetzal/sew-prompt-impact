Certainly! Below is an example of a Python module that manages a list of tasks based on the principles you've outlined in your baseline conventions. This module will include classes and functions to handle task management, ensuring simplicity, readability, and minimal duplication.

```python
# task_manager.py

class Task:
    def __init__(self, title, description='', completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        return f"Task(title={self.title!r}, description={self.description!r}, completed={self.completed})"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=''):
        task = Task(title, description)
        self.tasks.append(task)

    def complete_task(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                task.mark_completed()
                break
        else:
            raise ValueError(f"Task '{task_title}' not found.")

    def list_tasks(self, completed=False):
        return [task for task in self.tasks if task.completed == completed]

    def __repr__(self):
        return f"TaskManager(tasks={self.tasks})"


def test_task_manager():
    # All tests pass
    manager = TaskManager()
    
    # Reveals intent
    manager.add_task("Write code", "Implement the core functionality")
    manager.add_task("Test code", "Ensure all functions work as expected")
    
    assert len(manager.list_tasks()) == 2
    assert len(manager.list_tasks(completed=True)) == 0
    
    manager.complete_task("Write code")
    assert len(manager.list_tasks(completed=False)) == 1
    assert len(manager.list_tasks(completed=True)) == 1


if __name__ == "__main__":
    test_task_manager()
```

### Explanation:

1. **Code is Communication**: The `Task` and `TaskManager` classes are clearly defined, with straightforward method names like `add_task`, `complete_task`, and `list_tasks`.

2. **Simple Design Heuristics**:
   - **All Tests Pass**: The `test_task_manager` function ensures all operations work as intended.
   - **Reveals Intent**: Method names and variable names are descriptive.
   - **No Knowledge Duplication**: There is no duplicate code within the methods.
   - **Minimal Entities**: No unnecessary classes or parameters.

3. **Small, Safe Increments**: Each method performs a single operation, making it easy to understand and test.

4. **Tests are the Executable Spec**: The `test_task_manager` function acts as an executable specification for the module's behavior.

5. **Compose Over Inherit**: No inheritance is used where composition suffices.

6. **Functional Core, Imperative Shell**: The `TaskManager` class handles all side effects (like modifying the task list), while each `Task` object is immutable in terms of its interface.

7. **Psychological Safety**: This code can be reviewed based on functionality and correctness without criticizing the author.

8. **Version-control etiquette**: Although not shown here, commit messages should be descriptive, branches should be created from `main`, and pull requests (PRs) should require a passing CI/CD pipeline.

This module follows the conventions you've laid out, making it easy to understand, maintain, and extend.