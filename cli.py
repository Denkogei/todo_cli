import sqlite3
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

    valid_choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "0"]

   
    def is_valid_task_id(task_id):
        """Validate that the task ID is a positive integer and exists in the task database."""
        return isinstance(task_id, int) and task_id > 0

    def is_valid_task_description(description):
        """Validate that the task description is a non-empty string and does not consist only of numbers."""
        return isinstance(description, str) and description.strip() and not description.isdigit()

    def is_valid_username(fullname):
        """Validate that the username (fullname) exists in the database and does not contain numbers."""
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE fullname = ?", (fullname,))
        user = cursor.fetchone() 
        conn.close() 
        return user is not None 

    def view_all_users():
        """Fetch and display all users from the database."""
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall() 
        conn.close()
        
        if users:
            print("\nUsers:")
            for user in users:
                print(f"- {user[1]}") 
        else:
            print("No users found.")

    while True:
        show_main_menu()
        choice = input("Enter your choice: ").strip()

       
        if choice not in valid_choices:
            print("Invalid choice. Please try again.")
            continue

        if choice == "1":
            fullname = input("Enter user's full name: ").strip()
            if is_valid_username(fullname):
                print("User already exists.")
            else:
                add_user(fullname)  
                print(f"User {fullname} added successfully.")
        
        elif choice == "2":
            view_all_tasks() 

        elif choice == "3":
            title = input("Enter task description: ").strip()
            if is_valid_task_description(title): 
                username = input("Enter the username: ").strip()
                if is_valid_username(username):  
                    add_task(title, username) 
                    print(f"Task '{title}' added for user '{username}'.") 
                else:
                    print("Invalid username. No such user exists.")
            else:
                print("Invalid task description. Task description cannot be empty and cannot be just a number.")

        elif choice == "4": 
            view_all_users() 

        elif choice == "5": 
            try:
                task_id = int(input("Enter the Task ID to search: ").strip())
                if is_valid_task_id(task_id):
                    view_task_by_id(task_id)  
                else:
                    print("Invalid Task ID. Task ID should be a positive integer.")
            except ValueError:
                print("Invalid Task ID. Please enter a valid integer.")

        elif choice == "6":
            try:
                task_id = int(input("Enter the Task ID to mark as complete: ").strip())
                if is_valid_task_id(task_id):
                    mark_task_complete(task_id) 
                    print(f"Task ID {task_id} marked as complete.")
                else:
                    print("Invalid Task ID. Task ID should be a positive integer.")
            except ValueError:
                print("Invalid Task ID. Please enter a valid integer.")

        elif choice == "7":
            try:
                task_id = int(input("Enter the Task ID to delete: ").strip())
                if is_valid_task_id(task_id):
                    delete_task(task_id)  
                    print(f"Task ID {task_id} deleted.")
                else:
                    print("Invalid Task ID. Task ID should be a positive integer.")
            except ValueError:
                print("Invalid Task ID. Please enter a valid integer.")

        elif choice == "8":
            show_completed_tasks()  

        elif choice == "9":
            show_pending_tasks() 

        elif choice == "10":
            clear_all_tasks()  

        elif choice == "11":
            clear_all_users()  

        elif choice == "12": 
            username = input("Enter the user's full name to search: ").strip()
            view_user_by_name(username) 

        elif choice == "0":
            print("Exiting Todo App. Goodbye!")
            break
