#payments db 

from app import *

class PAYMENTS(db.Model):
    __tablename__ = 'PAYMENTS'
    id = db.Column(db.Integer, primary_key=True)
    Account = db.Column(db.Integer)
    GCR_No = db.Column(db.String(60))
    Payments = db.Column(db.Integer)
    PaymentType = db.Column(db.String(20))
    PaidBy = db.Column(db.String(60))
    PaidByTele = db.Column(db.String(10))
    Cashier = db.Column(db.String(25))
    Pc_name = db.Column(db.String(25))
    DatePaid = db.Column(db.DateTime(), default=datetime.datetime.utcnow())
    DatePaid = db.Column(db.DateTime(), default=datetime.datetime.today())



    def __init__(self, Account, GCR_No, Payments, PaymentType, PaidBy, PaidByTele, Cashier):
        self.Account = Account
        self.GCR_No = GCR_No
        self.Payments = Payments
        self.PaymentType = PaymentType
        self.PaidBy = PaidBy
        self.PaidByTele = PaidByTele
        self.Pc_name = Pc_name
        self.Cashier = Cashier

    def __repr__(self):
        return '<records %r>' % self.Account

#users db
class User(db.Model):
    __tablename__ = 'User'
    #__table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(10), unique=True)


    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username