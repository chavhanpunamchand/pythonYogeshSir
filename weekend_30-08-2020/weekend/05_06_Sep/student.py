class Student:
    collegeName="PICT"
    deptList=["IT","CSE"]

    def __init__(self,sid,sname,sage,smarks,saddress):
        self.studId=sid
        self.studName=sname
        self.studAge=sage
        self.studMarks=smarks
        self.studAddress=saddress

    def assing_optional_subj(self,subjnm):
        self.optionalSubj=subjnm

    @classmethod
    def create_new_student(cls,sid,sname,sage,smarks,saddress):
        if sid<=0:
            print("Invalid ID")
        if (sage>=18 and sage<=25):
            return Student(sid,sname,sage,smarks,saddress)
        print('Invalid Student Property -------->!')

    @staticmethod
    def conduct_examination():
        pass

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)

students=[]
while True:
    sid=int(input("Enter Student ID :"))
    sage=int(input("Enter Student age:"))

    s1=Student.create_new_student(sid=sid,sname="Punamchand",sage=sage, smarks=[55,66,77],saddress="Mumbai")
    if s1:
        students.append(s1)
    else:
        print('Invalid student....!{},{}'.format(sid,sage))

    choice=input("Do you want to continue ----> Yes/No :")
    if choice.lower() not in ["y","yes"]:
        break




    print('*'*50)
print('List of students:',students)
