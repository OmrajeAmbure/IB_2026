"""
1> create an employee with name and salary 
create 3 object and store in the list and display all emplyooe using loop
"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")

emp = []
for i in range(3):
    name = input("Enter employee name: ")
    salary = float(input("Enter employee salary: "))
    emp.append(Employee(name, salary))

for e in emp:
    e.display()
