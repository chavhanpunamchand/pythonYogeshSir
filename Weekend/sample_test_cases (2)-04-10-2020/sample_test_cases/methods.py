from selenium import webdriver
import time
FIREFOX_DRIVER_PATH = 'E:/selenium_drivers/geckodriver.exe'
CHROME_DRIVER_PATH = 'E:/selenium_drivers/chromedriver.exe'
APP_URL = 'file:///C:/Users/Yogesh/Desktop/sample.html'

which_browser = {
        "FIREFOX" : 'E:/selenium_drivers/geckodriver.exe',
        "CHROME"  : 'E:/selenium_drivers/chromedriver.exe',
        "OPERA"  : "KEEP OPERA EXECUTABLE PATH HERE",
        "IE"  : "KEEP INTERNET EXPLORER EXECUTABLE PATH HERE",
}

class InvalidBrowserType(BaseException):
    
    def __init__(self,message):
        self.errormessge = message
                
def launch_browser(browser,url):
    epath = which_browser.get(browser)
    driver = None
    print('Driver path -->',epath)
    if epath:
        if browser == "FIREFOX":
            driver = webdriver.Firefox(executable_path=epath)
        elif browser == "CHROME":
            driver = webdriver.Chrome(executable_path=epath)
        elif browser == "SAFARI":
            driver = webdriver.Safari(executable_path=epath)
        elif browser == "OPERA":
            driver = webdriver.Opera(executable_path=epath)
        elif browser == "IE":
            driver = webdriver.Ie(executable_path=epath)
        
        if driver:
            print('Entering \'{}\' '.format(url))
            driver.get(url)
            driver.maximize_window()        # maximize window here-->
            return driver
        else:
            print('Driver not initialized..!')
    else:
        raise InvalidBrowserType("This {} browser type not supported for automation run..!".format(browser))
    

class Emp:
    def __init__(self,eid:int,enm:str,eg:int,gen:str,adr:str,skils:list,des:str,hobbis:list):
        self.empId = eid
        self.empName = enm
        self.empAge = eg
        self.empGender = gen
        self.empAddress = adr
        self.empSkills = skils
        self.empDes = des
        self.empHobbies = hobbis

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''\n{self.__dict__}'''

from selenium.webdriver.support.ui import Select

def employee_registration(empinfo:Emp):

    driver = launch_browser("FIREFOX",APP_URL)

    idelmnt = driver.find_element_by_id('id')   # single input
    nmelmnt = driver.find_element_by_id('nm')   #single
    genelmnt = driver.find_elements_by_name('gender') #list=? wrap --> 2 elements inside list
    adrelmnt = driver.find_element_by_id('adid')    #s
    ageelmnt = driver.find_element_by_id('ag')  #s
    skillselmnt = driver.find_element_by_id('sk') #s            --> select--> to get dropdown feature/properties
    deselmnt = driver.find_element_by_id('ds')#s
    hobelmnt = driver.find_elements_by_name('hobbies')  #wrap -- 6 elements inside list
    submit = driver.find_element_by_xpath('/html/body/form/input[13]')


    print('Step1 : Enter Emp Id :')
    idelmnt.clear()             # idelement-- clear
    idelmnt.send_keys(empinfo.empId)  #empid --> enter --> idelement-- la-->
    time.sleep(1)
    print('Step2 : Enter Emp Name:')
    nmelmnt.send_keys(empinfo.empName)
    time.sleep(1)
    print('Step3 : Select Emp Gender :')
    for gen in genelmnt:
        if gen.get_attribute('value')==empinfo.empGender:
            gen.click()
            break
    time.sleep(1)
    print('Step4 : Enter Emp Address :')
    adrelmnt.send_keys(empinfo.empAddress)
    print('Step5 : Enter Emp Age :')
    ageelmnt.send_keys(empinfo.empAge)
    time.sleep(1)
    print('Step6 : Select Employee Skillsets :')
    skillselect = Select(skillselmnt)
    for skill in empinfo.empSkills: #multichoice
        skillselect.select_by_visible_text(skill)
    time.sleep(1)
    print('Step7 : Select Employee Designation :')
    roleSelect = Select(deselmnt)   #single choice
    roleSelect.select_by_value(empinfo.empDes)
    time.sleep(1)
    print('Step8 : Select Employee Hobbies :')
    for hobby in empinfo.empHobbies:  # CR CRM TV
        for hobbywb in hobelmnt:        # 10 -- wbelement
            if hobbywb.get_attribute('value')==hobby:
                hobbywb.click()
                break
    time.sleep(1)
    #print('Step9 : Submit on Button-->')

    #ch = input('Do you want to click on submit : [Y/N]')
    #if ch=='Y' or ch == 'y':
    #    submit.click()
    return driver



emp = Emp(eid=101,enm='AAAA',eg=25,gen='M',adr="Pune,Shivajinagar",skils=['Python2','Python4','Python1'],des='ds4',
          hobbis=['CR3','CR1','CR5','CR2'])
#employee_registration(emp)


import openpyxl
def read_excel_data():
    workbook = openpyxl.load_workbook('C:\\Users\\Yogesh\\Desktop\\empinfo.xlsx')
    sheet = workbook['EMPINFO']
    noofrows = sheet.max_row
    emplist = []
    for item in range(noofrows):
        rowno = str(item+1)
        print('------------------reading--> {}'.format(rowno) +"-------------------------")
        print('EmpId', sheet['A' + rowno].value)
        print('NAME', sheet['B' + rowno].value)
        print('AGE', sheet['C' + rowno].value)
        print('GEN', sheet['D' + rowno].value)
        print('ADDRESS', sheet['E' + rowno].value)
        print('SKILLS', sheet['F' + rowno].value)
        print('DES', sheet['G' + rowno].value)
        print('HOBBIES', sheet['H' + rowno].value)
        print('------------------reading--> {}'.format(rowno) + "-------------------------")
        emp = Emp(eid=sheet['A' + rowno].value, enm=sheet['B' + rowno].value, eg=sheet['C' + rowno].value,
                  gen=sheet['D' + rowno].value, adr=sheet['E' + rowno].value, skils=sheet['F' + rowno].value.split(','),
                  des=sheet['G' + rowno].value,
                  hobbis=sheet['H' + rowno].value.split(','))
        emplist.append(emp)
    return emplist
emplist = read_excel_data()
print('*'*60)
print(emplist)

for emp in emplist:
    driver = employee_registration(emp)
    ch = input('enter do want to close driver ')
    if ch=='Y' or ch=='y':
        driver.close()


import sys
sys.exit(0)
firebox = webdriver.Firefox()

#if u want to enter url in address bar
firebox.get("application url")

welement = firebox.find_element_by_id('aaa')
welement.send_keys('enter text in input box')

welement.get_attribute('value') #--> #constant value--> once page rendered
welement.get_property('checkbox')# checked/unchecked




# UserName
# Password


#
#       is_enabled --> is_displayed  --> is_clickable       --> element chya-->
#      T        F       T       F          T        F

#       f               t       --> possible
#       f              f       --> Not



#checkbox -- value--> attribute --> checked/unchecked--> property--> dom--render-->
            #attribute--> constant--> checked/unchecked
