# Description: This is the main file for the website. It contains the code for the website and the database.
# It uses flask to control launching the different pages and sqlite3 to control the database.


# The following libraries are imported to allow the website to run.
from flask import Flask, render_template, request, flash
import sqlite3


####Database content####

# The connection to the database is created here.
# The 'check_same_thread' is set to false to allow multiple threads to access the database.
connection = sqlite3.connect('database.db', check_same_thread=False)

cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, email TEXT NOT NULL, username TEXT NOT NULL, password TEXT NOT NULL)")
cursor.close()


####Flask content####

app = Flask(__name__)# The Flask app is created here. The name of the app is the name of the file.
app.config['SECRET_KEY'] = 'this_is_a_very_secret_key'# This just allows flash to output messages.

@app.route('/')# App route controls what appears in the url for the different pages.
@app.route('/home')
def home():
    return render_template('home.html')# The 'render_template' syntax is used to render templates in the templates folder.
    # Note: that the html if file is not in the templates folder, it will not be shown.

@app.route('/course-content')
def coursecontent():
    return render_template('course-content.html')

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
    # This is how the login system works. First it checks if the form has been answered by checking if the method is a post.
    # If not a post, the page loads as normal. It is important that this is done otherwise the page will always return an error.
    # All errors are handled using the try and except block which prevents the program from crashing.
    if request.method == 'POST':
        # If the form is a post, it will asign the input values to variables.
        form_id = request.form['form_id']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        # To differentiate the functions, the program checks the variable form_id to see if it is a signup or login form.
        # If it is a signup form, it will insert the email, username and password into the database.
        if  form_id == "signup":
            # All errors are handled using the try and except block which prevents the program from crashing.
            try:
                cursor = connection.cursor()
                cursor.execute(f"INSERT INTO users VALUES (NULL, '{email}', '{username}', '{password}')")
                connection.commit()
                cursor.close()
            except sqlite3.Error as error:
                flash('Database error', error)
                return render_template('login.html')
            finally:
                flash('Signup successful')
                return render_template('login.html')
        # If it is a login form, it will check the database to see if the email exists.
        elif form_id == "login":
            try:
                # If the email exists, it will check the password and the username if they match and if they don't return an error.
                cursor = connection.cursor()
                cursor.execute(f"SELECT * FROM users WHERE email=='{email}'")
                check = cursor.fetchone()
                cursor.close()
            except sqlite3.Error as error:
                flash('Database error', error)
                return render_template('login.html')
            finally:
                if check[2] != username or check[3] != password:
                    flash('Username or password is incorrect')
                    return render_template('login.html')
                elif check[2] == username and check[3] == password:
                    flash('Login successful')
                    return render_template('login.html')
                else:
                    flash('Function error')
                    return render_template('login.html')
        else:
            flash('Function error')
            return render_template('login.html')
    else:
        return render_template('login.html')

# This is the main function that runs the website.
if __name__ == '__main__':
    app.run(debug=True)