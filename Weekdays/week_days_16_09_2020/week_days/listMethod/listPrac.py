'''
complex data type:
1) list
         i)Dynamic in nature
         ii)searching operation fast, insertion and deletion operation slow.
         iii)insertion order is preserved
         iv)Duplicates are allowed
         v)Hetrogeneouse objects are allowed
        Array duplicate not allowed
        only homogenic
'''
# list1=[1,2,3,4,5,6,1,7,8,9]
# print("before method :=",list1)
# print("After method...")
# ans=list1.count(1)
# ans=list1.pop()
# list1.remove(9)
# ans=list1.append(25) return none original list append at last
# ans=list1.extend([10,20,30,40,50]) return none and add list at last position
# ans=list1.index(9) return index value
# ans=list1.insert(5,500) insert at index of particular value
# ans=list1.__getitem__(5)
# ans=list1.reverse() return none only original list will be change
# ans=list1.sort(reverse=True) return none and reserved order
import copy
# ans=copy.copy(list1) shallow copy , change in original
# deepans=copy.deepcopy(list1) no change in the original
# ans=list1.__reduce__()

squares=list(map(lambda x:x*2,range(1,10)))

squares1=[item for item in range(1,10)]


print(squares)
print(squares1)
# print(ans)
# print(deepans)

