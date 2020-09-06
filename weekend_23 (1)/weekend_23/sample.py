'''
    1. Procedural       -> sequential execution --> no control -- once
    2. Object Oriented --> execution driven by --> object--> first we need class/structure
    3. Functional Programming --> functions--> function itself objects--> drives execution

    2,3 --> we need to explicitly call --> 1 --> automatic--module loads into memory

    4. Aspect Oriented Programming --* aspect--> cross cutting concerns--

    arr = [10,20,30,40,50]  --> array -- contigous memory allocations --> indexing--> continous


class context -->
        types of methods --     static  class(cls) instance(ref)
        type of variable -->    class     instance

                        method                              variable    reads                               write                  modify
        calling -->     static --> class*    ref              class     only cls variables                  only same cls           only same cls
                        class ---> class*    ref              instance   is present in ref ? ref : cls      onle same ref           only same ref
                        instance  --> ref*

'''

num = 10                # num = 10      ---> 9x     sample [num=10]
print('Hello')         # console print -->          print                   Hello

def f1():               #f1 --> 10x                 sample [num=10,f1=1x]
    print('inside f1')  # first we need explictly give cal to function1 -- n times--> function hold set of instructions-- reuse

def f2():               #f2 --> 3x                  sample [num=10,f1=1x,f2=2x]
    print('inside f2')  # first we need explictly give cal to function2 --> n times ---- reuse


def f3():                                          # sample [num=10,f1=1x,f2=2x,f3=3x]
    print('inside f3 --1')
    print('inside f3 --2')
    print('inside f3 --3')
    f1()
    print('inside f3--4')
    print('inside f3--5')
    f2()
    print('inside f3--completed')


print('references printing -- inside sample ')              # Hello --> refs printing - 10 --1x --2x -- 3x

print(num) # 10                                         sample [num=10,f1=1x,f2=2x]

print(f1) # ref of f1   --> 1x

print(f2) #ref of f2

print(f3) #ref of f3


class ABC:          # whenver class loading happend --> sample [ABC[var-10,init=3x,m1=4x,m2=5x,m3=2x]]
    var = 10        # class variable --> we can call read --> either by classname or ref
                                        # add/modify --> only class name
    def __init__(self):     # at the time of object creation -- zero -   a = ABC()
        pass

    def m1(self):      #instance method -->[1--ref],zero        -->   a = ABC()     a.m1()-->required instance/obj to call this method
        pass           # every instance will get seperate copy as business wud be for indiviual instance
                       # in order to call this we need object
    @staticmethod
    def m2():         # static method --> [0],zero      --> A.m2()  --> make sure u calling it thru cls--> can be called by ob ref
        pass          # to write common business functionalities for all objects
                      # single copy for all objects
    @classmethod
    def m3(self):     # class method --> [1--cls],zero --> A.m3()   --> --> make sure u calling it thru cls--> can be called by ob ref
        pass          # acts as factory methods -- to generate instances
                      # single copy for all instances