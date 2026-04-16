from datetime import datetime

# Import validation functions
from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    try:
        # Validate inputs
        validate_task_title(title)
        validate_task_description(description)
        validate_due_date(due_date)

        task = {
            "title": title,
            "description": description,
            "due_date": due_date,
            "completed": False
        }

        tasks.append(task)
        print("Task added successfully!")

    except ValueError as e:
        print(f"Error: {e}")


# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    # Check if index is valid
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task index.")


# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    found = False

    for i, task in enumerate(tasks):
        if not task["completed"]:
            print(f"{i}. {task['title']} (Due: {task['due_date']})")
            found = True

    if not found:
        print("No pending tasks.")


# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        return 0

    completed = sum(1 for task in tasks if task["completed"])
    progress = (completed / len(tasks)) * 100

    return progress