from itertools import zip_longest,starmap,groupby,product,combinations_with_replacement,combinations,permutations
#product,comn,comp_rpl,per --> iterblable - repeate # dont check duplicate pair-->

#iterable -->

#iterable + lambdas --> once go thru --> collections module --> next week interviews- -> python core -->

ans = list(combinations_with_replacement([1,1,1,1,1],r=2))   #5*5        --> 11 11  11       --> dont check groups -->

print(ans)


import sys
sys.exit(0)


#product        :   self + ---> + <---   = all possible pairs
#permutation    :   --->    +   <----   =                           except pair with self
#combination    :   ----->              =                           except backward + self pairs
#combination with repl :     self + frwd                            except  backward


                                            #5*5*5      111 121 123 124 -->
                                             #5*5 --> 25pairs                                     #self      next        back -->
print(list(product([1,2,3,4,5],repeat=3)))  # create groups of two elements --> self pair  self+next self+back
print('*'*40)                               #pair ---> self + frwd + bckwrd
print(list(permutations([1,2,3,4,5],r=2)))  # frwd + backd --> bt no pair --> for self
print('*'*40)
print(list(combinations([1,2,3,4,5],r=2)))   # only forwd pairs --> but not with self + backwd
print('*'*40)
print(list(combinations_with_replacement([1,2,3,4,5],r=2))) # fwrd + self --> bt not bcwrd
print('*'*40)

import sys
sys.exit(0)




# order by  --> asc or desc
# reverse   -> insertation position chya opp
# group by  --> as per category --> we create groups -->


#scattered -->
values = [("math",44),("chem",47),("phy",67),("math",44),("phy",45),("math",83),
          ("phy",64),("chem",64),("math",45),("phy",54),("chem",22),("phy",95)
          ,("math",88),("chem",84),("phy",34),("math",67),("chem",56),("phy",74)]

#print(values)       # list -- multiple tuples --> scattered -->
# sorty by tuple chya zeroth index --> subj-- > sort by subject hoel
values.sort(key = lambda tupl : tupl[0])    # sort by --> tuple[0] --> subj --> sorting by subjects
#print('*'*40)
#print(values)       # sorted by subject print hoel

#ans = [('chem', 47), ('chem', 64), ('chem', 22), ('chem', 84), ('chem', 56)]

subjgrp = groupby(values,key=lambda tupl : tupl[0])     # group by subjects -->

for key,group  in subjgrp:    # group by --> subject ne xch --> chem --> phy --
    grp = list(group)

    print('Which Subject : ',key," List of Values : ",grp)  #list(group) --> checm -->
    ans = grp
    print(sum(list(starmap(lambda suj,marks:marks, ans))) / len(ans))
    print('*'*40)

import sys
sys.exit(0)

values = [12,34,56,35,77]
values1 = [(1,2),(3,4),(4,4),(4,55),(52,45)]
values2 = [(1,2,1,2),(3,4,3,4),(5,5,4,4),(6,74,7,55),(7,8,52,45)]

ans1 = list(map(lambda item : item*2,values))
ans2 = list(map(lambda item : item[0]*item[1],values1))   # index position we need to tell
ans2 = list(map(lambda item : item[0]*item[1]*item[2]*item[3],values2))   # index position we need to tell


ans3 = list(starmap(lambda i1,i2 : i1*i2,values1))   # index position we need to tell
ans4 = list(starmap(lambda i1,i2,i3,i4 : i1*i2*i3*i4,values2))   # index position we need to tell
print(ans1)
print(ans2)
print(ans3)
print(ans4)




import sys
sys.exit(0)
values1 = [1,2,3,4,5,6]
values2 = [100,200]

final = dict(zip(values1,values2))
final1 = dict(zip_longest(values1,values2,fillvalue='NA'))  #older key --> latest value
print(final)
print(final1)
import sys
sys.exit(0)







'''
Itertool every function returns iterable -->
iterable --> anything which we can process/iterate
iterator -- its implementation to make a class as iterable
every iterator is iterable.

'''
from itertools import count,cycle,repeat

#count --> start step --> step -- can be +ve/-ve --> can be intergral or floating-->
# it represents infinite -- iterable

#cycle -->  requires iterable and which processes all elements in circular with infinite

#repeate --> requires single elements which wil be repeated n times or infinite times.

#accumalate --> applies function on 2 input elements--> output of first two elements
            #will input for next execution as first param -
            # reduce = accumalate last ans --> accumalate returns all itermediate points.

#dropwhile --> requires predicate and iterable -->
            #predicate --> condition which returns true/false

            #till first false --> drop the element-- once first false found-->
            # start collecting all elements without applying predicate

# takewhile --: requires predicate and iterable
            #collect all elements till first false found -->
            # once first false found - dont predicate on remainging elements

# filter --> predicate/condition -- all elements

# compress -->data --> selectors -->
            #data-- iterable       -->
            # selectors iterable -->  whichever index position returns -- select the data

#filterfalse ->
# chain --> its kind of joinging multiple iterable as single one--> while iterating -- logically combined--> only for iterable

from itertools import filterfalse
predicate = lambda x : x%3==0

    #dropwhile chya ops takewhile
    #filter chya ops   filterfalse

#dropwhile      takewhile       filterfalse         filter
# p,i           p,i             p,i                 p,it                  #input
# itr            itr           itr                 lambdas                # frm where
# starts when   stops           collect             collect only
#first false    when            only                only those
                #firstfalse     those                wherever predicate is true
                                #whereever pred
                                #false
#--> only those those are not divisible -->
for item in filterfalse(predicate,[12,34,5,33,2,13,43,23,4,5,78,3]):
    print(item)

import sys
sys.exit(0)

import random
values1 = [random.randint(1,10) for item in range(10)]
values2 = [random.randint(1,15) for item in range(10)]
values3 = [random.randint(1,56) for item in range(10)]
values4 = [random.randint(1,24) for item in range(10)]
values5 = [random.randint(1,56) for item in range(10)]
from itertools import chain
ch = chain(values1,values2,values3,values4,values5)

for item in ch: # its kind of single list vr iterate kartay..
    print(item)




