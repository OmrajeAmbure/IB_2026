1 try was -> if num_find in num[n]: but it cause error beacuse (in) only used with iterable
    for n in range(len(num)):
        if num_find == num[n]:
            count+=1
    unique_value_count.update({num_find :count})    
    return unique_value_count

def unique_value_frq(*num):
    unique_value_count = {}
    for n in range(len(num)):
        current_num = num[n]
        count = 0
        for i in range(len(num)):
            if current_num == num[i]:
                count += 1
        unique_value_count.update({current_num: count})
    return unique_value_count

# print(value_count(34,34,34,67,7,7,34))
# print(unique_value_frq(7,34,34,67,7,7,34))

print("Enter The Numbers Want To Count Unique Integer : ")
n = int(input())
list1 = []

for i in range(n):
    inp = int(input(f"Enter number {i+1}: "))
    list1.append(inp)
    
tuple1 = tuple(list1)
print(unique_value_frq(*tuple1))
print("Enter The Number You want To Find Frequency : ")
search = int(input())
print(value_count(search,*tuple1))
