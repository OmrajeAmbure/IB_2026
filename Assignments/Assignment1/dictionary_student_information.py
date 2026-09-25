"""
Q29. Dictionary – Student Information
Create a dictionary containing:
student = {
"name": "Rahul",
"age": 21,
"marks": 85,
"course": "Python"
}
Write a program to:
Display the student's name.
Display the marks.
Update the marks.
Add a new key called city.
Display all keys.
Display all values.
"""
student = {
    "name": "Rahul",
    "age": 21,
    "marks": 85,
    "course": "Python"
}

# Display the student's name
print("Student's name:", student["name"])
print("Student's marks:", student["marks"])

# Update the marks
student["marks"] = 90
print("Updated marks:", student["marks"])

# Add a new key called city
student["city"] = "Delhi"
print("Student's city:", student["city"])

# Display all keys
print("All keys in the dictionary:")
for key in student:
    print(key)

# Display all values
print("All values in the dictionary:")
for value in student.values():
    print(value)