from all_persist_ops.service import EmpService
from all_persist_ops.employee import Employee


#r w a r+ w+ a+ rb wb   rb+ wb+ x
#read -> file shud be present --> else error
#write --> always create new file -->
#a --> if present-- use if not create new
#r+w+ -> read       /       write

#r --> read --> r+  -- read and write both operations--> file shud be present
#w --> write --> w+ -- read and write both operations --> file always new
#a+ --> read_write --> read and write both operations --> file present--use absent --> new create
#x --> file present asel tr error--> if no file --> no error..- --> only checks--->
            #if file present--error
#b--> binary mode--> serialization --> purpose
#x --> if file present--error --> this is just to check file present or not..
# r - ?  check file present - file present-- use krto --> reading--> if file present-- filenotfoundexception
# w -?   always new file --> let it be file present or absent.. existing data will be vanished in case file present
# x -? file present --> error--> file present--**
        #IF FILE PRESENT-- CREATE ANOTHER FILE --? R ? nO - W -nO -- a-nO -->X


FILE_MODE = {"FRESH": "w", "USE_DATA": "a", "VIEW":"r"}

class InvalidFileMode(Exception):

    def __init__(self,msg):
        self.message = msg

def get_file_instance(mode="FRESH"):
    value = FILE_MODE.get(mode)
    if value:
        try:
            return open('employee.txt',value) # w-- if not present-- will create new file
        except :
            print('Cannot Open File ')
    else:
        raise InvalidFileMode("{} this mode is not supported...".format(mode))
    '''
    if mode==value:
        return open('employee.txt','w') #REMOVE OLD DATA AND CREATE FRESH FILE
    elif mode=='USE_DATA':
        return open('employee.txt', 'a')#USE EXISTING FILE--EXISTING DATA APPEND--
    elif mode=='VIEW':
        return open('employee.txt', 'r')    #JUST VIEW--READ PURPOSE
    '''

def close_resources(file):
    try:
        if file:
            file.close()        # open -- programmatically file la close..
            print('File is closed..!')
        else:
            print('cannot close as its already closed..')
    except:
        pass

SEPERATOR = "\t\t"
class EmpTextServiceImpl(EmpService):

    def add_employee(self, emp):
        if type(emp) == Employee:
            file = get_file_instance(mode="USE_DATA")
            empinfo = str(emp.empId) +SEPERATOR+ emp.empName +SEPERATOR+ str(emp.empAge) +SEPERATOR+ str(emp.empSalary) +SEPERATOR+ emp.empRole +"\n"
            file.write(empinfo)
            close_resources(file)
            print('Emp <{}> added into text file..!'.format(emp.empId))
        else:
            print('Invalid Emp..cannot add into file.')

    def get_employee(self, empid):
        emplist = self.get_all_employees()
        for emp in emplist:
            if emp.empId == empid:
                return emp

        print('No emp with given id..!')

    def get_all_employees(self):
        file = get_file_instance('VIEW')
        alllines = [line.strip() for line in file.readlines()]
        emplist = []
        for line in alllines:
            row = line.split(SEPERATOR)
            emplist.append(Employee(eid=row[0],enm=row[1],eag=row[2],esal=row[3],erol=row[4]))
        return emplist


    def delete_employee(self, empid):   #ID
        femp = self.get_employee(empid) # PRESENT OR NOT
        if femp:    #PRESENT - ASEL TR
            allemps = self.get_all_employees()  # ALL EMP RETRIVE
            for emp in allemps:
                if emp.empId==empid:
                    allemps.remove(emp)    # ID MATCHING WALA REMOVE KARA
                    print('Emp removed..')
                    break
            file = get_file_instance('FRESH')  # EXISTING DATA  # EXISTING DATA REMOVE N CREATE NEW FILE
            for emp in allemps: # WRITE ALL DATA EXCEPT-- DELETED EMP
                empinfo = str(emp.empId) + SEPERATOR + emp.empName + SEPERATOR + str(emp.empAge) + SEPERATOR + str(
                    emp.empSalary) + SEPERATOR + emp.empRole + "\n"
                file.write(empinfo)

        else:
            print('Specificed employee id not present so canno remove')


    def update_employee(self, empid, values):
        femp = self.get_employee(empid)
        if femp:
            allemps = self.get_all_employees()
            for emp in allemps:
                if emp.empId==empid:
                    emp.empName = values.empName
                    emp.empAge = values.empAge
                    emp.empSalary = values.empSalary
                    emp.empRole = values.empRole
                    print('Emp Info Updated')
                    file = get_file_instance('FRESH')  # EXISTING DATA  # EXISTING DATA REMOVE N CREATE NEW FILE
                    for emp in allemps:  # WRITE ALL DATA EXCEPT-- DELETED EMP
                        empinfo = str(emp.empId) + SEPERATOR + emp.empName + SEPERATOR + str(emp.empAge) + SEPERATOR + str(
                            emp.empSalary) + SEPERATOR + emp.empRole + "\n"
                        file.write(empinfo)
                    break
        else:
            print('No Emp found with given id..cannot update..')


    def emp_avg_salary(self):
        emplist = self.get_all_employees()  # will return file to python emp list
        avgsal = 0.0
        noofemps = len(emplist) # no of emps in list
        totalSal = 0.0
        for emp in emplist:
            totalSal = totalSal + emp.empSalary
        avgsal = totalSal/noofemps
        print('Avg Salary -->',avgsal)
        return avgsal


    def get_rolebased_avg_salary(self,role):
        emplist = self.get_all_employees()
        noOfemps = 0
        totalSal = 0.0
        for emp in emplist:
            if emp.empRole == role:
                noOfemps = noOfemps + 1
                totalSal = totalSal + emp.empSalary
        avgsal = totalSal / noOfemps
        print('Manager\'s Avg Salary -->', avgsal)
        return avgsal

    def get_employees_based_on_role(self, rolenm):
        emplist = self.get_all_employees()
        newemplist = []
        for emp in emplist:
            if emp.empRole == rolenm:
                newemplist.append(emp)
        return newemplist


def get_input_from_user(idwant = False):
    eid = 0
    if idwant:
        print('Enter Values for Add Operations')
        eid = int(input('Enter Emp Id : '))
    else:
        print('Enter Values for update Operations')
    name = input('Enter Emp Name : ')
    eage = int(input('Enter Emp Age : '))
    esal = float(input('Enter Emp Salary : '))
    role = input('Enter Emp Role : ')
    return Employee(eid, name, eage, esal, role)

if __name__ == '__main__':
    textservice = EmpTextServiceImpl()
    #emp = get_input_from_user(idWant = True) # true--> id user kdn
    #textservice.add_employee(emp)
    #emps = textservice.get_all_employees()
    #print(emps)
    #emp = textservice.get_employee(101)
    #print(emp)
    #emps = textservice.get_all_employees()
    #print('Before -->',emps)
    #eid = int(input('Enter Id for Update :'))
    #empup = get_input_from_user(idwant=False)
    #textservice.update_employee(eid,empup)
    #emps = textservice.get_all_employees()
    #print('After ',emps)
    #eid = int(input('Enter Id for Delete :'))
    #textservice.delete_employee(eid)
