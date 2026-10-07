from datetime import date
from datetime import datetime


# ============================================================
#                    VISITOR DATA
# ============================================================

visitors = [
    {
        "id": "V001",
        "name": "Rahul",
        "phone": 9876543210,
        "age": 24,
        "purpose": "Interview",
        "person_to_meet": "HR Manager",
        "date_of_visit": date(2026, 10, 27),
        "entry_time": "10:30 AM",
        "exit_time": "12:30 PM",
        "status": "OUT"
    },

    {
        "id": "V002",
        "name": "Rohit",
        "phone": 8945896456,
        "age": 25,
        "purpose": "Seminer",
        "person_to_meet": "Student Coordinator",
        "date_of_visit": date(2026, 9, 28),
        "entry_time": "10:30 AM",
        "exit_time": None,
        "status": "IN"
    },

    {
        "id": "V003",
        "name": "Ramesh",
        "phone": 9876543210,
        "age": 24,
        "purpose": "Gust Session",
        "person_to_meet": "IB Team",
        "date_of_visit": date(2026, 9, 29),
        "entry_time": "04:00 PM",
        "exit_time": "05:00 PM",
        "status": "OUT"
    },

    {
        "id": "V004",
        "name": "Suresh",
        "phone": 9876543210,
        "age": 24,
        "purpose": "Finance Seminer",
        "person_to_meet": "IB Student",
        "date_of_visit": date(2026, 9, 28),
        "entry_time": None,
        "exit_time": None,
        "status": "REGISTERED"
    }
]


# ============================================================
#                    MAIN PROGRAM
# ============================================================

