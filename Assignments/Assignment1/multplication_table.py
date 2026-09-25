"""
Q25. Multiplication Table 
- Write a program to accept a number from the user and print its multiplication table from 1 to 10.
Example: 
Enter number: 7 
7 x 1 = 7 
7 x 2 = 14 
... 
7 x 10 = 70 
"""
num = int(input("Enter The Number You Want To Print Table : "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")
