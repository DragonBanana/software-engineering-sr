import json
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date, priority):
        self.id = id(self)  # Unique identifier for each task
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False  # Default status

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        """Convert task to dictionary for saving to a file."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "priority": self.priority,
            "completed": self.completed,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a task instance from a dictionary."""
        task = cls(data["title"], data["description"], data["due_date"], data["priority"])
        task.id = data["id"]
        task.completed = data["completed"]
        return task


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date, priority):
        task = Task(title, description, due_date, priority)
        self.tasks.append(task)
        print(f"Task '{title}' added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            status = "Completed" if task.completed else "Pending"
            print(f"[{task.id}] {task.title} (Priority: {task.priority}) - {status}")
            print(f"    Due: {task.due_date}")
            print(f"    Description: {task.description}")

    def view_tasks_by_priority(self, priority):
        filtered_tasks = [task for task in self.tasks if task.priority == priority]
        if not filtered_tasks:
            print(f"No tasks with priority {priority}.")
            return
        for task in filtered_tasks:
            status = "Completed" if task.completed else "Pending"
            print(f"[{task.id}] {task.title} - {status}")

    def mark_task_complete(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_complete()
                print(f"Task '{task.title}' marked as completed.")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                print(f"Task '{task.title}' deleted.")
                return
        print("Task not found.")

    def save_tasks(self, filename):
        with open(filename, "w") as file:
            data = [task.to_dict() for task in self.tasks]
            json.dump(data, file)
        print("Tasks saved successfully.")

    def load_tasks(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(task_data) for task_data in data]
            print("Tasks loaded successfully.")
        except FileNotFoundError:
            print("No saved tasks found.")

# Example usage
if __name__ == "__main__":
    manager = TaskManager()

    # Load tasks from a file
    manager.load_tasks("tasks.json")

    # Add a task
    manager.add_task("Finish project", "Complete the software design project", "2024-12-10", "High")

    # View tasks
    manager.view_tasks()

    # Mark a task as complete
    task_id = manager.tasks[0].id  # Get ID of the first task
    manager.mark_task_complete(task_id)

    # View tasks by priority
    manager.view_tasks_by_priority("High")

    # Save tasks to a file
    manager.save_tasks("tasks.json")