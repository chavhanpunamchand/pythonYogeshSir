'''
Types of methods --> static  instance class
Types of variables  --> global local nonlocal instance class
Types of params --> positional named default *args **kwargs
Rules of Identifiers --> Naming conventions -->
Loopings --> if..else --switch* -->

'''

class Student:
    collegeName = "PICT"            #class variable
    deptList = ["IT","CSE"]
                                #18+ --> <25
    def __init__(self, sid, sname, sage, smarks,saddress):              #sid,sname,sage --> scope ?? -->local
        self.studId = sid  # instance variable
        self.studName = sname
        self.studAge = sage
        self.studMarks = smarks
        self.studAddress = saddress


    def assign_optional_subj(self,subjnm):    #specific obj work #type of the method ???     subj --> every student la assign-->
        self.optionalSubj = subjnm

    @classmethod                # factory method --> object generates -->
    def create_new_student(cls,sid, sname, sage, smarks,saddress):  #classname  ->Student       n define --???
            if sid<=0:
                print('Invalid Id')
            if (sage>=18 and sage<=25):
                return Student(sid, sname, sage, smarks,saddress)   #constructor--> #return ?? --> fun break --> caller -->value
            print('Invalid Student Property-->!')



    @staticmethod           # asa business --> common --> all objects -->
    def conduct_examination():      # s1,s2,s3 -->          # student ad -->    online --> clg-visit    -->android
        pass
                    #website -->app
                    #form --> android--> iphone -->website --> ??   --> input -->

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)


students = []
while True:
    sid = int(input('Enter Student Id '))
    age = int(input('Enter Student Age '))

    #m1 = int(input('Enter Student M1 -> '))
   # m2 = int(input('Enter Student M2-->'))
   # m3 = int(input('Enter Student M3 --> '))

    s1 = Student.create_new_student(sid=sid, sname='Mr XXX', sage=age, smarks=[55,66,77],saddress='Pune') #collegename - COEP   -->read/modify->s1 madhe ch
    if s1:   # s1--> object or none [age [18-25],id>0] --> none
        students.append(s1)
    else:
        print('Invalid student..! {},{}'.format(sid,age))

    choice = input('Do you want to continue --> Yes/No')
    if choice.lower() not in ["y","yes"]:
        break

    print('*'*40)

print('here is the list of students -',students)


import sys
sys.exit(0)
#Student.m1()
#Student.m2()


print('S1 -->',s1)
print('S2 -->',s2)
print('S3 -->',s3)
import sys
sys.exit(0)
s1.assign_optional_subj("Env")  #

print(s1)   # 5
print(s2)   #5
print(s3)   #5
s1.collegeName = "COEP"     #will be added inside s1--> --> will be added only for s1--
s1.studId = 222     #modified --> only for s1 --

print(s2.collegeName)   #do we have collegename inside s2 --> no --> class --> PICT
print(s1.collegeName)   #do we have collegename inside 1 -->Yes --> COEP

Student.collegeName = "VIT"     #Classname.property --> check property inside --> class madhe
                                                                                    #present -- modify
                                                                                    #absent --> add --> only inside class

print(Student.collegeName)      # VIT      #class-->read/write/modify
print(s1.collegeName)           #COEP       # own property -->
print(s2.collegeName)           #VIT    --> still its referring to class property -->read


import sys
sys.exit(0)


