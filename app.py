from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from database import (init_db, get_all_tasks, add_task, delete_task, 
                      toggle_task, update_task, get_task_by_id, calculate_days_left,
                      create_user, verify_user, get_user_by_id)

app = Flask(__name__)
app.secret_key = 'taskeve_secret_key_2025'

# Setup login system
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Create database when app starts
init_db()

# User class for login system
class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

@login_manager.user_loader
def load_user(user_id):
    user_data = get_user_by_id(user_id)
    if user_data:
        return User(user_data['id'], user_data['username'])
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user_data = verify_user(username, password)
        if user_data:
            user = User(user_data['id'], user_data['username'])
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
        elif len(password) < 4:
            flash('Password must be at least 4 characters', 'danger')
        elif create_user(username, password):
            flash('Account created! Please login.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Username already taken', 'danger')
    
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    tasks = get_all_tasks(current_user.id)
    
    tasks_with_days = []
    for task in tasks:
        task_dict = dict(task)
        task_dict['days_left'] = calculate_days_left(task['due_date'])
        tasks_with_days.append(task_dict)
    
    return render_template('index.html', tasks=tasks_with_days, username=current_user.username)

@app.route('/add', methods=['POST'])
@login_required
def add():
    title = request.form.get('title')
    description = request.form.get('description', '')
    due_date = request.form.get('due_date', '')
    
    if title:
        add_task(current_user.id, title, description, due_date)
        flash('Task added successfully!', 'success')
    
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
@login_required
def delete(task_id):
    delete_task(task_id, current_user.id)
    flash('Task deleted.', 'danger')
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>')
@login_required
def toggle(task_id):
    toggle_task(task_id, current_user.id)
    flash('Task updated successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit(task_id):
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description', '')
        due_date = request.form.get('due_date', '')
        status = request.form.get('status', 'Pending')
        
        update_task(task_id, current_user.id, title, description, due_date, status)
        flash('Task updated successfully!', 'success')
        return redirect(url_for('index'))
    
    task = get_task_by_id(task_id, current_user.id)
    if not task:
        flash('Task not found', 'danger')
        return redirect(url_for('index'))
    
    return render_template('edit.html', task=task)

if __name__ == '__main__':
    app.run(debug=True)