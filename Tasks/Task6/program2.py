# create a list of dictionary with name & salary keys ,there should total 5 dict
data1 = [
    {
        "name": "om",
        "salary": 50000
    },
    {
        "name": "raj",
        "salary": 70000
    },
    {
        "name": "rohit",
        "salary": 80000
    },
    {
        "name": "mohit",
        "salary": 30000
    },
    {
        "name": "vinay",
        "salary": 10000
    }
]

# 1. sort according to salary

data1.sort(key = lambda sal: sal["salary"])
print("According to salary")
for emp in data1:
    print(emp)
    

# 2. Find Employees with a salaey > 45000

filterd_data = list(filter(lambda sal: sal["salary"]>45000,data1))
print("Employees with a salaey > 45000")
for emp in filterd_data:
    print(emp)
