"""Question: Student Management System
Write a menu-driven Python program to create a Student Management System using while True and match-case.

Store student details in a list of dictionaries.

Each student should have:

{
    "roll": 101,
    "name": "Rahul",
    "marks": 85
}
Display the following menu repeatedly:

===== STUDENT MANAGEMENT SYSTEM =====

1. Add Student
2. Display All Students
3. Search Student
4. Update Marks
5. Delete Student
6. Display Topper
7. Exit
Your program should perform the following operations:

Add Student: Accept roll number, name, and marks and add the student to the list. Duplicate roll numbers should not be allowed.

Display All Students: Display details of all students. If no students are available, display an appropriate message.

Search Student: Accept a roll number and display the student's details if found; otherwise display "Student not found".

Update Marks: Accept a roll number and update the marks of that student if the student exists.

Delete Student: Accept a roll number and delete the corresponding student from the list.

Display Topper: Find and display the student who has scored the highest marks.

Exit: Display a suitable message and terminate the program using break.
"""
student = [
    {
    "roll": 101,
    "name": "Rahul",
    "marks": 85
    }
]
topper = 0
while True:
    print("===== STUDENT MANAGEMENT SYSTEM =====")
    print("""
    1. Add Student
    2. Display All Students
    3. Search Student
    4. Update Marks
    5. Delete Student
    6. Display Topper
    7. Exit
    """)
    print("\nEnter Your Choice : ")
    choice = int(input())
    match choice :
        case 1:
            print("Enter The Roll Number : ");
            roll_no= int(input())
            for i in student:
                if roll_no in i.values():
                    break;
                
                print("Enter The Name Of Student : ")
                student_name = input()
                print("Enter The Marks Of Student : ")
                student_mark = int(input())
                student.append({"roll":roll_no,"name":student_name,"marks":student_mark})
        case 2:
            for i in student:
                print("Roll No : ",i.get("roll"))
                print("Nmae    : ",i.get("name"))
                print("Marks   : ",i.get("marks"))
                print()
        case 3:
                print("Enter The Roll Number For Search Student : ");
                roll_no= int(input())
                for i in student:
                    if roll_no in i.values():
                        print("Roll No : ",i.get("roll"))
                        print("Nmae    : ",i.get("name"))
                        print("Marks   : ",i.get("marks"))
                        print()
                        break;
                else:
                    print("Student Not Found...!")
                        
        case 4:
             for i in student:
                    print("Enter The Roll Number : ");
                    roll_no= int(input())
                    if roll_no in i.values():
                        i['roll'] = roll_no
                        # i.update({"roll":roll_no})
                        print("Enter The Name Of Student : ")
                        student_name = input()
                        # i.update({"roll":roll_no})
                        i['name'] = student_name
                        print("Enter The Marks Of Student : ")
                        student_mark = input()
                        i['marks'] = student_mark
                        print("Student Updated Successully...!")
                        break;
             else:
                print("Student Not Found...!")
                        
        case 5:
              print("Enter The Roll Number : ")
              roll_no = int(input())

              for i in student:
                if i.get('roll') == roll_no:
                    print("Student Found")
                    student.remove(i)  
                    break;
                else:
                    print("Student Not Found...!")
            

        case 6:
            """
                marks_list = []
                for i in student:
                    marks_list.append(int(i['marks']))

                topper_mark = max(marks_list)
                print(f"Highest Marks: {topper_mark}\n")

                for j in student:
                    if topper_mark == int(j['marks']):
                        print("Roll No : ", j.get("roll"))
                        print("Name    : ", j.get("name"))
                        print("Marks   : ", j.get("marks"))
                        print()
            """
            if len(student)== 0 :
                print()
            for stu in student:

                if stu['marks'] >= topper:
                    topper += stu['marks']
            print(topper)
        case 7:
            
            print("Thank You For Visiting...!")
            break;
            
                    
