"""
Q30. Collection-Based Problem
Create a list containing duplicate numbers:
numbers = [10, 20, 10, 30, 20, 40, 50, 30, 60]
Write a Python program to:
Remove duplicate values using a Set.
Convert the Set back into a List.
Sort the resulting List.
Convert the List into a Tuple.
Display the final Tuple.
Create a Dictionary containing the number as the key and its square as the value.
Expected dictionary format:
    {
        10: 100,
        20: 400,
        30: 900
    }
"""
numbers = [10, 20, 10, 30, 20, 40, 50, 30, 60]

# Remove duplicate values using a Set.
removed_values = set(numbers)
print("After Remove Duplicated : ",removed_values)

# Convert the Set back into a List.
list_converstion = list(removed_values)
print("After Converting Set Into List : ",list_converstion)

# Sort the resulting List.
list_converstion.sort()
print("After Sorting Result : ",list_converstion)

# Convert the List into a Tuple And Display the final Tuple.
tuple_converstion = tuple(list_converstion)
print("After Converting List Into Tuple : ",tuple_converstion)

# Create a Dictionary containing the number as the key and its square as the value.
n = int(input("Enter How Many Square You Want (ex.,upto 10) : "))
n = abs(n)
squares_of_given_number = {}
for i in range(1,n+1):
    squares_of_given_number.update({i:i**2})

print(squares_of_given_number.items())
