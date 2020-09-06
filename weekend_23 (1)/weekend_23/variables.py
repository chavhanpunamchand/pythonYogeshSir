class A:

    def __init__(self):
        self.x = 10     # instance          --> normal instance variable
        self._y=20      #instnace   _       --> restricted ---> protected
        self.__z=30     #instance   __      --> more restricted --> private

a = A()
print(a.__dict__)

import sys
sys.exit(0)







#company ----------> Accounts  --------> projects ---- ----> team ----------------> emps
#globale scope      within company      withing account         within account      username/password-- only emp
                                                                                    #empid --- within company
                                                                                    #emp project--> account
                                                                                    #project documents ->
'''
            scope                           def                         purpose                         no of copies                        when gets memory                                             who can access           
global      as long as module            at module level                PI_VALUE                        1                                   module loading                                              within app any module,fun,method,cls
            accesible                   at any place                    APPLICATION NAME


instance    object level                using ref.var = 10                 to hold obj properties          n -depends on obj                object creation, or else we can add later                   any one who can access ref/obj
    

class       class level                 at class level                   only common properties             1                              class loading or else we can add later                       class one who can access ref/obj         
                                        using class.var=10              for obj of that class

local       method/fun level            just inside function/method         temp variables                  n--depends on no of execution    at the time function/method calling
                                        without using cls/ref-->


'''


a = 10      # defined at module level - global

def fun():
    b= 20       #local


class X:
    c  = 30         #class level

    def __init__(self):
        self.y = 20     # y --obj creation --> instance variable

    def m1(self):       #
        self.d = 40     #m1 called --> d -- instance variable
        e = 50          #m1 called --> local
        X.f = 60        #m1 called --> f --class

    u = 60              #class level

X.g = 70            #class level

ob1  = X()      # ob1 --module -- global scope --> ob1 can be accesiable anywhere --> instance variables ???
ob2 = X()       #ob2 -- module -- global scope
ob1.h1 = 80     # instance variable --> ref1 thru  -->
ob2.h2 = 80     #instance variable --> ref2 thru

i = 90      # global scope









#note --> make no class variable variable defined inside contructor -->
        #constructor gets executed for every object--> class variables remains same--then what is the reason to ini every time
        # ini -- once


class A:                     # variables [A[]]
    var = 10                 # variables [ A[var init  m1   m2   m3]  ]

    def __init__(self,v):
        self.t = v       #a1[t=10]      #a2[t=10]
        #A. r = 5         # A[r=10] --> dont defined inside constructor --> once-- for

    def m1(self):
        y = 10                 #local variable --> m1
        self.x = 10             # instance variable --> added thru ref.prop
        A.x = 10                # class variable --> added thru class.prop

    @classmethod
    def m2(self):
        self.p = 20
        A.p = 40

    @staticmethod
    def m3():
        A.u = 20


print(A.__dict__)  # class context --> var=10 m1=m1x m2=m2x m3=m3x init=m4x

a1 = A("A")           #a1 --> t="A
a2 = A("B")           #a2 --> t=B

print(A.__dict__)   #var=10 m1=m1x m2=m2x m3=m3x init=m4x --> added thru a-m1 --> x=10
print(a1.__dict__)  #a1 -- t="A"        --> when u call --> m1 --->   m1--> 288x
print(a2.__dict__)  #a2 =  t="B"        --> when u call -- m1 ---> m1 -- 448x
a1.m1() #  a1 [t="a",m1[y=10]-->3x]--> m1 ins
a2.m1() # a2 [t="B" m1[y=10] -- 4x]


'''                 defined
class variable --> inside class -- class level
                   using class -- classname.variable=val

instance      -->  using ref -->  ref.variable = val


global variable -- define at module level


local variables --> inside function/method


'''



a = 10              #[var [a=10], fun[a=20]]        #global -- variables which is defined at module level

def fun():
    a = 20      # variables defined inside function /method






var1 = 10  # scope of this variable -> global -- module level scope --> varibles-module

def f1():
    var2 = 20  # local variable --> local scope -- only for f1




