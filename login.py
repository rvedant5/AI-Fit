# login.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data (replace with database)
users = {'john': 'password', 'emma': 'password'}


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        # Redirect to a different page if login is successful
        return redirect(url_for('success'))
    else:
        # Reload login page with an error message
        return render_template('login.html', message='Invalid username or password')


@app.route('/success')
def success():
    return 'Logged in successfully!'


if __name__ == '__main__':
    app.run(debug=True)
