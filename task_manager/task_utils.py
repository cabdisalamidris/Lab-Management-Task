from datetime import datetime
from .validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)

    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False,
    }
    tasks.append(task)
    print("Task added successfully!")
    return task
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if not isinstance(index, int):
        raise ValueError("Task number must be an integer.")

    if index < 1 or index > len(tasks):
        raise IndexError("Task number is out of range.")

    task = tasks[index - 1]
    task["completed"] = True
    print("Task marked as complete!")
    return task
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending_tasks = [task for task in tasks if not task["completed"]]

    if not pending_tasks:
        print("No pending tasks found.")
        return pending_tasks

    print("\nPending Tasks:")
    for index, task in enumerate(tasks, start=1):
        if not task["completed"]:
            print(f"{index}. {task['title']} (Due: {task['due_date']})")
            print(f"   Description: {task['description']}")
    return pending_tasks

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    total_tasks = len(tasks)
    if total_tasks == 0:
        return 0

    completed_tasks = sum(1 for task in tasks if task["completed"])
    progress = round((completed_tasks / total_tasks) * 100, 2)
    return progress