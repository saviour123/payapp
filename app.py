from flask	import Flask, render_template, request, url_for, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from functools import wraps



#creating the application object
app = Flask(__name__)
app.secret_key =  'saviourgidi'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/stms'
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



# #page decorators and functions
# @app.route('/welcome')
# @login_required
# def index():
# 	my_user = User.query.all()
# 	one_item = User.query.filter_by(username="test1").first()
# 	return render_template('index.html',my_user=my_user, one_item=one_item)


# ##customer profiling
# @app.route('/profile/<username>')
# @login_required
# def profile(username):
# 	user = User.query.filter_by(username=username).first()
# 	return render_template('profile.html',user=user)

# #searching with the search box
# # search_word = request.form[query]
# # @app.route('/search_q')
# # @login_required
# # def search_q():
# # 	search_word = request.form[query]
# # 	n_query = user.query.filter_by(username="{}").format('search_word')


# #routes and post, get method,
# #if request methos id post, if request.method == 'POST':

# #then 
# #get the content user = request.form['nm']


# #addin entry/post user
# @app.route('/add_user', methods=['POST'])
# @login_required
# def add_user():
# 	user = User(request.form['username'], request.form['email'])
# 	db.session.add(user)
# 	db.session.commit()
# 	return redirect(url_for('welcome'))


# Loggin route
@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
        	session['logged_in'] = True
        	flash('You are Logged In ')
        	return redirect(url_for('welcome'))
    return render_template('index.html', error=error)


#logging out
@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash("Thanks for using our service. \n You are Logged Out")
	return redirect(url_for('welcome'))

if __name__ == '__main__':
	app.run(debug=True)
