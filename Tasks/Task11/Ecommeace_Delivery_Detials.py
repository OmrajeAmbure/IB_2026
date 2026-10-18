class Product:
    def __init__(self,prodact_name,price):
        self.product_name = prodact_name;
        self.price = price
    def prodact_display(self):
        print(f"Product Name : {self.product_name}\nPrice : {self.price}")
class Order(Product):
    def __init__(self,product_name,price,quentity):
        super().__init__(product_name,price)
        self.quentity = quentity
    def order_deatils(self):
        total_amount = self.price * self.quentity
        print(f"Quentuity : {self.quentity}\nTotal Amount : {total_amount}")
class Delivery(Order):
    def __init__(self,product_name,price,quentity,develery_add,charges=40):
        super().__init__(product_name,price,quentity)
        self.develery_add = develery_add
        self.charges = charges
    def delivery_details(self):
        print(f"Delivery Address : {self.develery_add}\nDelivery Charges : {self.charges}")
print("Enter The Name Of Product : ")
product = input()
print("Enter The Price Of Product : ")
price = int(input())
print("Enter The Quentity Of Product : ")
quen = int(input())
print("Enter The Address : ")
add = input()
d = Delivery(product, price, quen, add,50)
print("========================== Order Summary =======================")
d.prodact_display()
d.order_deatils()
d.delivery_details()
