name = "Python"
version = 3.8
val1 = "This is {} lang and version is {}".format(name,version) # position
val2 = "This is {1} lang and version is {0}".format(version,name)   #index
val3 = "This is {nm} lang and version is {vr}".format(nm=name,vr=version)   #name
val4 = f"This is {name} lang and version is {version}"  #formatting-->
print("This is %s lang and version is %d" % (name,version)  )   # not in use --** # decimal place




print(val1)
print(val2)
print(val3)
print(val4)

import sys
sys.exit(0)


'''
Types of methods --> static  instance    class
Types   of Variables --> global  local  nonlocal     class   instance
Types of Paramerter/args -->    positional named default    *args       **kwargs
string formatting --> positional/named/
class --> object- -. str-- repr --> init --> eq--- hash-->
'''



def m1(x,y=20,*args,**kwargs):      #functions/methods/innerfunctions/inner functions --> applicable
    pass

m1()        # error     --> x - mandatory
m1(20)      #  x=20 y=20    empty       empty
m1(10,"A")  #x=10   y="A"   empty   empty
m1(10,20,30,40) #x=10   y=20    (30,40) empty
m1(50,y=20,a=58,x=20)  # 50     20          empty           (a:,x:)


#def m1(**kwargs,*args): # named --first nad the position ---No  --> rule break..*
#    pass

#m1(a=20,30,40,5) #named params --> last to first-- right to left-->

m1()    #yes        empty       empty
m1(a=20)           #empty       {a:20}
m1(20,30,40,{"a":20,"Y":20},(1,2),[2,34,{1:23,4:55}],a=2993)   #(20,30,40,{"a":20,"Y":20},(1,2),[2,34,{1:23,4:55}])    empty


def m1(x=None,*args,**kwargs):
    print(x,args)


m1(x=30)    # priority -- name la --> x=30          empty       empty
m1(30,30,x=50,y=30)       # x-30        (30)            {x:50,y:30}

m1()    # x-none args:empty--kwargs =empty
m1(10)  #x =10 --> empty    empty
m1(10,"A","x",20,{1:20})    #x-10,(a,x,20,{1:20})   ---> empty
m1(10,a=20,b=20)    #x-10   empty      dict--a:20,b:20
m1(10,10,20,3,(10,20),x=20,y=(10,20,30))  #x -->10      (10,20,3,(10,20))           x:20    y:(10,20,30)

m1(10)      # x--> 10 args--empty
m1(10,20,30)   # x-->10 --->20,30
m1()    #in case of default params -> works--> 10   --> None,Empty


import sys
sys.exit(0)

def m1(**kargs):        #many ---> dict -->name:key ---->value:value
    print('inside m1',kargs,len(kargs))
    #print(kargs.get('x').get('c'))
    print(kargs.get('c')) # as dict directly..

#d = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
m1(a=10,b=20,c=30,d=40)     #multiple params --named


import sys
sys.exit(0)




#*args -->

def m1(*args):      # multiple --params
    sum = 0
    for item in args:   # iterate to tuple --> elements
        if type(item) in (int,float,complex):
            sum = sum+item
    print(sum)

m1(10,20,30,"A","B","3",True)

import sys
sys.exit(0)
def m1(x):
    print(x,len(x)) # no of elements ?  -->

def m2(*x): # if u are not sure about no of params --> *arg --> internally type wud be tuple.. zero to n
    print(x,len(x)) # len --> 1--> 5

m1(10,20,30,40,50) # error --> 1
m2(10,20,30,40,50)  #zero to n


#       *args       --> arbitary
#       **kwargs    --> keyword args
                    #key present            key absent
#dict.get(key)       value                  none                    get(key)--> try: dict[key] --> return None
#dict[key]            value                 keyerror


def calculation(*args):     # args --> tuple -->
    print("Ans  is -->",args,len(args))
    print("Type of args -->",type(args))
     # read tuple --> type dict
    print("Val -->",args[2].get("TT"))       # dict[key]-->value--->agrsv--in key absent--error -->value
                                        #dict.get(key)-->value --> key absent --> None      -->value
    print('---------------------------\n')
