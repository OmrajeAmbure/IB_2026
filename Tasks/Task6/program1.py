"""
1. Find out the maximum number without using max functions using three numbers
"""

max_ = lambda num1,num2,num3 :  num1 if num1 > num2 else num2 if num2>num3 else num3
print("Maximum Number is : ",max_(5,6,9))

"""
1. Find out the maximum number using map 
"""



