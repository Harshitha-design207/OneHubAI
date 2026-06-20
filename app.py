from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# ================= DATABASE =================

def init_db():
    conn = sqlite3.connect("onehub.db")
    cursor = conn.cursor()

    # Users Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT,
        username TEXT UNIQUE,
        email TEXT UNIQUE,
        phone TEXT,
        password TEXT
    )
    """)

    # Leads Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS leads(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lead_name TEXT,
        email TEXT,
        phone TEXT,
        company TEXT,
        status TEXT
    )
    """)

    # Customers Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT,
        company TEXT
    )
    """)

    # Tasks Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_name TEXT,
        assigned_to TEXT,
        due_date TEXT,
        status TEXT
    )
    """)

    # Attendance Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_name TEXT,
        date TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

# ================= REGISTER =================

@app.route('/')
def register():
    return render_template('auth/register.html')


@app.route('/save_user', methods=['POST'])
def save_user():

    fullname = request.form['fullname']
    username = request.form['username']
    email = request.form['email']
    phone = request.form['phone']
    password = request.form['password']

    conn = sqlite3.connect("onehub.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users(fullname, username, email, phone, password) VALUES(?,?,?,?,?)",
        (fullname, username, email, phone, password)
    )

    conn.commit()
    conn.close()

    return redirect('/login')

# ================= LOGIN =================

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("onehub.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()
        conn.close()

        if user:
            return redirect('/dashboard')
        else:
            return "Invalid Username or Password"

    return render_template('auth/login.html')

# ================= DASHBOARD =================

@app.route('/dashboard')
def dashboard():

    conn = sqlite3.connect("onehub.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM leads")
    total_leads = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM customers")
    total_customers = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tasks")
    total_tasks = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM attendance WHERE status='Present'")
    present_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM attendance")
    total_attendance = cursor.fetchone()[0]

    attendance_percent = round((present_count / total_attendance) * 100) if total_attendance > 0 else 0

    conn.close()

    return render_template(
        'auth/user/dashboard.html',
        total_leads=total_leads,
        total_customers=total_customers,
        total_tasks=total_tasks,
        attendance_percent=attendance_percent
    )

# ================= LEADS =================

@app.route('/add-lead')
def add_lead():
    return render_template('auth/crm/add_lead.html')


@app.route('/save_lead', methods=['POST'])
def save_lead():

    lead_name = request.form['lead_name']
    email = request.form['email']
    phone = request.form['phone']
    company = request.form['company']
    status = request.form['status']

    conn = sqlite3.connect("onehub.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO leads
    (lead_name,email,phone,company,status)
    VALUES (?,?,?,?,?)
    """, (lead_name, email, phone, company, status))

    conn.commit()
    conn.close()

    return redirect('/leads')


@app.route('/leads')
def leads():

    conn = sqlite3.connect("onehub.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM leads")
    all_leads = cursor.fetchall()

    conn.close()

    return render_template(
        'auth/crm/leads.html',
        leads=all_leads
    )

# ================= CUSTOMERS =================

@app.route('/customers')
def customer():
    return render_template('auth/crm/customer.html')

# ================= TASKS =================

@app.route('/tasks')
def tasks():
    return render_template('auth/tasks/tasks.html')

# ================= ATTENDANCE =================

@app.route('/attendance')
def attendance():
    return render_template('auth/attendance/attendance.html')

# ================= DOCUMENTS =================

@app.route('/documents')
def documents():
    return render_template('auth/documents/documents.html')

# ================= RUN =================

if __name__ == '__main__':
    app.run(debug=True)