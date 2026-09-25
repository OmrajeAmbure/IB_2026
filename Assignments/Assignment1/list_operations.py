"""
Q28. List Operations
Create a list containing 10 student marks.
Write a program to:
Display all marks.
Display the highest mark.
Display the lowest mark.
Calculate the total marks.
Calculate the average marks.
Count how many students scored more than 75.
"""

student_marks = [85, 92, 78, 65, 90, 88, 72, 95, 80, 70]

# Display all marks
print("Student Marks:", student_marks)

# Display the highest mark
highest_mark = student_marks[0]
for i in student_marks:
    if i > highest_mark:
        highest_mark = i
print("Highest Mark:", highest_mark)

# Display the lowest mark
lowest_mark = student_marks[0]
for i in student_marks:
    if i < lowest_mark:
        lowest_mark = i
print("Lowest Mark:", lowest_mark)

# Calculate the total marks
total_marks = 0
for i in student_marks:
    total_marks += i
print("Total Marks:", total_marks)

# Calculate the average marks
average_marks = total_marks // len(student_marks)
print("Average Marks:", average_marks)

# Count how many students scored more than 75
count_above_75 = 0
for i in student_marks:
    if i > 75:
        count_above_75 += 1
print("Number of students scored more than 75:", count_above_75)

