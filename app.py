from flask	import Flask, render_template, request, url_for, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from functools import wraps



#creating the application object
app = Flask(__name__)
app.secret_key =  'saviourgidi'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://scott:tiger@localhost:port/mydatabase'
db = SQLAlchemy(app)
 




#login Decorators
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('Please Login in First')
			return redirect(url_for('login'))
	return wrap

#page decorators and functions
@app.route('/welcome')
@login_required
def welcome():
	return render_template('welcome.html')

# Loggin route
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
        	session['logged_in'] = True
        	flash('You are Logged In ')
        	return redirect(url_for('welcome'))
    return render_template('login.html', error=error)


#logging out
@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash("Thanks for using our service. \n You are Logged Out")
	return redirect(url_for('welcome'))

if __name__ == '__main__':
	app.run(debug=True)