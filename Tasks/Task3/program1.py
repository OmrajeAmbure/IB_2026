# create a student data collect name,rollno,marks
students_data = {
        "name":"om",
        "rollno":1,
        "marks":{
            "english":80,
            "maths":70,
            "Science":60,
            "Computer Science":90
        }
    }

# create a dictionary with student included 4 subject marks

total_marks = 0

for i in students_data["marks"].values():
    total_marks = total_marks + i;

avg_score = total_marks/len(students_data["marks"].values())

# display the marks in following form marks and total_marks ,avrage
print()
for i in students_data["marks"]:
    print(f"{i} = {students_data['marks'][i]}")
print()
print("Total Marks : ",total_marks)
print("Average : ",avg_score,"%")
print()

#count the subject marks grater then 80
count = 0
for i in students_data["marks"].values():
    if i >= 80:
        count+=1
print("There are",count,"Student marks grater then 80")

# display higest marks
maxmarks = (max(students_data["marks"].values()))
student = []
mark = 0
for i,j in students_data["marks"].items():
    if j == maxmarks:
        student.append(i)
        mark = j
print(f"Higest Marks : {student[0]} : {mark}")



