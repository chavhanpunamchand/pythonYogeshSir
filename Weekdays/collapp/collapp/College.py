

class College:

    def __init__(self,collId,collName,collAddress): #init
        self.collegeRegId = collId
        self.collegeName = collName
        self.collgeAddress = collAddress

    def __str__(self):
        return f'''
            College Id : {self.collegeRegId},
            College Name : {self.collegeName},
            College Address : {self.collgeAddress},
        '''

    def __repr__(self):     #  when u want to print group of collegues
        return str(self)    #str --> one by one list items


c1 = College(10112,"PICT1","PUNE1")
c2 = College(23112,"PICT2","PUNE2")
c3 = College(42112,"PICT3","PUNE3")

#colleges = [College(10112,"PICT1","PUNE1"),College(10112,"PICT1","PUNE1")]

listOfColleges = [c1,c2,c3]


print(listOfColleges) # repr--> one by one to str



import sys
sys.exit(0)

print(c1) # will call str
print(listOfColleges[0]) # will call str

print(c1) # pict1

listOfColleges[0].collegeName = "XYZ"

print(c1) #xyz

print(id(c1))
print(id(listOfColleges[0]))

print(c1,":",listOfColleges[0])
print(type(c1),":",type(listOfColleges[0])) # college type
print(id(c1),id(listOfColleges[0]))# interger repr

'''
print(c2,":",listOfColleges[1])
print(type(c2),":",type(listOfColleges[1]))
print(id(c1),id(listOfColleges[0]))# interger repr
print(c3,":",listOfColleges[2])
print(id(c1),id(listOfColleges[0]))# interger repr
print(type(c2),":",type(listOfColleges[2]))
'''
#0x22883  --> 16      -->       1278137821  --> 10

