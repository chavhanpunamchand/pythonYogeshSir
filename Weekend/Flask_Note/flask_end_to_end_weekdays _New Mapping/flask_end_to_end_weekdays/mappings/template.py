from flask_end_to_end_weekdays.mappings.orm_config import db

class Employee(db.Model):
    eid = db.Column("emp_id",db.Integer(),primary_key=True)
    name = db.Column("emp_name",db.String(100))
    age = db.Column("emp_age", db.Integer())
    email = db.Column("emp_email", db.String(100))
    salary = db.Column("emp_sal", db.Float())

class Address(db.Model):
    aid = db.Column("adr_id", db.Integer(), primary_key=True)
    city = db.Column("adr_city", db.String(100))
    pincode = db.Column("adr_pin", db.Integer())
    state = db.Column("adr_state", db.String(100))



db.create_all()