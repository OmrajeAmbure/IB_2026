# Cafe Table System
"""
Cafe Table System

A small café has tables numbered from 1 to 10.

Create a class named "CafeTable".

Each table object should contain:

- Table number
- Customer name
- Number of people
- Booking status

The café name should be common for all tables, so create it as a class-level attribute.

Create the following methods:

1. "book_table()" — Books an available table for a customer.
2. "cancel_booking()" — Cancels the booking and makes the table available again.
3. "show_table()" — Displays the table's booking information.

Conditions:

- A table is initially Available.
- An available table can be booked.
- A booked table cannot be booked again.
- Cancelling a booking should make the table Available.
- Each table must maintain its own booking information.
- Create 5 table objects and test different operations.
- Maintain a class-level count of the currently booked tables.

Task

Write a Python program using classes, objects, instance attributes, class attributes, "__init__()", and methods to implement this café table booking system.
"""
class Cafe_Table:
    # Clss Level Variables
    Cafe_Name = "COLD CAFE" 
    Table_Avliable = 3
    table_no = 0
    booking_status = True
    booked_count = 0
    def book_table(self,cust_name,no_of_people):
        print(f"\nAvlable Tables : {Cafe_Table.Table_Avliable}")
        if Cafe_Table.Table_Avliable == 0:
            self.booking_status = False
        else:
            self.cust_name = cust_name
            self.no_of_people = no_of_people

            Cafe_Table.table_no += 1

            self.table_no = Cafe_Table.table_no

            Cafe_Table.Table_Avliable -= 1

            self.booking_status = True

            Cafe_Table.booked_count += 1

            print(f"Table {self.table_no} booked successfully!")

    print(f"================Welcome to {Cafe_Name}==================")
    def show_table(self):
        if self.booking_status:
            print("\n---------- Booking Details ----------")
            print(f"Table Number   : {self.table_no}")
            print(f"Customer Name  : {self.cust_name}")
            print(f"No of People   : {self.no_of_people}")
            print(f"Booking Status : {self.booking_status}")
        else:
            print("No booking available.")
            
       
    def cancel_booking(self):
         if self.booking_status:
            Cafe_Table.Table_Avliable += 1
            Cafe_Table.booked_count -= 1
            self.booking_status = False
            print(f"Table {self.table_no} booking cancelled.")
         else:
            print("No booking to cancel.")


customers = [Cafe_Table(),Cafe_Table(),Cafe_Table(),Cafe_Table(),Cafe_Table()]

while True:
    num = int(input("Enter Table Number (1-5): "))
    selected_table = customers[num - 1]
    if selected_table :
        print("\n1. Book Table \n2. Cancel Booking \n3. Show Table \n4. View Booked Count \n5. Exit")
        choice = int(input("Choose option (1-5): "))
        match choice:
            case 1:
                name = input("Enter Name: ")
                people = int(input("Enter No. of People: "))
                selected_table.book_table(name, people)
            case 2:
                selected_table.cancel_booking()
            case 3:
                print("Enter The Table No : ")
                search = int(input())
                for i in range(len(customers)):
                    if i == search:
                        i.show_table()
            case 4:
                print(f"Total booked tables right now: {CafeTable.booked_count}")
            case 5:
                print("Thank You For Visting Out Cafe...!")
                break;
    else:
        print("Tables Not Exit")


