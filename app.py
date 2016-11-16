from flask	import Flask, render_template, request, url_for, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from functools import wraps



#creating the application object
app = Flask(__name__)
app.secret_key =  'saviourgidi'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/test_stms'
db = SQLAlchemy(app)

#my model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


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

#search function
@app.route('/search_q', methods=['GET', 'POST'])
@login_required
def search_q():
    if request.method == 'POST':
        q_db = User.query.filter_by(username="{}").format(request.form['query'])
    else:
        flash('record not in database')
        return redirect(url_for(search_q))
    return render_template("index.html", q_db=q_db)

# #page decorators and functions
@app.route('/index',methods=['GET','POST'])
@login_required
def index():
    my_user = User.query.all()
    return render_template('index.html', my_user=my_user)



#addin entry/post user
@app.route('/add_user', methods=['POST'])
@login_required
def add_user():
	user = User(request.form['username'], request.form['email'])
	db.session.add(user)
	db.session.commit()
	return redirect(url_for('index'))


# Loggin route
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You are Logged In')
            print 'you are logg'
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


#logging out
@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash("Thanks for using our service. \n You are Logged Out")
	return redirect(url_for('login'))

if __name__ == '__main__':
	app.run(debug=True)
