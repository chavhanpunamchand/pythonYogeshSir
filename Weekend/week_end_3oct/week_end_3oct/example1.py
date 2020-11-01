from collections import OrderedDict,defaultdict,deque,Counter,ChainMap,namedtuple

#Counter,ChainMap,namedtuple --> decorators/closures/property/innerfunct/asserts--> multithreading*

#queue --> first in first out       --> last in last out
#stack --> first in last out        --> last in first out
#linked list -->
        #singly     node        --> first -- head   --> tail -> last node           --> [data,next]
        #doubly     node        --> first -> head    --> tail ->last node           --> [prev,data,next]

            #next ---> node ---> prev --> node -->      data --> object
            #node --> prev--none-> head
                    #last --none -- tail

values = deque([1,2,3,4,5])

print(values)
values.rotate(1)

print(values)

import sys
sys.exit(0)
values.appendleft(10)   # start-->left la - --0th index
values.append(10)       # end --> right la  =len index la

values.extend([1,2])        # end --> right la  =len index la
values.extendleft([22,33])  # start-->left la - --0th index

values.rotate(-1)    #[1,2,3,4,5]    --> 1 --> 1 2 3 4 5
                                     #         5 1 2 3 4


import sys
sys.exit(0)

normdict= {'a': 10, 'b': 20, 'c': 3, 'd': 4, 'e': 5}


normdict.get('a') # Yes --> 10
normdict.get('x') # No --> None
normdict['a'] # Yes --> 10
#normdict['x'] # No --> keyerror


a1 = normdict.setdefault('x',22)    # x key present -->no --> x:22--add this inside dict at last--> a1--> 22
                                        #{'a': 10, 'b': 20, 'c': 3, 'd': 4, 'e': 5,'x':22}  --> a1-->22

a2 = normdict.setdefault('a',66)    # a key present -- yes --> no changes inside dict --> a2 --> None
                                        #{'a': 10, 'b': 20, 'c': 3, 'd': 4, 'e': 5} --> a2 - 10
    # setdefault works for single key-->



dfdict = defaultdict(list,a=10,b=20,c=3,d=4,e=5)  #key


dfdict.get('a') # Yes --> 10
dfdict.get('x') # No --> None
dfdict['a'] # Yes --> 10
dfdict['x'] # No --> 0



print(dfdict)

import sys
sys.exit(0)


# OrderedDict  --> maintains - key insertion seq --->  OrderedDict  =~  Dict[3.6 version]
            #-->    move_to_end --> last-True[end]/False[start]-->
            # --> deprected --> not in use much --> after python 3.6 version -- all these function/features-- normal dict madhe
orderDict = OrderedDict()
orderDict[1] = 101
orderDict[2] = 102
orderDict[3] = 103
orderDict[4] = 104

print(orderDict)







orderDict.move_to_end(2)    # 2 wala key -- last la
orderDict.move_to_end(3,last=False)    # 3 wala key -- first la-->  --> Last=False --> First True
print(orderDict)
import sys
sys.exit(0)



values1 = list(range(1,11))
values2 = list(range(11,21))

values = dict(zip(values1,values2))

print(values)



'''
    dict --> key:value
            key -- unique -- not duplicate
                   single None allowed
                   Key insertion seq -- maintained-- >=3.6-->
                   Key -- hashable --> required--> index--> hashtable madhe
            value
                  duplicate allowed
                  multiple nonetype allowed
                  
'''




import sys
sys.exit(0)
from week_end_3oct.sample import getemployess_list
from itertools import groupby,takewhile,dropwhile,filterfalse,tee,zip_longest
import random


class A:

    def __iter__(self):
        pass

    def __next__(self):
        pass

a = A()
a.__iter__()        #same == > all instance methods     -->same
iter(a)             #same       - only for built in --> output same


values = [10,20]
values.__len__()  # object ref --> instance method-->
len(values)  # built in madhe asl pahije-->











#zip -->  v1:40     v2:40   --> 40
#zip -->  v1:20     v2:40   --> 20
#zip -->  v1:60     v2:40   --> 40

#zip_l -->  v1:40     v2:40   --> 40
#zip_l -->  v1:20     v2:40   --> 40
#zip_l -->  v1:60     v2:40   --> 60    --> None



#zip --> lowest prynt pair banvel
#ziplongest--> highest--> dont look at key  /or value

values1 = list(range(1,31))  #30        -- 50
values2 = list(range(101,151)) #20      --100      50 ch        #50

final = zip_longest(values1,values2)

for val in final:
    print(val)

#print(final)


import sys
sys.exit(0)




values = {1:55,2:37, 3:136, 4:617, 5:914, 6:808}



#ans = list(tee(values,5))

#print("--",values*5)

print(ans)



import sys
sys.exit(0)


values = [55,37, 136, 617, 914, 808, 834, 842, 195, 47, 13, 349, 778, 985, 131, 45, 304, 764, 902, 150, 623, 395, 895, 982, 124, 911, 905, 770, 370, 847, 523, 777, 222, 909, 191, 137, 864, 634, 13, 891, 412, 881, 860, 520, 718, 174, 856, 177, 544, 352, 439]




print(values)
ans1 = list(takewhile(lambda x : x%5==0,values))        # collect till -- first false found -- as long as true ahe
ans2 = list(dropwhile(lambda x : x%5==0,values))        # collect from --> first false      --> as long
ans3 = list(filterfalse(lambda x : x%5==0,values))      # collect all--> false wale
ans4 = list(filter(lambda x:x%5==0,values))             # collect all --> true wale

print("TakeWhile -->",ans1)
print("DropWhile -->",ans2)
print("FilterFalse -->",ans3)
print("Filter -->",ans4)






import sys
sys.exit(0)


emplist = getemployess_list(20)
#print(emplist)  # sort by -- orderby-->
emplist.sort(key=lambda emp : emp.empDept,reverse=True)

groups = groupby(emplist,key=lambda emp : emp.empDept)

groups.get("TESTING")   # all emps -- belongs to testing
groups.get("DEV")   # all emps -- belongs to testing


for key,value in groupby(emplist,key=lambda emp : emp.empDept):
    print(key ,"--> ",list(value))








import sys
sys.exit()

#starmap --> complex of complex vr processing--> starmap -->    [()()()()]  --> starmap
#complex --> map -->                                            [,n,n]

from itertools import starmap
import random

values = [(("MATH",random.randint(30,100)),("CHEM",random.randint(30,100)),("PHY",random.randint(30,100))) for item in range(10)]
print(values)
ans = list(starmap(lambda e1,e2,e3:e1[1]+e2[1]+e3[1],values))

print(ans)      # index position-->


ans.sort(reverse=True)

print(ans[0])

#ans = list(map(lambda x:print(x[0][0],x[1],x[2]),values))



#print(values)
#values = [(("Math":random.randint(30,100)),("Phy":random.randint(30,100)),("Chem":random.randint(30,100))) for item in range(10)]
#ans = list(map(lambda item: print(item),values))
#print(values)

#values[0].get("Math")   --> first student math marks-->

#ans = list(starmap(lambda x,y,z : print('X-->',x,"  Y-->",y,"  Z-->",z),values))
#list(lambda x,y,z:) #math--> data-> list--> desc--> first--> topper-->