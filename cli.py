from models.users import add_user, clear_all_users, create_users_table
from models.tasks import create_tasks_table, add_task, view_all_tasks, mark_task_complete, delete_task, show_completed_tasks, show_pending_tasks, clear_all_tasks

def show_main_menu():
    print("\nWelcome to the Todo App!")
    print("===========================")
    print("Please choose an option:")
    print("1. Add User")
    print("2. View all tasks")
    print("3. Add a task")
    print("5. Mark Task as Complete")
    print("6. Delete a Task")
    print("7. Show Completed Tasks")
    print("8. Show Pending Tasks")
    print("9. Clear All Tasks")
    print("10. Clear All Users")
    print("0. Exit")

def run_cli():
    """Run the command-line interface."""
    # Ensure the tables are created
    create_users_table()
    create_tasks_table()

    while True:
        show_main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            fullname = input("Enter user's full name: ")
            add_user(fullname)
        elif choice == "2":
            view_all_tasks()
        elif choice == "3":
            title = input("Enter task description: ")
            username = input("Enter the username: ")
            add_task(title, username)
        elif choice == "5":
            task_id = int(input("Enter the Task ID to mark as complete: "))
            mark_task_complete(task_id)
        elif choice == "6":
            task_id = int(input("Enter the Task ID to delete: "))
            delete_task(task_id)
        elif choice == "7":
            show_completed_tasks()
        elif choice == "8":
            show_pending_tasks()
        elif choice == "9":
            clear_all_tasks()
        elif choice == "10":
            clear_all_users()
        elif choice == "0":
            print("Exiting Todo App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
