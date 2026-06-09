from datetime import datetime

def validate_task_title(title):
    if not isinstance(title, str):
        return False
    return len(title.strip()) > 0
    
def validate_task_description(description):
    if not isinstance(description, str):
        return False
    return len(description.strip()) >= 5
    
def validate_due_date(due_date):
    if not isinstance(due_date, str):
        return False

    due_date = due_date.strip()
    try:
        parsed_date = datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        return False

    today = datetime.now().date()
    return parsed_date >= today
