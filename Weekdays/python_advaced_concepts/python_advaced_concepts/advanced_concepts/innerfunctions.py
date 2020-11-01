

# whoever holds function ref --can call to the function -->
            #fun --> assign -- passon-- as param --*    fun()   -->fun calling --> 1 function can have n ref--*



def f1():
    print('inside f1')


def f2(val):
    print('inside f2')
    val()           # f1 --> f1 wil be called
    print('f2 completed')


a = f1      # f1 ref--> assigned to a -> a and f1 holds -- same function ref
x = f2(a)       # f2 calling--> a --> function ref--> f1 --> f1  as param to the f2 --> f2()--> inside f2--> inside f1--> f2 completed
y = f2(f1)      # f2 calling --> f1 -->function -> f1   --> f1 as param to the f2                inside f2--> inside f1--> f2 completed

print(x)    # none
print(y)    #none
print(a)    # f1 fun ref --> 3x
print(f2)   # f2 fun ref --> 5x
print(f1)   # f1 fun ref --> 3x




import sys
sys.exit(0)




def outer():                # 2x
    print('inside outer')

    def inner():        # memory - milel --> 4x     --. 5x
        print('inside inner')

    return inner

                # outer -- a  --> 2x
a = outer   #--> no calling-- fun ref assignment    --> a and outer --> holds -- same function ref-->
b = outer() # we are calling to outer 2x --> return madhe --> inner ref -->  b --> holds 4x which is inner fun ref
c = a()     # a()   --> 2x -outer ref --> calling to outer --> c--> inner ref
d = b()     # b() --> inner function calling    --> none
x = c()     # c() --> inner function calling    --> none

        #2 - inner outer--> 2 inner inner

print(a)    # o->2x ---> outer function la      --> a is outer  --> True --> is checks ref equality
print(b)    # i->4x         # b is c --> false --> b hold inner --> c hold inner --> both are diff mem locations
print(c)    # i->5x
print(d)    # d - None
print(x)    # d - None
print(outer) # 0-2x

#b --> inner ref        --> 4x --> inner function ref
#c --> inner ref        --> 5x --> inner function ref


import sys
sys.exit(0)


def f1():
    print('inside f1')


a  = f1()   # call to the function and hold return value inside-- a
f1()        # call to the function -- dont hold return value
b = f1      # assign function ref to b--> now we have 2 function ref --> b and f1 -->

#same
f1()
b()

#same
print(f1)
print(b)


def x(v):   # f1
    print('inside x')
    v()     # calling to f1 --> outer       ---> calling to outer -->

a = x(f1)
b = x(b)


a = x() # call and return value hold it inside a        # a()   --> depend --> a callable type--> a()
b = x   # assign x fun ref to b     --> x() -- b()







def outer():
    print('inside outer')
    def inner():
        print('inside inner')


a = outer()     # console -- Inside outer -->  a holds --> None
b = outer       # b -- outer ref -->           outer functions --> outer,b

#a()     # a()   --> return value--> None --> none is not callable---> error
b()     #b -- outer itself--> call to outer --> console --> inside outer

print(a)    # None
print(b)    # outer ref
print(outer)#outer ref

print(a())  # error --> a holds --> None() --> No






import sys
sys.exit(0)

                #outer ---> 1x

def outer():    #1x        # at the time loading of this module/file
    print("Inside Outer Function")

    def inner():        # local --> memory will be given --> at the time outer execution
        print('Inside Inner Function')

    print('Outer Completed..')

    #return inner        # inner ref --in return

#inner() # not visiable -> its local function --> to outer--> only outer can call

#outer() #

print(outer)        #function ref prints  --> 1x
print(outer())      # return value print--> first will a give call to outer--> --> return --> None--> return value


a = outer       # a holds --> function ref-->               #1x --> outer -- a
b = outer()     # b holds --> return value which none       # b --> None    --> b-- hold ref inner

a()     # this will also call to outer function as it holds outer ref-->    a() -- > outer calling
b() # none()    --> not allowed--> none --? none is not calling--> function--class -- method --> callable->

