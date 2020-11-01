


#property -- decorators--->


#property --> applies business constraints on fields->  withi --> single way to retrive/modify-->
            #married --> gen--male -->      Mr. Name        female --> Miss.name        -->getter
            #unmarried --> gen male -->     Mr Name         female --> Mrs.name         -->getter

#yes--
#empage => 0    -->> 22 --> 56

class InvalidEmpAge(BaseException):
    def __init__(self,msg):
        self.error = msg



#Emp()  --> init -->    Emp -- memory--> tyna-> constructo-- ini-->

class Emp:

    def __init__(self,empnm,empag):     # after memory allocated-->
        self.empName = empnm
        self.empAge = empag

    @property
    def empAge(self):
        return self._empAge

    @empAge.setter
    def empAge(self,empag):
        if empag < 22 or empag > 56:
            raise InvalidEmpAge("Emp Age should be in between 22 - 56 ")
        else:
            self._empAge = empag





class Emp:

    def __init__(self,empnm,empag):     # after memory allocated-->
        self.empName = empnm
        self.set_age(empag)

    def set_age(self,empag):  #setter madhe
        if empag < 22 or empag > 56:
            raise InvalidEmpAge("Emp Age should be in between 22 - 56 ")
        else:
            self._empAge = empag

    def get_age(self):
        return self._empAge

    def __str__(self):
        return f'''\n {self.__dict__}'''

    def __repr__(self):
        return str(self)

    def perform_logic_before_del(self):
        print('emp is going to be deleted..')

    empAge = property(get_age,set_age,perform_logic_before_del)

#if logic is inside constructor --> memory allocation happens before constructor calling-->

#ways --> constructor la--> either-- setter  la -->  direct property la

try:
    e1 = Emp("Mr. AAAA",36)      #  calling setter
    e1.set_age(44)      #calling to setter
    e1.empAge = 32  # internally -- calling setter
    del e1.empAge
except InvalidEmpAge as e:
    print(e.error)

#22-->
import sys
sys.exit(0)




#iterator-- generators--> decorators-->
#classmethod-->staticmethod--> python -->


def outer1(fun):
    def inner(*param):
        print('*'*40)
        fun(param)
        print('*'*40)
    return inner

def outer2(fun):
    def inner(*param):
        print('$'*40)
        fun(param)
        print('$'*40)
    return inner

@outer2         #outer2 loaded --> outer1 loaded --> business fun1 --> business fun1unload--> outer1unl--> outer2
@outer1
def business_one(*param):           #outer2(outer1(business_one))(*param)  -->
    print('inside business one',param)

@outer1            #o1-load --o2 - load -- b2 load --b2-unload--o2-unload--o1-unload
@outer2
def business_two(*param):   #oute1(oute2(businesstwo))(*params) -->
    print('inside business two',param)


business_one(10,20)
#business_two(100,200)

#class-> as iterable--> iterator--> next,iter
#fun -- as iterable --> gen --> yield --

#decorator --> extending functionalities of existing function--> common-->
            #pluin--plugout-->

#decorator--> business function -->     no param
#decorator--> business function -->     business function param -->same param
#decorator--> business function -->     business function param --> all function with diff params
#decorator--> business function -->     decorator -param --> business fun too param..
#decorator chaining--> seq matters --> yes-->


#manager-->

import time

def check_type(typ):
    def smart_cal(fun):
        def inner(*args):
            #print(fun,typ,*args)
            for item in args:
                if type(item)==int:
                    continue
                else:
                    print('Cannot call business function-- int param required...')
                    return "Invalid params"
            if typ=='+':
                return fun(*args)# directly call to business function

            elif typ=='*':     # type *    --> multiply
                iszero = False      #flag -->False
                for item in args:
                    if item==0:
                        iszero=True
                        break
                if not iszero:  # False
                    return fun(*args)
                else:
                    return "Invalid params"
            elif typ=="/":
                if args[1]:
                    return fun(*args)
                else:
                    return "invalid params"
            else:
                return 'Invalid Operation...'
        return inner
    return smart_cal


