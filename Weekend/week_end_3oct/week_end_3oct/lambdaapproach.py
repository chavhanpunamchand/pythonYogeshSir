from sample import getemployess_list
# filter -- map --> reduce -->


    #lambda ==> anonymous function -- function without name--> shud be written inside one line--> short hand -->
#map --> to proces every element and return all
#filter --> to filterout--> not process-->
#reduce --> single element will be the output--

#map(f,list)    --> visit each and every element and process [we can apply condition then process]--> len(list) --> process
#filter(f,list) -> visit each and every eleement but--> filter--> only those emp will be collected--> condition satify-->


#filter- map -->depend situation -->

emplist = getemployess_list(10)
print(emplist)

from functools import reduce
from sample import Emp
ans = reduce(lambda x1,x2 : x1.empSal + x2.empSal if type(x1)==Emp else x1+x2.empSal, emplist)# e1.sal,e2.sal--> float,e3
                #x1,x2 --> e1,e2        ---> e1.empSal + e2.empSal -->float
                #x1,x3 -->float,e3 -->     o
print('Reduce -->',ans/10)
allSal= map(lambda emp : emp.empSal,emplist)
print(allSal)   #sum of all emp sal--> single element-->




print("Avg Sal -->",sum(allSal)/len(emplist))

import sys
sys.exit(0)

print(emplist)
def process_sal(emp):
    if emp.empAge>50:
        emp.bonus =round(emp.empSal*1.10,2)
    return emp

finalist = list(map(lambda emp: process_sal(emp),emplist))
print(finalist)

import sys
sys.exit(0)

print(emplist) #10
print('*'*40)
filteredemp = list(filter(lambda emp : emp.empAge>50,emplist))  # cannot say--> output
print(filteredemp)
print('*'*40)

def process_sal(emp):
    emp.empSal = emp.empSal*1.10
    return emp

bonuslist = list(map(lambda emp : process_sal(emp),filteredemp)) #--> output
print(bonuslist)