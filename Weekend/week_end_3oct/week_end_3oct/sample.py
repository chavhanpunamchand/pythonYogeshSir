import random
class Emp:
    '''This is sample structure to hold emp info -- which will be used to showcase itertools lambda examples'''
    def __init__(self,eid,enm,eag,esal,edept):
        self.empId = eid
        self.empName = enm
        self.empAge = eag
        self.empSal = esal
        self.empDept = edept

    def __str__(self):
        #return f'''\n {self.empId}, {self.empName}, {self.empAge}, {self.empSal}, {self.empDept} '''
        return f'''\n {self.__dict__}'''
    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.empId == other.empId

    def __hash__(self):
        return self.empId



def generate_sequence():
    cnt = 100
    while True:
        cnt = cnt + 1       #stateful
        yield cnt

geninst = generate_sequence()

def getchar():
    return chr(random.randint(65,90)) # A-Z --> one char

def generate_name(): # will generate random name in between --> 5-10 chars
    name = ""
    for item in range(1,random.randint(6,10)): # 5-10 chya madhe
        name = name + getchar()
    return name

DEPT_LIST = ["HR","ACCOUNT","TESTING","DEV","SUPPORT"]

def dummy_employee():
    return Emp(eid=next(geninst),enm=generate_name(),eag=random.randint(22,56),
               esal=round(random.randint(30000,60000)/3,2),edept=DEPT_LIST[random.randint(0,len(DEPT_LIST)-1)])


def getemployess_list(n):
    emplist = []
    for item in range(n):
        emplist.append(dummy_employee())
    return emplist
