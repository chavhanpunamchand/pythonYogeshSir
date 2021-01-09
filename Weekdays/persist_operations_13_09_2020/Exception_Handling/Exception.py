'''
try:

except:

finally:

'''

try:
    x=int(input("Enter the first number:"))
    y=int(input("Enter 2nd num"))
    t=x/y
except ZeroDivisionError as z:
    print("In valid number : Please enter the proper number",z)
except ValueError as v:
    print("In valid number : Please enter the proper value of the number",v)
else:
    print("Division of two num is:",t)




