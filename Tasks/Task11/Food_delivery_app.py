# Food Delivery App 
class Customer:
    def __init__(self,name,mobile_number):
        self.name = name
        self.mobile_number = mobile_number
    def customer_deatils(self):
        print(f"Customer Name : {self.name}\n Mobile Number : {self.mobile_number}")
class FoodOrder(Customer):
    def __init__(self,foodname,que,price):
        self.foodname = foodname
        self.que = que
        self.price = price
    def total_bill(self):
        self.price = self.que * self.price
        print(f"FoodName : {self.foodname}\nQuetintay : {self.que}\nPrice : {self.price}")

print("Enter The Name Of Customer : ")
name = input()
print("Enter The Name Of Mobile Number : ")
mobile_number = int(input())
cust = Customer(name,mobile_number)
print("Enter The Name Of Food : ")
foodname = input()
print("Enter The Quentity : ")
que = int(input())
print("Enter The price : ")
price = int(input())
order = FoodOrder(foodname,que,price)

print("\n =================== Customer Details ===================")
cust.customer_deatils()
print("\n =================== Order Details ===================")
order.total_bill()