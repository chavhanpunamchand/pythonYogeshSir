'''

Transfer --> break
            continue
            return
            exit
            try
            except
            finally
            pass
            raise

'''

# return --> return --> stops method/fun execution there itself --> and handovers execution
        #point to --> the caller -->
#return  --> can only be inside method/function --> class--> while/if

# return --> immediately caller kde --> only inside fun/method
            # only inside function -- with or without looping
            # breaks everything --> loops and so on --> to caller
# break --> outside current loop ---> only inside looping --> for/while -->
            # with without function --> but only inside for/while
            # break --> breaks only current loop--> outside current loop

for item in range(5):       # 0                         1                        2               3               4
    if item == 3:
        continue
    for sitem in range(5):  # 0:0   0:1  0:2  0:3       1:0 1:1 1:2 1:3
        print(item,sitem,end='\t\t')
        if sitem == 3 or item == 3:
            break  # current loop--> only inner loop

    print('\n')

# 0          1           2           3           4
  #0:0      1:0         2:0         3:0         4:0
  #0:1      1:1         2:1                     4:1
  #0:2      1:2         2:2                     4:2
  #0:3      1:3         2:3                     4:3
import sys
sys.exit(0)

def f1():
    #for item in range(2):     # will be executed directly
    while True:
        num1 = input(input('Enter Number'))     # user is not entering 10 --> loop execution will not stop
        if num1 == 10:
            break      # 10 enter --> while break + function break --> caller

    print('Function execution completed..')

result = f1()   # 10                 --> None           # 10 --> atleast in 2 attempts --> 10 --> will be none

import sys
sys.exit(0)


def m1(input):  # what is expected returns --> int --1      --> str -->AA --> None -
    if input == 10:
        return 1        # will handover -- 1 to the caller --> will immediately stops function execution
    elif input== "A":
        return "AA"


a = m1()  #caller   #  return  --> 100 % --> atleast None
print(a)

# every function/method -- has return --> if no return keywords specificed -- > its return None

def m1():
    print('inside m1')  # after execution -->
                        # return None --> which is implicit condition

a = m1()        # None
