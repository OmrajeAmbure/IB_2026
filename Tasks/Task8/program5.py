class CafeTable:
    cafe_name = "COLD CAFE"
    booked_count = 0 

    def __init__(self, table_number):
        self.table_number = table_number
        self.customer_name = ""
        self.number_of_people = 0
        self.booking_status = "Available"

    def book_table(self, name, people):
        if self.booking_status == "Booked":
            print("This table is already booked!")
        else:
            self.customer_name = name
            self.number_of_people = people
            self.booking_status = "Booked"
            CafeTable.booked_count += 1
            print(f"Table {self.table_number} booked successfully!")

    def cancel_booking(self):
        if self.booking_status == "Available":
            print("This table is already empty!")
        else:
            self.customer_name = ""
            self.number_of_people = 0
            self.booking_status = "Available"
            CafeTable.booked_count -= 1
            print(f"Booking cancelled for Table {self.table_number}.")

    def show_table(self):
        print(f"\n--- Table {self.table_number} ---")
        print(f"Status: {self.booking_status}")
        if self.booking_status == "Booked":
            print(f"Customer: {self.customer_name}")
            print(f"People: {self.number_of_people}")



# 1. Create 5 separate table objects in a list
tables = [CafeTable(1), CafeTable(2), CafeTable(3), CafeTable(4), CafeTable(5)]

print(f"=== Welcome to {CafeTable.cafe_name} ===")

while True:
    print("\n1. Book Table \n2. Cancel Booking \n3. Show Table \n4. View Booked Count \n5. Exit")
    choice = input("Choose option (1-5): ")

    if choice == '5':
        print("Goodbye!")
        break
    if choice in ['1', '2', '3']:
        num = int(input("Enter Table Number (1-5): "))
        selected_table = tables[num - 1] 

        if choice == '1':
            name = input("Enter Name: ")
            people = int(input("Enter No. of People: "))
            selected_table.book_table(name, people)

        elif choice == '2':
            selected_table.cancel_booking()

        elif choice == '3':
            selected_table.show_table()

    elif choice == '4':
        print(f"Total booked tables right now: {CafeTable.booked_count}")
        
    else:
        print("Invalid option!")
