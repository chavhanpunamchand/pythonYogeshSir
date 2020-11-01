from itertools import cycle,count,repeat
from itertools import accumulate,chain,compress,dropwhile,filterfalse,islice,starmap,groupby,takewhile
import random
from operator import add,mul,sub,floordiv,pow   # lambda - anonymous -->fun


values = [random.randint(1,25) for item in range(10)]
print(values)
ans = list(takewhile(lambda x : x%3==1,values)) # collect til the time--> first false found
print(ans)                                      #dropwhile --> dont collect till the first false found

import sys
sys.exit(0)
class Emp:

    def __init__(self,eid,enm,esal,erol):
        self.empId = eid
        self.empname = enm
        self.empSal  =esal
        self.empRole = erol

    def __str__(self):
        return f'''\n Emp Id : {self.empId}, Emp Name : {self.empname}, Emp Salary : {self.empSal},   Emp Role : {self.empRole}'''

    def __repr__(self):
        return str(self)


ROLES = ["SSE","MANGER","LEAD","Sr.Manager","BA"]
def get_dummy_emps(n=10):  # create n random employees
    emplist = []
    for item in range(n):
        emplist.append(Emp(random.randint(1,100),"AAA{}".format(random.randint(1,100)),round(random.randint(3000,10000),2),ROLES[random.randint(0,4)]))
    return emplist

emplist = get_dummy_emps(5) #  # called here --> to get list of emps

print(emplist)
emplist.sort(key=lambda emp:emp.empRole)

print(emplist)

result = groupby(emplist,lambda emp:emp.empRole)

print('-----------------------------')
for key,grp in result:
    print(key +" \t :", list(grp))
    print('\n')


result.get("Manager")   # all mangaer -- iterable--*
result.get("SSE")   # all mangaer -- iterable--*



import sys
sys.exit(0)

#L = [("a", 1), ("a", 2), ("b", 3), ("b", 4)]

# Key function
#key_func = lambda x: x[0]

#for key, group in groupby(L, key_func):
#    print(key + " :", list(group))


values = [(chr(random.randint(65,70)),random.randint(1,100) )for item in range(10)]

values.sort(key=lambda x: x[0]) # sorting based on first param

#ans = groupby(values,lambda x: x[0])
fun = lambda x: x[0]
for key, group in groupby(values,fun):
    print(key + " :", list(group))


#note --> group by -- first sort by key --> and the apply
#print('Result -->',finalgroups)

#print(values)
import sys
sys.exit(0)

#map reduce filter ---> lambda ->

values = [random.randint(1,25) for item in range(10)]
values1 = [(random.randint(1,25),random.randint(1,25),random.randint(1,25),index) for index,item in enumerate(range(10))] #[(0,22),(1,23)

#finalans = starmap(lambda a,x,y,z : a+x+y+z,values1) # python itself-->

#finalans = starmap(lambda x,y : x+y,values1) # python itself-->
#finalans = list(map(lambda x : x[0]*x[1],values1)) --> unpickling--> dev la
#print(list(finalans))

print(values1)

import sys
sys.exit(0)

finalans = list(map(lambda x : x*2,values))

print(values)
print(finalans)
import sys
sys.exit(0)



class Emp:

    def __init__(self,eid,enm,esal,erol):
        self.empId = eid
        self.empname = enm
        self.empSal  =esal
        self.empRole = erol

    def __str__(self):
        return f'''\n Emp Id : {self.empId}, Emp Name : {self.empname}, Emp Salary : {self.empSal},   Emp Role : {self.empRole}'''

    def __repr__(self):
        return str(self)

ROLES = ["SSE","MANGER","LEAD","Sr.Manager","BA"]
def get_dummy_emps(n=10):  # create n random employees
    emplist = []
    for item in range(n):
        emplist.append(Emp(random.randint(1,100),"AAA{}".format(random.randint(1,100)),round(random.randint(3000,10000),2),ROLES[random.randint(0,4)]))
    return emplist

emplist = get_dummy_emps(10) #  # called here --> to get list of emps

#byte short int long float double -->
# 1   2      4    8      4    8

#f f --> f
#i +f --> f
#f + i --> f
#i + i --> i
#cp*i*f --> cp
def total_sal():        # val1 op val2 ---> ans type -->whichever type is higher ->
    sum = 0.0
    for emp in emplist:
        sum = emp.empSal+sum
    print('Normal Fun-->',sum)

from functools import reduce

totalsal = reduce(lambda emp1,emp2: emp1.empSal+emp2.empSal if type(emp1)==Emp else emp1+emp2.empSal ,emplist,0.0)
print(totalsal)#
            #[e1,e2,e3,e4,e5]       --> e1,e2   --> e1.sal+e2.sal --> float,e3
