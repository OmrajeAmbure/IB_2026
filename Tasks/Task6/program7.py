# find the name len havaing more then 4 len
data = ['om','ram','rohit','vinay','omraje','ashish']

len_4_letter = list(filter(lambda name: len(name)>4,data))
print(len_4_letter)
