"""
7> crete employe class with name ,id,salary add multiple emp to list ask user user
to enter emp id to serach if found disply that emp name and salary if not found display
emp not found ask whether user want to serach for anather emp, find and display highest
salary if multiple emp with highest saalry disply all of them
"""
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    # Method to display employee details
    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}")

# List to store employees
employees = []

# Adding multiple employees
n = int(input("Enter the number of employees to add: "))
for i in range(n):
    print(f"\nEnter details for Employee {i+1}:")
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    salary = float(input("Enter Employee Salary: "))
    employees.append(Employee(emp_id, name, salary))

# Search loop by employee ID
while True:
    search_id = int(input("\nEnter Employee ID to search: "))
    found = False
    
    for emp in employees:
        if emp.emp_id == search_id:
            print("Employee Found!")
            emp.display()  # Calling the display method
            found = True
            break
            
    if not found:
        print("Employee not found")
        
    choice = input("Do you want to search for another employee? (y/n): ").strip().lower()
    if choice != 'y':
        break

# Find and display the highest salary and all employees who have it
if employees:
    max_salary = max(emp.salary for emp in employees)
    highest_paid_emps = [emp for emp in employees if emp.salary == max_salary]
    
    print(f"\nHighest Salary: {max_salary}")
    print("Employee(s) with the highest salary:")
    for emp in highest_paid_emps:
        emp.display()  # Reusing the display method here as well