@check_type('+')        # decorator with param
def add(*args,**kwargs):
    total = sum(args)
    return total

@check_type("/")
def div(*args,**kwargs):        #fun with param
    ans = round(args[0]/args[1],2)
    return ans

@check_type('*')
def mul(*args,**kwargs):
    mul = 1
    for item in args:
        mul = mul*item
    return mul



if __name__ == '__main__':
    ans = div(30,0)
    print(ans)
import sys
sys.exit(0)

def check_fun_perm(fun):
    def inner(*num):    # arbitary -->
        starttime = time.time()
        fun(*num)
        endtime = time.time()
        print(fun,'required time-->',endtime-starttime)
    return inner

@check_fun_perm
def m1():                           #m1()               check_fun_perm(m1)(param)
    print('inside m1- business')
    for item in range(50):
        if item%3==0:
            time.sleep(1)
    print('m1 function completed')

@check_fun_perm
def m2(*num):
    print('inside m2- business')
    for item in range(num[0]):
        if item % 9 == 12:
            time.sleep(1)
    print('m2 function completed')

@check_fun_perm
def m3(*num):
    print('inside m3- business')
    for item in range(num[0]):
        if item % num[1] == 0:
            time.sleep(1)
    print('m3 function completed')

@check_fun_perm
def m4(*num):
    print('inside m4- business')
    for item in range(num[0]):
        if item % 7 == 0:
            time.sleep(1)
    print('completed m4- business')




if __name__ == '__main__':
    m1()
    m2(150)
    m3(50,3)
    m4(40)




import sys
sys.exit(0)


def m1():
    starttime = time.time()
    print('inside m1- business')
    for item in range(100):
        if item%3==0:
            time.sleep(1)
    endtime = time.time()
    print('m1 function completed',endtime-starttime)


def m2():
    starttime = time.time()
    print('inside m2- business')
    for item in range(160):
        if item % 9 == 12:
            time.sleep(1)
    endtime = time.time()
    print('m2 function completed', endtime - starttime)


def m3():
    starttime = time.time()
    print('inside m3- business')
    for item in range(30):
        if item % 6 == 0:
            time.sleep(1)
    endtime = time.time()
    print('m3 function completed', endtime - starttime)


def m4():
    starttime = time.time()
    print('inside m4- business')
    for item in range(80):
        if item % 7 == 0:
            time.sleep(1)
    endtime = time.time()
    print('m4 function completed', endtime - starttime)



if __name__ == '__main__':
    m1()
    m2()
    m3()
    m4()
import sys
sys.exit(0)
def outer(fun):       # x--> holds addition function ch ref-->
    def inner(a,b):
        if type(a) == int and type(b)== int:
            result = fun(a,b)  # will call to addition function with 2 params--> 100,200
            print(result)
        else:
            print('Invalid Params-->')
    return inner


@outer
def addition(a,b):      # param --> 100+200 -> result-->
    result = a+b
    return result

#addition(10,20)            outer(addition)(10,20)

@outer
def sub(a,b):      # param --> 100+200 -> result-->
    result = a-b
    return result

@outer
def div(a,b):      # param --> 100+200 -> result-->
    result = a/b
    return result

#decorator --> without modifying existing logic--> we can add new functionlity-->
            # we can extend the capabilties of existing function -->

@outer          #business logic wrapped inside ---> outer--?> validation -- inside outer-->
def mul(a,b):      # param --> 100+200 -> result-->
    result = a*b
    return result




#outer(addition)(100,200)

sub("A",200)

import sys
sys.exit(0)

outer(100)(10,20)
innref = outer(100) #p--> outer
innref(10,20)   #-- inner





def outer():
  def inner():    # ob1   ob2    ob3 --> every call to outer
    print('inside inner function')
    return inner

a = outer   #outer ref
b = outer()# RETURN VALUE OF OUTER--> INNER REF
c = a()     # RETURN VALUE OF OUTER--> INNER REF

#b and c --> type-->same
            #mem -- diff--> content--

#b and c --> same of diff ---> ?? diff-->









