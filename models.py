class PAYMENTS(db.Model):
    __tablename__ = 'PAYMENTS'
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