def calculate_avg_count(*num):
    count = 0
    sum_ = 0
    for i in num:
        count+=1;
        sum_ += i;
    
    print(f"Count : {count}")
    print(f"Sum : {sum_}")
    print(f"Avg : {(sum_/count)}")

print("Enter The Numbers Want To Count Avg : ")
n = int(input())

list1 = []
for i in range(n):
    inp = int(input(f"Enter number {i+1}: "))
    list1.append(inp)
list1 = tuple(list1)
calculate_avg_count(*list1)
