'''
Exception Handling -> why to handle exception --?? -->


        exception       --> events or condition =--> which we can handle programmatically -->
                            --> file read --> file absent -->
                            --> values[3] ---> len(2) ---> exception
                            --> 10/0     --> zerodiv

        error           --> events or condition -->cannot be handled programmatically --> cannot be handled
                                stackoverflow
                                outofmemory
                                hardwarefailure


        try
                    -->risky code- -> which might generate --> exception
                    code which might generate exception -->
        except
                    in case there is exception in try -->
                    if exception is there in program

        else
                    -> in case try successful --> safe code
                    if no exception in try block
        finally -->
                    resource cleaup
                    always -->


        raise


        assert


'''


import time
import random
def get_user_input():
    for item in range(3):       #0  1  2
        try:
            no1 = int(input('Enter Number  : '))
            return no1
        except:
            print('Invalid Number')

    print('Attempt Exceeds...!')

def get_two_numbers_from_user():   #10 --> 5   -- int((no1/no2)/5---> 0    --> list.append()
    while True:
        num1 = get_user_input()
        print('*'*40)
        if num1:
            print('Number 1 --> ',num1)
            num2 = get_user_input()

            print('Number 2 --> ', num2)
            if num2:
                return num1,num2

val = get_two_numbers_from_user()
print(val)

import sys
sys.exit(0)
'''
print('Generated No {}/{}'.format(no1,no2))
        time.sleep(1)
        ans = no1/no2       # 10 2  --> 5      --> 3.33                33333333333
        print(ans,int(ans),int(ans)%num==0)
        if int(ans)%num==0:
            values.append(ans)
            print('Till -->', values)

        if len(values)==noof:
            return values


values =  get_random_value_divisiable_by(10,5)
print(values)

'''

#REGISTRATION --> SECTIONS --> PERSONAL DETAILS -- ADDRESS DETAILS -- EDUCATIONAL --
#APPLICATION --> USER ENGAGE --> ???--? APPLICATIONS --> USERBASE --> APPLICATION EARNING --
#APPICATION USER FRIENDLY-->