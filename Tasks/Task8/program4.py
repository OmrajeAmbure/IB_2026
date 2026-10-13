class Cafe_Table:

    # Class Level Variables
    Cafe_Name = "COLD CAFE"
    Total_Tables = 5
    Table_Available = 5
    booked_count = 0

    def __init__(self, table_no):
        # Object Level Variables
        self.table_no = table_no
        self.booking_status = False
        self.cust_name = None
        self.no_of_people = 0

    def book_table(self, cust_name, no_of_people):

        if self.booking_status:
            print(f"Table {self.table_no} is already booked.")
            return

        if Cafe_Table.Table_Available == 0:
            print("Sorry! No tables are available.")
            return

        self.cust_name = cust_name
        self.no_of_people = no_of_people

        self.booking_status = True

        Cafe_Table.Table_Available -= 1
        Cafe_Table.booked_count += 1

        print(f"Table {self.table_no} booked successfully!")

    def show_table(self):

        print("\n---------- Booking Details ----------")
        print(f"Table Number   : {self.table_no}")
        print(f"Customer Name  : {self.cust_name}")
        print(f"No of People   : {self.no_of_people}")
        print(f"Booking Status : {self.booking_status}")

    def cancel_booking(self):

        if not self.booking_status:
            print(f"Table {self.table_no} is not booked.")
            return

        self.booking_status = False
        self.cust_name = None
        self.no_of_people = 0

        Cafe_Table.Table_Available += 1
        Cafe_Table.booked_count -= 1

        print(f"Table {self.table_no} booking cancelled.")


# Create 5 tables
customers = [
    Cafe_Table(1),
    Cafe_Table(2),
    Cafe_Table(3),
    Cafe_Table(4),
    Cafe_Table(5)
]


print(f"\n================ Welcome to {Cafe_Table.Cafe_Name} ================")


while True:

    print("\nAvailable Tables:", Cafe_Table.Table_Available)
    print("Booked Tables   :", Cafe_Table.booked_count)

    num = int(input("\nEnter Table Number (1-5): "))

    # Check table number
    if num < 1 or num > len(customers):
        print("Table does not exist!")
        continue

    selected_table = customers[num - 1]

    print("""
1. Book Table
2. Cancel Booking
3. Show Table
4. View Booked Count
5. Show All Tables
6. Exit
""")

    choice = int(input("Choose option (1-6): "))

    match choice:

        case 1:
            name = input("Enter Name: ")
            people = int(input("Enter No. of People: "))

            selected_table.book_table(name, people)

        case 2:
            selected_table.cancel_booking()

        case 3:
            selected_table.show_table()

        case 4:
            print(
                f"Total booked tables right now: "
                f"{Cafe_Table.booked_count}"
            )

        case 5:
            print("\n========== ALL TABLES ==========")

            for table in customers:
                table.show_table()

        case 6:
            print("\nThank You For Visiting Our Cafe...!")
            break
