#pass  -->  system.exit(0)  +ve[forceful]  -ve[abnormal termination]  0 [normal termination]

def m1():
    pass

print('hello')
m1()

import sys
sys.exit(0) # stops execution here











#init   -   --> no return --> implicitily returns = current object ref
#str ---> shud be string
#repr --> shud be string -->
'''

continue --> for/while --> current loop chya current iteration la -- next iteration execution --Yes --> first loop required
break --> for/while ---> current loop chya iteration stop+ next iteration cannot be executed--> directly outside-->
                        only current loop chya---> current loop la exit --> first loop required
return ---> function/method-> -- first function/methods --> if condition is matching--> directly--> exit--execution
        control--> caller --> all loops --> one go break --> caller -> can handover the value-->
            ---> None --- or any other value-->

pass
exit
        #exception handling
try
except
else
finally

'''
#user input --> 3 --> 10 numbers -->
import time
import random
def get_random_value_divisiable_by(noof,num):
    values = []
    while True:
        #no = int(input('Enter Number : '))
        no = random.randint(1,1000)
        print('Generated No {} '.format(no))
        time.sleep(1)
        if no>0 and no%num==0:
            values.append(no)
            print('Till Values -->', values)

        if len(values)==noof:
            return values[6]





values =  get_random_value_divisiable_by(10,5)
print(values)

import sys
sys.exit(0)
'''

for item in range():                    for (int i=0;i<5;i++)      (ini ; condition  ; incrm.decr)
    pass

Loopings -->
        selective
                --> if..else            -->     any one --> not more than that -->
                        # boolean False --> 0   ---> None ---> EmptyComplex Types

            if there are multiple conditions --> ifelse--> performance-->slow


                --> switch *** --> Not provided in python -->




        Iterative
                --> for
                -->while
                --> do..while

        Transfer
                -- break
                -->continue
                -->return
                -->pass
                -->system.exit
                -->raise
                -->

if                                  if condition : body
if..else                            if condiction : body else: body
if..elif                            if condiction : body elif condition: body
if..elif..elif.....*
if..elif..else
if..elif..elif..* else

if --word --> condition -->
else--> always at last- -> default -->


condition --> at the last -- boolean type -->
                #False -->          false   --      0           -- empty complex type       -> none
num = 0                                                             [],{},set(),()
                                                                    [0] --> 1
if false:             #10 -->  present - > absent -->
    pass






if condition:
    body
elif condition:
    body
elif condition:
    body
else:
    body


if..else
for --> when you are sure about no of iteration in advance
while --> if you are sure about no of iterations --> first condition then body --> may or may not be body execution
do..while --> first body then condition --> atleast once--body will surely gets executed

trasnfer statement -->
                break ->  looping --.max current loop la break--exit --> current loop and next iterations
                continue --looping --> max current iteration la continue --> current iteration only
                return -->function/methods          -->




for item in range(10):
    if item==2:
        break

#return --> return --> caller ????? ----> function /methods
'''

def m1():
    for outer in range(5):      #rows      continue --> 01234                   break -- 0 1 2 3 4          return 0
        for item in range(5):   #colns     inner   0134 0134 0134 - 0123                01 01 01 - 01           01 --> directly to caller
            if outer==3 or item == 2:   #0:0    0:1     0:2
                return outer,item
            print(outer,item,end='\t\t')
        print()

a = m1()    #--? tuple --> (0,2)
import sys
sys.exit(0)
 # whatever input-  --> string -->      # xrange --> deprecated --in python3 -- existing + range() --> backword compitablity

val = list(range(10))

for index,item in enumerate("abcd"):
    print(index,item)

import sys
sys.exit(0)

print(val)

# --> for --> list of elements -->
for item in [10, 203, 203, 405, 606]:  # start iteration from 0th index-->till index  is 9
    print(item)


class Student:

    def __init__(self, sid, sname, sage, smarks,saddress):  # nothing-->    implicitily --> initialized obj ref return
        self.studId = sid
        self.studName = sname
        self.studAge = sage
        self.studMarks = smarks
        self.studAddress = saddress
        #return 10           # this is not going to work here --> implicit return asto --> current object ref..

    def __str__(self):              # return value --????   --> always returns --> string --> string
        return f'''{self.__dict__}'''

    def __repr__(self):         #  string --> str--string--repr-->string--??
        return str(self)



