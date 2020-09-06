
def no_of_times_inputs(n): # 3 --> 3
    print('\n\n') # first--->second
    n1 = int(input('Enter Number   : '))  # --> 0  --?     False --> None,False,Empty-- Zero
        #10
    if not n1: # value present --> true     -- 0 --- False --> 0 false-->  ! -->  true--> only zero asel tr
        cnt = 2
        for item in range(n-1):  # 3 times    # 3 times
            #print('Invalid Param,enter Again',n1) # invalid -- 0
            n1 = int(input('Enter Number   : '))  #    0
            if n1:  # 0 --> absent --> +ve/-ve --> present  # --> false
                return n1   # value present --> value
            else:
                cnt = cnt+1
    return n1
                                      #mul/div/add/sub        doub          incase invalid->any case
def take_input_from_user(choice):   # value -- n1,n2    --> value -- n1 --> value --False

    if choice == 3: #mul -> zero        # multiplication case --> both value zero --
                                            # num1 --> present --> num2 -->
        n1 = no_of_times_inputs(3)  # 5 times -->  --> value -- > None --> 5 times
        if n1:      # n1 present asel tr -->
            n2 = no_of_times_inputs(3)  # value -- > none       # total 6 times
            if n2:          #present
                return n1,n2        # return both values
            else:
                print('Invalid param 2 for -- Multiplication')

        print('Invalid param 1 for -- Multiplication')
        return False        #in case problem in any value--> false

    elif choice == 4:   #div-- second zero --no
        n1 = int(input('Enter Number-->1 : '))  # str
        n2 = take_input_from_user(5)
        if n2:
            return n1,n2
        return False
    elif choice == 5: # double
        n1 = int(input('Enter Number-->1 : '))  # str
        return n1

    n1 = int(input('Enter Number-->1 : '))  # str
    n2 = int(input('Enter Number 2  : '))  # str

    return n1,n2

def add(n1,n2):
    result = n1+n2
    return result

def sub(n1,n2):
    result = n1 - n2
    return result

def mul(n1,n2):
    result = n1 * n2
    return result

def div(n1,n2):
    result = n1 / n2
    return result

def doub(n1):
    result = n1*2
    return result


while True:
    print('''
            1. Addition
            2. Substraction
            3. Multiplication
            4. Division
            5. Doubles
    ''')

    choice = int(input('Enter Your Choice : '))  #3
     #

    operations = {
                3: mul,
                1: add,         # ref for addition function
                2: sub,         # sub function
                4: div,
                5: doub
    }

    ans = operations.get(choice)        # mul function ref
    if ans: # when it will be None --> jr key nasel ->  1-5 --> 0- >5 --> None

        userinput = take_input_from_user(choice)    #(n1,n2) (n1) False
        if userinput==False:        # invalid param
            print('Invalid Parameters') # function params are wrong
            continue
        elif userinput==int: # one value -->    #single -> double
            result = doub(userinput)
        else:
            result = ans(userinput[0],userinput[1])      #
        print('Result -->',result)
    else:
        print("Invalid Choice") # operation wrong

import sys
sys.exit(0)

if choice == 1:
   add(n1,n2)
elif choice == 2:
   sub(n1,n2)
elif choice == 3:
   mul(n1,n2)
elif choice == 4:
   div(n1,n2)
elif choice == 5:
   doub(n1,n2)




import sys
sys.exit(0)





class Student: # user defined structure --> i want student datatype for business-->
    def __init__(self,sid,snm,sag,smarks,sdept):
        self.studId = sid
        self.studName=snm
        self.studAge = sag
        self.studMarks = smarks
        self.studDept = sdept

    def __str__(self):
        return f'''
            Stud Id : {self.studId}
            Stud Age : {self.studAge}
            Stud Name : {self.studName}
            Stud Marks : {self.studMarks}
            Stud Dept : {self.studDept}
        '''

    def __repr__(self):
        return str(self)


    def __eq__(self, other):
        return self.studId == other.studId

s1 = Student(sid=101,snm='AAA',sag=20,smarks={"phy":40,"chem":80,"math":79},sdept="IT") # 200
s2 = Student(sid=102,snm='BBB',sag=22,smarks={"phy":50,"chem":80,"math":70},sdept="IT") # 200
s3 = Student(sid=103,snm='CCC',sag=23,smarks={"phy":40,"chem":80,"math":80},sdept="IT") # 200
                     # t1   t2
                        #{"A":160,B:170,C:170} ---> 160,170,170 --> 170,170,160 ---> [0][1] --> wont work
                                                                #-->200 170 170 -->  will work --
#first two topper -->

collegeStudents = [s1,s2,s3]
def total_marks(marks):     # to retrive total marks
    phy = marks.get('phy')
    chem = marks.get('chem')
    math = marks.get('math')
    result = phy+chem+math
    return result

