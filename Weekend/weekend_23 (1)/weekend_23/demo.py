from python_loopings.weekend_23.sample import num,f1,f2,f3  # hello -- refprinting-->10 1x 2x 3x
                                                            #sample[num-10,f1-1x,f2-2x,f3-3x]

from python_loopings.weekend_23.variables import a,f1

print(f1) # ref of f1

def f1(): #f1 -- exisiting ref - release -- new ref         #demo [f1-4x]
    print('inside demo')


print(f1) # new ref of f1

print('printing inside demo')               # demo --<printing
print(num) # 10                                 10 1x 2x 3x

print(f1) # ref of f1

print(f2) #ref of f2

print(f3) #ref of f3