while True:

    print("""
    ========================================
        VISITOR MANAGEMENT SYSTEM
    ========================================

    1. Register Visitor
    2. Check-In Visitor
    3. Check-Out Visitor
    4. View All Visitors
    5. Search Visitor
    6. Currently Inside
    7. Today's Visitors
    8. Visitor History
    9. Daily Report
    10. Exit
    """)

    choice = int(input("Enter your choice: "))


    # ========================================================
    #                    REGISTER VISITOR
    # ========================================================

    match choice:

        case 1:

            print(
                "=========================== "
                "Enter The Register Visitor Details "
                "==========================="
            )

            visitor_id = input("Enter The ID : ")
            name = input("Enter The Name : ")
            phone = int(input("Enter The Phone Number : "))
            age = int(input("Enter Your Age : "))
            purpose = input(
                "Enter The Purpose of The Visit "
                "(eg., Interview): "
            )
            person_to_meet = input(
                "Enter The Person Name to Meet : "
            )

            try:

                year = int(input("Enter Year (YYYY): "))
                month = int(input("Enter Month (1-12): "))
                day = int(input("Enter Day (1-31): "))

                date_of_visit = date(year, month, day)

            except ValueError as e:

                print(f"Invalid date: {e}")
                print("Visitor registration cancelled.")

                continue


            visitors.append({

                "id": visitor_id,
                "name": name,
                "phone": phone,
                "age": age,
                "purpose": purpose,
                "person_to_meet": person_to_meet,
                "date_of_visit": date_of_visit,
                "entry_time": None,
                "exit_time": None,
                "status": "REGISTERED"

            })

            print("Visitor Registered Successfully!")


    # ========================================================
    #                    CHECK-IN VISITOR
    # ========================================================

        case 2:

            print(
                "=========================== "
                "Check-In Visitor "
                "==========================="
            )

            visit_id = input("Enter The Visitor ID : ")

            found = False

            for visitor in visitors:

                if visit_id == visitor["id"]:

                    found = True

                    if visitor["status"] == "IN":

                        print("Visitor is already checked in!")

                    elif visitor["status"] == "OUT":

                        print("Visitor has already checked out!")

                    else:

                        check_in_time = datetime.now().strftime(
                            "%I:%M %p"
                        )

                        visitor["entry_time"] = check_in_time
                        visitor["exit_time"] = None
                        visitor["status"] = "IN"

                        print(
                            f"Visitor Checked In at: "
                            f"{check_in_time}"
                        )

                    break

            if found == False:

                print(
                    f"Visitor ID {visit_id} Not Found...!"
                )


    # ========================================================
    #                    CHECK-OUT VISITOR
    # ========================================================

        case 3:

            print(
                "=========================== "
                "Check-Out Visitor "
                "==========================="
            )

            visit_id = input("Enter The Visitor ID : ")

            found = False

            for visitor in visitors:

                if visit_id == visitor["id"]:

                    found = True

                    if visitor["status"] == "REGISTERED":

                        print(
                            "Visitor has not checked in yet!"
                        )

                    elif visitor["status"] == "OUT":

                        print(
                            "Visitor is already checked out!"
                        )

                    else:

                        check_out_time = datetime.now().strftime(
                            "%I:%M %p"
                        )

                        visitor["exit_time"] = check_out_time
                        visitor["status"] = "OUT"

                        print(
                            f"Visitor Checked Out at: "
                            f"{check_out_time}"
                        )

                    break

            if found == False:

                print(
                    f"Visitor ID {visit_id} Not Found...!"
                )


    # ========================================================
    #                    VIEW ALL VISITORS
    # ========================================================

        case 4:

            print(
                "=========================== "
                "View All Visitors "
                "==========================="
            )

            if len(visitors) == 0:

                print("No visitors found!")

            else:

                for visitor in visitors:

                    print("ID : ", visitor["id"])
                    print("Name : ", visitor["name"])
                    print("Phone : ", visitor["phone"])
                    print("Age : ", visitor["age"])
                    print("Purpose : ", visitor["purpose"])
                    print(
                        "Person To Meet : ",
                        visitor["person_to_meet"]
                    )
                    print(
                        "Date Of Visit : ",
                        visitor["date_of_visit"]
                    )
                    print(
                        "Entry Time : ",
                        visitor["entry_time"]
                    )
                    print(
                        "Exit Time : ",
                        visitor["exit_time"]
                    )
                    print(
                        "Current Status : ",
                        visitor["status"]
                    )

                    print()


    # ========================================================
    #                    SEARCH VISITOR
    # ========================================================

        case 5:

            print(
                "=========================== "
                "Search Visitor "
                "==========================="
            )

            visit_id = input("Enter The Visitor ID : ")

            found = False

            for visitor in visitors:

                if visit_id == visitor["id"]:

                    found = True

                    print("ID : ", visitor["id"])
                    print("Name : ", visitor["name"])
                    print("Phone : ", visitor["phone"])
                    print("Age : ", visitor["age"])
                    print("Purpose : ", visitor["purpose"])
                    print(
                        "Person To Meet : ",
                        visitor["person_to_meet"]
                    )
                    print(
                        "Date Of Visit : ",
                        visitor["date_of_visit"]
                    )
                    print(
                        "Entry Time : ",
                        visitor["entry_time"]
                    )
                    print(
                        "Exit Time : ",
                        visitor["exit_time"]
                    )
                    print(
                        "Current Status : ",
                        visitor["status"]
                    )

                    print()

                    break

            if found == False:

                print(
                    f"Visitor ID {visit_id} Not Found...!"
                )


    # ========================================================
    #                    CURRENTLY INSIDE
    # ========================================================

        case 6:

            print(
                "=========================== "
                "Currently Inside "
                "==========================="
            )

            found = False

            for visitor in visitors:

                if visitor["status"] == "IN":

                    found = True

                    print("ID : ", visitor["id"])
                    print("Name : ", visitor["name"])
                    print("Phone : ", visitor["phone"])
                    print("Age : ", visitor["age"])
                    print("Purpose : ", visitor["purpose"])
                    print(
                        "Person To Meet : ",
                        visitor["person_to_meet"]
                    )
                    print(
                        "Date Of Visit : ",
                        visitor["date_of_visit"]
                    )
                    print(
                        "Entry Time : ",
                        visitor["entry_time"]
                    )
                    print(
                        "Exit Time : ",
                        visitor["exit_time"]
                    )
                    print(
                        "Current Status : ",
                        visitor["status"]
                    )

                    print()


            if found == False:

                print(
                    "No visitors are currently inside."
                )


    # ========================================================
    #                    TODAY'S VISITORS
    # ========================================================

        case 7:

            print(
                "=========================== "
                "Today's Visitors "
                "==========================="
            )

            today = date.today()

            found = False

            print(f"Today's Date : {today}")
            print()

            for visitor in visitors:

                if visitor["date_of_visit"] == today:

                    found = True

                    print("ID : ", visitor["id"])
                    print("Name : ", visitor["name"])
                    print("Phone : ", visitor["phone"])
                    print("Age : ", visitor["age"])
                    print("Purpose : ", visitor["purpose"])
                    print(
                        "Person To Meet : ",
                        visitor["person_to_meet"]
                    )
                    print(
                        "Date Of Visit : ",
                        visitor["date_of_visit"]
                    )
                    print(
                        "Entry Time : ",
                        visitor["entry_time"]
                    )
                    print(
                        "Exit Time : ",
                        visitor["exit_time"]
                    )
                    print(
                        "Current Status : ",
                        visitor["status"]
                    )

                    print()


            if found == False:

                print(
                    "No visitors found for today!"
                )


    # ========================================================
    #                    VISITOR HISTORY
    # ========================================================

        case 8:

            print(
                "=========================== "
                "Visitor History "
                "==========================="
            )

            visit_id = input("Enter The Visitor ID : ")

            found = False

            for visitor in visitors:

                if visit_id == visitor["id"]:

                    found = True

                    print()
                    print("--------- VISITOR HISTORY ---------")

                    print(
                        "Visitor ID     : ",
                        visitor["id"]
                    )

                    print(
                        "Name           : ",
                        visitor["name"]
                    )

                    print(
                        "Visit Date     : ",
                        visitor["date_of_visit"]
                    )

                    print(
                        "Purpose        : ",
                        visitor["purpose"]
                    )

                    print(
                        "Person Met     : ",
                        visitor["person_to_meet"]
                    )

                    print(
                        "Entry Time     : ",
                        visitor["entry_time"]
                    )

                    print(
                        "Exit Time      : ",
                        visitor["exit_time"]
                    )

                    print(
                        "Current Status : ",
                        visitor["status"]
                    )

                    # Calculate duration
                    if (
                        visitor["entry_time"] is not None
                        and visitor["exit_time"] is not None
                    ):

                        entry_time = datetime.strptime(
                            visitor["entry_time"],
                            "%I:%M %p"
                        )

                        exit_time = datetime.strptime(
                            visitor["exit_time"],
                            "%I:%M %p"
                        )

                        duration = exit_time - entry_time

                        print(
                            "Visit Duration : ",
                            duration
                        )

                    else:

                        print(
                            "Visit Duration : Not Available"
                        )

                    print("-----------------------------------")

                    break


            if found == False:

                print(
                    f"Visitor ID {visit_id} Not Found...!"
                )


    # ========================================================
    #                    DAILY REPORT
    # ========================================================

        case 9:

            print(
                "=========================== "
                "Daily Report "
                "==========================="
            )

            today = date.today()

            total_visitors = 0
            currently_inside = 0
            checked_out = 0
            registered = 0

            interview_count = 0
            meeting_count = 0
            seminar_count = 0
            other_count = 0


            # ------------------------------------------------
            # Count today's visitors
            # ------------------------------------------------

            for visitor in visitors:

                if visitor["date_of_visit"] == today:

                    total_visitors += 1

                    if visitor["status"] == "IN":

                        currently_inside += 1

                    elif visitor["status"] == "OUT":

                        checked_out += 1

                    elif visitor["status"] == "REGISTERED":

                        registered += 1


                    # ----------------------------------------
                    # Purpose count
                    # ----------------------------------------

                    purpose = visitor["purpose"].lower()

                    if "interview" in purpose:

                        interview_count += 1

                    elif "meeting" in purpose:

                        meeting_count += 1

                    elif "seminar" in purpose:

                        seminar_count += 1

                    else:
                        other_count += 1


            print()
            print("Date :", today)

            print("----------------------------------------")

            print(
                "Total Visitors   : ",
                total_visitors
            )

            print(
                "Currently Inside : ",
                currently_inside
            )

            print(
                "Checked Out      : ",
                checked_out
            )

            print(
                "Registered       : ",
                registered
            )

            print("----------------------------------------")

            print("PURPOSE SUMMARY")

            print(
                "Interview        : ",
                interview_count
            )

            print(
                "Meeting          : ",
                meeting_count
            )

            print(
                "Seminar          : ",
                seminar_count
            )

            print(
                "Other            : ",
                other_count
            )

            print("----------------------------------------")

            print("VISIT DURATION")

            duration_found = False

            for visitor in visitors:

                if (
                    visitor["date_of_visit"] == today
                    and visitor["entry_time"] is not None
                    and visitor["exit_time"] is not None
                ):

                    duration_found = True

                    entry_time = datetime.strptime(
                        visitor["entry_time"],
                        "%I:%M %p"
                    )

                    exit_time = datetime.strptime(
                        visitor["exit_time"],
                        "%I:%M %p"
                    )

                    duration = exit_time - entry_time

                    print(
                        f"Visitor ID : {visitor['id']} "
                        f"| Name : {visitor['name']} "
                        f"| Duration : {duration}"
                    )


            if duration_found == False:

                print(
                    "No completed visits found for today."
                )

            print("----------------------------------------")


    # ========================================================
    #                         EXIT
    # ========================================================

        case 10:

            print(
                "Thank you for using "
                "Visitor Management System!"
            )

            break


    # ========================================================
    #                    INVALID CHOICE
    # ========================================================

        case _:

            print(
                "Invalid choice! "
                "Please enter a number from 1 to 10."
            )