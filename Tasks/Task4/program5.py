def unique_value(*num):
    count = 0
    unique_value = []
    for i in range(len(num)):
        if num[i] in num[i+1:]:
            continue;
        unique_value.append(num[i])
    return unique_value

print("Enter The Numbers Want To Count Unique Integer : ")
n = int(input())

list1 = []
for i in range(n):
    inp = int(input(f"Enter number {i+1}: "))
    list1.append(inp)
tuple1 = tuple(list1)
print(unique_value(*tuple1))
