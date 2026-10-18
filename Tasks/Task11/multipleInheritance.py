class A:
    def process(self):
        print("Inside A")

class B(A):
    def process(self):
        print("Inside B")

class C(A):
    def process(self):
        print("Inside C")

class D(B, C):
    pass

obj = D()
obj.process()  # Output: Inside B

print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
