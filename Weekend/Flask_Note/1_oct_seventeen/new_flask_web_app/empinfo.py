

class Employee:

    def __init__(self,eid,enm,eag,gen,city,esal,eml,role,skills,hobbies):
        self.empId = eid
        self.empName= enm
        self.empAge= eag
        self.empSalary =esal
        self.empGen = gen
        self.empCity = city,
        self.empRole = role
        self.empEmail = eml
        self.empSkills = skills
        self.empHobbies = hobbies

    def __str__(self):
        return f'''
            ID : {self.empId}     Name : {self.empName}     Age : {self.empAge}
            Salary : {self.empSalary} City : {self.empCity}     Role : {self.empRole}     
            Email : {self.empEmail} Gender : {self.empGen}     
            Skills : {self.empSkills}     Hobbies : {self.empHobbies}
        '''

    def __repr__(self):
        return str(self)

