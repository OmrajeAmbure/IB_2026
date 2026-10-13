class Demo:
    def __init__(self,name,age,**marks):
        self.name = name
        self.age = age
        self.marks = marks
    def marks_summery(self):
        for subj,mark in self.marks.items():
            print(f"{subj} : {mark}")
    def display(self):
        print(self.name) # Instence Variable
        print(self.age)
d1 = Demo("omraje",21,math=89,science=78,English=90)
d1.display()
d1.marks_summery()
