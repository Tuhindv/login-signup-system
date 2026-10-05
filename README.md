# 🔐 Login & Signup System

A simple **Login and Signup System** built with Python and FastAPI.

This project is created for learning and practicing user authentication, form handling, password hashing, and FastAPI web development.

## 🚀 Features

* 📝 User Signup
* 🔐 User Login
* 🚪 Logout
* 🔒 Password hashing using `bcrypt`
* 📧 Email-based authentication
* 🎨 Simple and clean HTML/CSS interface
* 👤 User information stored locally
* ⚡ FastAPI backend

## 🛠️ Technologies Used

* Python
* FastAPI
* Uvicorn
* HTML5
* CSS3
* Jinja2
* bcrypt

## 📁 Project Structure

```text
login-signup-system/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── static/
│   └── css/
│       └── style.css
│
└── templates/
    ├── login.html
    ├── signup.html
    └── gallery.html
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Tuhindv/login-signup-system.git
```

### 2. Open the project folder

```bash
cd login-signup-system
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Project

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Open your browser:

```text
http://127.0.0.1:8000
```

## 🔑 How It Works

### Signup

Users can create an account using:

* Name
* Email
* Password
* Confirm Password

### Login

Registered users can log in using their:

* Email
* Password

After successful login, the user can access the application's main page.

## 🔒 Security

Passwords are hashed using `bcrypt` before being stored.

Private/local files are excluded from GitHub using `.gitignore`.

```text
venv/
__pycache__/
users.json
static/images/*
```

## 🎯 Learning Objectives

This project helped me practice:

* FastAPI
* Python
* HTML & CSS
* Form handling
* User authentication
* Password hashing
* Jinja2 templates
* Git & GitHub

## 👨‍💻 Author

**Tuhin Biswas**

GitHub: https://github.com/Tuhindv

## 📄 License

This project is created for learning and educational purposes.
