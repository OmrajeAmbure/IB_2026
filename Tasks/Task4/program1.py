def find_even_odd(*number):
    even = 0
    odd  = 0
    for n in number:
        if n%2==0:
            even+=1
        elif n%2==1:
            odd+=1
        else:
            print("Enter A Valid Number")
    print(f"Number Of Enven : {even}")
    print(f"Number Of Enven : {odd}")

print("Enter The Numbers Want To Count Even and Odd : ")
n = int(input())

list1 = []
for i in range(n):
    inp = int(input(f"Enter number {i+1}: "))
    list1.append(inp)
list1 = tuple(list1)
find_even_odd(*list1)
