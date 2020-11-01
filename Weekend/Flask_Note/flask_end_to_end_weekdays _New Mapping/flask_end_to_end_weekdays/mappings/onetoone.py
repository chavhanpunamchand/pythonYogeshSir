from flask_end_to_end_weekdays.helper.app_queries import *
from flask_sqlalchemy import SQLAlchemy
from flask_end_to_end_weekdays.configurations.app_config import app
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(USERNAME,PASSWORD,HOST,DB_NAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False      # dont showcase warning msgs
app.config['SQLALCHEMY_ECHO']=False      # print queries
db = SQLAlchemy(app)

#__tablename__ --> overrides default table name --> default name = modelname

#1-1
class Employee(db.Model):               #   Employee
    #__tablename__ = "EMP_INFO"          #   EMP_INFO    --> emp_id emp_name emp_age emp_sal
    eid = db.Column('emp_id', db.Integer(), primary_key=True)
    name = db.Column('emp_name', db.String(100))
    age = db.Column('emp_age', db.Integer())
    salary = db.Column('emp_sal', db.Float())
    adrid = db.Column("ADR_FK_KEY",db.ForeignKey('address.adr_id'),unique=True,nullable=True) # we are adding a fk inside emp --> adr madn

#nullable=False --> in fk --> makes ur relationship--tightly coupled..

class Address(db.Model):
    #__tablename__ = "ADR_INFO"      # ADR_INFO --> adr_id adr_city adr_pincode adr_state
    aid = db.Column('adr_id', db.Integer(), primary_key=True)
    city = db.Column('adr_city', db.String(100))
    state = db.Column('adr_state', db.String(100))
    pincode = db.Column('adr_pincode', db.Integer())

def prepare_address_stuff():
    db.create_all()
    print('Table created')
    ad1 = Address(aid=101, city='Pune1', state='MH1', pincode=123445)
    ad2 = Address(aid=102, city='Pune2', state='MH2', pincode=123446)
    ad3 = Address(aid=103, city='Pune3', state='MH3', pincode=123447)

    db.session.add_all([ad1, ad2, ad3])
    db.session.commit()

    print('3 Address records inserted')


import time
import sys
db.create_all()
if __name__ == '__main__':
    #prepare_address_stuff()
    #sys.exit(0)
    for item in range(1,6):
        e1 = Employee(eid=item,name='YYY',age=25,salary=55444.56)
         #e1.adrid = 103      # going to work ?? --> NO       one to one --> 1 adr --> max --> 1 emp can hold
        db.session.add(e1)
        db.session.commit()

    sys.exit(0)

    sys.exit(0)
    db.drop_all()
    print('Removed')
    time.sleep(3)
    print('Creating')
    db.create_all()
    print('Created')