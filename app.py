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
class records(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account =db.Column(db.String(60))
    GCR_No = db.Column(db.String(60))
    paid_by = db.Column(db.String(60))
    paid_by_tele = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    last_edited_user = db.Column(db.String(25))
    confirmed_at = db.Column(db.DateTime())
    created = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    Date_request = db.Column(db.DateTime())




    def __init__(self, account, GCR_No, paid_by, paid_by_tele, amount, last_edited_user):
        self.account = account
        self.GCR_No = GCR_No
        self.paid_by = paid_by
        self.paid_by_tele = paid_by_tele
        self.amount = amount
        self.last_edited_user = last_edited_user


    def __repr__(self):
        return '<records %r>' % self.account


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
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


#logging out
@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash("Thanks for using our service. \n You are Logged Out")
	return redirect(url_for('login'))

# #home rounte
@app.route('/index',methods=['GET','POST'])
@login_required
def index():
    data_rec = records.query.all()
    return render_template('index.html', data_rec=data_rec)


#add record/post user
@app.route('/add_rec', methods=['POST', 'GET'])
@login_required
def add_rec():
    if request.method == 'POST':
        #collect form data
        account = request.form['account']
        GCR_No = request.form['GCR_No']
        paid_by = request.form['paid_by']
        paid_by_tele = request.form['paid_by_tele']
        amount = request.form['amount']
        last_edited_user = request.form['last_edited_user']
        #add records
        entry = records(account, GCR_No, paid_by, paid_by_tele, amount, last_edited_user)
        db.session.add(entry)
        db.session.commit()
        flash('Record entered succesfully')
        return redirect(url_for('index'))
    return render_template('add_new.html')

#search function
@login_required
@app.route('/search', methods=['POST'])
def search():
    query_tag = request.form['search']
    search_tag = records.query.filter_by(account=query_tag).all()
    return render_template('search.html', search_tag=search_tag)


if __name__ == '__main__':
	app.run(debug=True)
