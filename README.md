# Todo CLI App

#### A command-line interface (CLI) application for managing users and tasks in a simple, user-friendly manner.

#### By **Dennis Kemboi**

---

## Description

The Todo CLI App is a Python-based application that enables users to manage tasks and users efficiently via the command line. This app includes functionalities for adding users, creating tasks, marking tasks as complete, and more.

It uses SQLite as the database and employs a modular structure to ensure maintainability and scalability.

---

## Features

- **User Management**
  - Add new users.
  - View all users.
  - Search for a specific user by name.
  - Clear all users.

- **Task Management**
  - Add tasks for specific users.
  - View all tasks.
  - Search for a task by its ID.
  - Mark tasks as complete.
  - View pending and completed tasks.
  - Delete individual tasks.
  - Clear all tasks.

---

## How to Use

### Requirements

- A computer with Python 3.x installed.
- A basic understanding of the command-line interface.

### Installation Process

1. Clone this repository:

   ```bash
   git clone git@github.com:Denkogei/todo_cli.git
   cd todo-cli
   code .
   python3 app.py      #Run the application
Welcome to the Todo App!
===========================
Please choose an option:
1. Add User
2. View all tasks
3. Add a task
4. View all users
5. Search Task by ID
6. Search User by Name
7. Mark Task as Complete
8. Delete a Task
9. Show Completed Tasks
10. Show Pending Tasks
11. Clear All Tasks
12. Clear All Users
0. Exit

# Project Structure

```plaintext
├── app.py              # Main entry point for the CLI app
├── cli.app             # CLI logic file
├── todo.db             # SQLite database file
├── Pipfile             # Dependencies and virtual environment setup
├── README.md           # Documentation
├── models/
│   ├── tasks.py        # Task management functionality
│   └── users.py        # User management functionality

## Technologies Used

- Python
- Sqllite3


If you have any questions, suggestions, or need assistance, please contact:

- Email: <denkogei11@gmail.com>

## License

MIT License

Copyright &copy; 2024 Dennis Kemboi

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

        