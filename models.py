# #payments db 
# this is the schema for creating the tables, ther are 
# three tables here, read the line carefully and always get a backup

from app import *
from app import db
db = SQLAlchemy(app)

# table 1(db_records) this is the table for records, 
# records can then be imported as csv file.
class db_records(db.Model):
    __tablename__ = 'db_records'
    id = db.Column(db.Integer, primary_key=True)
    Account = db.Column(db.String(60))
    Address = db.Column(db.String(60))
    OwnerName = db.Column(db.String(60))
    Suburb = db.Column(db.String(60))
    RateableV = db.Column(db.Float)
    Zone = db.Column(db.String(60))
    Use_ = db.Column(db.String(60))
    Rate = db.Column(db.Float)
    CurrentTax = db.Column(db.Float)
    Arrears = db.Column(db.Float)
    Payment = db.Column(db.Float)
    Balance = db.Column(db.Float)
    Telephone = db.Column(db.String(60))
    Email = db.Column(db.String(60))
    BillingDate = db.Column(db.Integer)
    BLOCKIMAGES = db.Column(db.String(10))
    COMM = db.Column(db.String(60))
    DIV = db.Column(db.Integer)
    BLOCK = db.Column(db.Integer)
    PARCEL = db.Column(db.Integer)
    Discount = db.Column(db.String(60))
    Served = db.Column(db.String(60))
    Date_Served = db.Column(db.String(60))
    Warning_Notice = db.Column(db.String(60))
    Final_Warning_Notice = db.Column(db.String(60))
    Court_Summon = db.Column(db.String(60))
    PictureID = db.Column(db.String(60))
    PictureURL = db.Column(db.String(60))
    SumBuiding = db.Column(db.Float)
    SHAPE = db.Column(db.String(1000))

        


    #initialize the db elements
    def __init__(self, Account,Address,OwnerName,Suburb,RateableV,Zone,Use_,Rate,CurrentTax,Arrears,Payment,Balance,Telephone,Email,BillingDate,BLOCKIMAGES,COMM,DIV,BLOCK,PARCEL,Discount,Served,Date_Served,Warning_Notice,Final_Warning_Notice,Court_Summon,PictureID,PictureURL,SumBuiding,SHAPE):
        self.Account = Account
        self.Address = Address
        self.OwnerName = OwnerName
        self.Suburb = Suburb
        self.RateableV = RateableV
        self.Zone = Zone
        self.Use_ = Use_
        self.rate = rate
        self.CurrentTax = CurrentTax
        self.Arrears = Arrears
        self.Payment = Payment
        self.Balance = Balance
        self.Telephone = Telephone
        self.Email = Email
        self.BillingDate = BillingDate
        self.BLOCKIMAGES = BLOCKIMAGES
        self.COMM = COMM
        self.DIV = DIV
        self.BLOCK = BLOCK
        self.PARCEL = PARCEL
        self.Discount = Discount
        self.Served = Served
        self.Date_Served = Date_Served
        self.Warning_Notice = Warning_Notice
        self.Final_Warning_Notice = Final_Warning_Notice
        self.Court_Summon = Court_Summon
        self.PictureID = PictureID
        self.PictureURL = PictureURL
        self.SumBuiding = SumBuiding
        self.SHAPE = SHAPE

def __repr__(self):
        return '<db_records %r>' % self.Account


# table 2
# this table holds the transaction, and payments
class db_payments(db.Model):
    __tablename__ = 'db_payments'
    id = db.Column(db.Integer, primary_key=True)
    Account = db.Column(db.Integer)
    GCR_No = db.Column(db.String(60))
    Payments = db.Column(db.Float, nullable=False)
    PaymentType = db.Column(db.String(20))
    PaidBy = db.Column(db.String(60))
    PaidByTele = db.Column(db.String(10))
    Cashier = db.Column(db.String(25))
    Pc_name = db.Column(db.String(25))
    DatePaid = db.Column(db.DateTime(), default=datetime.datetime.utcnow())
    Date = db.Column(db.DateTime(), default=datetime.datetime.today())



    def __init__(self, Account, GCR_No, Payments, PaymentType, PaidBy, PaidByTele, Pc_name, Cashier):
        self.Account = Account
        self.GCR_No = GCR_No
        self.Payments = Payments
        self.PaymentType = PaymentType
        self.PaidBy = PaidBy
        self.PaidByTele = PaidByTele
        self.Pc_name = Pc_name
        self.Cashier = Cashier

    def __repr__(self):
        return '<db_payments %r>' % self.Account

# table 3
#users db
class db_user(db.Model):
    __tablename__ = 'db_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(10), unique=True)


    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<db_user %r>' % self.username


