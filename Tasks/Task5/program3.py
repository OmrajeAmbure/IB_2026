"""
Employee Management

Create:
employee(**details)

Accept:
name
basic_salary
bonus
department
bonus should have a default value of 5000.

Inside the function create a nested function:
calculate_salary()

Calculate and display:
Employee Name
Department
Basic Salary
Bonus
Total Salary
"""
def employee(bonus=5000,**details):
    def calculate_salary():
        total_salary = details['basic_salary'] + bonus
        return total_salary
    print("Name : ",details['name'])
    print("Department : ",details['department'])
    print("Basic Salary : ",details['basic_salary'])
    print("Bonus : ",bonus)
    print("Total Salary : ",calculate_salary())

employee(
    name="Om",
    basic_salary=50000,
    bonus=10000,
    department="Finance"
)

