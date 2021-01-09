'''
Graceful terminatrion of your program is nothing but exception handling.
try:

except:
else:
finally:

Divison of two number
try:
    a=int(input("Enter the 1st num: "))
    b=int(input("Enter the 2nd num: "))
except ValueError as v:
    print("Invalid number plesae enter proper number...")
else:
    try:
        c=a/b
    except ZeroDivisionError as z:
        print("2nd number zero not allowed please enter Non Zero......")
    else:
        print("Division of two number is: ",int(c))
'''

try:
    a=int(input("Enter the 1st num: "))
    b=int(input("Enter the 2nd num: "))
    c = a / b
except ValueError as v:
    print("Invalid number plesae enter proper number...")
except ZeroDivisionError as z:
        print("2nd number zero not allowed please enter Non Zero......")
else:
    print("Division of two number is: ",int(c))
