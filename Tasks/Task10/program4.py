"""
4>create an emplpoye class with name, id ,salary employee details from user store
multiple emp in the list allow user to add emp until they choose to stop and display
all emp detail at the end
"""
class Employee:
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary
    def display(self):
        print(f"""
EMP_ID : {self.id} 
Name : {self.name} 
Salary : {self.salary}
        """)

employees = []
while True:
    print(""" 
        1. Add Employee
        2. Diaplay
        3. Stop
    """)
    print("Enter The Choice To Perform Opration : ")
    chocie = int(input())
    match chocie:
        case 1:
            print("Enter The Employee ID : ")
            id = input()
            print("Enter The Name of Employee : ")
            name = input()
            print("Enter The Salary of Employee : ")
            salary = input()
            employees.append(Employee(id,name,salary))
        case 2:
            print("================== Employees Details ==================")
            for emp in employees:
                if emp == None:
                    print("No Employees Found...!")
                emp.display()
            print()
        case 3:
            break

