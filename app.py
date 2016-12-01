from flask import Flask, render_template, request, url_for, redirect, session, flash, g
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required 
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import datetime, os
from models import *


#creating the application object
app = Flask(__name__)
app.config.from_object('config.BaseConfig')
db = SQLAlchemy(app)

# # Create a user to test with
# @app.before_first_request
# def create_user():
#     db.create_all()
#     admin_user = db_user(username='saviour', password='saviour')
#     db.session.add(admin_user)
#     db.session.commit()




#login check point decorator
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
    global username
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        #search database for the record
        session['username'] = username #store username, submitted with form on line 84
        u_login = db_user.query.filter_by(username=username)
        data_rec = db_user.query.all()       
        for i in u_login:
            if username != i.username or password != i.password:
                error = 'Invalid Credentials, Please try again'
            # elif not db_user.query.all() = None:
            #     error = "Wrong Username or Password, Contact Your Admin"
            else:
                session['logged_in'] = True
                flash('you are logged In')
                return redirect(url_for('index'))
    return render_template('login.html', error=error)


#logging out
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.clear()
    flash("Thanks for using our service. \n You are Logged Out")
    return redirect(url_for('login'))

#home route
@app.route('/index',methods=['GET','POST'])
@login_required
def index():
    #data_rec = db_payments.query.all()
    return render_template('index.html')


#add record/post user
@app.route('/add_rec', methods=['POST', 'GET'])
@login_required
def add_rec():
    if request.method == 'POST':
        Account = request.form['Account']
        GCR_No = request.form['GCR_No']
        Payments = request.form['Payments']
        PaymentType = request.form['PaymentType'].strip('`')
        PaidBy = request.form['PaidBy']
        PaidByTele = request.form['PaidByTele']
        Cashier = session['username']
        pc_name = os.environ.get('USERNAME')
        PostData = [Account, GCR_No, Payments, PaymentType, PaidBy, PaidByTele, Cashier]
        result = request.form #this line was served to print page, make sure you learn jinja before fooling
        entry = db_payments(Account, GCR_No, Payments, PaymentType, PaidBy, PaidByTele, Cashier, pc_name)  
        db.session.add(entry)
        db.session.commit()
        return render_template('print_page.html', result=result, Cashier=Cashier)
    search = db_records.query.filter_by(Account=query_tag).all()
    return render_template('add_new.html', search=search)


#search function
@login_required
@app.route('/search', methods=['POST'])
def search():
    error = None
    global query_tag
    query_tag = request.form['search']
    session['query_tag'] = query_tag
    try:
        search = db_records.query.filter_by(Account=query_tag).all()
    except:
        error = 'Record does not exist, Contact administrator'
    return render_template('search.html', search=search, error=error)


#adding login routing
@login_required
@app.route('/add_login', methods=['POST', 'GET'])
def add_login():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            login_details = db_user(username, password)
            db.session.add(login_details)
            db.session.commit()
            flash('User added succesfully')
            return redirect(url_for('index'))
        except:
            return redirect(url_for(error))
    return render_template('add_login.html')

#error handling
@login_required
@app.route('/error')
def error():
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)