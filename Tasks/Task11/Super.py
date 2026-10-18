"""
class person: 
    def __init__(self, name): 
        self.name = name 

class student(person): 

    def __init__(self, name, marks): 
        person.__init__(self,name)
        self.marks = marks 

    def display(self): 
        print(f"Name : {self.name}") 
        print(f"Marks : {self.marks}") 

# 4. Added quotes around string 'omraje' and passed name to student
stu = student("omraje", 87) 
stu.display()
"""
class person: 
    def __init__(self, name): 
        self.name = name 

class student(person): 

    def __init__(self, name, marks): 
        super().__init__(name)
        self.marks = marks 

    def display(self): 
        print(f"Name : {self.name}") 
        print(f"Marks : {self.marks}") 

stu = student("omraje", 87) 
stu.display()