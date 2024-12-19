import sqlite3

def get_db_connection():
    """Get a connection to the SQLite database."""
    return sqlite3.connect('todo.db')

def create_tasks_table():
    """Create the tasks table if it doesn't exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            _id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            status TEXT CHECK(status IN ('pending', 'completed', 'in-progress')) DEFAULT 'pending',
            userId INTEGER,
            FOREIGN KEY (userId) REFERENCES users(_id)
        )
    """)
    conn.commit()
    conn.close()

def add_task(title, username):
    """Add a task to the tasks table."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT _id FROM users WHERE fullname = ?", (username,))
    user = cursor.fetchone()
    if user:
        user_id = user[0]
        cursor.execute("INSERT INTO tasks (title, userId, status) VALUES (?, ?, ?)", (title, user_id, "pending"))  
        conn.commit()
        print(f"Task '{title}' added for user '{username}'.")
    else:
        print(f"User '{username}' not found. Please add the user first.")
    conn.close()


def view_all_tasks():
    """View all tasks."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT tasks._id, tasks.title, tasks.status, users.fullname
        FROM tasks
        LEFT JOIN users ON tasks.userId = users._id
    """)
    tasks = cursor.fetchall()
    conn.close()

    if tasks:
        print("\nAll Tasks:")
        print("ID | Title | Status | User")
        print("-" * 30)
        for task in tasks:
            print(f"{task[0]} | {task[1]} | {task[2]} | {task[3]}")
    else:
        print("No tasks found.")

def mark_task_complete(task_id):
    """Mark a task as complete."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = 'completed' WHERE _id = ?", (task_id,))
    if cursor.rowcount > 0:
        print(f"Task ID {task_id} marked as completed.")
    else:
        print(f"Task ID {task_id} not found.")
    conn.commit()
    conn.close()

def delete_task(task_id):
    """Delete a task."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE _id = ?", (task_id,))
    if cursor.rowcount > 0:
        print(f"Task ID {task_id} deleted.")
    else:
        print(f"Task ID {task_id} not found.")
    conn.commit()
    conn.close()

def show_completed_tasks():
    """Show all completed tasks."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT tasks._id, tasks.title, users.fullname
        FROM tasks
        LEFT JOIN users ON tasks.userId = users._id
        WHERE tasks.status = 'completed'
    """)
    tasks = cursor.fetchall()
    conn.close()

    if tasks:
        print("\nCompleted Tasks:")
        print("ID | Title | User")
        print("-" * 30)
        for task in tasks:
            print(f"{task[0]} | {task[1]} | {task[2]}")
    else:
        print("No completed tasks found.")

def show_pending_tasks():
    """Show all pending tasks."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT tasks._id, tasks.title, users.fullname
        FROM tasks
        LEFT JOIN users ON tasks.userId = users._id
        WHERE tasks.status = 'pending'
    """)
    tasks = cursor.fetchall()
    conn.close()

    if tasks:
        print("\nPending Tasks:")
        print("ID | Title | User")
        print("-" * 30)
        for task in tasks:
            print(f"{task[0]} | {task[1]} | {task[2]}")
    else:
        print("No pending tasks found.")

def clear_all_tasks():
    """Clear all tasks."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks")
    conn.commit()
    conn.close()
    print("All tasks cleared.")


def view_task_by_id(task_id):
    """View a specific task by its ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT tasks._id, tasks.title, tasks.status, users.fullname FROM tasks INNER JOIN users ON tasks.userId = users._id WHERE tasks._id = ?", (task_id,))
    task = cursor.fetchone()
    if task:
        task_id, title, status, fullname = task
        print(f"Task ID: {task_id}")
        print(f"Title: {title}")
        print(f"Status: {status}") 
        print(f"Assigned to: {fullname}")
    else:
        print(f"Task with ID {task_id} not found.")
    conn.close()

