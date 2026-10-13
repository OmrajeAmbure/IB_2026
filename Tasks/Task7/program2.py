class Student:
    name = "omraje"
    class_ = "BE"
    dep = "AI&DS"
    roll_no = 1
    marks = {"python":80,"java":90,"php":40}

    def diplay_details(self):
        print(f"""
    Name : {self.name}
    Class : {self.class_}
    Department : {self.dep}
    Roll No : {self.roll_no}
        """)
    def marks_details(self):
        sum_ = 0
        max_subj = 0
        min_subj = 100
        for i,j in self.marks.items():
            sum_+=j
            if max_subj < j:
                max_subj = j
            if min_subj > j:
                min_subj = j
        avg = sum_/len(self.marks.values())
        is_pass_or_fail = lambda avg : "PASS" if avg>40 else "FAIL" 
        print("=========Marks Summary===========")
        print(f"""
    Minimim Marks Subject : {max_subj}
    Maxmuim Marks Subject : {min_subj}
    Sum of All Subject : {sum_}
    Avrage Of ALL Subject : {avg}
    PASS OR FAIL : {is_pass_or_fail(avg)}
""")
    
stu1 = Student()
print("Enter The Student Name : ")
stu1.name = input()
print("Enter The Student Class : ")
stu1.class_ = input()
print("Enter The Student Department : ")
stu1.dep = input()
print("Enter The Student Roll No : ")
stu1.roll_no = input()

print("Enter How Many Subject Marks Wnat to Store ? : ")
n = int(input())
for i in range(n):
    subj = input("Enter Subject Name : ")
    marks = input(f"Enter The Marks of {subj} : ")
    stu1.marks.update({subj:marks})

stu1.diplay_details()
stu1.marks_details()

