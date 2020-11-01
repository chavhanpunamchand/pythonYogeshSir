class A:                        # class -->     A[var6,m1,m2,m3]
    var6 = 10

    def __init__(self):
        self.var7 = 70       # at the time of object creation
        A.var8 = 80
        var9 = 90


    def m1(self):               #m1 -->
        self.var7=70            # at the time of calling to m1-->
        A.var8=80
        var9=90

    def m2(self):
        self.var10 = 70
        A.var11 = 80
        var12 = 90

    def m3(self):
        self.var13 = 70
        A.var14 = 80
        var15 = 90

var16=160

a1 = A()
a2 = A()
a1.m1()
a2.m2()
print(A.__dict__)