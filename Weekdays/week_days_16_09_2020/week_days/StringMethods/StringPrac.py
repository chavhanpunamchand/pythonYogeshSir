'''
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
'''
# 1. nstr=str.capitalize()
# 2. nstr=str.casefold()
# 3. nstr=str.center(50)
# 4. nstr=str.count('a')
# 5. nstr=str.encode('UTF-8','strict')
# 6. str.encode()


# name="punamchand"
# newname=name.capitalize()
# print(name)
# print(newname)
# output:-
# punamchand
# Punamchand

# name="Yogesh"
# print("Yogesh".casefold()) output:- yogesh
# print("Yogesh".center(50))

sen1="Punamchand is a good boy"
print(sen1.find('good'))





import sys
sys.exit(0)

#comparision of string operators(<,<=,>,>=) and equality operators(==, !=) for string
str1=input("Enter 1st String :")
str2=input("Enter 2nd String :")
if str1==str2:
    print("Both string are equal")
elif str1 < str2:
    print("1st string less than 2nd String")
else:
    print("2nd string is greater than 1st string")

# print(nstr)
# string is sequence of charactor,
# char is cov into unicode in python and stored in memory with address
# in python string is a object

name='P'
sub="computer"
desc='''computer field is very important for the future development.
        machine learning and Artificial intelligent work together.
        '''
print(name)
print(sub)
print(desc)




