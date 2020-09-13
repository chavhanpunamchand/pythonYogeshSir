

class Employee:

    def __init__(self,eid,enm,esal,eag,email):
        self.empId=int(eid)
        self.empName = enm
        self.empAge = int(eag)
        self.empSal = float(esal)
        self.empEmail = email

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''{self.empId},{self.empName},{self.empAge},{self.empSal},{self.empEmail}'''

