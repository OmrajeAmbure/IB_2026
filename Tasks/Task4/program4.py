def calculate_avg_count(*num):
    count = 0
    sum_ = 0
    
    for i in num:
        count+=1;
        sum_ += i;
    avg = sum_/count
    print(f"Count : {count}")
    print(f"Sum : {sum_}")
    print(f"Avg : {avg}")
    grater_then_avg = []
    for n in num:
        if n > avg:
            grater_then_avg.append(n)
    print(f"Number Grater Tham avg : {grater_then_avg}")

print("Enter The Numbers Want To Count Avg : ")
n = int(input())

list1 = []
for i in range(n):
    inp = int(input(f"Enter number {i+1}: "))
    list1.append(inp)
list1 = tuple(list1)
calculate_avg_count(*list1)
