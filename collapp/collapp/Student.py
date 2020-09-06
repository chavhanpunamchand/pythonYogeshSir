'''
__init__ --> constructor --> to initialize object properties

'''
#one class --> can have n instances/objects
#n instance--> 10 common properties--> write down constructore-- define 10 props and init

class Student:

    def __init__(self,sid,snm,sag,semail): # these props will be avaiable for all objects of this class
        self.studId = sid
        self.studName = snm
        self.studAge = sag
        self.studEmail = semail

s11 = Student(101,"ABCD",20,"abc@gmail.com") # memory --> s1     --> lines of code
s12 = Student(121,"XABCD",23,"abc@gmail.com")# object--> creation--> constructor calling--> constructor-- props ini


print(s11)
print(s12)


class Stud:
    pass

s2 = Stud()     # bydefault python adds init -->  no params #--mem-- s2
s2.name = "PQRS"
s2.id = 10
s2.email = "pqrs@gmail.com"
s2.age = 30

s22 = Stud()
s22.namee = "ABCD"



class StudentInfo:

    def m1(self, sid, snm, sag, semail):  # these props will be avaiable for all objects of this class
        self.studId = sid
        self.studName = snm
        self.studAge = sag
        self.studEmail = semail

s1 = StudentInfo()  #there is default constructor   --> initialization part-->
s1.m1(10,"ABC",29,"ABC@gmail.com") # one line--> extra-->

s11 = StudentInfo()  #there is default constructor   --> initialization part-->



