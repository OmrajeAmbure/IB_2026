set1 = {}
print(type(set1))

set2 = {1,2,3,4,4,5,6,7,7,"om",5.6,"raj"}
print(type(set1))
print(set2)
print(set2)
print(set2)
set2.add("54") # add one element
print(set2)
set2.update(["vivak","mohit"]) # add multiple element
print(set2)
set2.remove("vivak") # remove but throw error
print(set2)
set2.discard("mohit") # remove the element but not show the error
print(set2)


set2.pop() 
print(set2)
set2.pop() 
print(set2)

set2.clear()
print(set2)
