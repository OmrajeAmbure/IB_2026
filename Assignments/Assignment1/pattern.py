"""
Q26. Number Pattern Write a Python program 
using a nested for loop to print the following pattern: 

* 
* *
* * *
* * * * 
* * * * * 
"""

for i in range(1, 6):
    for j in range(i):
        print("* ", end="")
    print()  

