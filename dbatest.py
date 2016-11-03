from flask import Flask
from flask_sqlalchemy import import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pymssql://scott:tiger@hostname:port/dbname"
db = SQLAlchemy(app)

##engine = create_engine('mssql+pymssql://scott:tiger@hostname:port/dbname')

db = SQLAlchemy(app)
class students(db.Model):
  id = db.Column('student_id', db.Integer, primary_key = True)
  name = :
  name = db.Column(db.String(100))
  city = db.Column(db.String(50))
  addr = db.Column(db.String(200))
  pin = db.Column(db.String(10))

  def __init__(self, name, city, addr<Plug>PeepOpenin):
    self.name = name
    self.city = city
    self.addr = addr
    self.pin = pin
