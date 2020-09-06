#simple
#complex
#user defined types *


def m1():       # memory localation            m1 ---> 100x
    print('m1--one')

def m1():                                     # m1 --> 283x
    print('m1---two')



m1()    # 283--> m1-- two

class Customer:

    def __init__(self, cid, cnm): # 182x
        self.custId = cid
        self.custName = cnm

    def __init__(self,cid,cnm,cag,cemail,cbal): #1834x
        self.custId = cid
        self.custName = cnm
        self.custAge = cag
        self.custEmail = cemail
        self.custBalance = cbal

#c2 = Customer(10,"ABC") # this wont work
#print(c2)
c1 = Customer(10,"ABC",29,"abc@gmail.com",2992.34)
print(c1)