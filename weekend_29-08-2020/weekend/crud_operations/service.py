
#service --> ???        Bank -- Contract --> what services--->              HDFC SBI -->
from abc import ABC,abstractmethod

#abstraction --> showcase only essential details to enduser-- hide implementations- -> security --> business
        #laptop --> features --> ?
                #purpose -->games -- personal use --->

                #laptop --> what service -->

#what servies       # parent -- m1      --> child m1 --> child m1--overriden -- child parent inherit-- m1override
class StudentService(ABC):  #constract--> what services u are going to offer-->

    @abstractmethod
    def add_student(self):      #constract -->abstract - no body
        pass

    @abstractmethod
    def delete_student(self):
        pass

    @abstractmethod
    def update_student(self):
        pass

    @abstractmethod
    def fetch_single_student(self):
        pass

    @abstractmethod
    def fetch_all_students(self):
        pass

from Basics.weekend.crud_operations.student import Student

#implementation --> abstraction --> what services ???       --? how --> implementation --**
class StudentServiceImpl(StudentService):   #whatever contracts u have specificed inside--service---> implementatios-->impl
    studentList = []            # class variable    --???   Using class name

    #method --> type -- instance ---> StudentServiceImpl --> implement-->service la
    def add_student(self,stud):     #stud --param--> stud--? expected type --> Student type [id,nm,ag,]
        if type(stud)==Student:
            StudentServiceImpl.studentList.append(stud)
            print('Student Added Successfully...!')
        else:
            print('Invalid Student..!')


    def delete_student(self,sid):
        flag = False
        for stud in StudentServiceImpl.studentList:
            if stud.studId == sid:
                StudentServiceImpl.studentList.remove(stud)
                flag=True
                break   # once found-->dont check next students --> break loop

        if flag:
            print('Student Removed')
        else:
            print('Student Record Not Found..!')

    def update_student(self,sid,pstud):
        student = None          #none
        for stud in StudentServiceImpl.studentList:     #iterate stud list
            if stud.studId == sid:      # match -- id---sid
                student = stud
                break

        if student:
            student.studName = pstud.studName
            student.studAge = pstud.studAge
            student.studAddress = pstud.studAddress
            print('Student Information Updated...!')
        else:
            print('No record found..!')

    def fetch_single_student(self,sid):
        for stud in StudentServiceImpl.studentList:
            if stud.studId == sid:
                return stud



    def fetch_all_students(self):
        return StudentServiceImpl.studentList