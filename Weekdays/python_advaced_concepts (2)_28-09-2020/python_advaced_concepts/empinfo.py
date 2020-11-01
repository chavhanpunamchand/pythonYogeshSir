




# use case --> file --> log file --> text --> 1000 --> screen --> 10 lines at
# gallary --> 10k pics-->
            #user defined instance --> iteratble
                    #class -->  iter next --> --> pre--> next -->
            # complex types -- str -->

#application --> website --> iPhone -- Android --> TV ?? --> laptop --> screensize-->
#iterable --> iter and next -->


# what steps we need to follow to make specific as an iterable -->  iter    next    -->

class Employee:

    def __init__(self,eid,enm,eag,address,des):
        self.empId = eid
        self.empName = enm
        self.empAge = eag
        self.empAddress=address
        self.empDesignation=des


    def __str__(self):
        return f'''\n [{self.empId}{self.empName}{self.empAge}{self.empAddress}{self.empDesignation}]'''

    def __repr__(self):
        return str(self)


    def __iter__(self):     # conversion --> self--> instance pairs--> list madhe
        Employee.values = list(self.__dict__.items())     # key value pairs --> Class level variable -> values --> pair-->5 pair
        Employee.count = 0
        return self         # emp instance returning

    def __next__(self):
        if Employee.count>=5:
            raise StopIteration("All Emp Pairs are consumed..!")
        else:
            val = Employee.values[Employee.count] # first pair -0   --> exception ?? --> 0-4
            Employee.count= Employee.count + 1      # count-- 1
            return val

e1 = Employee(101,"Mr.AAA",23,"Pune",['LEAD','PROJ MANAGER'])   # e1 --> i want to make it iterable-*
#e1 = e1.__iter__()
#print(next(e1))    #    first pair->
#print(next(e1))     # second pair -->

for no,pair in enumerate(e1):
    print(no,pair)



#list of emps -->  single emp fields la --*


import sys
sys.exit(0)
'''
# complex [set list tuple dict ] str range(10)(python3) x_range(2)(python2) --> iterable types
values = [10,20,30,40,50]
for item in values:
    print(item)

for item in range(10):
    print(item)

'''
e1 = Employee(101,"Mr.AAA",23,"Pune",['LEAD','PROJ MANAGER'])   # e1 --> i want to make it iterable-*

for item in e1: # e1 instance --> not an iterable --> ?? No -->
    print(item)



import sys
sys.exit(0)

class InvalidEmpAge(BaseException):

    def __init__(self,msg):
        self.errormsg = msg



class Employee:

    def __init__(self,eid,enm,eag):
        self.empId = eid
        self.empName = enm
        self.set_age(eag)  # setter call

    def set_age(self,ag):       # setter --> setter
        if ag<18 or ag>58:
           raise InvalidEmpAge("Emp Age should be in between 18-58")    #exception throw--> condition --> caller
        else:
            self._empAge = ag          # no direct access to empAge -->

    def get_age(self):          #getter
        return self._empAge

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''{self.__dict__}'''

    empAge = property(get_age,set_age)  # empAge --> field--set --> setter function --> get-- getter function


e1 = Employee(101,"AAA",22) # can we set wrong value--> No  --> --. constructor calls to setter -- business logic
print(e1)  # 23

e1.set_age(26)  # set ?? -- Yes # here also logic will be called

print(e1)   # 45 --

e1.empAge=27  # does setter will be called ?? -- No     --> interanlly - value set operation -- setter

print(e1)

import sys
sys.exit(0)

         #-20 -- numeric value -->
# age --> 20 --> valid or invalid -??    college
# age -- 5  --> valid or invalid        --> kids


#business requirement --> emp--> <18 --> >58    --> 18 - 58 -- client requirement- business req

class InvalidEmpAge(BaseException):

    def __init__(self,msg):
        self.errormsg = msg



class Employee:

    def __init__(self,eid:int,enm:str,eag:int):     # eid-int -->enm -->str -->eag:int  # after obj creation
        self.empId = eid
        self.empName = enm
        if eag<18 or eag>58:
           raise InvalidEmpAge("Emp Age should be in between 18-58")    #exception throw--> condition --> caller
        else:
            self.empAge = eag

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''Emp Id : {self.empId},Emp Name : {self.empName}, Emp Age : {self.empAge}'''

e1  = None
try:
    eag = int(input('Enter Age'))       #       # 1 ka ch thikani
    e1 = Employee(101,"Mr. AAAAA", eag) # class
    print(e1)
except InvalidEmpAge as ag:
    print(ag.errormsg)

    # does constructor-called- -> business fail ??
e1.empAge = 10      # problem -->  constructor calling la --> proper value pass--> obj created then --> wrong value set

print(e1)   # age-10