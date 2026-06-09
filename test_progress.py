#!/usr/bin/env python3
from task_manager.task_utils import calculate_progress

tasks = [
    {"title": "Task 1", "description": "testing", "due_date": "2024-05-26", "completed": True},
    {"title": "Task 2", "description": "testing", "due_date": "2024-05-26", "completed": False}
]
result = calculate_progress(tasks)
print(result)
