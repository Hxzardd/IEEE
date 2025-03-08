from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import timedelta, datetime
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'default_secret')

SESSION_TIMEOUT = timedelta(minutes=20)

def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def login_required(f):
    def wrapper(*args, **kwargs):
        if 'username' not in session:
            flash("Please log in to access this page.")
            return redirect(url_for('signin'))
        
        # Check if session has expired
        last_activity = session.get('last_activity')
        if last_activity:
            now = datetime.now()
            last_activity_time = datetime.strptime(last_activity, '%Y-%m-%d %H:%M:%S')
            if now - last_activity_time > SESSION_TIMEOUT:
                session.pop('username', None)
                flash("Session expired. Please log in again.")
                return redirect(url_for('signin'))
        
        session['last_activity'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return f(*args, **kwargs)
    
    wrapper.__name__ = f.__name__
    return wrapper

@app.route('/')
def index():
    return redirect(url_for('signin'))

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE username = ? AND password = ?", 
                            (username, password)).fetchone()
        conn.close()
        
        if user:
            session['username'] = username
            session['last_activity'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid credentials. Please try again.")
            return redirect(url_for('signin'))
    
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        try:
            conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            flash("Account created successfully. Please log in.")
            return redirect(url_for('signin'))
        except sqlite3.IntegrityError:
            flash("Username already exists. Please choose a different one.")
            return redirect(url_for('signup'))
        finally:
            conn.close()
    
    return render_template('signup.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return f"Hello, {session['username']}! Welcome to your dashboard."

@app.route('/logout')
@login_required
def logout():
    session.pop('username', None)
    flash("Logged out successfully.")
    return redirect(url_for('signin'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
