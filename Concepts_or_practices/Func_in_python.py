import math

"""
def area_of_circle():
    pi = math.pi
    radius = 3
    area_of_cicle = round(pi*(radius**2),2)
    print(area_of_cicle)

area_of_circle()
print("*****************")
area_of_circle()
"""
"""
n1 = int(input("Enter The num 1 :"))
n2 = int(input("Enter The num 2 :"))
n3 = int(input("Enter The num 3 :"))

def add():
    add = n1+n2+n3
    # print(add)
    return add
def square():
    square1 = n1**2
    square2 = n2**2
    square3 = n3**3
    # print(square1," ",square2," ",square3)
    return square1,square2,square3
    
def display():
    print("Addtion : ",add())
    print("Square : ",square())
display()
"""

def add(n1,n2,n3):
    add = n1+n2+n3
    # print(add)
    return n1

def square(n1,n2,n3):
    square1 = n1**2
    square2 = n2**2
    square3 = n3**3
    # print(square1," ",square2," ",square3)
    return square1,square2,square3
    
def display():
    print("Addtion : ",add(12,4,6))
    print("Square : ",square(12,4,6))
display()