total_sal()




#lambda -->     map                 filter                  reduce
            #map --> process each and every element and return all --> 10 --> 10
            #map(fun(p1),iterable)
            #filter(condtionalfunction(p1),iterable) --? visit all elements -- but -- collect only condition satisfied
                                # 10 -->0,10,0-10
            #reduce --> reduce(fun(p1,p2) --> logic--)  --> accumulate--> will return ans


#map --> filter --> reduce -->

#from functools import reduce

#values = [random.randint(1,10) for item in range(5)]
#print(values)
#ans = reduce(lambda x,y : x+y,values,initial=2) #  1 4 5 6 7
                                # 1,4 --> 5,5 -->10,6---> 16+7 --> 23 last ans*
#print(ans)
#aand = accumulate(values,lambda x,y : x+y)
#print(list(aand))
import sys
sys.exit(0)

#filter --> 10 --> 3 pune -->
        #10 --> 3-increment -->
        #filter --map ---> output -- kami --> process
        #map  - filter -- process -- and kami -- >



#lambda --> normal function without name-- shud be written in one line
            #lambda : 10                                    # def m1: return 10
            #lambda : None                                   # def m1()  :
            #lambda x : x                                    # def m1(x) : return x
            #lambda x,y,z : x+y+z                            #def m1(x,y,z): return x+y+z
            #lambda x,y : x+y if x<10 else x-y               #def m1(x,y):
                                                                    #if x<10 : return x+ y
                                                                    #else return x-y

            #lambda x,y,z : x+y if x<10 else (z- y if y<z else z)
                                                             # def m1(x,y,z,):
                                                                    #if x<10: return x+y
                            #                                        else :
                            #                                               if(y<z):return z-y
                                                                            #else: return z
#map filter reduce
#map --> if u want to process each and every element from given iterable-->map
        # 10 elements --> after processing --> 10 elements
#filter --> based on certain condition data--> filter out --> condition - predicate--*
        #10 elements --> condition  --> 0, 0-10, 10 --< based on condition

#reduce -->*




class Emp:

    def __init__(self,eid,enm,esal,erol):
        self.empId = eid
        self.empname = enm
        self.empSal  =esal
        self.empRole = erol

    def __str__(self):
        return f'''\n Emp Id : {self.empId}, Emp Name : {self.empname}, Emp Salary : {self.empSal},   Emp Role : {self.empRole}'''

    def __repr__(self):
        return str(self)

ROLES = ["SSE","MANGER","LEAD","Sr.Manager","BA"]
def get_dummy_emps(n=10):  # create n random employees
    emplist = []
    for item in range(n):
        emplist.append(Emp(random.randint(1,100),"AAA{}".format(random.randint(1,100)),round(random.randint(3000,10000),2),ROLES[random.randint(0,4)]))
    return emplist

emplist = get_dummy_emps(10) #  # called here --> to get list of emps


emplist.append(Emp(73,"YYYY{}".format(random.randint(1,100)),45464,ROLES[random.randint(0,4)]))
print('Original -->',emplist)
#problem stmt --> 1
# salary increment --> jr tyacha
# id < 50 --> 10%           -->
# 50-70  --> 5%     # --> 1-70  -->
# after increment --> i want to find --> 3 max salary whose role in manager --> emps  --> 3 emps.salaries


def proces_emp(emp):
    if emp.empId<50:
        emp.empSal= emp.empSal*1.10
    elif emp.empId<70:
        emp.empSal= emp.empSal*1.05

    return emp  # increment salary --> [emp[id,nam,sal],emp,emp,emp]


                #[salaries-->??]

#map(lambda emp : emp.empSal*1.10 if emp.empId<50 else (emp.empSal*1.05 if emp.empId<70 else emp.empSal))

postincrement = list(map(lambda emp : proces_emp(emp) if emp.empId<50 else (proces_emp(emp) if emp.empId<70 else proces_emp(emp)),emplist))

print(postincrement)
#sort it by empsalary --> desc--> pick last 3
def incr_sal(emp):
    return emp.empSal

postincrement.sort(key= lambda emp:emp.empSal,reverse=True)# --??
#postincrement.sort(key= incr_sal,reverse=True)# --?? desc-->

print(postincrement[0:3])




#print(emplist)



import sys
sys.exit(0)


def proces_emp(item):
    if item.empId<50:
        item.empSal = item.empSal*1.10
    return item

print("Before processed --> \n",emplist)
postinc = list(map(lambda emp: proces_emp(emp),emplist))
print("After Processed processed --> \n",postinc)

