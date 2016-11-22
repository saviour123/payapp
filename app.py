from flask	import Flask, render_template, request, url_for, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import datetime



#creating the application object
app = Flask(__name__)
app.secret_key =  'saviourgidi'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@192.168.1.6/stms'
db = SQLAlchemy(app)

#my model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account =db.Column(db.String, unique=True)
    paid_by = db.Column(db.String(120), unique=True)
    paid_by_tele = db.Column(db.Integer, unique=True)
    amount = db.Column(db.Integer)
    GCR_No = db.Column(db.String(120), unique=True)
    last_edited_user = db.Column(db.String(25))
    confirmed_at = db.Column(db.DateTime())
    created = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    Date_request = db.Column(db.DateTime())

    #db.INT, primary_key=True, autoincrement=False, nullable=False


    def __init__(self, username, email):
        self.account = account
        self.paid_by = paid_by
        self.paid_by_tele = paid_by_tele
        self.amount = amount
        self.GCR_No = GCR_No
        self.last_edited_user = last_edited_user


    def __repr__(self):
        return '<User %r>' % self.account


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

#search function
@app.route('/search', methods=['POST'])
def search():
    query_tag = request.form['search']
    search_tag = User.query.filter_by(username=query_tag).all()
    return render_template('search.html', search_tag=search_tag)


if __name__ == '__main__':
	app.run(debug=True)
