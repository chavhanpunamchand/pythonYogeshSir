'''

Iterative --> points
do..while --atleast once --> thru flag--*       --> not provided in python
while --> may or may not


range
random
random.randoint
enumerate
dict.keys
dict.values
dict.items


for --> when u are sure about no of iterations in advance
    --> when u are not sure about no of iterations in advance --> read data from db--> read data from files-->
while           --> may or may not body execution --> condition and then body
do..while    --> atleast once body execution --> body then condition --> condition bypass it thru flag-->


for -> loop --

Iterative --> statements --> execute the body as long as condition is satisfied
    for
    while
    do.while       * --> not in python --> we need to explicitly --> implement this
    range(10)   start--> 0    end=10      step=1
    range(1,10) step=1
    range(1,10,3)   start -1 end 10 --> incr -->3
                    1  4  7
for(initialization;conditions;incremet/decrement) --> other lang
        //body


for -->                                                                         start      stop     step
        range       --> seq  --> start stop -> step --->        range(10)   -->    0        10      1   --> 0-9
                                start -> include --             range(1,10) -->    1        10      1   -->1-9
                                stop --> dont include           range(1,10,2)       1       10      2   -->1,3,5,7,9
                                step --> increment by
        list/set/tuple  --> item --> simply element --
        dict -->
        step1
                1.dict --> keys --> based on keys using dict.get(key) -> value    --> we need to retrive
                2.dict.keys --keys --> based on keys using dict.get(key) -> value --> we need to retrive

        step2
                packed = pickling = (10,20,30,40,50)                values = (10,20,30)     for item in dict.items() -->  (key,value)
                unpacked--unpickling = 10,20,40,50                  v1,v2,v3 = 10,20,30     for k,v in dict.items() -->     key value
                3.dict.items() -- pair -->        for  k,v in   dict.items() --> unpacked   1 11 --> direct
                                                for  i,k,v in   enumerate(dict.items()) --> unpacked   0,1 11 --> direct

                                                for item  in dict.items() --> packed     (1,11) -> direct
                                                for i,item  in enumerate(dict.items()) --> packed     (1,11) -> direct
            step1 --> key -- we can retrive value
            step2 -- key,value -->direct
        step3
                dict.values()  --> only values --> u cannot retrive keys--based
                only values -->

        enumerate --> assign numbers to the  --> counter --> 0,1,2,3 -->
'''

import sys
import random


# i want to read the file print -> all lines- ->
#body -->

# fib -> series --> 0 1 1 2 3 5 8 --->

val = int(input('Enter Stop Point '))   # 5

#do --> atleast once -->
num1 = 0        # 0     1
num2 = 1        #1
result = 0      #0
counter = 1     #1

# swap -->
while (counter<=val):   # true                              #final ans --->     0,1,1,2
    print(result,end=',')   #1
    counter +=1             # 4
    num1 = num2             #1
    num2 = result           # 1
    result = num1 + num2    #1+1    --> 2



sys.exit(0)



while True:
    file = open('File')
    if not file.readlines():    # in case no lines
        break



num1 = int(input('Enter NO -->'))
num2 = int(input('Enter NO -->'))
while num1 == num2:
    break


while True:         # do while --> atleast once
    num1 = int(input('Enter NO -->'))
    num2 = int(input('Enter NO -->'))
    if num1 == num2:
        break








flag = 1
val = int(input('Enter Number : '))
while flag or val%2==0: #   # when no is even
    print('inside body')              #atleast once body execution happens                  # may or may not body execution
    val = int(input('Enter Number : '))
    flag=0              # reset -> next time flag will not bypass--> execution
print('Outside body -->')
sys.exit(0)



#do while kind of implementation --> while do.while --> with the help of flag
flag = [0]  # present
num = int(input('Enter Number : '))
                      # once --> first --> gc --> atleast once ->       do while --> implementation
while not num%3==0 or flag:     #   loop will execute unless entered number is not divisible by 3
    print('Inside Body')     #gc --> always --> cannot-->depends on condition
    num = int(input('Enter Number : '))
    flag.clear() #empty --> absent

