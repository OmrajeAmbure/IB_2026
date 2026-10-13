"""
6>analysis of stu result create a stu class with name and marks accept any no of st
store there object in a list disply all display who score 60 or more marks display st
who score below 40 calculate avg marks of student

"""
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def disply(self):
        print(f"Name : {self.name}\nMark : {self.marks}")

students = []
while True:
    print("""
    1. Add Student
    2. Display
    3. Analysis
    4. Exit
    """)
    print("Enter The Choice : ")
    choice = int(input())
    match choice:
        case 1:
            print("Enter The Student Name : ")
            name = input()
            print("Enter The Student Marks (out of 100): ")
            mark = int(input())
            students.append(Student(name,mark))
        case 2:
            print("=================== Student Details ===================")
            for stu in students:
                stu.disply()
                print()
        case 3:
            print("=================== Student Marks Analysis ===================")
            below_60 = []
            below_80 = []
            sum = 0
            for stu in students:
                sum += stu.marks
                if stu.marks <= 60:
                    below_60.append(stu)
                elif stu.marks >= 60 and stu.marks <= 80:
                    below_80.append(stu)
                else:
                    continue
            avg = sum/len(students)

            print("sum : ",sum)
            print("Total Studnet : ",len(students))
            print("\nBelow 60 Marks Students : ")
            for stu in below_60:
                print(f"Name : {stu.name}\nMark : {stu.marks}")
                print()
            print("Below 80 Marks Students : ")
            for stu in below_80:
                print(f"Name : {stu.name}\nMark : {stu.marks}")
                print()
            print("Avrage Of All Students : ",avg)
        case 4:
            break;
