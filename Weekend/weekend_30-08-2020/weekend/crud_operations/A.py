#from Basics.weekend.crud_operations.B import *
#        A B C D   --> Bdriver --> main

print('inside a')       # console
print('A-->',__name__)  #console                --> who executes this line-->another module --> owner-->
print('a completed')    #console

def f1():               # A[f1--8x]
    print('inside a-f1')


def f2():               #A[f1-8x,f2-3x]
    print('inside a-f2')

class X:                #A[f1-8x,f2-3x, A[m1--44x]]
    def m1(self):
        print('inside m1-->A')