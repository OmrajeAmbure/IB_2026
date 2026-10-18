# Bank Management System using Hierarchical Inheritance

# Parent Class
class BankAccount:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def display_account(self):
        print("Account Number:", self.account_no)
        print("Account Holder:", self.name)
        print("Account Balance:", self.balance)


# Child Class 1
class SavingsAccount(BankAccount):
    def __init__(self, account_no, name, balance, interest_rate):
        super().__init__(account_no, name, balance)
        self.interest_rate = interest_rate

    def display_savings_account(self):
        self.display_account()
        print("Interest Rate:", self.interest_rate, "%")


# Child Class 2
class CurrentAccount(BankAccount):
    def __init__(self, account_no, name, balance, overdraft_limit):
        super().__init__(account_no, name, balance)
        self.overdraft_limit = overdraft_limit

    def display_current_account(self):
        self.display_account()
        print("Overdraft Limit:", self.overdraft_limit)


# Child Class 3
class SalaryAccount(BankAccount):
    def __init__(self, account_no, name, balance, company_name):
        super().__init__(account_no, name, balance)
        self.company_name = company_name

    def display_salary_account(self):
        self.display_account()
        print("Company Name:", self.company_name)


# List of Objects
accounts = []

# Menu-Driven Program
while True:
    print("\n========== BANK MANAGEMENT SYSTEM ==========")
    print("1. Create Savings Account")
    print("2. Create Current Account")
    print("3. Create Salary Account")
    print("4. Display All Accounts")
    print("5. Search Account")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        account_no = int(input("Enter Account Number: "))
        name = input("Enter Account Holder Name: ")
        balance = float(input("Enter Account Balance: "))
        interest_rate = float(input("Enter Interest Rate (%): "))

        account = SavingsAccount(
            account_no, name, balance, interest_rate
        )
        accounts.append(account)

        print("Savings Account Created Successfully!")

    elif choice == "2":
        account_no = int(input("Enter Account Number: "))
        name = input("Enter Account Holder Name: ")
        balance = float(input("Enter Account Balance: "))
        overdraft_limit = float(input("Enter Overdraft Limit: "))

        account = CurrentAccount(
            account_no, name, balance, overdraft_limit
        )
        accounts.append(account)

        print("Current Account Created Successfully!")

    elif choice == "3":
        account_no = int(input("Enter Account Number: "))
        name = input("Enter Account Holder Name: ")
        balance = float(input("Enter Account Balance: "))
        company_name = input("Enter Company Name: ")

        account = SalaryAccount(
            account_no, name, balance, company_name
        )
        accounts.append(account)

        print("Salary Account Created Successfully!")

    elif choice == "4":
        if len(accounts) == 0:
            print("No Accounts Available.")
        else:
            print("\n========== ALL BANK ACCOUNTS ==========")

            for account in accounts:
                print("\n--------------------------------")

                if isinstance(account, SavingsAccount):
                    account.display_savings_account()

                elif isinstance(account, CurrentAccount):
                    account.display_current_account()

                elif isinstance(account, SalaryAccount):
                    account.display_salary_account()

    elif choice == "5":
        search_no = int(input("Enter Account Number to Search: "))
        found = False

        for account in accounts:
            if account.account_no == search_no:
                print("\nAccount Found!")
                print("--------------------------------")

                if isinstance(account, SavingsAccount):
                    account.display_savings_account()

                elif isinstance(account, CurrentAccount):
                    account.display_current_account()

                elif isinstance(account, SalaryAccount):
                    account.display_salary_account()

                found = True
                break

        if not found:
            print("Account Not Found.")

    elif choice == "6":
        print("Thank You for Using Bank Management System!")
        break

    else:
        print("Invalid Choice! Please Try Again.")
