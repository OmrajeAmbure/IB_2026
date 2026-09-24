# ATM Withdrawl System
print("Enter The Balence : ")
balence = int(input())

"""
    if balence < 0:
        print("Invalid Amount")
    elif withdrawal_amount>=balence:
        print("Insuffecient Balence")
    elif withdrawal_amount>=15000:
        print("Withdrawal Limit Excedded")
    elif withdrawal_amount % 100 != 0:
        print("Amount must be a multiple of 100")
    else:
        balence = balence - withdrawal_amount
        print("Withdrwal Successfully")
        print("Remainig Value is ",balence)
        continue;
"""

while True:
    print("""
        1.Check Balance
        2. Deposite
        3. withdrwal
        4. Exit
    """)
    choice = int(input())
    if choice == 1:
        print(balence)
    elif choice == 2:
        print("Enter The Amount You Want Deposite : ")
        amount = int(input())
        balence = balence + amount
    elif choice == 3:
        print("Enter The Amount You Want withdrwal : ")
        withdrawal_amount = int(input())
        balence = balence - withdrawal_amount
        print("Remainig Value is ",balence)
    elif choice == 4:
        print("Thank YOu")
        break;
