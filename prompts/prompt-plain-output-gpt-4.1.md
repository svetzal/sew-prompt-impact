Certainly! Below is a simple Python module named `task_manager.py` that allows you to manage a list of tasks. Each task can have a description and a completion status.

**Features:**
- Add tasks
- List tasks
- Mark tasks as done
- Remove tasks

---

```python
# task_manager.py

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __repr__(self):
        status = "[✓]" if self.completed else "[ ]"
        return f"{status} {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))

    def list_tasks(self, show_all=True):
        if show_all:
            return list(enumerate(self.tasks, start=1))
        else:
            return [(i + 1, t) for i, t in enumerate(self.tasks) if not t.completed]

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            return True
        return False

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            return True
        return False
```

---

**Example Usage:**

```python
if __name__ == "__main__":
    tm = TaskManager()
    tm.add_task("Buy groceries")
    tm.add_task("Read a book")
    tm.add_task("Exercise")

    print("All tasks:")
    for i, task in tm.list_tasks():
        print(f"{i}. {task}")

    print("\nMarking task 2 as complete.\n")
    tm.complete_task(1)

    print("Incomplete tasks:")
    for i, task in tm.list_tasks(show_all=False):
        print(f"{i}. {task}")

    print("\nRemoving task 1.\n")
    tm.remove_task(0)

    print("All tasks:")
    for i, task in tm.list_tasks():
        print(f"{i}. {task}")
```

---

Let me know if you need enhancements, like file saving/loading, due dates, priorities, or a command-line interface!