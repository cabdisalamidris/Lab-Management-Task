from datetime import datetime

def validate_task_title(title):
    if not isinstance(title, str):
        raise ValueError("Title must be a string.")
    if len(title.strip()) == 0:
        raise ValueError("Title cannot be empty.")
    return True
    
def validate_task_description(description):
    if not isinstance(description, str):
        raise ValueError("Description must be a string.")
    if len(description.strip()) < 5:
        raise ValueError("Description must be at least 5 characters long.")
    if len(description) > 500:
        raise ValueError("Description must not exceed 500 characters.")
    return True
    
def validate_due_date(due_date):
    if not isinstance(due_date, str):
        raise ValueError("Due date must be a string.")

    due_date = due_date.strip()
    try:
        parsed_date = datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format.")

    return True
