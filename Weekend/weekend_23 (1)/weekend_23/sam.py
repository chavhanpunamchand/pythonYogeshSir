# global x --> function will not have x variable-- will refer to global x --> in case global x -- error

#nonlocal --> always inside inner function -->  nonlocal -- write/read access to first local --> inside --> outside

'''
instance --> using ref
local --> inside method/fun
class --> using classname or class level
global --> at module level
nonlocal --> inside inner function using nonlocal


'''



a= 10
def outer():
    nonlocal a        # no local --> global -->       error
    a = 20  #
    def inner():
        global a  # local --> outer chya
        # a --> 20
        a = 25              # modification
        # a --> 25

    inner()
    # a --> 25
    a = 45
    # a --> 45


#a -- 10
outer()
#a - 10



x = 10

def outer():
    #global x
    #x -- 10
    x = 20
    #x --> 20

    def inner():
        #global x -->
        #x - 20
        x = 30
        #x --> 30-->

    # x --> 20
    inner()
    # x --> 30
    x= 40
    # x --> 40

#x --> 10
outer()
#x --> 40



x = 10          # --> global                # sam[x=10]

def outer():    # outer function            # sam[x=10,outer]
    global x  # outer cannot have its own x --> will refer to global x --> global
    #print('2. Inside Outer -->', x) #10
    print('2. Inside Outer -->', x)  # 20  #globae
    x = 20      # global --> global 20
    print('2. Inside Outer -->',x)     #20  #local
    def inner():    # inner function    --> fun --> local for outer-->  #
        global x        # inner cannot have its own x --> will modify to Global x
        x = 30  #local --> inner cha
        print('Inside Inner -->', x)    #30
    print('Inside After Inner Defined -->', x)  #20
    inner()             #
    print('Inside After Inner Called -->', x)# 20


print('1. Outside Outer -->',x) #10       # 10        # sam[x=10,outer]
outer()                             #calling    # sam[x=10,outer[x=20,inner[x=30]]]
print('Outside Outer -->',x) #10

#10 20  20  30  20 10

import sys
sys.exit(0)

'''
    


'''





#private    --> only to those who have given access --> no new members
                #[123]  --> google meet --> gmail addresses -->1@gmail  2@gma   3@gmail
                                                                #       2x@gmail --> expliictly add -->
#restricted -->url -> 1 2 3 -->     123 --> 4 [diff way]

#no -->
#public -- in python -->
# --> normal way -->
#_ -->  internal meaning --> example -- same as  normal variables --scope -- as per type --
#__ -- name mangling -- name changed --> access way is diff --> scope   --> as per type

class Emp:

    var1 = 10
    _var2 = 20
    __var1 = 30


    def __init__(self,n1,n2,n3):
        self.a = n1
        self._b = n2
        self.__c = n3


print(Emp.__dict__)
e1 = Emp(1,2,3)
e2 = Emp(4,5,6)

print(Emp.__dict__) #[emp [var1,_var2,var3],init]
print(e1.__dict__)  #[a=1,b=2,c=3]
print(e2.__dict__)  #[a=4,b=5,c=6]


print('Class Variables')
print(Emp.var1)
print(Emp._var2)
print(Emp._Emp__var3)
#print(Emp.__var3)   # error --> do we have --> __var3 -- inside Emp --> No --> restricted access -->

print('using ref1')
print(e1.var1)
print(e1._var2)
print(e1._Emp__var3)

print('using ref2')
print(e2.var1)
print(e2._var2)
print(e2._Emp__var3)

print('Access Instance variables -->')

print('')
print(e1.a)
print(e1._b)    # internal no meaning -->
print(e1._Emp__c3) # __  --> restricted --> access --->     private --> scope           --> name mangling--> place name change
                        # --> no private --> open to all --> access with predefined way




print(e1.a)
print(e1._b)
print(e1._Emp__c3)










import sys
sys.exit(0)


from python_loopings.weekend_23.SS import A,a

