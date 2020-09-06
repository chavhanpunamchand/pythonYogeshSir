
import sys
name = "Python"
version = 3

#all ways formatting-->

#string formatting
values = "This is {} lang version is {}".format(name,version) #position
print(values)
                                                      #0  1
values = "This is {1} lang version is {0}".format(version,name)#indexes
print(values)
#direct
values = f"This is {name} lang version is {version}"# direct formatting --> 3.6-->
print(values)
#names
values = "This is {x} lang version is {y}".format(y=version,x=name) #names
print(values)



sys.exit(0)






class Account:

    def __init__(self,accNo,accType,accBal):
        self.accountNo = accNo
        self.accountType = accType
        self.accountBalance = accBal

#simple holds single value at a time
#complex --> holds group of elements--> cud be hom or hetro
num = 10        # num var --> pointing to mem location--> on which 10 int type value holds  --> int type object
values = [10,"A","C"]#values--> variable--> holding list type of datatype-->--> list type object
    #list --> system defined datatype --> datatype
    #properties --> system -->
ac1  = Account(10011,"Saving",2883.45)#ac1 --> variable  --memory--> complex-->dev--
                                      #ac1 --> datatype -- Account [no,type,balance]

ac2  = Account(10011,"Saving",2883.45) # ac1 -- user defined datatype
                                        #proper --> developers

#class -->  template/structure/user,system defined structure    --> list-- class-- python- system
                                                               # --> user  developer
#object --  real world entity/instance/ user,system defined datatype

        #account --> structure --> developer        --> specific  to thr business
        #obj --> developer