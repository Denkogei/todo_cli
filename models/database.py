import sqlite3

DATABASE_PATH = 'todo.db'

def get_db_connection():
    """Create and return a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE_PATH)
    return conn

def create_tables():
    """Create the users and tasks tables if they don't already exist."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create the users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        _id INTEGER PRIMARY KEY,
        fullname TEXT NOT NULL
    )
    """)

    # Create the tasks table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        _id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        status TEXT CHECK(status IN ('pending', 'completed', 'in-progress')) DEFAULT 'pending',
        userId INTEGER,
        FOREIGN KEY (userId) REFERENCES users(_id)
    )
    """)

    conn.commit()
    conn.close()

def close_connection(conn):
    """Close the database connection."""
    if conn:
        conn.close()
