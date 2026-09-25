"""
Q27. Stop When Number is Found
Write a program that repeatedly accepts numbers from the user.
If the user enters a positive number, continue.
If the user enters 0, stop the program using break.
Display the numbers entered before stopping
"""
# Initialize an empty list to keep track of the numbers entered
numbers = []

while True:
    # Accept input from the user and convert it to an integer
    num = int(input("Enter a number: "))
    
    # If the user enters 0, stop the program using break
    if num == 0:
        break
        
    # If the user enters a positive number, append it and continue
    elif num > 0:
        numbers.append(num)
        
    else:
        print("Negative number entered. Only positive numbers or 0 are expected.")

# Display the numbers entered before stopping
print("Numbers entered before stopping:", numbers)
