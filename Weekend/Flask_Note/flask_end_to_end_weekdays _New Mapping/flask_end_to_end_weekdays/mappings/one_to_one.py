import random
print(random.randint(1,10000))

import sys
sys.exit(0)


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
USERNAME = "root"
PASSWORD = "root"
DB_NAME = "flaskdb"
PORT = 3306
HOST = "localhost"
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(USERNAME,PASSWORD,HOST,DB_NAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False      # dont showcase warning msgs
app.config['SQLALCHEMY_ECHO']=False      # print queries
db = SQLAlchemy(app)

#emp.adrref = adr           --> userlist-False
#emp.adrref = [adr1,adr2,adr3] --> uselist-True                 ---> database --> unique -True

class Employee(db.Model):               # emp cols --> 5 cols       --> emp python fields --> 6
    eid = db.Column("emp_id",db.Integer(),primary_key=True) #int
    name = db.Column("emp_name",db.String(100)) #str
    age = db.Column("emp_age", db.Integer())    #int
    email = db.Column("emp_email", db.String(100))  #str
    salary = db.Column("emp_sal", db.Float())   #float
    adrref = db.relationship("Address",uselist=False,backref="empref",lazy=False) #address     # unidrirlship-never adds column at db side

    def __str__(self):
        return f'''{self.name}, {self.email}, {self.adrref}'''

    def __repr__(self):
        return str(self)

#emp --> cols --> 5 colns           python fields -- 6

class Address(db.Model):    #Address(aid=1111,city='Pune',pincode=122334,state='MH',empid=)
    aid = db.Column("adr_id", db.Integer(), primary_key=True)
    city = db.Column("adr_city", db.String(100))
    pincode = db.Column("adr_pin", db.Integer())
    state = db.Column("adr_state", db.String(100))
    empid = db.Column("eid", db.ForeignKey("employee.emp_id"),unique=True,nullable=True)

    def __str__(self):
        return f'''{self.city}, {self.state}'''

    def __repr__(self):
        return str(self)
    #empref
#adr - 5 colns --> python fields --> 6

db.create_all()

'''
    fk == can be at any side --> fk --> unique - TRUE
    nullable --> depends --> tightly coupled -- False ---> loosly coupled pahije asel --> True
    
column_names --> database side conventions
    address --> python side -->            columns              
                    aid     --> int         adr_id
                    city        str         adr_city
                    state       str         adr_state
                    pincode     int         adr_pin   
                    empid       int         eid                     ---> fk -- > unique -True
    
    adr = Address()
    adr.aid/city/state/pincode/empid
    
    employee
                   eid      int     emp_id
                   name     str     emp_name
                   age      int     emp_age
                   email    str     emp_email
                   salary   float   emp_salary
    emp = Employee()
    emp.eid/name/age/email/salary
    
    
'''