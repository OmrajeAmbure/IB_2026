class A:
    def show(self):
        print("print A")
class B(A):
    def show(self):
        super().show()
        print("print B")
class C(A):
    def show(self):
        super().show()
        print("print C")
class D(B,C):
    def show(self):
        super().show()
        print("print D")
d = D()
d.show()