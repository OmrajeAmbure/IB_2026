print("-------------------- Movie Ticket Pricing --------------------")

print("Enter How Many Tickets You Want To Buy:")
n = int(input())

print("Enter The Day:")
day = input()

price = 0

count = {
    'Free': 0,
    '100': 0,
    '200': 0,
    '120': 0
}

for i in range(1, n + 1):

    print(f"Enter The Age of {i}:")
    age = int(input())

    if age < 0 or age > 100:
        print("Enter Valid Age...!")
        continue

    if age <= 5:
        print("Ticket Price: Free")
        count['Free'] += 1

    elif age <= 12:
        print("Ticket Price: ₹100")
        price += 100
        count['100'] += 1

    elif age <= 59:
        print("Ticket Price: ₹200")
        price += 200
        count['200'] += 1

    else:
        print("Ticket Price: ₹120")
        price += 120
        count['120'] += 1


# Wednesday discount
if day.casefold() == "wednesday" or day.casefold() == "w":

    print("\nCongratulations! Today is Wednesday.")
    print("You got a 25% discount!")

    discount_price = price * 25 / 100
    final_price = price - discount_price

    print("\n-------------------- Bill --------------------")
    print(f"Number of Tickets       : {n}")
    print(f"Total Amount             : ₹{price}")
    print(f"Discount (25%)           : ₹{discount_price}")
    print(f"Final Amount             : ₹{final_price}")
    print(f"Free Tickets             : {count['Free']}")
    print(f"₹100 Tickets             : {count['100']}")
    print(f"₹200 Tickets             : {count['200']}")
    print(f"₹120 Tickets             : {count['120']}")

else:

    print("\nNo Discount Available...!")

    print("\n-------------------- Bill --------------------")
    print(f"Number of Tickets       : {n}")
    print(f"Total Amount             : ₹{price}")
    print(f"Free Tickets             : {count['Free']}")
    print(f"₹100 Tickets             : {count['100']}")
    print(f"₹200 Tickets             : {count['200']}")
    print(f"₹120 Tickets             : {count['120']}")
