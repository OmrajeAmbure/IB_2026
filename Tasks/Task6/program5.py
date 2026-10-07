# using lambda create a list with evevn number with even numbers replace 10
data = [10,15,20,25,30,35]

even_with_replace_10 = list(map(lambda num : 10 if num%2==0 else num,data))
print(even_with_replace_10)

"""
even_with_replace_10 = list(map(lambda num : num=10 if num%2==0 else num,data))
print(even_with_replace_10)
"""
