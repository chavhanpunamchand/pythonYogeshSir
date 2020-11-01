from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format('root','root','localhost','flaskdb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)


class Employee(db.Model):
    eid  = db.Column('emp_id',db.Integer(),primary_key=True)
    name = db.Column('emp_name',db.String(30))


class Address(db.Model):
    aid  = db.Column('adr_id',db.Integer(),primary_key=True)
    city = db.Column('adr_city', db.String(30))
    empid = db.Column('eid',db.ForeignKey('employee.emp_id'),unique=True,nullable=False)    #extra-query -->to fetch emp