print("Divisible by 3 -->", num)
sys.exit(0)






#every iterator --> group of elements --> list,set,tuple,dict


#while --> condition --> then body      -> may or may not
#do..while-->body first --> then condition --> atleast once
'''
    while condition:        --> body may or may not execute --> always --> depends on condition
            body
            
    
    
    do
        body                --> atleast once body will surely execute -- irrespective of condition
    while  condition
'''



#for item in range(1000):        # if we are sure about no of iterations -->
                                # if we are not sure about no of iteration in advance
while True:     #   # start loop --> unless not break --> if num divisible by 3 --> when ??==? no-->
    num = int(input('Enter Number :'))
    if num%3==0:
        print('Number found',num)
        break

sys.exit(0)





sys.exit(0)

                                       #no of attempts --> no --> if u are not sure about of numbers---> while
num = int(input('Enter Number : '))     # no of elements --> to reach to this condition ??
if num%3 == 0:
    print('Number Found -- >',num)

sys.exit(0)



values = [random.randint(1,100) for item in range(10)]      # this line is exactly to --> 51 to 57 lines -> compressive--> short hand expression -- short cut

print(values)

# i want to print all those -- nums divisiable by 3-->      #3 stop
for item in values:     #10
    if item%3==0:
        print(item)
        break

sys.exit(0)
values = []
for item in range(10):      # 10 times -->
    val = random.randint(1,100)    # 1 - 100 --> both inclusive -> random no generates
    values.append(val)

print(values)






sys.exit(0)

valuesList = list(range(1,20))
valuesSet = set(range(1,20))
valuesTuple = tuple(range(1,20))
valuesList1 = list(range(1,10)) # 9 -->1------> 9       1:11,2:12 --> key
valuesList2 = list(range(11,20)) #9--> 11----> 19                 -->value
valuesDict = dict(zip(valuesList1,valuesList2))


for cnt,pair in enumerate(valuesDict.items()):
    print(cnt,pair)     #0  (1,11)      1 (2,12)


sys.exit(0)
print('For List -->')
for index,item in enumerate(valuesList):      # if we want counter for the element
    print(index,item)         #       0:1 --> 8:9
print('For Set --->')
for index,item in enumerate(valuesSet): # enumerate --> assigns counter to the elements-->
    print(index,item)

sys.exit(0)

#values = [10,"A",True]  # item ?? --? first int --> second --string--> 3rd --> boolean
                      #list --> group of elements as single entity -->
                            # array --> type of array --> object --> hom data elements



print('Dict  Items ->',valuesDict)
print('using dict --> items() method --> unpacked')
for key,val in valuesDict.items():
    print(key,val)          #1 11


print('using dict --> items() method --> packed --> tuple pairs')
for pair in valuesDict.items():
    print(pair)         #tuple(1,11)    (2,12)  (3,13)



sys.exit(0)
print('using dict --> values() method')
for val in valuesDict.values():
    print(val)                  #only values --> 11 12  -----> 19



sys.exit(0)

print('Tuple Iterations using for loop')
for item in valuesTuple:
    print(item,end=' . ') #tuple elements sepereated by dot


print('using dict.nothing which is bydefault --> keys()')
for item in valuesDict:     #default .keys()
    print('Key {}'.format(item),"Value {}".format(valuesDict.get(item)))             #only keys  --> 1 2 3 4------> 9



print('using dict --> keys() method')
for key in valuesDict.keys():   #
    print('Key {}'.format(key),"Value {}".format(valuesDict.get(key)))             #only keys  --> 1 2 3 4------> 9


print('List Of Items ->',valuesList)

print('List Iterations using for loop')
for item in valuesList:
    print(item,end=' # ') #list elements sepearated by hash #

print('Set Iterations using for loop')
for item in valuesSet:
    print(item, end=' , ')  # set elements sepearated by ,

        #include--1 but not 10
val = range(1,20,2) #1                      <10
ans = list(val)
print(ans)

for item in ans:
    print(item,end=',')

sys.exit(0)

val  = range(10)    # seq -->
print(val,type(val))
rlist = set(range(10))
print(rlist)