def get_topper():
    batch = {}  #dict -->   {"A":170,"B":170,"C":180}
    for stud in collegeStudents:
        sum = total_marks(stud.studMarks) # 1 stud total marks
        batch[stud.studName] = sum

    #batch --> A:160 B:170 C:170        --> topper1 -->2 -->topper:1
    #batch --> first ranker and second ranker
              #1 - M         -  0-1-m
            #{A:160,B:170,C:180,D:140,E 170}  -->
    allmarks = batch.values()           # 160 170 180 140 170,180
    allmarks = set(allmarks)            #160 170 180 140    --> unique      -->
    allmarks = list(allmarks)           #[160 170 180 140 170 180]      #[160 170 180 140]
    allmarks.sort()                     #[140 160, 170 170 180 180 ]     [140 160 170 180]
    allmarks.reverse()                  #[180 180 170 170 160 140]       [180 170 160 140] --> [0] [1]

    topperm1 = allmarks[0]              #180 ---> topper
    if len(allmarks)>=2:
        topperm2 = allmarks[1]              #180

    for name,marks in batch.items():        #dict--> 180 -- first topper --> 180 -- second topper
        if marks== topperm1:
            print("First Ranker -->",name)
        elif len(allmarks)>=2 and marks == topperm2:
            print("Second Ranker -->", name)

    '''
    toppermarks = 0
    toppername =None
    for key,val in batch.items():
        if toppermarks<val:
            toppername=key
            toppermarks = val
    print(toppername,toppermarks)
'''



get_topper()






import sys
sys.exit(0)



collegeStudents = [s1,s2,s3]
# first question --> can u tell me the topper --> input- -> topper name
# sum marks -->  --> bank --> 10k -> deposit -> trasnc -->??
def total_marks(marks):  #function --> marks --> total      --> {"phy":10,"chem":20,"math":30}
    phy = marks.get('phy')
    chem = marks.get('chem')
    math = marks.get('math')    #developer --***
    result = phy+chem+math
    return result  # 60
                        #A --> [10,20,30]       #B --> [10,20,30]   #C --> [10,20,30] D[10,20,50]E[10,20,50]      --> A:60 B:60 C:60
def get_topper():       #171 171 --> 2 --> group of elements
    topper = None  #none    A       D
    temp = 0        #0  --> 60  --> 80
    studs = [] #empty   [(B,60),(C,60)] []  [(E,80)]
    for stud in collegeStudents:  #          E
        totalmarks = total_marks(stud.studMarks)  # totalmarks --> 80
        if temp<totalmarks:  #80<80-->False
            temp = totalmarks
            topper = stud.studName  #D
            studs.clear()  #prev clear --> marks less
        elif temp==totalmarks:  # in case more than one students --> same
            studs.append((stud.studName,totalmarks)) #s3 --->171
    studs.append((topper,temp))

    print('Topper -->',studs)

#topper --> return ??
#ans = get_topper()  #None
#print('Topper is -->',ans)

get_topper()

import sys
sys.exit(0)


#return --> returns value to the caller --> any datatype value
#function with pass or without return --> returns nothing-- None

def m1(num1,num2):      # function with body --[business logic] --> returns nothing
    result = num1 + num2
    print(result)

def m2(num1,num2):  # function with body -->[business logic] -> return int,float,str
    result = num1 + num2
    print(result)
    return result       # output of this function is required for another function/outside

ans = m1(10,20) # None
ans = m2("A","B") # AB --> str
ans = m2(10,20) # 30 -> int
ans = m2(10.3,20)# 30.3 --> float

#agr --> student


def m1():           # m1--> body --> returns nothing--> None
    print('Inside m1')

def m2():       # m2 -- with no body --> return None
    pass

def m3():       #m3 --> body --> return 10 -- int type data
    return 10


m1()
m2()
m3()



if m1():
    print('inside if')
elif m2():
    print('inside elif--1')






while True:
    age = int(input('Enter Your Age'))       #str
    print('You Entered --> ',age)

    if age<=10 and age>0:
        print('Kid')
    elif age<=20:
        print('Student')
    elif age<=50:
        print('Employee')
    else:
        print('Invalid Age')

import sys
sys.exit(0)





#8.30 -->           8.20-->8.35 -->timeframe


#condition --> false --> None,0,False,empty
#condition --> true--> datapresent - "",10,2003.34,True

val1 = [()]   #empty
val2 = False
val3 = None
val4 = ""
val5 = "A"
val6 = 10.23

#max --> 1 loop body  --> start checking from -->till -> true found --> true-->
                        #--> else

if val1:        #val1 --> single value --> non-empty
    print('Inside if')
elif val2: #value present or not --> True
    print('Inside elif-1')
elif val3:
    print('Inside elif-2')
elif val4:
    print('Inside elif-3')
elif val5:
    print('Inside elif-4')
elif val6:
    print('Inside elif-5')
else:
    print('inside else')
