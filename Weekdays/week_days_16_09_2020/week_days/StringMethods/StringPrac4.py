'''

format_map()	Formats specified values in a string
index()  	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
'''
str1=input("Enter string: ")
# print("{}".format(str1))
if str1.isspace():
    print("Given string having space......")
elif str1.islower():
    print("Given string is lower Case")
elif str1.isidentifier():
    print("string is identifier.......")
else:
    print("Not identifier....")


