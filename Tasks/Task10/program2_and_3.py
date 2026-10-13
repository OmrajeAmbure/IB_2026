"""
2> crete the students calss with name and marks store five students object in a list
and display only thise studen whose score more 80 marks

3>create a list of students object aacept the name from the user and search for students
in the list if found display their marks otherwise print student not found
"""
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def disply(self):
        print(f"Nmae : {self.name} Marks : {self.marks}")

    def display_mraks(self):
        print(f"Marks : {self.marks}")

students = []

for stu in range(3):
    print(f"Enter The Name Of Student {stu+1} : ")
    name = input()
    print(f"Enter The Mark Of Student {stu+1} (out of 100) : ")
    mark = int(input())
    students.append(Student(name,mark))

for stu in students:
    if stu.marks > 80:
        stu.disply()

# Search For Students
print("Enter The Name To Search The Student : ")
search_name = input()
for stu in students:
    if stu.name == search_name:
        stu.display_mraks()
        break;
else:
    print("Student Not Found...!")