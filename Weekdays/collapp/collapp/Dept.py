
class DeptInfo: # classname --> start with capital + camelcase
    #self --> current obj ref->  current this
    def __init__(self,did,dnm,dcode):
        self.deptId = did           #vari--> start with small + camelcase+ meaningful
        self.deptName = dnm
        self.deptCode = dcode

    def m1(self):  #python defined --> dunder -->
        return f'''
                Dept Id :   {self.deptId} 
                Dept Name :  {self.deptName}
                Dept Code :  {self.deptCode}
        '''

 # = --> right to left execution  --> memory location --> constructor--init-- props init-->d1
d1 = DeptInfo(111,"Information Tech","IT") # d1 -- dept complex
d2 = DeptInfo(121,"Computer","CSE")   #mem assign --> contructorinit call-->current.id,nm,code--> d2

d1

print(d1) # python will search for str method inside that class-->
                                    #Present --> print whatever written inside str
                                    #absent --> will check parent DeptInfo
                                                #object--> python defined-->str-->
                                                            # memory location


print(d2) # check str-- present- -call



class Dept:
    def __init__(self,did,dnm):
        self.deptId = did
        self.deptName = dnm

d1 = Dept(101,"ABCD")   # d1--> mem -- > 2 propert--> 101,ABCD
d2 = Dept() #error