'''

                            how to write                                param                               syntax          
classmethod                 @classmethod                      first param --> reserved --> cls          @classmethod                                                calling
                                                                                                        def m1(cls):           cls->class name                      Classname.m1()                                       
                                                                                                          pass                                                       obj.m1() #can be called--> ideally u shud call it thru -->classname       
                                                                                                          
instancemethod              NA                               first param -->reserved --> self           def m1(self)            self --current object ref           obj = Class()
                                                                                                            pass                                                    obj.m1()

staticmethod                @staticmethod                   no param reserved                           @staticmethod
                                                                                                        def m1()            no ques                                 Classname.m1()
                                                                                                            pass                                                    obj.m1()    # 


#obj --> any method can be called -->           ob1  ob2  ob3 -->       ob2.m1()        --> class.m1()
#class --> can not be called instance method -->        class.instanceMethod()  --????

#class --> static or class method --> 
#obj  --> instance --> static/class [not recommanded]

                          @c
Classname.m1()     --> object --> m1(x) -->class method -->
                            #x --> classname
class -->    either class level define --> or using classname.variable -
instance --> using obj ref

class
    read        --> class.property      --> if property present inside class--> retrive
                                            if property is absent inside class --> error
    add/modify     classname.property=val --> if present inside class->modify
                                                            absent -->add
    
ref

    read            -- first check inside same ref--> present -->read
                                                      absent --> check inside class-->
                                                                            present -->read
                                                                            absent -->error
    add/modify      --> check inside same ref --> present -->modify
                                                absent --add --> in same ref--


                code reuse          encapsulated                        to write repeated steps
Function -->        Yes                 -                                   Yes
Methods -->         Yes                 Yes --> inside class                Yes

'''
class Student:
    collegeName = "PICT"  # college name same --> for every object      # how many times will get --> 1 --whenever class gets loaded --> when module get loaded --> 1

    #self-->reserved--implicit -->
    #self --> which object gets created--> memory --> memory --> ref --> self-->
    def __init__(self,sid,sname,sage,smarks,saddress):   # at the time object creation--> inside obj--> no of times u create
        self.studId = sid
        self.studName = sname
        self.studAge = sage
        self.studMarks = smarks
        self.studAddress=saddress

    @classmethod            #self -->classname --> classname.xyz = 100      --> if xyz present inside class--> xyz--modify
    def m1(self):           # where does this xyz will be added -- self -->cls -->  cls.xyz=100     --> cls.m1() ref.m1()
        self.xyz = 100      # where ?? obj --> whoever calls to this m1 --> will get this xyz property

    def m2(self):       # instance method --> self --> obj ref -->      ref.m2()
        self.pqr = 100

    @staticmethod
    def m3():       #m3(10) m3("A") -->cls.m3(0)        ref.m3()
        pass

s1 = Student(sid=101,sname='AAAA',sage=20,smarks=[55,66,77],saddress="Pune")    # init--self --s1
s2 = Student(sid=102,sname='BBAA',sage=22,smarks=[66,36,79],saddress="Pune")    #init -self ->s2

print('Student Class -->',Student.__dict__) # at class level

print('*'*40)
print('S1 -->',s1.__dict__)# s1 madhe
print('*'*40)
print('S2--->',s2.__dict__)#s2 -->
print('*'*40)

s2.m1() # self --> s2 --> s2.xyz = 100      # property --> @classmethod

print('*'*40)
print('S1 -->',s1.__dict__)# s1 madhe
print('*'*40)
print('S2--->',s2.__dict__)#s2 -->
print('*'*40)
print('Student Class -->',Student.__dict__) # at class level




import sys
sys.exit(0)






class X:

    @classmethod                   # first param--> reversed -->classname -->
    def m1(cls):               # m1 --> zero                       x--> current obj ref---> SELF
        print('inside m1',cls) # class -->X                     x --> current class name -->CLS

    @staticmethod
    def m2():               # no param reserved
        print('inside m2')

    def m3(self):       #instance -->self --> current obj ref --> --> first param reserved for obj ref
        print('inside m3')

    def m4(self):
        print('inside m4')


X.m1()  # --> first reserved --> implicit param --> type --> class-->

                                                                    #scope                  mem                                         no of times?
var1 = 10                                                             #global       -->     at the time of sample module loading        1
def fun():      #fun ---> 4x    -> left karel
    var2 = 20                                                         #local        --> when fun gets call                              depends no of time call

def fun():      #fun ---> 56x   --type--> function--> scope-->global --  at the time of sample module gets loaded
    var3= 30            #var3 -- fun --> int --> local to fun --> when fun gets call--> no of time--> no of times u call

def fun1():    #fun1 --> 73x
    var4 = 40

    def inner():                        #inner --> local inner --> fun1 --> fun1 calls --> no of times u call to fun1
        var5 = 50

class A:                        # class -->     A[var6,m1,m2,m3]
    var6 = 10

    def __init__(self):
        self.var7 = 70       # at the time of object creation
        A.var8 = 80
        var9 = 90


    def m1(self):               #m1 -->
        self.var7=70            # at the time of calling to m1-->
        A.var8=80
        var9=90

    def m2(self):
        self.var10 = 70
        A.var11 = 80
        var12 = 90

    def m3(self):
        self.var13 = 70
        A.var14 = 80
        var15 = 90

var16=160

a1 = A()
a2 = A()
a1.m1()
a2.m2()



