from collections import OrderedDict,defaultdict,deque,namedtuple,ChainMap,Counter

import random


v1 = [5, 3, 3, 5, 2, 4, 5, 4]#[random.randint(1,5) for item in range(8)]
v2 = [7, 2, 5, 9, 5, 2, 7, 10, 10, 8]#[random.randint(1,10) for item in range(10)]

print(v1)
print(v2)

c1 = Counter(v1)
c2 = Counter(v2)

print(c1)
print(c2)

print(list(c1.elements()))

for item in c1: # no of keys--> 5 3 4 2
    print(item)

for item in c1.elements():  #5, 5, 5, 3, 3, 2, 4, 4
    print(item)

import sys
sys.exit(0)
c1.subtract(c2)

print(c1)
import sys
sys.exit(0)


values =[25, 22, 18, 12, 2, 17, 7, 1, 10, 21, 10, 19, 14, 9, 17, 19, 13, 13, 4, 10, 9, 5, 5, 3, 17, 4, 8, 15, 12, 6, 15, 24, 14, 8, 1, 4, 3, 3, 8, 22, 11, 7, 21, 8, 3, 15, 14, 5, 9, 8] #[random.randint(1,25) for item in range(50)]

print('or values-->',values)
count = Counter(values)

ans = count.most_common(5)    # first five--> mostly generated

print(count)

print(ans)


import sys
sys.exit(0)
#chainedmap -->
    #searching --> firstmapping-- not found-- next not found--> next--> till first found-- or key error
    #modification la open-->always only first-->
    #map.parents--> discard first and make 2nd open for --modification
    #map.maps --> values data --> so index basis vr modify -- double-- create chained with recent data
    #map.new_child --> we can create any mapping-- as first--> so that will be open for modification-->


d1 = {chr(item):item for item in range(65,70)}      # Y:55  Z:5
d2 = {chr(item):item+10 for item in range(65,70)}      #X :44  Z:#
d3 = {chr(item):item+20 for item in range(65,70)}      #Y:33   X: 20

d2["X"]=44
d3["X"]=20

d1["Y"]=55
d3["Y"]=33

d1["Z"]=5
d2["Z"]=3

d3["T"]=35

#print(d1)
#print(d2)
#print(d3)

'''
d1-->{'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'Y': 55, 'Z': 5}     --f1
d2-->{'A': 75, 'B': 76, 'C': 77, 'D': 78, 'E': 79, 'X': 44, 'Z': 3}     --f2
d3-->{'A': 85, 'B': 86, 'C': 87, 'D': 88, 'E': 89, 'X': 20, 'Y': 33,'T':3}    --f3
'''


#print('*'*40)
#searching --> first--> not found--> second--> not found--> next
#modification/add --> first--*      --> key--replace--> add--> only inside first dict-->

chmap = ChainMap(d1,d2,d3)#LOOKUP SEARCH --> START FROM FIRST DICT--> TILL FIRST FOUND--.

chm1 = chmap.parents

#chm1  #discard first--> d2 open for modification

chm1['B']=200

chm1.new_child(d1)  # d1 double--> first--> and open for modification-->

chm1['B']=200       # first-->d1 -> d1 is first--> open for modification-->


data = chm1.maps
data[7]['B']=2000

ch1 = ChainMap(data)    # 8th wali pair cha b modified asel



#print(chmap)
#print(chmap['T'])  # start from first dict--> search for A key--> till first found-    --> may not found--> even searched inside all dicts

#chmap1 = chmap.parents  # discard and first then return --- d2,d3 --> d2 first--> open for modification
#print(chmap1)   # no W -->
#chmap1['W']=100      #chained map-> open--crud-- add/remove/update--> first open

#print(chmap1)

values = chmap.maps
values[2]['E']=189
chmap = ChainMap(values)
print(chmap)


#chainmap.parents --> discard first and 2nd  open for modification -->
#chainmap.maps --> list  of values --> indexing-- and key using karu--> we can modify any --> again chained map
#chainmap.new_child-->


import sys
sys.exit(0)

import pymysql

#namedtuples--> assigns names to the indexes of tuple--> namedtuple is extened version of tuple-- in which we can access elements thru +  index+name
# on th go-> tuple- property assign --> plus--> index+name-> name--accessing better as compare to indexing
def fetch_data():
    studtuple = namedtuple('StudInfo', ['studId', 'studName', 'studAge', 'studFees', 'studSubj', 'studEmail'])
    conn = pymysql.connect('localhost', 'root', 'root', 'pydb')
    channel = conn.cursor()
    channel.execute('select * from stud_info')
    for st in map(studtuple._make,channel.fetchall()):
        print(st.studId,st.studName,st.studAge,st.studEmail,st.studSubj,st.studFees)
        print('*'*40 )


