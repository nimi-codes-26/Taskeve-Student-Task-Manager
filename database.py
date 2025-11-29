import sqlite3
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

def init_db():
    """Initialize the database and create tables"""
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create tasks table with user_id field
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            status TEXT DEFAULT 'Pending',
            completed INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    conn.commit()
    conn.close()

def get_db_connection():
    """Create a database connection"""
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row
    return conn

# USER FUNCTIONS
def create_user(username, password):
    """Create a new user"""
    conn = get_db_connection()
    password_hash = generate_password_hash(password)
    try:
        conn.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', 
                     (username, password_hash))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False  # Username already exists

def verify_user(username, password):
    """Verify user credentials"""
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    conn.close()
    
    if user and check_password_hash(user['password_hash'], password):
        return user
    return None

def get_user_by_id(user_id):
    """Get user by ID"""
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    conn.close()
    return user

def get_user_by_username(username):
    """Get user by username"""
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    conn.close()
    return user

# TASK FUNCTIONS (now with user_id)
def get_all_tasks(user_id):
    """Get all tasks for a specific user"""
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks WHERE user_id = ? ORDER BY due_date ASC, created_at DESC', 
                         (user_id,)).fetchall()
    conn.close()
    return tasks

def add_task(user_id, title, description='', due_date=''):
    """Add a new task for a specific user"""
    conn = get_db_connection()
    conn.execute('INSERT INTO tasks (user_id, title, description, due_date, status) VALUES (?, ?, ?, ?, ?)', 
                 (user_id, title, description, due_date, 'Pending'))
    conn.commit()
    conn.close()

def delete_task(task_id, user_id):
    """Delete a task (only if it belongs to the user)"""
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ? AND user_id = ?', (task_id, user_id))
    conn.commit()
    conn.close()

def toggle_task(task_id, user_id):
    """Toggle task completion status (only if it belongs to the user)"""
    conn = get_db_connection()
    task = conn.execute('SELECT completed, status FROM tasks WHERE id = ? AND user_id = ?', 
                        (task_id, user_id)).fetchone()
    if task:
        new_completed = 0 if task['completed'] else 1
        new_status = 'Completed' if new_completed else 'Pending'
        conn.execute('UPDATE tasks SET completed = ?, status = ? WHERE id = ? AND user_id = ?', 
                     (new_completed, new_status, task_id, user_id))
        conn.commit()
    conn.close()

def update_task(task_id, user_id, title, description, due_date, status):
    """Update an existing task (only if it belongs to the user)"""
    conn = get_db_connection()
    completed = 1 if status == 'Completed' else 0
    conn.execute('''UPDATE tasks 
                    SET title = ?, description = ?, due_date = ?, status = ?, completed = ?
                    WHERE id = ? AND user_id = ?''', 
                 (title, description, due_date, status, completed, task_id, user_id))
    conn.commit()
    conn.close()

def get_task_by_id(task_id, user_id):
    """Get a single task by ID (only if it belongs to the user)"""
    conn = get_db_connection()
    task = conn.execute('SELECT * FROM tasks WHERE id = ? AND user_id = ?', 
                        (task_id, user_id)).fetchone()
    conn.close()
    return task

def calculate_days_left(due_date):
    """Calculate days left until due date"""
    if not due_date:
        return None
    try:
        due = datetime.strptime(due_date, '%Y-%m-%d')
        today = datetime.now()
        delta = (due - today).days
        return delta
    except:
        return None