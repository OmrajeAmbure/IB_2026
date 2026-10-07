def find_minimum_maximum(*num):
    max_1 = num[0]
    min_1 = num[0]
    for n in num:
        if n > max_1:
            max_1 = n
        elif n < min_1:
            min_1 = n
    print(f"The maximum number is: {max_1}")
    print(f"The minimum number is: {min_1}")

print("Enter The Numbers Want To Count maximum and minimum : ")
n = int(input())

list1 = []
for i in range(n):
    inp = int(input(f"Enter number {i+1}: "))
    list1.append(inp)
list1 = tuple(list1)
find_minimum_maximum(*list1)
