"""
8> create a stu class with name ,roll no ,marks display menu 1.add stu , 2,disply all stu
3.serach stu by roll no , 4.update stu marks , 5.delete stu ,6.display class topper ,7.exit
1)do not allowed duplicate roll number
2)display suitble mesg when stu not found all case add
3)keep the menu is running until exit is select
"""
from unittest import case


class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Marks: {self.marks}")

students = []
while True:
    print("""
        1.Add Student 
        2.Disply All Student
        3.Serach Student By Roll No
        4.Update Student Marks 
        5.Delete Student 
        6.Display Class Topper 
        7.EXIT
    """)
    print("Enter The Choice : ")
    choice = int(input())
    match choice:
        case 1:
            print("Enter The Student Roll No : ")
            roll_no = int(input())
            print("Enter The Student Name : ")
            name = input()
            print("Enter The Student Marks (out of 100): ")
            marks = int(input())
            students.append(Student(roll_no,name,marks))
        case 2:
            print("=================== Student Details ===================")
            for stu in students:
                stu.display()
                print()
        case 3:
            print("=================== Serach Student By Roll No ===================")
            print("Enter The Roll No To Search :")
            search = int(input())
            for stu in students:
                if stu.roll_no == search:
                    print(f"Roll No : {stu.roll_no}\nName : {stu.name}\nMarks : {stu.marks}")
                    break
            else:
                print("Student Not Found...!")
        case 4:
            print("=================== Update Student Marks ===================")
            print("Enter The Roll No or Name To Update The Marks :")
            search = int(input())
            for stu in students:
                if stu.roll_no == search or stu.name == search:
                    print("Enter The Updated Marks : ")
                    marks = int(input())
                    stu.marks = marks
                    break
            else:
                print("Student Not Found...!")
        case 5:
            print("=================== Delete Student ===================")
            print("Enter The Roll No To Delete Student :")
            search = int(input())
            for stu in students:
                if stu.roll_no == search:
                    students.remove(stu)  # <-- Changed 'search' to 'stu'
                    print("Student Deleted Successfully!")
                    break
            else:
                print("Student Not Found...!")

        case 6:
            print("=================== Display Class Topper ===================")
            topper = 0
            for stu in students:
                if stu.marks > topper:
                    topper = stu.marks
            print(f"Class Topper : {topper}")
            for stu in students:
                if stu.marks == topper:
                    print(f"\nRoll No : {stu.roll_no}\nName : {stu.name}\nMarks : {stu.marks}")
            
        case 7:
            print("Thank You For Visiting...!")
            break