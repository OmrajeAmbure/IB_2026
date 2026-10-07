"""
Student Management
Create:
student_report(**students)

Example:
student_report(
    Rahul=85,
    Amit=35,
    Sneha=92,
    Priya=67,
    Karan=28
)

The program should display:
Total Students
Highest Scorer
Lowest Scorer
Average Marks
Passed Students
Failed Students
Inside student_report(), create

nested functions:

find_total()
find_average()
find_topper()
find_lowest()
check_result()
"""
def student_report(**students):
    def find_total():
        return len(students)
    def find_average():
        if len(students) == 0:
            return 0
        sum = 0 
        for mark in students.values():
            sum += mark
        avg = sum/len(students)
        return avg
    def find_topper():
        if len(students) == 0:
            return 0
        topper = 0
        topper_res = {}
        for name,mark in students.items():
            if mark > topper:
                topper = mark
                topper_res['topper'] = name,mark
        return topper_res['topper']
    def find_lowest():
        if len(students) == 0:
            return 0
        lowest = 100
        lowest_res = {}
        for name,mark in students.items():
            if mark < lowest:
                lowest = mark
                lowest_res['lowest'] = name,mark
        return lowest_res['lowest']
    def check_result():
        passed = {}
        failed = {}
        for name,mark in students.items():
            if mark > 40 and mark < 100:
                passed[name] = mark
            elif mark > 0 and mark < 40:
                failed[name] = mark
        return [passed,failed]
    print(f"""
Total Students : {find_total()}
Highest Scorer : {find_topper()}
Lowest Scorer  : {find_lowest()}
Average Marks  : {find_average()}\n""")
    res = check_result()
    for i in range(len(res)):
        if i == 0:
            print("Passed Students : ")
            for name,mark in res[i].items():
                print(f"{name} : {mark}",end=",")
        if i == 1:
            print("\nFailed Students : ")
            for name,mark in res[i].items():
                print(f"{name} : {mark}",end=",")
student_report(
    Rahul=85,
    Amit=35,
    Sneha=92,
    Priya=67,
    Karan=28
)
