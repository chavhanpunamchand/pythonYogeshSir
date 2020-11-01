'''
String is group of chars

'''



import sys
exit(0)

# The replace() method returns a copy of the string
# where all occurrences of a substring is replaced with another substring.
s="Punamchand is very bad boy and bad manner person"
print(s.replace('bad','good'))
# output:= Punamchand is very good boy and good manner person



# The find() method returns the index of first occurrence of the substring (if found).
# If not found, it returns -1.
s1="Python is a good programing language and good to start as a software developer"
print(s1.find('good'))
# output :=12


# The string encode() method returns encoded version of the given string.
strg="Django study for website developement"
print(strg.encode())




# The expandtabs() method returns a copy of string with all tab characters '\t' replaced with whitespace characters
# until the next multiple of tabsize parameter.
s1="Now\ta day\tLearing\tpython\tis\tvery\timportant"
print(s1.expandtabs())




# endswith()
# The endswith() method returns True if a string ends with the specified suffix. If not, it returns False.

s1="Python is awesome programming language."

print(s1.endswith('.'))


s1="Punamchand is a good man and he is a programming genius"
# The string count() method returns the number of occurrences of a substring in the given string.
# s2='is'
# n=s1.count(s2)
print(s1.count('a'))
# print(n)



s="Python Programming language"
ns=s.center(80,"*")
print(ns)

firstString = "der Fluß"
secondString = "der Fluss"

print(firstString.lower())
print(secondString.lower())

print(firstString.casefold())
print(secondString.casefold())


# ß is equivalent to ss
if firstString.lower() == secondString.lower():
    print('The strings are equal.')
else:
    print('The strings are not equal.')



s1="Punamchand Moha"
s2="pallavi Chavhan"

# ns1=s1.capitalize()
# ns2=s2.capitalize()
# print(ns1)
# print(ns2)
print(s1.casefold())# lower case convertion