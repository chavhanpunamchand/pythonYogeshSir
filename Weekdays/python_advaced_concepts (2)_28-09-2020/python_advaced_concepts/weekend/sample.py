from itertools import cycle,repeat,count        # infinite--> purpose-- use case-->
from itertools import accumulate,chain
import time


#string method->
#build in function
# itertools -->     #
#chain --> logical combine and iterate --> dont overlap values--> with each other-->
# itertools-- all methods returns iterable instance--*

val1 = {ind:item for ind,item in enumerate(range(1,11))}  #

val2 = {ind:item for ind,item in enumerate(range(101,111))}    #

val2[1]=1000
val2[5]=1003

print(val1)
print(val2)
#val1.update(val2)   # ans will be in value      --> orignial data lost--*

values = chain(val1.items(),val2.items())

for item in values:
    print(item)



import sys
sys.exit(0)


#val3 = val1+val2        # memory more-->


values = chain(val1,val2)   #
for item in values:
    print(item)


#for item in val3:
#    print(item)

import sys
sys.exit(0)

values = [1,2,3,4,5,6,7,8,9,10]

                   # 1,2 --> 1+2+2 ---> 5
                   #5,3 --> 5+3+2 --> 10
                   #10,
def my_operations(n1,n2):   # writ whatever logic u want --> 2 params
    return n1+n2+2


val = accumulate(values,my_operations)# infinite ?? --> No
ans = list(val)     # list madhe collected-- as its not infinite
print(ans)



import sys
sys.exit(0)




def get_entry_pass(stud):
    print(stud,'inside get entry pass')
    time.sleep(1)

def visit_account_dept(stud):
    print(stud,'inside visit account dept')
    time.sleep(1)

def clear_fees(stud):
    print(stud,'inside clear fees')
    time.sleep(1)

def document_verification(stud):
    print(stud,'inside document verification')
    time.sleep(1)

values = ["s"+str(item) for item in range(1,101)] # 100 student --> create list- s1-s100

student_clearance = [get_entry_pass,visit_account_dept,clear_fees,document_verification]    # which steps/function

student_admin_proces = cycle(student_clearance)     #infinite time --> students--> s1--> 4 s2: 4  -> ad

cnt = 1     #
val = 0

for process in student_admin_proces:  # get_entry_pass
    process(values[val])
    if cnt %4 == 0:
        val = val+1
        print('*'*40)
    cnt = cnt+1





import sys
sys.exit(0)


values = [10,23,455,67,8,99,]

val = cycle(values) # infinite --> college --> student -->  gateentry pass--> account section -- document verification--

for item in val:
    print(item)
    time.sleep(1)

import sys
sys.exit(0)



val = repeat(10)


for item in val:
    print(item)
    time.sleep(1)
#values = list(val)  #
#print(values)


import sys
sys.exit(0)
cnt = count(start=1,step=-0.5) # 1 -->  1+1 --  2+1 -->  infinite-->


for item in cnt:
    print(item)
    time.sleep(1)





def infinite_loop():
    while True:
        yield 1


gen = infinite_loop()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

while True:
    print('infinite')


import sys
sys.exit(0)


value = [1]

for item in value:                  # infinite -->
    value.append(item)
    print(value)

#

import sys
sys.exit(0)


for item in range(10):      # infinite --No
    print(item)











#yield  -->any function --> generateor instance--> next(gen)    --> fun --pause--> local state preserve
#return  --> function break along with all loops    -->

                                            # iterable
#for item in a:      # a- itearble --> Iterators or Generators -->
#    pass                             #iter/next       --> iter/next


a = list(range(10))     #iterator functions

for item in range(10):   # -- generateor functionality
    print(item)

print(a,type(a))
import sys
sys.exit(0)

#iterator --> class level      --> iter/next    --> iter--> iteralle instance--> next logic-->
#generator --> function/method--> yield          --> yeild--> pause function execution and resume that point onwards on next call

def xx():
    cnt = 0
    yield cnt                     #local variable - state preseve --> next--< return cnt
    cnt  = cnt + 1                #0+1
    yield cnt                    #local variable - state preseve --> next--< return cnt
    cnt  = cnt + 1               #2
    return cnt                    #local variable - state preseve --> next--< return cnt


a = xx()        # no call --> returns generator instance --> yield --> return
print(a)
print(next(a))  #0
print(next(a))  #1

print(next(a))  #-stop iteration

import sys
sys.exit(0)

#yield -- > function pause --> local variable--> save --?? my_instance-- object-- [localvariable]--> next-->
            #last pause points --> execution resume -->


def my_function():                  # my_function instance memory -> gene--> program chalu ahe--> program stop
    print('inside function')
    for item in range(10):
        print('Loop -->',item)
        yield item                     # 1-- pause

