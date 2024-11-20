# NCI 2024 Bogdan Munteanu x21126097@student.ncirl.ie
# Below is an example of a simple Flask web application in Python with SQLite3 as the database.
# The purpose is to demonstrate insecure coding practices.
# Why Python and Flask? Because is fast! 

from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# DATABASE SETUP - Create a SQLite3 database and a users table
def init_db():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

init_db()

# INSECURE CODE - Example of an SQL Injection Vulnerable Login Page
@app.route('/login_insecure', methods=['GET', 'POST'])
def login_insecure():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # SQL Injection Vulnerable Code (DO NOT USE THIS IN PRODUCTION)
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        c.execute(query)
        user = c.fetchone()
        conn.close()
        
        if user:
            return 'Login successful!'
        else:
            return 'Login failed!'
    return render_template_string('''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    ''')



# XSS VULNERABILITY - INSECURE PAGE
@app.route('/comment_insecure', methods=['GET', 'POST'])
def comment_insecure():
    if request.method == 'POST':
        comment = request.form['comment']
        return f"<h1>Comment Submitted:</h1><p>{comment}</p>"
    return render_template_string('''
        <form method="post">
            Comment: <input type="text" name="comment"><br>
            <input type="submit" value="Submit">
        </form>
    ''')



if __name__ == '__main__':
    app.run(debug=True)

