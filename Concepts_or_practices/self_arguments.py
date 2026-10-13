class Demo:
    name = "Om" # default variable or Class Variable
    age = 21
    def marks_summery(self,**marks):# Tempraory Variable
        for subj,mark in marks.items():
            print(f"{subj} : {mark}")
    def display(self):
        print(self.name) # Instence Variable
        print(self.age)


d1 = Demo()
d1.name = "Omraje"
d1.age = 21
d1.display()
d1.marks_summery(math=89,science=78,English=90)
