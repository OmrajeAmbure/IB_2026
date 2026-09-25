"""
Q. 23 Student Performance Analyzer
Write a Python program to accept marks of 10 students using a for loop.
For each student, accept marks for:
Python
Java
SQL
Calculate the total and percentage for each student.
Based on the percentage, assign the result:
90 and above → Excellent
75–89 → Very Good
60–74 → Good
40–59 → Average
Below 40 → Fail
The program should finally display:
Total and percentage of each student
Number of students who passed
Number of students who failed
Highest percentage
Lowest percentage
Number of students scoring 75 or above
Challenge: Do not use List, Dictionary, Set, or Tuple. Use only variables, for
loop, if-elif-else, operators, and type conversion.
"""
print("-------------------------Student Performance Analyzer------------------------------")
total_marks = 0
percentage = 0
passed_student = 0
failed_student = 0
higest_percentage = 0
lowest_percentage = 0
above_75 = 0
for i in range(1,11):
    print("Enter The Name Of Student : ")
    name = input()
    print("Enter The Marks of The Following : ")
    print("Pyhton : ")
    pyhton_marks = int(input())
    print("Java : ")
    java_marks = int(input())
    print("SQl : ")
    sql_marks = int(input())

    print(f"Name of Student : {name}")
    
    total_marks = pyhton_marks + java_marks + sql_marks
    percentage = (total_marks / 300) * 100


    if percentage > higest_percentage :
        temp = percentage
        higest_percentage = temp
    

    print(f"Total Marks : {total_marks}")
    print(f"Percentage : {percentage}")
    
    if percentage >= 90:
        print("Excellent")
        above_75 += 1
        passed_student += 1
    elif percentage >= 75 and percentage >= 89:
        print("Very Good")
        above_75 += 1
        passed_student += 1
    elif percentage >= 60 and percentage >= 74:
        print("Good")
        passed_student += 1
    elif percentage >= 40 and percentage >= 59:
        print("Average")
        above_75 += 1
        passed_student += 1
        lowest_percentage += 1
    elif percentage >= 40:
        print("Fail")
        lowest_percentage += 1
        failed_student += 1
    else:
        print("Enter The Valid Marks...!")

print(f"Number of students who passed : {passed_student}")
print(f"Number of students who failed : {failed_student}")
print(f"")
print(f"Number of students scoring 75 or above : {above_75}")

