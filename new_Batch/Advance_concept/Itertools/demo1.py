
for item in range(1,128):
    print(chr(item),item)



values1 = [1022,20,30,40,50,60,70,80,90,100] # 10 elements
print(id(values1))
print(id(values1[0]))
values2 = [1022,20,30,40,50,60,70,80,90,100]  #10 elements
values1.extend(values2) # 20 elements
print(id(values1[0]))
print(id(values1))

