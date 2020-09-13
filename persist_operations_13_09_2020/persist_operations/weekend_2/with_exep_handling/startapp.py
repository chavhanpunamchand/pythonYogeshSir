





from operations import *
from empinfo import Employee

fileOps = FileOperations()
excelops = ExcelSheetOperations()
import openpyxl


print(excelops.get_all_employees())


import sys
sys.exit(0)
for item in range(2):

    emp = Employee(eid=101+item,enm="AAAA"+str(item),esal=33282.34,eag=29,email='abc@gmail.com')

    try:
        excelops.add_employee(emp)
    except SalaryNotAsPerExpectations as s:
        print(s.message)



import sys
sys.exit(0)
def get_emp(empid):
    emp = fileOps.get_employee(empid)
    if emp:
        print(emp)
    else:
        print('Emp Not Present ')




if __name__ == '__main__':
    #for item in range(1,11):
    #    fileOps.add_employee(Employee(eid=1111+item,enm='AAAA'+str(item),esal=2933.34+item,eag=23+item,email='abc{}@gmail.com'.format(item)))
    print(fileOps.get_all_employees())
    #ans = fileOps.remove_employee(1115)
    #print(ans)