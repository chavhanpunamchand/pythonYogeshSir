from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format('root','root','localhost','flaskdb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
                                                                               # F   F
#mapping --> many to many -->           eid name age   aid         aid city     aid eid

#transcational data --> updated --> created -->
stud_subj = db.Table('stud_subj',
    db.Column('stud_id', db.ForeignKey('student.stud_id'), primary_key=True),
    db.Column('subj_id', db.ForeignKey('subject.subj_id'), primary_key=True)
)

class College(db.Model):
    id = db.Column('college_id',db.Integer(),primary_key=True)
    name = db.Column('college_name',db.String(30))
    adrid = db.Column("adr_id",db.ForeignKey("address.adr_id"),unique=True,nullable=False)
    depts = db.relationship("Dept", uselist=True, backref="collref", lazy=True)


class Student(db.Model):
    id = db.Column('stud_id',db.Integer(),primary_key=True)
    name = db.Column('stud_name',db.String(30))
    #age = db.Column('stud_age',db.Integer(),default=20)
    deptid = db.Column("dept_id", db.ForeignKey("dept.dept_id"), unique=False, nullable=True)

class Subject(db.Model):
    id = db.Column('subj_id',db.Integer(),primary_key=True)
    name = db.Column('subj_name',db.String(30))
    studs = db.relationship('Student', secondary=stud_subj, backref=db.backref('subjs', lazy=True))

#studs --> list of students --> append[student] or extend[list of students]
class Address(db.Model):
    id = db.Column('adr_id',db.Integer(),primary_key=True)
    city = db.Column('adr_city',db.String(30))
    college = db.relationship(College,uselist=False,backref="adrref",lazy=True)

class Dept(db.Model):
    id = db.Column('dept_id',db.Integer(),primary_key=True)
    name = db.Column('dept_name',db.String(30))
    students = db.relationship(Student,uselist=True,backref="deptref",lazy=True)
    cid = db.Column("collge_id", db.ForeignKey("college.college_id"), unique=False, nullable=True)



if __name__ == '__main__':
    db.create_all()