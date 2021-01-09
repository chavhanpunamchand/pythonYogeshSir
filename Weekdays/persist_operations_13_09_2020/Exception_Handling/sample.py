'''
An iterator is an object that contains a countable number of values.
An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
Technically, in Python, an iterator is an object which implements the iterator protocol,
which consist of the methods __iter__() and __next__() .
'''
class PowTwo:
    def __init__(self,max=0):
        self.max=max

    def __iter__(self):
        self.n=0
        return self

    def __next__(self):
        if self.n <= self.max:
            # result=2 ** self.n
            temp=0
            t1=self.n
            t2=self.n +1
            result= + self.n +1
            temp=result
            self.n +=1
            return result
        else:
            raise StopIteration

# create an object
num=PowTwo(4)

# create an iterable from the object
i=iter(num)


# using next to get the next iterator element
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))











import sys
sys.exit(0)
i=9

def f1(l1):
    global i
    i=0
    d=l1[i]+l1[i+1]
    i=i+1
    yield d



list1=[10,20,30,40,50]
# print(f1(list1))
print(next(f1(list1)))
print(next(f1(list1)))








import sys
sys.exit(0)

import time

a=[10,20,30,40,50]

s=iter(a)

print(next(s))
time.sleep(1)
print(next(s))
time.sleep(1)
print(next(s))
time.sleep(1)

print(next(s))
time.sleep(1)

print(next(s))
time.sleep(1)
