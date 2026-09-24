contact = {
        "omraje": 9158165824,
        "raj": 78348935,
        "vinay": 902384953,
        "mohit": 3752487589
}

while True:
    print('''
        1. Print The ALL contact
        2. Add contact number
        3. search the number
        4. Update the contact
        5. delete contacts
        6. EXIT
    ''')
    operation = int(input())
    match operation:
        case 1:
            for i in contact:
                print(f" Name: {i} Phone Number : {contact[i]} ")
        case 2:
            # Add contact number
            print("Enter The How Many Student Wnat to Add : ")
            n = int(input())
            for i in range(n):
                name = input("Enter The Name : ")
                number = input("Enter The Number : ")
                contact.update({name : number})
        case 3:
            # search the number
            print("Enter The Name To Find The Number: ")
            ser = input()
            for i in contact:
                if i == ser:
                    print(f"| Name: {i}  Phone Number : {contact[i]} ")
        case 4:
            # Update the contact
            print("Enter The Name To Update The Number: ")
            ser = input()
            for i in contact:
                if i == ser:
                    print("Enter The Updated Number : ")
                    value = input()
                    contact[i] = int(value)
        case 5:
            # delete contacts
            print("Enter The Name To Delete The Number: ")
            delete_inp = input()
            poped_value = contact.pop(delete_inp)
        case 6:
            break;


