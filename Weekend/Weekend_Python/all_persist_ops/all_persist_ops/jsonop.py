from all_persist_ops.service import EmpService

#json is kind of dict --> key shud be str only->
#values -->


from all_persist_ops.helper import get_input_from_user
import json # who provided this module --python --> dumps -- converts object into json format

#emp = get_input_from_user(idwant=True) # emp object-->


FILE_MODE = {"FRESH": "w", "USE_DATA": "a", "VIEW":"r"}

class InvalidFileMode(Exception):

    def __init__(self,msg):
        self.message = msg

def get_file_instance(mode="FRESH"):
    value = FILE_MODE.get(mode)
    if value:
        try:
            return open('employee.json',value) # w-- if not present-- will create new file
        except :
            pass
            #print('Cannot Open File ')
    else:
        raise InvalidFileMode("{} this mode is not supported...".format(mode))


def close_resources(file):
    try:
        if file:
            file.close()        # open -- programmatically file la close..
            #print('File is closed..!')
        else:
            pass
            #print('cannot close as its already closed..')
    except:
        pass






from all_persist_ops.employee import Employee

class EmpJSONServiceImpl(EmpService):
    def add_employee(self, emp):
        if type(emp) == Employee:
            file = get_file_instance(mode='VIEW')   # read sathi open
            allemps = []
            try:
                allemps = json.loads(file.read())
            except:
                pass
            allemps.append(emp.__dict__) #       3+1 --> 4
            close_resources(file) #existing file close  #
            file = get_file_instance(mode='FRESH')  # file--> fresh file open
            jsonemps = []
            for emp in allemps:     # 4 --> fresh file madhe 4 emps write..
                jsonemps.append(emp)
            file.write(json.dumps(jsonemps))
            close_resources(file)
        else:
            print('Invalid Emp')

    def get_employee(self, empid):
        emplist = self.get_all_employees()
        for emp in emplist:
            if emp.empId == empid:
                return emp

        print('No emp with given id..!')

    def get_all_employees(self):
        file = get_file_instance('VIEW')
        allemps = []
        try:
            allemps = json.loads(file.read())
        except:
            return allemps

        emplist = []
        for line in allemps:
            emplist.append(Employee(eid=line.get('empId'),
                                    enm=line.get('empName'),
                                    eag=line.get('empAge'),
                                    esal=line.get('empSalary'),
                                    erol=line.get('empRole')))
        return emplist


    def delete_employee(self, empid):
        allemps = self.get_all_employees()
        found = False
        for emp in allemps:
            if emp.empId == empid:
                found = True
                allemps.remove(emp)
                print('Emp record Removed..')
                break

        if found:
            get_file_instance('FRESH')  # remove existing data--> just added
            for emp in allemps:
                self.add_employee(emp)
        else:
            print('No emp found cannot delete...')

    def update_employee(self, empid, values):
        allemps = self.get_all_employees()
        found = False
        for emp in allemps:
            if emp.empId == empid:
                found = True
                emp.empName = values.empName
                emp.empAge = values.empAge
                emp.empSalary  = values.empSalary
                emp.empRole = values.empRole
                print('Emp record updated...')
                break

        if found:
            get_file_instance('FRESH')  #existing
            for emp in allemps:
                self.add_employee(emp)
        else:
            print('No emp found cannot update...')

    def emp_avg_salary(self):
        emplist = self.get_all_employees()  # will return file to python emp list
        avgsal = 0.0
        noofemps = len(emplist)  # no of emps in list
        totalSal = 0.0
        for emp in emplist:
            totalSal = totalSal + emp.empSalary
        avgsal = totalSal / noofemps
        print('Avg Salary -->', avgsal)
        return avgsal

    def get_rolebased_avg_salary(self, role):
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


if __name__ == '__main__':

    jsonService = EmpJSONServiceImpl()
    '''
    for item in range(3):
        emp = get_input_from_user(idwant=True)  # emp object-->
        jsonService.add_employee(emp)
    '''

    #print('all emps written successfully..!')
    print(jsonService.get_all_employees())
    #print(jsonService.get_employee(101))
    eid  = int(input('Enter id for delete :'))
    #if jsonService.get_employee(eid):
    #    emp = get_input_from_user(idwant=False)  # emp object-->
    #    jsonService.update_employee(eid,emp)
    jsonService.delete_employee(eid)
    #print(jsonService.get_all_employees())



# choice- -> json/file/txt/excel --> 7 ops

#main --> ops ?? --> JSON EXCEL TEXT  CSV
                        #7-8 -- TRY -- DATABASE --*
#https://www.mysql.com/downloads/
# mysql download--> 8.x     ---> postgres --> 12.x --> version s downaload and install -->