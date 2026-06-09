try:
    from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress, tasks
except ImportError:
    from task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress, tasks

# Define the main function
def main():
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            title = input("Enter task title: ").strip()
            description = input("Enter task description: ").strip()
            due_date = input("Enter due date (YYYY-MM-DD): ").strip()
            try:
                add_task(title, description, due_date)
            except ValueError as error:
                print(f"Error: {error}")
        elif choice == "2":
            if not tasks:
                print("No tasks available to mark as complete.")
                continue
            view_pending_tasks(tasks)
            try:
                index = int(input("Enter the task number to mark as complete: ").strip())
                mark_task_as_complete(index, tasks)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
            except IndexError:
                print("Task number out of range. Please try again.")
        elif choice == "3":
            view_pending_tasks(tasks)
        elif choice == "4":
            progress = calculate_progress(tasks)
            print(f"Progress: {progress}% completed")
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
