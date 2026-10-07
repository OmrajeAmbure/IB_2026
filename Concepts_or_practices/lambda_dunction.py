"""
 return value come with the variable
 lambda function is small ananymous function that can take any numbers of args 
 but contain only one expression

 syntax = var = lambda arg1,arg2... : expression

 condtional statment with : 

"""

"""
power4_1parm = lambda num: num**4
power4_2parm = lambda num,power: num**power              
print(power4_1parm(2))
print(power4_2parm(2,4))
print()


even_odd = lambda num : "Even Number " if num%2==0 else "Odd Number"
print(even_odd(3))
print(even_odd(4))

print()

positive_negative = lambda num : "Positive Number " if num > 0 else "Negative Number"

print(positive_negative(-3))
print(positive_negative(4))

no_arg = lambda : print("Hello")
no_arg()

no_arg1 = lambda a : print(a)
print(no_arg1(7))
no_arg1(7)


# lambda with miltiple conditions

even_odd = lambda num : "Even Number " if num%2==0 else "Odd Value" if num%2==1 else "Number is not valid"
print(even_odd(3))
print(even_odd(4))
print(even_odd(-7))
"""


"""
# map functions
nums = [1,2,3,4,5,6]
show = map(lambda x:x*x,nums)
print(type(show))
print(show)

show = list(map(lambda x:x*x,nums))
print(type(show))
print(show)

# filter functions

nums = [1,2,3,4,5,6]
show = filter(lambda x:x%2==0,nums)
print(type(show))
print(show)
"""
# filter Functions
nums = [0,0,1,2,3,4,-5,6,7,-8,9,-10,-11,12,-13,14,15]

print("Original List : ",nums)
print()
even_number = list(filter(lambda x:x%2==0,nums))
odd_number = list(filter(lambda x:x%2==1,nums))
positive_number  = list(filter(lambda n : n>0,nums))
negative_number  = list(filter(lambda n : n<0,nums))
zeros  = list(filter(lambda n : n==0 ,nums))


print("Even List : ",even_number)
print("Odd List : ",odd_number)
print("Positive Number : ",positive_number)
print("Negative Number : ",negative_number)
print("Zeros : ",zeros)




