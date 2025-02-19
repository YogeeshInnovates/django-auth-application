# 🏆 Django Authentication System

## 📜 Project Description
This is a Django-based authentication system with user login, signup, password reset, and profile management. It ensures secure user access and authentication-based page restrictions.

---

## ⚙️ Features
✔️ User authentication using email or username and password  
✔️ Pages: Login, Signup, Forgot Password, Change Password, Dashboard, Profile  
✔️ Access restriction based on authentication status  
✔️ Email-based password reset functionality  
✔️ Secure password management with Django’s authentication system  

---

## 🛠️ Technologies Used
- **Django** (Python framework)
- **SQLite** (default) / **PostgreSQL**
- **Bootstrap** (for UI)

---

## 📋 Setup Instructions

### 🔧 Prerequisites
- Python 3.x
- Django 3.x

### 📝 Installation
1. Clone the repository:
   
```bash
git clone https://github.com/YogeeshInnovates/django-auth-application.git
cd django-auth-application


Install the required packages:

pip install -r requirements.txt
Set up the database:

python manage.py migrate
Create a superuser:

python manage.py createsuperuser
Run the development server:

python manage.py runserver
Access the application: Open your browser and navigate to http://127.0.0.1:8000

Email Configuration
Before running the project, update settings.py with your email credentials:

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_16_digit_app_password'  # Use your app password
Usage
Signup: Sign up using a username and email

Login: Login with credentials

Password Reset: Reset password via email

Dashboard: Access the dashboard and view user profile

Change Password: Change password securely

Internship Assignment
This project is developed for the WhatBytes Internship Assignment.

Update & Push README to GitHub
git add README.md
git commit -m "Updated README with project details"
git push origin main
