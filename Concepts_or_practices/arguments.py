"""
def show(name,age,marks,add):
    print(name)
    print(age)
    print(marks)
    print(add)

show("om",15,marks=78,add="pune")
"""
"""
def emp(id,name,salary,dep="Dev"):
    print(id)
    print(name)
    print(salary)
    print(dep)

emp("rama",4000,salary=5500)
"""
"""
emp(101, "rama", 4000, "HR")                 
emp(101, "rama", 4000, dep="HR")
emp(101, "rama", dep="HR",salary=4000) 
emp(101, "rama", salary=4000, dep="HR") 
emp(id=101, name="rama", salary=4000, dep="HR") 
emp(dep="HR", id=101, salary=4000, name="rama")
"""
"""
def student_details(name, age, **marks):
    marks_subjet = marks.values()
    print("Name :", name.upper())
    print("Age :", age)
    print("=======Marks=========")
    for sub,mar in marks.items():
        print(f"{sub} : {mar}")
    print("=======Avrage=========")
    print("Avg Marks :", sum(marks_subjet)/len(marks))

student_details("om", 21, eng=87, science=78, history=90)

"""
def student_details(name,dep="AIDS", *marks,**details):
    marks_subjet = marks
    print("Name :", name.upper())
    print("=======Details=========")
    for i,j in details.items():
        print(f"{i} : {j}")
    print(f"Department : {dep}")
    print("=======Avrage=========")
    print("Avg Marks :", sum(marks_subjet)/len(marks_subjet))

student_details("om",87, 78, 90, age=43,add="pune",gender="Male")
# postition maters when we combine aribatory agrs and abritory kwargs
# positionak -> first , atibatory -> second,key aribitory kargs -> last
# student_details((87, 78, 90), name= "om",age=43,add="pune",gender="Male")

print()
def outer(a,b):
    def inner(b):
        print(a)
        print(b)
    inner(b)
outer(43,32)
print()

def calculate_result(marks):
    def is_pass(mark):
        return mark >= 40 # hide The logic 

    for mark in marks:
        if is_pass(mark):
            print(mark, "Pass")
        else:
            print(mark, "Fail")

calculate_result([80, 35, 67, 20])
