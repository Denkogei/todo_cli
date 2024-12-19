from models.users import add_user, clear_all_users, create_users_table, view_all_users, view_user_by_name
from models.tasks import create_tasks_table, add_task, view_all_tasks, view_task_by_id, mark_task_complete, delete_task, show_completed_tasks, show_pending_tasks, clear_all_tasks

def show_main_menu():
    print("\nWelcome to the Todo App!")
    print("===========================")
    print("Please choose an option:")
    print("1. Add User")
    print("2. View all tasks")
    print("3. Add a task")
    print("4. View all users")
    print("5. Search Task by ID")  
    print("6. Mark Task as Complete")
    print("7. Delete a Task")
    print("8. Show Completed Tasks")
    print("9. Show Pending Tasks")
    print("10. Clear All Tasks")
    print("11. Clear All Users")
    print("12. Search Specific User")  
    print("0. Exit")

def run_cli():
    """Run the command-line interface."""
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
        elif choice == "4":
            view_all_users()
        elif choice == "5": 
            task_id = int(input("Enter the Task ID to search: "))
            view_task_by_id(task_id)
        elif choice == "6":
            task_id = int(input("Enter the Task ID to mark as complete: "))
            mark_task_complete(task_id)
        elif choice == "7":
            task_id = int(input("Enter the Task ID to delete: "))
            delete_task(task_id)
        elif choice == "8":
            show_completed_tasks()
        elif choice == "9":
            show_pending_tasks()
        elif choice == "10":
            clear_all_tasks()
        elif choice == "11":
            clear_all_users()
        elif choice == "12": 
            username = input("Enter the user's full name to search: ")
            view_user_by_name(username)
        elif choice == "0":
            print("Exiting Todo App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