import random

students = []

def add_new_student():      # nothing
    studid = int(input('Enter Student Id : '))
    studNm = input('Enter Student Name :')
    students.append(Student(sid=studid, sname=studNm, sage=random.randint(18,25), smarks=[random.randint(1,100),random.randint(1,100),random.randint(1,100)],saddress='Pune')) # calling to constructor -->)
    return "Student Added Successfully...!"


def get_student():      # caller --> student -->
    sid = int(input('Enter Student For Fetch --> Id : '))   #2
    for stud in students:       # iterative     [s1[id-1,nm],s2[id-2,nm],s3[id-3,nm]]
        if stud.studId == sid:
            return stud                 #student --> id nm age mark-->      # for--break- --> function -->break

    return "Student Not Present with given Id..!"   #

def delete_student():
    sid = int(input('Enter Student Id for Delete : '))

    for stud in students:
        if stud.studId ==sid:
            students.remove(stud)
            return "Student removed successfully...!"

    return "Student not found so cannot remove..!"


def update_student():
    sid = int(input('Enter student Id : '))

    for stud in students:
        if stud.studId == sid:
            name  = input('Enter name : ')
            age = int(input('Enter Age'))
            stud.studName = name
            stud.studAge = age
            return "Student Record Updated...!"

    return "Invalid Id --cannot update"



def get_all_students():
    if students:
        return students     #if not empty...!
    else:
        return "No records...!"


#s1  = Student(sid=111, sname='XXXX', sage=23, smarks=45,saddress='Pune') # calling to constructor -->

#flag = True
while True:
    print('''
            1. Add Student 
            2. Update Student
            3. Delete Student
            4. Get Single Student
            5. Get All Students
    ''')

    choice = int(input('Enter Your Choice : '))     # 55

    operations =   {
                    1:add_new_student,
                    2:update_student,
                    3:delete_student,
                    4:get_student,
                    5:get_all_students
    }
    funref = operations.get(choice)      # 1--> getallref-->        1-->add_new_student
    if funref:
        val = funref()
        print(val)
    else:
        print('Invalid Choice...!')

    ch = input('Do you want to continue --> Yes/No  :  ')
    if ch.lower() not in ["y","yes"]:
        break

    print('----------------------------------------------')

import sys
sys.exit(0)

#replace such kind of conditions--> thru switch
if choice==1:                   # 1sec
    add_new_student()
elif choice==2:
    update_student()
elif choice==3:
    delete_student()
elif choice==4:
    get_student()
elif choice==5:                 # body ...*
    get_all_students()
else:
    print('Invalid Choice...!')



import sys
sys.exit(0)




import sys
sys.exit(0)



def m1(self):       # nothing --??? -->        no       --   return      [none]        return val
    pass            #none
    #return              #none
    #return val          #specific value


s1  = Student(sid=111, sname='XXXX', sage=23, smarks=45,saddress='Pune') # calling to constructor -->
#current memory -- initialization --
a = s1.m1() #none -->???

#s1 -- shud be none --??

def m1():       # 10 --> int
    return 10


def m2():       # int -->whatever returned from m1 --> will be returned
    return m1()

import sys
sys.exit(0)

def m1():               # returns ??? --------> No ---> None
    return 0            # 0


num = [0,False]                       # -- false --> None --> 0 --> emptyComplexTypes--False

if num[1]:      #else---> num[1] -- False       # step by step - checking
    print('inside if')
else:
    print('else')

values = [1,2,3,4,5,6,7,8]

if values[0]==10:           # condition --> as long as satisfy --> body ?? -> whichever match found --> else--> default
    print('if')
elif values[1]==10:
    pass







import sys
sys.exit(0)



for item in range(3):  #0----> 9
    val = int(input('Enter Value : '))
    if val%2==0:
        print('Even No',val)
    else:
        print('Odd Number',val)

import sys
sys.exit(0)

