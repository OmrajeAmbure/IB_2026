# Tea Order
class Tea_Order():
    count = 0
    Tea_Stall_Name = "B.E. CHAI WALLHA"
    def __init__(self,cust_name,tea_type,quentity):
        self.cust_name = cust_name
        self.tea_type = tea_type
        self.quentity = quentity
        Tea_Order.count += quentity
    print(f"=============Wlecome to {Tea_Stall_Name}=================")
    def display(self):

        print(f"\nCutomer Name : {self.cust_name}")
        print(f"Tea Type : {self.tea_type}")
        print(f"Quentity : {self.quentity}")
        print(f"Total Sells : {self.count}")

cus1 = Tea_Order("Rohit","cold Tea",4)
cus1.display()
cus2 = Tea_Order("Mohit","Hurbale Tea",3)
cus2.display()
cus3 = Tea_Order("Om","Natural Tea",2)
cus3.display()
