# student Card
class Student_card():
    class_name = "BE AI&DS"
    def __init__(self,name,roll_no,div):
        self.name = name
        self.roll_no = roll_no
        self.div = div

    print(f"========= Welcome TO {class_name} ClassRoom")
    def display(self):
        print(f"Name : {self.name}")
        print(f"Roll NO : {self.roll_no}")
        print(f"Deivison : {self.div}")
s1 = Student_card("omraje",1,"A")
s1.display()
s2 = Student_card("Raj",2,"B")
s2.display()
s3 = Student_card("Mohit",3,"C")
s3.display()