import sys
sys.exit(0)

#filter -- iterable --> 50  --> [only true wale] --> 0, 0-50, 50
#map -- iterable    --> 50  --> 50
#<50--id -->

#empsalary - empid -- >50       --> filter ---> <50 --> then =process --> result --> tech emp-- <50
#empsalary - empid -- >50       --> map ---> <50 --> then =process --> result --> tech emp-- <50

#empsalary - empid -- >50       --> filter -- map -->
#empsalary - empid -- >50       --> filter -- map -->
#empsalary - empid -- >50       --> filter -- map -->
#empsalary - empid -- >50       --> filter -- map -->


import sys
sys.exit(0)







#filterfalse -- collect -- je false
#filter --> je true --> 

# lambdas [anonymous function -- single line] --> map(fun,iterable)  filter  reduce
                                                    #PIC ONE ELEMENT-- PASS IT FUNCTION -- PROCESS -- COLLECT THE RESULT
    #10 ---> 10 -- 2
values = [random.randint(25000,50000) for item in range(10)] #10 candiates -- marks

def myfun(x):
    return x>37000      # True- - False

#ans = list(filter(myfun,values)) #using -- normal function
ans1 = list(filter(lambda x : x>=37000,values))# using lambda function
ans2 = list(filterfalse(lambda x : x>37000,values))

print(values)
print(ans1)# all salaries >=37k --
print(ans2)# # all salaryries<37k

import sys
sys.exit(0)




ans = list(map(lambda item : {"actual": item ,"increment":round(item*1.05,2),"perc":round(item*0.05)} if item<30000 else {"actual": item ,"increment":item,"perc":0},values))

print('After Increment ..')
for item in ans:
    print(item)

import sys
sys.exit(0)


print('Actual Salaries -->',values)
                                # lambda item : {"actual": item ,"increment":round(item*1.05,2),"perc":round(item*0.05)} if item<30000 else {"actual": item ,"increment":item,"perc":0}
def apply_increment(values):    # lambda item : item*1.05 if item<30000 else item
    incremented_salary = []
    for item in values:
        if item<30000:
            incremented_salary.append({"actual": item ,"increment":round(item*1.05,2),"perc":round(item*0.05)})
        else:
            incremented_salary.append({"actual": item ,"increment":item,"perc":0})

    return incremented_salary


for item in apply_increment(values):
    print(item)

import sys
sys.exit(0)



print('Actual Salaries -->',values)
result = list(map(lambda item : item*1.05 if item<30000 else item,values))
print(result)

import sys
sys.exit(0)

print('Actual Salaries -->',values)

def apply_increment(values):    # lambda item : item*1.05 if item<30000 else item
    incremented_salary = []
    for item in values:
        if item<30000:
            incremented_salary.append({"actual": item ,"increment":item*1.05,"perc":item*0.05})
        else:
            incremented_salary.append({"actual": item ,"increment":item,"perc":0})

    return incremented_salary

print('POST Increment Salaries -->',apply_increment(values))

import sys
sys.exit(0)

ans = sum(values) # in build function -->   # 25 -> fail    --> 35 : 40-- pass  37:42 -- pass 40:

import sys
sys.exit(0)

def calculations(n1,n2,n3): #normal function
    if n1>n2 and n1>n3:
        return n1
    elif n2>n3:
        return n2
    return n3
#a = calculations        # ref of cal function
ans = calculations(10,23,4) #calling to function
print('NormalFunction -',ans)
#lambda n1,n2 :  x*10 if x<2 else (x**2 if x<4 else x+10)
funref = lambda n1,n2,n3: n1 if n1>n2 and n1>n3 else (n2 if n2>n3 else n3)  #diff--> perfm
print('lambdaFunction -',funref(10,23,4))

import sys
sys.exit(0)

funref = lambda n1,n2,n3: n1+n2+n3
print(funref)   # ref to anonymous function
ans = funref(10,23,4)
print('LambdaAns  -->',ans)


import sys
sys.exit(0)




def my_fun(item):
    if item %2 == 0:
        return True
    return False

values = [22,44,66,23,45,67,8,2,34,33] #1,25 --> 10
#result = filterfalse(my_fun,values)
#result = filterfalse(lambda item : True if item%2==0 else False,values)
result = filterfalse(lambda item : item%2==0,values) #lambda --> one line madhe code-->
print("FilterFalse Ans -->",list(result))   # 23 45 67 33
result = dropwhile(lambda item : item%3==1,values)
print("DropWhile Ans -->",list(result)) #44,66,23,45,67,8,2,34,33

