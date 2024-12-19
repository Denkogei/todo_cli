import sqlite3

def get_db_connection():
    return sqlite3.connect('todo.db')  

def create_users_table():
    """Create the users table if it doesn't exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    print("Creating users table...") 
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            _id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    print("Users table created (or already exists).") 

def add_user(fullname):
    """Add a user to the users table."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (fullname) VALUES (?)", (fullname,))
    conn.commit()
    conn.close()
    print(f"User {fullname} added.") 

def clear_all_users():
    """Clear all users from the users table."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users")
    conn.commit()
    conn.close()
    print("All users cleared.")  
