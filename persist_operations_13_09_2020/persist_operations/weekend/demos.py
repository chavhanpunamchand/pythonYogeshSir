
class Stud:

    def __init__(self,sid,snm,sag,mrks):
        self.studId = sid
        self.studName = snm
        self.studAge = sag
        self.studAvgMarks = mrks

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)




class InvalidStudException(BaseException):

    def __init__(self, msg ,*args, **kwargs):  # real signature unknown
        self.message = msg


class InvalidStudIdExeption(Exception):
    def __init__(self, msg ,*args, **kwargs):  # real signature unknown
        self.message = msg


def get_int_input(param,type = 'int'):
    try:
        num = int(input('Enter {} :'.format(param)))        # int
        if num<=0 or num>60:
            raise InvalidStudIdExeption("Only Stud ids shud be in between 1 to 60")
    except ValueError as v:
        if type=='int':
            print('required numeric input')
        else:
            print('required numeric/decimal input')

def get_studnet_input():
    try:
        sid = get_int_input("Id ")
        snm = input('Enter StudName :')
        sage = get_int_input("Age ")
        marks = get_int_input("Avg Marks ",'float')
    except InvalidStudIdExeption as s:
        print(s.message)
    except :
        pass
    else:
        if sid and snm and sage and marks:
            stud = Stud(sid,snm,sage,marks)
            print('Stud Instance Created..', stud)
        else:
            raise InvalidStudException("All Mandatory student properties required..!")

try:
    stud = get_studnet_input()
except InvalidStudException as e:
    print(e.message)


print('will be executed smoothly..!')

import sys
sys.exit(0)










import sys
sys.exit(0)
# try --> code which might generate exception --> event or condition-- programmtatically handle-->


# value not accepted- ->     what is correct value --> end user--> problem --> App user friendly-->

no1 = input('Enter Number1 : ')
if no1 and no1.isnumeric():
    num = int(no1)
    print(num)
else:
    print('Enter Numeric value')

import sys
sys.exit(0)

while True:
    try:
        no1 = int(input('Enter Number1 : '))         # code risky --> user can enter any value.
        no2 = int(input('Enter Number2 : '))
        result = no1/no2
        print('Ans is --> ',result)
    except ValueError as e:      # same message for all-->
        print('Numerics are allowed')

    except ZeroDivisionError as e:
        pass
    except BaseException as e:
        print(type(e))
        print('generic error')



print('calling another code..')
