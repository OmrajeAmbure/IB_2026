def positive_negative_find(*nums):
    postive_number = []
    negative_number = []
    zero_number = []
    for num in nums:
        if num>0:
            postive_number.append(num)
        elif num<0:
            negative_number.append(num)
        elif num==0:
            zero_number.append(num)
    print(f"Positive Number : {postive_number}")
    print(f"Negative Number : {negative_number}")
    print(f"Zero Number : {zero_number}")

print("Enter The Numbers Want To Number To Compare Postive And Negative : ")
n = int(input())
list1 = []
for i in range(n):
    inp = int(input(f"Enter number {i+1}: "))
    list1.append(inp)
tuple1 = tuple(list1)
positive_negative_find(*tuple1)
