
#next --> looping-->  use cases of these type-->
#--> datatypes --> simple and complex --> ds -> array queue stack linkedlist [singly/doubly] hashtable
                #complex types --> list set tuple dict
                #methods -- and thr working-->


#DICT -> HASHTABLE
values = {1:100,2:200,"A":103,"B":200} #key immutable -- unique --> value --> mutable--duplicate allowed

#ans = values.setdefault('A',20)     # A-- key present -- Yes --> orig-- No change ans--> 103
ans = values.setdefault('X',20)     # X-- key present -- No --> orig-- Change will add that pair-- in values - X:20--ans--20

print(ans)
print(values)
import sys
sys.exit(0)
values.get('X') # key present-- value return-- absent--> None --> polite
values['X'] # key present- value return -- not present--> keyerror --> aggressive



values.values() # returns only values from given dict
values.keys()   #returns only keys from given dict
values.popitem()    #returns pairs -- key,value -- from given dict #will remove last pair
values.pop('k') #give key pair will be removed--> if no key present-- error
values.fromkeys([]) #given values pasn dict banvel with default None values
values.get('')  #given key chi value return karel-- if key not present-- None
values.update({})   # will change original dict-->
values.copy()   #shallow copy
values.clear()  #will remove all pairs







print(values)
values.popitem()            # pop(key) --given key cha pair    --> popitem()   -- last pair
print(values)

import sys
sys.exit(0)
ans = values.fromkeys([10,20,30,40])
ans[10]='A'
ans[20]='B'

print(ans)
import sys
sys.exit(0)
print(values)
pairs = values.items()

vals = list(values.values()) #-- 100,200,103,200
keys = set(values.keys())   # 1,2,A,B
values.update({1:33,4:55})  #values change--> {1:33,2:200,"A":103,"B":200,4:55}

print(pairs)
print('keys :',keys)
print('vals :',vals)
print(values)

#values[7]=2000

#print(values)



import sys
sys.exit(0)



#list - all methods -- set all methods --
#ds             -- set ds


values = {10,20}

print(values)
ans = values.remove(100)
print(values)


values = (10,203,40,50)

values[2]=7 # error --> no changes allowed -> predefined constants -->  days in week,month names,seasons,env names-->


import sys
sys.exit(0)


values= set()
values.union() # both unique --> ans return karel -- orig-- unchanged
values.discard(100) #   nasel --> None - polite -- present --remove
values.remove(100)  #nsel --error   --> aggr    --< present -remove



v2 = {10}
v1 = {10,20}             #common --> 20 40 50    --> only in v1 --> 10 30    --> only v2 --> 100,300

v1.isdisjoint(v2)   # no common element in both - True
print(v1.issubset(v2))     # False
print(v1.issuperset(v2))  #-->True
print(v1.union(v2))    #

import sys
sys.exit(0)
print('before')
print(v1)
print(v2)
#v1.update(v2)           # ans --> v1[CHANGED]--> 10,20,30,40,50,100,300  --> v2(UNCHANGED) -- 100,20,300,40,50
#v1.difference_update(v2)  # ans --> v1[CHANGED]--> 10,30  --> v2(UNCHANGED) -- 100,20,300,40,50 -- only in v1
#v2.difference_update(v1)  # ans --> v1[UNCHANGED]--> 10,20,30,40,50  --> v2(CHANGED) -- 100,300 -- only in v2
#v1.symmetric_difference_update(v2) #ans v1[changed] - 10,30,100,300     v2[UNCHANGED] -100,20,300,40,50 -- UNCOMMON
#v2.symmetric_difference_update(v1) #ans v2[changed] - 10,30,100,300     v1[UNCHANGED] -10,20,30,40,50 -- UNCOMMON
#v1.intersection_update(v2)  # v1[change]- 20 40 50      v2 [unchanged] 100,20,300,40,50 --> common
#v2.intersection_update(v1)  # v2[change]- 20 40 50      v1 [unchanged] 10,20,30,40,50 --> common

ans = v1.difference(v2)   # v1 and v2 -- unchanged --> result will be inside ans--> 10,30 -- only in v1
ans = v1.intersection(v2)# v1 and v2 -- unchanged --> result will be inside ans--> 20,40,50
ans = v1.symmetric_difference(v2)# v1 and v2 -- unchanged --> result will be inside ans-->100,300,10,30


ans = v2.difference(v1)   # v1 and v2 -- unchanged --> result will be inside ans--> 100,300 --> only in v2
ans = v2.intersection(v1)# v1 and v2 -- unchanged --> result will be inside ans--> 20,40,50--> both common
ans = v2.symmetric_difference(v1)# v1 and v2 -- unchanged --> result will be inside ans-->100,300,10,30 --> both uncommon



print('after')
print(v1)
print(v2)
print(ans)
