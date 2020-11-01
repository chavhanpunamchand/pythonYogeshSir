

class Student:

    def __init__(self,sid,snm,sag,sadr='Pune'):
        self.studId  = sid
        self.studName = snm
        self.studAge = sag
        self.studAddress = sadr

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''
             Student Id : {self.studId}
             Student Name : {self.studName}
             Student Age : {self.studAge}
             Student Address : {self.studAddress}
        '''