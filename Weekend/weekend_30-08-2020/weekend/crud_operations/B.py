from abc import ABC,abstractmethod

class A:  #abc --> contract-- methods

    @abstractmethod     #no impl
    def m1(self):
        pass

    def m2(self):
        print('inside m2')

class B(A):

    def m1(self):
        pass

    def m3(self):
        pass

    def m2(self): # B-->
        pass

a = A()
print(a)

