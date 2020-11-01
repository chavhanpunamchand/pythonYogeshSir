from selenium import webdriver      # webdriver is nothing but ur browser
from selenium.webdriver.support.ui import Select

#dev --> code + site
        #code la
#tester --> application -- site --> no code-->

#functionality --> whitebox             blackbox[]
#testing--> find out all elements we normally interact with-->
#webdriver methods
#webelement methods
#locators -- use cases--> when to use --

#angular --> selenium wont work--> protractor-->
#windows --> popup --> selenium --> rpa -->
#otp --> mobile automation -->

#automation --limitations-->


#selenium version less than 3 version -->
#selenium 3.14 -->

#webdriver --> instance of Browser-->
#webelement -->


FIREFOX_DRIVER_PATH = 'E:/selenium_drivers/geckodriver.exe'
CHROME_DRIVER_PATH = 'E:/selenium_drivers/chromedriver.exe'

APPLICATION_URL = "https://demoqa.com/automation-practice-form/"


def test_radio_buttons():
    browser = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH)
    browser.get('https://www.techlistic.com/p/selenium-practice-form.html')
    print('will select radio buttons')
    genders = browser.find_elements_by_name('sex')
    for gen in genders:
        if gen.get_attribute('value') == 'Male':
            gen.click()
            break

    print('will select--> 2 checkboxss')
    skills = browser.find_elements_by_name('profession')
    for skl in skills:
        if skl.get_attribute('value') in ['Manual Tester', 'Automation Tester']:
            skl.click()


    print('will select --> 2 checkboxes')
    tools  = browser.find_elements_by_name('tool')
    for tl in tools:
        if tl.get_attribute('value') in ['QTP','Selenium Webdriver']:
            tl.click()


    print('Single Choice')
    continents = browser.find_element_by_id('continents')
    Select(continents).select_by_visible_text('Australia')

    print('Multichoice')
    selenium_commands = browser.find_element_by_id('selenium_commands')
    multichoice  = Select(selenium_commands)
    multichoice.select_by_visible_text('Wait Commands')
    multichoice.select_by_visible_text('Navigation Commands')
    multichoice.select_by_visible_text('Switch Commands')

test_radio_buttons()
import sys
sys.exit(0)

def check_for_radio_toolsqa():
    print('Step1 --> Launch Firefox Browser.')
    browser = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH)
    print('Step2 --> Enter Application Url')
    browser.get('https://demoqa.com/automation-practice-form/')
    print('select --gender types--')
    try:
        genders = browser.find_elements_by_name('gender')
        for gen in genders:
            if gen.get_attribute('value') == 'Male':
                gen.click()
                break
    except BaseException as e:
        print(e.args)
        print('inside name')

    try:
        browser.find_element_by_id('gender-radio-1').click()
    except BaseException as e:
        print(e.args)
        print('inside id')

    try:
        browser.find_element_by_xpath('//*[@id="gender-radio-1"]').click()
    except BaseException as e:
        print(e.args)
        print('inside xpath')

check_for_radio_toolsqa()
import sys
sys.exit(0)

def test_radio_buttons():
    browser = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH)
    browser.get('https://www.techlistic.com/p/selenium-practice-form.html')
    genders = browser.find_elements_by_name('sex')
    for gen in genders:
        if gen.get_attribute('value')=='Male':
            gen.click()
            break

    skills = browser.find_elements_by_name('profession')
    for skl in skills:
        if skl.get_attribute('value') in ['Manual Tester','Automation Tester']:
            skl.click()



test_radio_buttons()



#webdriver [browser] -> find_element_by_id [id thru search]   --> webelement [interact] --> send_keys [enter text]-->

import time


def fill_tools_qa_practice_form():
    print('Step1 --> Launch Firefox Browser.')
    browser = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH)
    print('Step2 --> Enter Application Url')
    browser.get('https://demoqa.com/automation-practice-form/')
    print('Step3 --> Enter FirstName ')
    firstname = browser.find_element_by_id('firstName')
    firstname.send_keys('Yogesh')
    print('Step4 --> Enter LastName ')
    lastname = browser.find_element_by_id('lastName')
    lastname.send_keys('Chame')
    print('Step5 --> Enter LastName ')
    email = browser.find_element_by_id('userEmail')
    email.send_keys('yogymax@gmail.com')
    print('Step6 --> Select Gender Types ')
    try:
        browser.find_element_by_xpath('//*[@id="gender-radio-1"]').click()
    except:
        pass
    print('Step7 --> Enter Mobile Number ..')
    try:
        mobile = browser.find_element_by_id('userNumber')
        mobile.send_keys('1231231231')
    except:
        pass
    print('Step8 -->Enter DOB')
    try:
        dob = browser.find_element_by_id('dateOfBirthInput')
        dob.send_keys('03 Nov 2020')
    except:
        pass
    print('Step9 --> Enter Subjects')
    try:
        subjects = browser.find_element_by_xpath('//*[@id="subjectsContainer"]/div/div[1]')
        subjects.send_keys('Python,Selenium,Automation')
    except:
        pass
    print('Step9 --> Enter Subjects')
    try:
        hobbies = browser.find_elements_by_class_name('custom-control-input')
        for hobby in hobbies:
            if hobby.get_attribute('value') in ["1","3"]:
                hobby.click()
    except:
        pass

    print('Step10 --> Enter Current Address ')
    try:
        currAddress = browser.find_element_by_id('currentAddress')
        currAddress.send_keys('Katraj Pune')
    except:
        pass
    print('Step11 --> Select State')
    try:
        dropdown = browser.find_element_by_xpath('//*[@id="state"]/div/div[1]/div[1]') # konal point karel -- dropdown
        dropState = Select(dropdown)    # add all thoese features--required to interact with dropdown
        dropState.select_by_visible_text('NCR')
    except:
        pass

    print('Step12 --> Select City')
    try:
        city = browser.find_element_by_xpath('//*[@id="city"]/div/div[1]/div[1]') #relative-->
        dropCity = Select(city)
        dropCity.select_by_visible_text('Noida')
    except:
        pass


if __name__ == '__main__':
    fill_tools_qa_practice_form()


import sys
sys.exit(0)
def launch_firefox_browser(url,user,pwd):
    try:
        print('Open Firefox window')
        browser = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH)

        print('Enter Application Url in address bar ')
        browser.get(url)    #

        print('Search by id --> Username/Password/Submit --> webelements')

        username = browser.find_element_by_id('txtUsername')    #Search for txtUsername -> id -on webdriver[browser]
        password = browser.find_element_by_id('txtPassword')
        loginbtn = browser.find_element_by_id('btnLogin')

        time.sleep(2)
        username.send_keys(user)   #enter AAAAAAA in username webelement
        time.sleep(2)
        password.send_keys(pwd)   #enter BBBBBBB in password webelement
        time.sleep(2)
        loginbtn.click()    # click on this element

    except BaseException as e:
        print(e.args)


def launch_chrome_browser():
    try:
        browser = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        return browser
    except BaseException as e:
        print(e.args)


if __name__ == '__main__':
    #launch_chrome_browser()    #
    launch_firefox_browser("https://orangehrmopensource-demo.orangehrmlive.com/","admin","admin123") #firefox window--> address bar--application url- username-AAAA-password-BB-loginbtn

