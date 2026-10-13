"""
create a bank class perfrom the following onjects deposite(parm),withdraw(parm) and display_balence(parms)
for 3 customer
"""


class Bank:
    balance = 5000
    name  = "om"
    ac_number = 8745864785
    
    def deposite(self,deposite_amount):
        self.balance += deposite_amount
    def withdraw(self,withdawl_amount):
        self.balance -= withdawl_amount
    def display(self):
        print(f"Amount : {self.name}")
        print(f"Ac Number : {self.ac_number}")
        print(f"Balance : {self.balance}")

    def display_amount(self):
        print(f"Balance : {self.balance}")
        
cus1 = Bank()
cus1.name = 'raj'
cus1.balance = 50000
cus1.ac_number = 8756745345

cus1.display()
cus1.deposite(5000)
cus1.display_amount()
cus1.withdraw(1000)
cus1.display_amount()






"""
cus2 = Bank()


print("CUSTOMER NUMBER 1 \n\n")
cus2.display()
print("Enter The Amount Deposite : ")
dep = int(input())
cus2.deposite(dep)
cus2.display()
print("Enter The Amount Withdraw : ")
withdraw = int(input())
cus2.withdraw(withdraw)
cus2.display()

cus3 = Bank()


print("CUSTOMER NUMBER 1 \n\n")
cus3.display()
print("Enter The Amount Deposite : ")
dep = int(input())
cus1.deposite(dep)
cus1.display()
print("Enter The Amount Withdraw : ")
withdraw = int(input())
cus1.withdraw(withdraw)
cus1.display()
"""
