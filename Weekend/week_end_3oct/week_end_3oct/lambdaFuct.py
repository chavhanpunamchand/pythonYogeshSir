


# full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
# nName=full_name('Punamchand','Chavhan')
# print(nName)


full_name=lambda first,last:f"Full Name:{first.title()} {last.title()}"
nName=full_name("Punamchand","chavhan")
print(nName)


import sys
sys.exit(0)


def indetity(x):
    return x


print(indetity(10))

y=(lambda x:x)(10)
print(y)