#print(10%2==0)  # True
#print(12%2==0)  # False





import sys
sys.exit(0)

    # predicate -- any function --> who returns -- true,false ->Test
values = [random.randint(1,100) for item in range(10)] #1,25 --> 10
print(values)
ans = islice(values,0,5)#iterable --> itertools # its equivalent -- to--> slicing-- list --<   [start:stop:step]   --> list
print(list(ans))

import sys
sys.exit(0)


def myownpredicate(item):
    if item%2==0:
        return True
    return False

for item in range(10):
    values = [random.randint(1,100) for item in range(5)] #1,25 --> 10
    result = filterfalse(myownpredicate,values)
    print("Original -->",values)
    print("Final values -->",list(result))

    print('*'*30)

import sys
sys.exit(0)

for item in range(5):
    values = [random.randint(1,100) for item in range(5)] #1,25 --> 10
    print("Values -->",values)
    iterlist = dropwhile(myownpredicate,values)
    print("Final ANs -->",list(iterlist))
    print('*'*30)

import sys
sys.exit(0)

print(values)
def fun():
    finallist = []
    for item in values:
        if not item%3==0:
            finallist.append(None)
        else:
            finallist.append(item)

    return finallist
selecter = fun()  # excel --> NA --> 28,34,55 --> selector -->
#print(selecter)

result = compress(values,[0,1])  # creates new data --> true,false-- [none,false,emptycomplextype,0]
print(list(result))


#compress([1,2,3,4,5,6,7,8,9,10],[0,False,None,1,3,4,False,[],3])  #4   --> last

#compress(values,fun) #image --> binary -- 01100101 --> discard

import sys
sys.exit(0)





def my_processing(n1,n2):
    return n1+n2
#values = [random.randint(1,100) for item in range(10)]
values = list(range(11))
print(len(values)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = accumulate(values,my_processing)  # my_processing(6,4)  --> 10 --> at last-->

#result -->ACCOMULATE -- ITERABLE --> MYPROCESSING --> COLLECTION --> metadata --> abount --> acc--*

print(result.__reduce__())

import sys
sys.exit(0)

#ans = result.__reduce__()
#print("Accumulate result -->",len(list(result))) #[0,1,3,6]

ans = list(result.__reduce__())
print(ans,type(ans))

print(list(ans[1]))


#for item in ans:
#    print(list(item))















import sys
sys.exit(0)


# values ---> [s1,s2,s3,s4] --> s#20 --     #next --> next song -->
                                            #prev --> prev song
                                            #start --> first
                                            #end    --> last



class MyMusicPlayer:
    
    def __init__(self,val=20):
        self.values = list(range(val))
        self.start = 0
        self.end =  len(self.values)
    
    def __iter__(self):
        pass
    
    def __next__(self,param="prev"):
        pass                    # PREV,STARTOVER,AT_LAST
    
    def prev(self):
        pass            #current --> -1
    
    def start_over(self):
        pass           #START -- 0
    
    def at_last(self):
        pass            #START -->LEN(LIST)-1

#generators -> memory point view --> 


def myfunction():
    count = 0
    for item in range(5):
        count  = count + 1
        yield count

gen = myfunction()      # not calling

print(next(gen))    #       --> as long as yield --> 10 times--> 10 times-- local variable state preserves
print(next(gen))
print(next(gen))
print(next(gen))

for item in gen:
    print('ge inside ',item)#


gen = myfunction()      # not calling   =--> 5 times again

for item in gen:
    print('inside another loop -->',item)

import sys
sys.exit(0)




class MyIterator:
    
    def __init__(self,num = 5,noof=25):
        self.values = list(range(1,noof+1))     #25
        self.perpage = num                      #5

    def __iter__(self):
        return  self
    
    def __next__(self):
        if self.values: # check list empty nasel tr     # 15
            val = self.values[0:self.perpage]   #0-5    #0-5    --> 0-4--5 elements
            self.values = self.values[self.perpage:len(self.values)]    #[,25]--> --> prev--> 5 removed
            return val
        else:
            raise StopIteration("All elements are consumed..")
    
myob = MyIterator()
myitr = myob.__iter__() # iterater instance of myiterator class # -> 5 times-->
#as long as stop iteration not raise


for item in myitr:
    print('inside loop-->',item)        # 5 times -->


print(next(myitr))      # nothing to consume-- will raise-- stopiteration here itself
print(next(myitr))
print(next(myitr))
print(next(myitr))
#print(next(myitr))


myitr = myob.__iter__() # iterater instance of myiterator class # -> 5 times--> --> new intsance --> again 5 times