fetch_data()
import sys
sys.exit(0)





def obtain_connection():
    try:
        return pymysql.connect('localhost','root','root','pydb')
    except:
        print('Problem in database connection-->try again..!')

#thru named tuple -->>
studtuple = namedtuple('StudInfo',['studId','studName','studAge','studFees','studSubj','studEmail'])
#records = ((1,'VVVAAAA',22,4333.3,'M102','xxx@gmail.com'),(2,'VVVAAAA',22,4333.3,'M102','xxx@gmail.com'),
#           (3,'VVVAAAA',22,4333.3,'M102','xxx@gmail.com'),(4,'VVVAAAA',22,4333.3,'M102','xxx@gmail.com'))

#studtuple._make((1,'VVVAAAA',22,4333.3,'M102','xxx@gmail.com'))
'''
for rec in records:
    st = studtuple._make(rec)    #          (studId:1,studname'VVVAAAA',22,4333.3,'M102','xxx@gmail.com')
    print(st.studId)
    print(st.studName)
    print(st.studAge)
    print(st.studFees)
    print(st.studEmail)
    print(st.studSubj)
    print('*'*40)
'''

def fetch_stud_data():
    conn = obtain_connection()
    channel = conn.cursor()
    channel.execute('select * from stud_info') #iterable
    records = channel.fetchall()
    #map(,records)   #((s1data),(s2data),(),(),(),())

    for st in  map(studtuple._make,records):
       print(st.studId)
       print(st.studName)
       print(st.studAge)
       print(st.studFees)
       print(st.studEmail)
       print(st.studSubj)
       print('*' * 40)


fetch_stud_data()

import sys
sys.exit(0)

'''

    for rec in records:
        st = studtuple._make(rec) 
        print(st.studId)
        print(st.studName)
        print(st.studAge)
        print(st.studFees)
        print(st.studEmail)
        print(st.studSubj)
        print('*' * 40)
'''

#Tranditional Approach->
class Student:
    def __init__(self,sid,snm,sag,sfees,subj,email):
        self.studId = int(sid)
        self.studName = snm
        self.studAge = int(sag)
        self.studFees = float(sfees)
        self.studSubj = subj
        self.studEmail = email

    def __str__(self):
        return f'''\n {self.__dict__}'''

    def __repr__(self):
        return str(self)



def fetch_stud_data():
    conn = obtain_connection()
    channel = conn.cursor()
    channel.execute('select * from stud_info')
    studinfo = channel.fetchall()           #((s1),(s2),())
    studlist = []
    for stud in studinfo:
        st = Student(stud[0],stud[1],stud[2],stud[3],stud[4],stud[5])
        studlist.append(st)

    return studlist


studlist = fetch_stud_data()
print(studlist)
import sys
sys.exit(0)

namedtpl = namedtuple('subjects',["math","phy","chem"])
values = namedtpl(10,20,30) # tuple -->
print(values[0],values.math)    # thr u -- name --> namedtuple--> tuple--> thru indexes--> now we can access it thru either--> index or else thru name-->
print(values[1],values.phy)
print(values[2],values.chem)

















import sys
sys.exit(0)

from itertools import product,permutations,combinations,combinations_with_replacement

#ans = list(product([1,1,1,1,1],repeat=3))           #5*5 -- diff-->
#print(ans)

                                                    #   (1,1)       (1,2)           (2,1)
ans = list(product([1,2,3,4,5],repeat=2)) #5*5*5    -> self sbt + all next sbt + prev sbt allowed -- pairing
print(ans)
print('*'*40)
ans = list(permutations([1,2,3,4,5],r=2)) #5*5*5   ->  all next sbt + prev sbt allowed -- pairing   -->except self
print(ans)
print('*'*40)
ans = list(combinations([1,2,3,4,5],r=2)) #5*5*5    -->  all next sbt -- pairing except--> self+prev
print(ans)
print('*'*40)
ans = list(combinations_with_replacement([1,2,3,4,5],r=2)) #5*5*5   # self + next sbt ---> except prev
print(ans)
print('*'*40)

'''
Product -->[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)]
****************************************
Permutation -->[(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)]
****************************************
Combination -->[(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
****************************************
Combination_with_replacement -->[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 2), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5), (4, 4), (4, 5), (5, 5)]
****************************************

'''
