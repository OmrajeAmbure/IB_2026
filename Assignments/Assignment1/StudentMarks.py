"""
Q21. Student Marks
Write a Python program to accept marks of a student and display:
A for marks 90 and above
B for marks 75–89
C for marks 60–74
D for marks 40–59
Fail for marks below 40
Also display Invalid Marks if marks are below 0 or above 100.
"""

print("Enter The Marks : ")
marks = int(input())

if marks > 100 or marks<0:
    print("Invalid Marks. The Marks Should Be Correct Format : ")
else:
    if marks >= 90:
        print("A")
    elif marks >= 75 and marks <= 89:
        print("B")
    elif marks >= 60 and marks <= 74:
        print("C")
    elif marks >= 40 and marks <= 59:
        print("D")
    else:
        print("Fail")


