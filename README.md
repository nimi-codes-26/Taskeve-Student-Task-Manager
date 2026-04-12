# 📚 TASKEVE - Student Task Manager

A lightweight Python + Flask web application that helps students manage academic tasks and deadlines through a simple, organized interface.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey.svg)

## 🎯 Project Overview

**TASKEVE** is designed to solve common problems students face:
- Managing multiple assignment deadlines
- Tracking project submissions
- Organizing exam-related tasks
- Reducing academic stress through better planning

## ✨ Key Features

- 🔐 **User Authentication** - Secure registration and login system
- ➕ **Add Tasks** - Create tasks with title, description, and due date
- ✏️ **Edit Tasks** - Modify existing task details
- 🗑️ **Delete Tasks** - Remove completed or unnecessary tasks
- ✅ **Mark Complete** - Toggle task status between pending and completed
- ⏰ **Days Left Calculator** - Automatic countdown to due dates
- 🚨 **Urgent Alerts** - Color-coded warnings for overdue tasks
- 👤 **Personal Dashboard** - Each user sees only their own tasks

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.8+ |
| **Framework** | Flask |
| **Database** | SQLite |
| **Frontend** | HTML, CSS |
| **Authentication** | Flask-Login |
| **Password Security** | Werkzeug Password Hashing |

### Python Libraries Used:
- `Flask` - Web framework
- `flask-login` - User session management
- `sqlite3` - Database operations
- `datetime` - Date calculations
- `werkzeug.security` - Password hashing

## 📁 Project Structure
```
Taskeve-Student-Task-Manager/
├── app.py                  # Main Flask application
├── database.py             # Database operations
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Git ignore rules
├── templates/             # HTML templates
│   ├── index.html         # Main dashboard
│   ├── login.html         # Login page
│   ├── register.html      # Registration page
│   └── edit.html          # Edit task page
└── static/                # Static files
    └── style.css          # Styling
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/nimi-codes-26/Taskeve-Student-Task-Manager.git
cd Taskeve-Student-Task-Manager
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Run the Application
```bash
python app.py
```

### Step 6: Open in Browser
Navigate to: `http://127.0.0.1:5000`

## 📖 How to Use

1. **Register**: Create a new account with username and password
2. **Login**: Access your personal dashboard
3. **Add Task**: Click "Add Task" button and fill in details
4. **View Tasks**: See all your tasks with due dates and status
5. **Edit Task**: Click "Edit" to modify task information
6. **Complete Task**: Click checkbox to mark as done
7. **Delete Task**: Remove tasks you no longer need
8. **Logout**: Securely end your session

## 💾 Database Schema

### Users Table
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| username | TEXT | Unique username |
| password_hash | TEXT | Hashed password |
| created_at | TIMESTAMP | Account creation time |

### Tasks Table
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| user_id | INTEGER | Foreign key to users |
| title | TEXT | Task title |
| description | TEXT | Task details |
| due_date | TEXT | Deadline date |
| status | TEXT | Pending/Completed |
| completed | INTEGER | 0 or 1 |
| created_at | TIMESTAMP | Task creation time |

## 🔐 Security Features

- ✅ Password hashing using Werkzeug
- ✅ Session-based authentication
- ✅ User-specific task isolation
- ✅ Protected routes with @login_required
- ✅ SQL injection prevention

## 🎓 Learning Outcomes

This project demonstrates:
- Flask web framework fundamentals
- RESTful routing and HTTP methods
- SQLite database integration
- User authentication implementation
- CRUD operations (Create, Read, Update, Delete)
- Template rendering with Jinja2
- Form handling and validation
- Session management
- Password security best practices

## 🔮 Future Enhancements

- 📧 Email notifications for upcoming deadlines
- 📊 Task analytics with matplotlib graphs
- 🏷️ Task categories and priority levels
- 📱 Responsive mobile design
- 🔔 Browser push notifications
- 📅 Calendar view integration
- 🌐 Multi-language support
- 🤝 Task sharing and collaboration

## 🙏 Acknowledgments

- Flask Documentation Team
- Python Community
- Stack Overflow Contributors
- W3Schools Tutorials
- Our Faculty for guidance and support

## 📄 License

This project is created for educational purposes as part of academic coursework.

## 📞 Contact

For queries or suggestions:
- **GitHub**: [@nimi-codes-26](https://github.com/nimi-codes-26)
- **Repository**: [Taskeve-Student-Task-Manager](https://github.com/nimi-codes-26/Taskeve-Student-Task-Manager)

## 🐛 Known Issues

Currently, there are no known critical bugs. For reporting issues or contributing improvements, please create an issue on GitHub.

---

**Made with ❤️ by Nimisha**

.....