#calculation()
#calculation(10)
#calculation(10,20,30)
#calculation(10,20,30,40,"A","B","X",30,4,5,67,("X","Y"),["P","Q","R"],{"XX":100,"YY":200},{10,20})
calculation(("X","Y"),["P","Q","R"],{"XX":100,"YY":200},{10,20},10,"A",True,None)

import sys
sys.exit(0)



#positional param   -- no of params + seq/position
#named params       --> no of params --> names
#default            ---> shud start from right to left--> mandatory = all params - default params-->
                                                            # positional or named


def fun(n1,n2,n3,n4=40,n5=50):
    print(n1,n2,n3,n4,n5)

fun(10,20,30)   #n1 n2 n3
fun(10,20,30,40,52)# n1 n2 n3 n4
fun(n1=10,n2=20,n3=30,n5=56)    # named with default*

#param --> args
                        #no of args               #sequence/position      params-arg-names          remarks
#positional     -->       yes                       yes                         -
#names          -->      yes                        no                          same
#default        -->     all params-default          @Position--yes              -               make sure default value
#                                                    @named --No                same            assignments shud start from last

def fun1(id,name,age=30,sal=2278.34): #params      #fun1("XXXX",20,3993.34)
    print('inside function')
    print("ID :{} Name :{} Age :{} Sal : {}".format(id,name,age,sal))


#fun1(101,"Mr. XXXX",30,34505.6)  #args--> position --> positional args--> no of param ??
#fun1(name="Mr YYY",sal=3773.4,id=123,age=32) # named params/args --> param and args names exactly same

#default with
#fun1(101,"Mr. XXXX",30,2000.3) #       position
#fun1(name="Mr YYY",id=123,age=32)  # named


import sys
sys.exit(0)




#ref --> read -->first inside same ref --> class-->
#nonlocal --> cannot same variable inside innerfu
                #nonlocal keyword --> will always be inside --> inner function-->
                #wherever u write nonlocal -- in that function same variable name cannot be there
                #provides write access to nearest local variable ---*

            #global and nonlocal --> keyword provide write access
                #global -> global variable --> funcitons/innnerfunction/method/inner methods
                #nonlocal --> nearest local variables ---> inside functions--> inside method--> not possible for global



var = "X"   # global    --*****
def outer():
    global var      #no local --> as its already accessing to global
    var = "A"       # do we have local variable here ??? --> no
                        #nonlocal --> global
    def inner1():
        #nonlocal var    # modify access to nearest local -->        outer  -check local var -->
        global var
        var = "B"  # this will be modified..

        def inner2():
            global var  #
            var2 = "X"  #*

            def inner3():                             #3                                2               1           outer       global
                nonlocal var2       #no problem ?
                var2="Y"
#                print(var1)     #read--> check inside local scope ??--no--stepback-->    n               n             y
                print(var2)     #read -->           no                                  no                y
#                print(var3)     #read               no                                  y
                print(var)      #read               n                                   n               n               n           y

var = "A"

def outer():
    var = "B"   #local to outer
    print('inside outer1 -->',var) #B      # read -->local
    def inner():
        nonlocal var            #inner--> cannot have--var variable --> can modify/update--> outer local var value
        print('Inside Inner3 --',var) # C   --> local scope ?--> outer--> yes
        var = "C"
    print('Inside Outer2 -->',var)  #B
    inner()
    print('After Inner Calling4-->',var)#B

outer()
print('Execution Completed5..',var)#A





'''
types --> 
        global --> defined at module/file level     --> global -- just provide write access to the function--> global variable cha
        local  --> inside method/function/inner[method/fun]
        nonlocal --> provides write access to nearest local variable --> this keyword will always inside inner function/method 
        class --> defined at class level or using class name
        instance --> defined with object refer

type of methods                                             how we can access       --> ideally         purpose
        static      --> ()      --> @staticmethod   -->     classname or ref            classname       common business
        class           (cls)   -->@classmethod     -->     classname or ref            classname       factory method
        instance        (self)  --> ----            -->     ref                         ref             business--specific for objects


types of params -->
            positional
            named
            default
            args                --> arbitary        --*
            kargs               --> keyword args    --**

'''