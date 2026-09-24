"""
Q6. Employee Attendance Analyzer – Hard
Write a Python program to store the attendance status of 10 employees in a
list.
The list should contain only:
"P" # Present
"A" # Absent
"L" # Leave
The program should:
1. Count the total number of Present, Absent, and Leave employees.
2. Calculate the attendance percentage using:
Attendance % = Present / Total Working Days × 100
For this question, assume 10 working days for each employee.
3. Display employees whose attendance is below 75%.
4. Store employee names and their number of present days in a dictionary.
5. Find the employee with the highest number of present days without
using max().
6. Display:
Employee Name
Present Days
Attendance Percentage
Attendance Status
where:
● >= 75% → Eligible
● < 75% → Low Attendance
Concepts expected:
List, Dictionary, for loop, if-elif-else, comparison operators, variables and
nested logic
"""

print("=================== Employee Attendance Analyzer =========================")
totoal = 0
employees = []
Attendance = 0
print("Enter How Many Employee Want Store : ")
total_emp = int(input())
for i in range(1,total_emp+1):
    print(f"Enter The {i} Employee Details : ")
    print("Enter The Name : ")
    name = input()
    # Assume of 10 days Records
    status = []
    present = 0
    absent = 0
    leave = 0
    eligable = []
    for i in range(1,6):
        print(f"Enter The Day {i} Status [A|P|L]: ")
        inp = input()
        if inp == "P" or inp == "p":
            status.append(inp)
            present += 1
        elif inp == "A" or inp == "a":
            status.append(inp)
            absent += 1
        elif inp == "L" or inp == "l":
            status.append(inp)
            leave += 1
    Attendance = present / 5 * 100
    if Attendance >= 75:
        eligable.append("Eligible")
    else:
        eligable.append("Low Attendance")

    employees.append({"Name":name,"Attendance_record":status,"Prsent_days":present,"Absent_days":absent,"Persentage":Attendance,"Attendance_status":eligable[0] })
    


for i in range(len(employees)):
    for i,j in employees[i].items():
        print(f"{i}:{j}")
