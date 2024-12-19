import sqlite3

def get_db_connection():
    """Establish and return a connection to the database."""
    return sqlite3.connect('todo.db')  

def create_users_table():
    """Create the users table if it doesn't exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            _id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_user(fullname):
    """Add a user to the users table."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (fullname) VALUES (?)", (fullname,))
    conn.commit()
    conn.close()
    print(f"User {fullname} added.") 

def view_all_users():
    """Fetch and display all users from the users table."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT _id, fullname FROM users")
    users = cursor.fetchall()
    if users:
        print("\nList of All Users:")
        print("==================")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}")
    else:
        print("\nNo users found.")
    conn.close()

def clear_all_users():
    """Clear all users from the users table."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users")
    conn.commit()
    conn.close()
    print("All users cleared.")  


def view_user_by_name(username):
    """Search for a user by name and display all their tasks."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT _id, fullname FROM users WHERE fullname = ?", (username,))
    user = cursor.fetchone()

    if user:
        user_id, fullname = user
        print(f"\nUser: {fullname}")

        cursor.execute("""
            SELECT tasks._id, tasks.title, tasks.status
            FROM tasks
            WHERE tasks.userId = ?
        """, (user_id,))

        tasks = cursor.fetchall()
        
        if tasks:
            print(f"Tasks assigned to {fullname}:")
            for task in tasks:
                task_id, title, status = task
                print(f"  Task ID: {task_id}, Title: {title}, Status: {status}")
        else:
            print(f"{fullname} has no tasks assigned.")
    else:
        print(f"User '{username}' not found.")
    
    conn.close()
