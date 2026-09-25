"""
Q22. Write a Python program to accept 10 numbers from the user using a for loop and calculate:
    
    ● How many numbers are positive 
    ● How many numbers are negative 
    ● How many numbers are zero 
    ● Sum of all positive numbers 
    ● Sum of all negative numbers 
    At the end, display all five results. 
    Positive numbers:   
    Negative numbers:  
    Zeros:  
    Positive Sum:  
    Negative Sum:  
    
    Condition: Do not use a List to store the numbers. Use variables and a loop to solve the problem. 
"""
postive_sum=0
negative_sun=0
postive_count=0
negative_count=0
zeros = 0 
for i in range(1,11):
    print(f"Enter The {i} Number : ")
    num = int(input())
    if num == 0:
        zeros += 1
    elif num > 1:
        postive_count += 1;
        postive_sum += num;
    elif num < 0:
        negative_count += 1;
        negative_sun += num;
    else:
        print("Enter Valid Number...!")
print("================Results======================")
print(f"""Positive numbers:  {postive_count}
Negative numbers:  {negative_count}
Zeros:  {zeros}
Positive Sum: {postive_sum} 
Negative Sum: {negative_sun}
""")