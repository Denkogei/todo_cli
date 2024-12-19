import sqlite3

def get_db_connection():
    return sqlite3.connect('todo.db')  # Connect to the SQLite database

def create_users_table():
    """Create the users table if it doesn't exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    print("Creating users table...")  # Debugging line
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            _id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    print("Users table created (or already exists).")  # Debugging line

def add_user(fullname):
    """Add a user to the users table."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (fullname) VALUES (?)", (fullname,))
    conn.commit()
    conn.close()
    print(f"User {fullname} added.")  # Debugging line

def clear_all_users():
    """Clear all users from the users table."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users")
    conn.commit()
    conn.close()
    print("All users cleared.")  # Debugging line
