"""
Q24. Sum of Numbers Write a Python program using a while loop to accept 
a number n and calculate the sum of numbers from 1 to n.
 
Example: 
Input: 5 
Output: 15 

"""
n = int(input("Enter The Numbers: "))
sum_total = 0

if n <= 0:
    print("Enter A Valid Number...!")
else:
    while n != 0:
        sum_total = sum_total + n
        n = n - 1
    print("Sum:", sum_total)

