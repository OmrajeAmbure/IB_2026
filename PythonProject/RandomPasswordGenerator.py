import random
import string

print("Welcome to the Python Password Generator!")

letters = list(string.ascii_letters)  # a-z and A-Z
digits = list(string.digits)          # 0-9
symbols = list("!@#$%^&*()_+-=[]{}|;:,.<>?")

# Combine all lists into one master list
all_characters = letters + digits + symbols
print(letters,"\n")
print(digits,"\n")
print(symbols)

# 2. Get user input for password length
while True:
    try:
        length = int(input("Enter the desired password length (minimum 8): "))
        if length >= 8:
            break
        print("Password must be at least 8 characters long for security.")
    except ValueError:
        print("Please enter a valid number.")

# 3. Generate the password
password_list = []

for i in range(length):
    random_char = random.choice(all_characters)
    password_list.append(random_char) 

# 4. Convert the list back into a single string
password = "".join(password_list)

print(f"\n Your secure random password is: {password}")
