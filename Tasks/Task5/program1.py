"""
1.Student Performance
Create:
performance(**marks)

The function should display:

Highest marks
Lowest marks
Average
Passed students
Failed students
Number of students above average
"""
def performance(**marks):
    scores = list(marks.values())
    highest = 0
    lowest = 100
    total_marks = 0
    for mark in marks.values():
        if mark > highest:
            highest = mark;
        if mark > 0 and mark < 100:
            total_marks += mark
        if mark < lowest:
            lowest = mark;
    # highest = max(scores)
    # lowest = min(scores)
    average = total_marks / len(scores)
    passed = 0
    failed = 0
    above_avg = 0
    for mark in marks.values():
        if mark > 40:
            passed += 1
        else:
            failed += 1
        if mark > average:
            above_avg += 1    
    print(f"Highest marks: {highest}")
    print(f"Lowest marks: {lowest}")
    print(f"Average marks: {average:.2f}")
    print(f"Passed students: {passed}")
    print(f"Failed students: {failed}")
    print(f"Number of students above average: {above_avg}")

performance(om=85, vinay=38, rohit=92, mohit=55, raj=70)    
