from models.database import get_db_connection

def show_main_menu():
    print("\nWelcome to the Todo App!")
    print("===========================")
    print("Please choose an option:")
    print("1. Add User")
    print("2. View all tasks")
    print("3. Add a task")
    print("4. Update a task")
    print("5. Delete a task")
    print("6. Mark task as complete")
    print("7. Show completed tasks")
    print("8. Show pending tasks")
    print("9. Clear all tasks")
    print("10. Exit")

def add_user():
    """Add a new user to the users table."""
    fullname = input("Enter user's full name: ")
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (fullname) VALUES (?)", (fullname,))
    conn.commit()

    print(f"User '{fullname}' added successfully.")
    conn.close()

def view_all_tasks():
    """Display all tasks with user names."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        SELECT tasks._id, tasks.title, tasks.status, users._id, users.fullname 
        FROM tasks 
        LEFT JOIN users ON tasks.userId = users._id
        """)
        tasks = cursor.fetchall()

        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nAll Tasks:")
            for task in tasks:
                task_id, title, status, user_id, user_name = task
                print(f"Task ID: {task_id}, Title: {title}, Status: {status}, User ID: {user_id}, User Name: {user_name or 'Unknown User'}")
    except Exception as e:
        print("Error fetching tasks:", e)

    conn.close()

def add_task():
    """Add a new task."""
    conn = get_db_connection()
    cursor = conn.cursor()

    title = input("Enter the task description: ")
    user_id = input("Enter the user ID: ")

    # Check if the user ID exists in the database
    cursor.execute("SELECT * FROM users WHERE _id = ?", (user_id,))
    user = cursor.fetchone()

    if user:
        status = "pending"
        try:
            cursor.execute("INSERT INTO tasks (title, status, userId) VALUES (?, ?, ?)", (title, status, user_id))
            conn.commit()
            print(f"Task '{title}' added successfully.")
        except Exception as e:
            print("Error adding task:", e)
    else:
        print("Invalid user ID, task not added.")
    
    conn.close()

def update_task():
    """Update an existing task."""
    print("Updating a task... (this feature is under construction)")

def delete_task():
    """Delete a task."""
    print("Deleting a task... (this feature is under construction)")

def mark_task_complete():
    """Mark a task as complete."""
    print("Marking a task as complete... (this feature is under construction)")

def show_completed_tasks():
    """Display all completed tasks with user names."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        SELECT tasks._id, tasks.title, tasks.status, users.fullname
        FROM tasks
        LEFT JOIN users ON tasks.userId = users._id
        WHERE tasks.status = 'completed'
        """)
        tasks = cursor.fetchall()

        if len(tasks) == 0:
            print("No completed tasks found.")
        else:
            print("\nCompleted Tasks:")
            for task in tasks:
                task_id, title, status, user_name = task
                print(f"Task ID: {task_id}, Title: {title}, Status: {status}, User Name: {user_name or 'Unknown User'}")
    except Exception as e:
        print("Error fetching completed tasks:", e)

    conn.close()

def show_pending_tasks():
    """Display all pending tasks with user names."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        SELECT tasks._id, tasks.title, tasks.status, users.fullname
        FROM tasks
        LEFT JOIN users ON tasks.userId = users._id
        WHERE tasks.status = 'pending'
        """)
        tasks = cursor.fetchall()

        if len(tasks) == 0:
            print("No pending tasks found.")
        else:
            print("\nPending Tasks:")
            for task in tasks:
                task_id, title, status, user_name = task
                print(f"Task ID: {task_id}, Title: {title}, Status: {status}, User Name: {user_name or 'Unknown User'}")
    except Exception as e:
        print("Error fetching pending tasks:", e)

    conn.close()

def clear_all_tasks():
    """Clear all tasks from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM tasks")
        conn.commit()
        print("All tasks cleared.")
    except Exception as e:
        print("Error clearing tasks:", e)

    conn.close()

def exit_app():
    """Exit the application."""
    print("Exiting Todo App. Goodbye!")
    exit()

def run_cli():
    """Run the command-line interface."""
    while True:
        show_main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            view_all_tasks()
        elif choice == "3":
            add_task()
        elif choice == "4":
            update_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            mark_task_complete()
        elif choice == "7":
            show_completed_tasks()
        elif choice == "8":
            show_pending_tasks()
        elif choice == "9":
            clear_all_tasks()
        elif choice == "10":
            exit_app()
        else:
            print("Invalid choice. Please try again.")