a = my_function()

#print(a)    #

#print(next(a))  #0
#print(next(a))  #1      --> yield --> function la pause--> executation resumes from that point onwards...

for item in a:              # a --> generator -- function la iterate krtoy..
    print(item)


import sys
sys.exit(0)



# calling to the function takes return value inside a --> a holds None
#b = my_function         # function ref --> hold inside b -- > b and my_function - are pointing to same mem location

#print(my_function is b)     # True      is --> ref/mem -->

print(next(a)) # functionla --> return 10
print(next(a)) # functionla --> return 10

#print(ans, type(ans))   #0  int
#print(ans, type(ans))   #0  int


import sys
sys.exit(0)


#iterator --> generator --> both are iterable
#class         fun
#iter,next      yeild
#parent        child



# --> go thru -- build in function --> string class functions -->   * today --> udyachya batch la

# --> complex type --> list,set,tuple,dict --> str,range   --> iterable
        #  iter next --> iter--> iterable instance return
                    #--> next --> return one element
                                                              # element processing-- seq
    #list,set,tuple,dict --> str ---> iter,next --> Iterator    --> Iterable --> class level
    #range --> function --->                    --> Generator   --> Iterable --> function level
#iterable -?
# str--> iter --> iterable instance returns --> next [one by one element]   -- raises --stopiteration
# list--> iter --> iterable instance returns --> next [one by one element]  -- raises --stopiteration
# set--> iter --> iterable instance returns --> next [one by one element]   -- raises --stopiteration
# tuple--> iter --> iterable instance returns --> next [one by one element] -- raises --stopiteration
# dict--> iter --> iterable instance returns --> next [one by one element]  -- raises --stopiteration
#range --> functions --> generator -- >*
#iterable --> iter --- next --stop points -->
# --> iterable -->  iter -- next -- [stopiteration] ===?
        #-->    generator-->            iterator--> generator ->        generator is child iterator


        #class -- iterable --> Iterator --> iter/next methods -->
        #functional -- iterators-- Generator --> any function which has atleast yield  keyword
        #iterator
                #generator -->


     # 1inch -->  7 lines -->       --> function -->
class ProcessFile:                  # iterable

    def __init__(self,screensize,start=0,flag='W'):
        with open('sample.txt','r') as file:
            self.flag = flag
            self.alllines = [line.strip() for line in file.readlines()] #294
            self.allwords = [lin.split(" ") for lin in self.alllines]
            self.finalwordlist = []
            for word  in self.allwords:
                self.finalwordlist.extend(word)
            self.screensize = screensize                                #7
            self.start = start

    def __iter__(self):     # will process file instance as --> Iterable
         # 0
        self.nextstop = self.start + self.screensize  # 20
        if self.flag == 'W':
            self.end = len(self.finalwordlist)
        else:
            self.end = len(self.alllines)  # 294

        return self

    def __next__(self):     # write u logic--> to return --> on each iteration
        if self.end > self.nextstop:
            if self.flag=='W':
                lines = self.finalwordlist[self.start:self.nextstop]
            else:
                lines = self.alllines[self.start:self.nextstop]
            self.start = self.start + self.screensize
            self.nextstop = self.nextstop + self.screensize
            print('-------------------------------------------------')
            return lines
        else:
            raise StopIteration("All elements processing completed..")



MOBILE_SCREEN_SIZE = 100
procesfile = ProcessFile(MOBILE_SCREEN_SIZE,start=0,flag='L')
#print(procesfile.finalwordlist)
#import sys
#sys.exit(0)

#print(next(procesitr))      # 0-9--> first 1-10 lines
#print(next(procesitr))      # 10-19--> first 11-20 lines
import time

procesitr = iter(procesfile)


for lin in procesfile:
    print(lin)
    time.sleep(1)


import sys
sys.exit(0)
values = [10,20,30,40,50]   #searching --> process -->



for v in values:        # iterable --> t1 t1 -->
    print(v)


#list ---> index -->  append --> array

for item in range(10):      #0-9
    print(item)

for v in values:            #iter(values)           --> iter ---> next
    print(v)                #next(v)    --> Stopiteration --> iteranally --> for handles--> stopiteration
        #iter --> in build function -->  sequential processing/iteratation -- allows on group of elements
val = iter(values)        # --> converted this list type into iterable
print(next(val))    #1st
print(next(val))    #2nd
print(next(val))
print(next(val))
print(next(val))
print(next(val))    # exception --> Stopiteration-->

while val:      #looping    --> iterable
    print(val)



#for item in values:         # iterate --> value--list --> iterable -->
#    print(item)