"""
def multiplay(*num):
    print(num)
    print(type(num))
    total = 1;
    for n in num:
        total = total * n;
    return total

print(multiplay(12,32))
print(multiplay(12,32,65))
print(multiplay(12,32,65,8))
print()
"""
"""

def display_namess(*marks,name): # error , we must be define the normal argument first
    print(name)
    for i in marks:
        print(i)
display_namess(87,88,67,"raj")
"""
"""
def display_namess (name,*marks): # error , we must be define the normal argument first
    print(name)
    print(marks)
    for i in marks:
        print(i)
display_namess(87,88,67,"raj")
"""

def compare_number(*num):
    max_1 = num[0]
    for n in num:
        if n > max_1:
            max_1 = n
    print(f"The maximum number is: {max_1}")

"""
print("Enter The Numbers Want To Compare : ")
n = int(input())

for i in range(n):
    inp = int(input(f"Enter number {i+1}: "))
    compare_number(inp)
"""


print("Enter The Numbers Want To Compare : ")
n = int(input())

list1 = []
for i in range(n):
    inp = int(input(f"Enter number {i+1}: "))
    list1.append(inp)
list1 = tuple(list1)
compare_number(*list1)


