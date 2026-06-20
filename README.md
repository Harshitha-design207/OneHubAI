# OneHub AI 🚀

## CRM & ERP Management System

OneHub AI is a web-based CRM and ERP platform developed using Flask, SQLite, HTML, CSS, and Bootstrap. It helps organizations manage leads, customers, tasks, attendance, and business operations from a single dashboard.

## Features

### User Management
- User Registration
- User Login
- Secure Authentication

### Lead Management
- Add New Leads
- View Lead Details
- Track Lead Status

### Customer Management
- Manage Customer Information
- Store Customer Records
- Customer Status Tracking

### Task Management
- Assign Tasks
- Track Pending Tasks
- Manage Daily Activities

### Attendance Management
- Employee Attendance Tracking
- Attendance Status Monitoring

### Dashboard
- Total Leads Overview
- Customer Statistics
- Task Summary
- Attendance Summary

## Technologies Used

- Python
- Flask
- SQLite
- HTML5
- CSS3
- Bootstrap 5
- Git & GitHub

## Project Structure

```text
OneHubAI/
│
├── app.py
├── onehub.db
├── templates/
│   ├── auth/
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── crm/
│   │   │   ├── add_lead.html
│   │   │   └── customer.html
│   │   ├── tasks/
│   │   │   └── tasks.html
│   │   ├── attendance/
│   │   │   └── attendance.html
│   │   └── user/
│   │       └── dashboard.html
│
└── README.md
git clone https://github.com/Harshitha-design207/OneHubAI.git
2) Navigate to project folder
cd OneHubAI
3) install dependences
pip install flask
run the code
python app.py
open in the browser
http://127.0.0.1:5000/dashboard
