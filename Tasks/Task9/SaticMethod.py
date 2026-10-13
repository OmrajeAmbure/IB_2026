# Wihtout Static method
class StaticMethod:
    def method(self):
        print("ALL methods()")

# How to call it:
obj = StaticMethod()
obj.method()


class stcaticMethod:
    @staticmethod
    def method(): # Not Used Self Beacuse it not depand on object
        print("ALL ")

stcaticMethod.method() # Satic Method Call using the ClassName

