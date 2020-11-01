from abc import ABC,abstractmethod

# what services are supported --->
class EmployeeService(ABC): # which services u are going to provide

    @abstractmethod
    def add_employee(self,emp):
        pass

    @abstractmethod
    def get_employee(self,empid):
        pass

    @abstractmethod
    def get_all_employees(self):
        pass

    @abstractmethod
    def remove_employee(self,empid):
        pass

    @abstractmethod
    def remove_all_employees(self):
        pass

    @abstractmethod
    def update_employee_info(self,empid,newval):
        pass