'''
python -- > public -->
                private variables ??? --> NO
                restricted -- variables- -> somewhat -->        __
                
                method --> dont add method with double underscore --> coding --->  __ python provided
                __ --> name mangling --> to make some what restricted --> will not be accessible directly.
                


        __  --> system provided ---> dunder --> 
    -->  normal and underscore varibale -->  self.x             --> self.x  =   normal
    --> _ __ --> naming confusion   -->      self._y            --> self._y =   protected
                                            self.__z            --> self._ClassName__z = private -->    restricted -- cannot be accesed normal way -->
                                                                    name mangling -->
                                                                    
                                                                    variables -- with   self.__var = 
                                                                    
                                          As per Generic Lang -->rules --  
                                            private means --> shud be accessiable within a class
                                            protected --> within package and child classes can accesses -->
                                            
'''

print(A.__dict__)
print('Using --1',a.__dict__)  # we are using that class-- can create instance --> so can access a ref properties
a.x = 30
a._y  = 40
a._A__z= 60

print('Using --2',a.__dict__)  # we are using that class-- can create instance --> so can access a ref properties
print(A.__dict__)



import sys
sys.exit(0)
'''

 ref--read          read - cls/ref
    add/modify      add/modify -- only cls
instance            class
instance            class static


                    read                                    add/modify
class.prop          check only inside                    present-- modify   -- only inside cls
                    same class                           absent -->add
                    present -- retrive
                    absent -- error


ref1.prop       check inside ref1                         present -modify only inside ref1
                    present --retrive                     absent --add -- only inside ref1
                    absent -- class --
                                    present--retrive
                                    absent-- error
ref2.prop       check inside ref2                       present-- modify
                    present --retrive                   absent -- add
                    absent -- class --
                                    present--retrive
                                    absent-- error


class --> var1 -- 10
ref1 ---> var1 --20
ref2 -->  var2 - 30 --



#cls -- cls     --> ref -- ref -- absent tr cls madhn
print(ref2.var1) --> 10 -- do we have var2-- no--> class -- 10
print(ref1.var1) --> 20 -- do we have var2-- yes--10

add/modify -- changes will happen only same either clss or same ref
ref1.var1=33 --> 20 replaced it by 33 -->   inside ref1memory oprtn diff-> new ref --> modify --
ref2.var1=44 --> add inside ref2          --inside ref2                            --> add --
class.var1 = 55 --> modify -- inside class


'''



class A:
    var = 10



print('Class thru cls variable --> read',A.var) # Yes --> 10
a1 = A() # default init -> provided by object class
print('REF thru cls variable --> a1read',a1.var)   #Yes --> 10
a2 = A() # default init -> provided by object class
print('REF thru cls variable --> a2read',a2.var)   #Yes --> 10



print('A Class -->',A.__dict__)
print('a1 Ref -->',a1.__dict__)
print('a2 Ref ',a2.__dict__)

print('After Modification-->')
a1.var = 20     # modify --> a1 --> present -- check a1 --> NO --> will simply add it inside a1 -->20


print('Class thru cls variable --> read',A.var) # Yes --> 10        --> cls
#a1 = A() # default init -> provided by object class
print('REF thru cls variable --> a1read',a1.var)   #Yes --> 20 -->ref to a1 now
#a2 = A() # default init -> provided by object class
print('REF thru cls variable --> a2read',a2.var)   #Yes --> 10 --> refs to cls

print('A Class -->',A.__dict__)
print('a1 Ref -->',a1.__dict__)
print('a2 Ref ',a2.__dict__)

a2.var=10 #- check first inside a2 --> no--> add inside a2
a1.var=30 #-- modify -- a1 --> 20 ---> 30
A.var= 22 #class --> 10 -- 22

print('A Class -->',A.__dict__)  # var --> 22
print('a1 Ref -->',a1.__dict__)# 30
print('a2 Ref ',a2.__dict__)#10
    #read la error possible -->                           #add/modify
#read -->       cls --> only cls present -- error       add/modify --> cls --> only clss
               #objx--> objx -- cls --error                         objx -- modify -- add

print('Class thru cls variable --> read',A.var) # Yes --> 2        --> cls
#a1 = A() # default init -> provided by object class
print('REF thru cls variable --> a1read',a1.var)   #Yes --> 30-->ref to a1 now
#a2 = A() # default init -> provided by object class
print('REF thru cls variable --> a2read',a2.var)   #Yes --> 10 --> refs to cls
