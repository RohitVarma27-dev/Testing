"""Tiny in-memory to-do list for practice."""


class TodoList:
    """Manage a list of tasks."""

    def __init__(self):
        self.tasks = []

    def add(self, task):
        """Add a task."""
        self.tasks.append({"task": task, "done": False})

    def complete(self, index):
        """Mark task at index as done."""
        self.tasks[index]["done"] = True

    def show(self):
        """Print all tasks with status."""
        for i, item in enumerate(self.tasks):
            status = "x" if item["done"] else " "
            print(f"[{status}] {i}: {item['task']}")


if __name__ == "__main__":
    todo = TodoList()
    todo.add("Learn git add")
    todo.add("Learn git commit")
    todo.add("Learn git push")
    todo.complete(0)
    todo.show()
