# 1. create set using inbuilt and reomve the duplicates from set

set1= set([1,2,4,4,5])
print(set1)
print(type(set1))


set1.add(6) # single
set1.update([7,8]) # multiple
print(set1)

set1.remove(5) # specific element
print(set1)
element = set1.pop() # last element
print(element)
print(set1)

print(set1.discard(6)) # None
# print(set1.remove(6)) # KeyError: 6



