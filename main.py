from flask import Flask, render_template, request, flash
import sqlite3

connection = sqlite3.connect('database.db', check_same_thread=False)

cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, email TEXT NOT NULL, username TEXT NOT NULL, password TEXT NOT NULL)")
cursor.close()

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/course')
def course():
    return render_template('course.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/sign-in', methods=['POST', 'GET'])
def signin():
    return render_template('signin.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        if id=="signin":
            try:
                cursor = connection.cursor()
                cursor.execute(f"INSERT INTO users VALUES (NULL, '{email}', '{username}', '{password}')")
                connection.commit()
                cursor.close()
            except sqlite3.Error as error:
                return render_template('login.html')
            finally:
                render_template('login.html')
        else:
            try:
                cursor = connection.cursor()
                cursor.execute(f"SELECT * FROM users WHERE email={email}")
                output = cursor.fetchone()
                print(output)
                cursor.close()
            except sqlite3.Error as error:
                return render_template('login.html')
            finally:
                return render_template('login.html')
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)