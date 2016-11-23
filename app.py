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
class PAYMENTS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    OBJECTID = db.Column(db.Integer)
    Account =db.Column(db.String(60))
    Amount_Due = db.Column(db.Integer)
    GCR_No = db.Column(db.String(60))
    Payments = db.Column(db.Integer)
    PaymentType = db.Column(db.String(20))
    DatePaid = db.Column(db.DateTime(), default=datetime.datetime.utcnow())
    PaidBy = db.Column(db.String(60))
    PaidByTele = db.Column(db.String(10))
    Cashier = db.Column(db.String(25))
    Date = db.Column(db.DateTime(), default=datetime.date.today())


    def __init__(self, Account, GCR_No, Payments, PaymentType, PaidBy, PaidByTele, Cashier):
        self.Account = Account
        self.GCR_No = GCR_No
        self.Payments = Payments
        self.PaymentType = PaymentType
        self.PaidBy = PaidBy
        self.PaidByTele = PaidByTele
        self.Cashier = Cashier


    def __repr__(self):
        return '<records %r>' % self.Account


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
    data_rec = PAYMENTS.query.all()
    return render_template('index.html', data_rec=data_rec)


#add record/post user
@app.route('/add_rec', methods=['POST', 'GET'])
@login_required
def add_rec():
    if request.method == 'POST':
        Account = request.form['Account']
        GCR_No = request.form['GCR_No']
        Payments = request.form['Payments']
        PaymentType = request.form['PaymentType']
        PaidBy = request.form['PaidBy']
        PaidByTele = request.form['PaidByTele']
        Cashier = request.form['Cashier']
        result = request.form
        global PostData
        PostData = [Account, GCR_No, Payments, PaymentType, PaidBy, PaidByTele, Cashier]
        entry = PAYMENTS(Account, GCR_No, Payments, PaymentType, PaidBy, PaidByTele, Cashier)
        db.session.add(entry)
        db.session.commit()
        return render_template('print_page.html', result=result)
    return render_template('add_new.html')


#search function
@login_required
@app.route('/search', methods=['POST'])
def search():
    error = None
    query_tag = request.form['search']
    search_tag = PAYMENTS.query.filter_by(Account=query_tag).all()
    return render_template('search.html', search_tag=search_tag)


if __name__ == '__main__':
	app.run(debug=True)
