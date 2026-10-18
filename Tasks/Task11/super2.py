class A:
    def work(self):
        print("Work A")
class B(A):
    def work(self):
        super().work()
        print("Work B")
class C(B):
    def work(self):
        super().work()
        print("Work C")
c = C()
c.work()