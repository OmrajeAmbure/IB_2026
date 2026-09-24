python_student = {'rahul','amit','priya','neha'}
java_student = {'amit','neha','rohan','karan'}

print("who learn both java and python : ",python_student & java_student)
print("who learn only python : ",python_student - java_student)
print("who learn only java : ",java_student - python_student)
print("total unqueq student : ",python_student | java_student)
total_unique_student = python_student | java_student
count = 0

for i in total_unique_student:
    count += 1
    print("Count of element : ",count)

    
print("\ntotal unqueq count : ",count)
