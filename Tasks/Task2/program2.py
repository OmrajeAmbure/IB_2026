set1 = {1,2,3,4,5,6,7,8,9,10}

# square of set number
print("Square of Number :- ")
for i in set1:
    square = i*i
    print(square)

# even of set number
print("Even Number :- ")
for i in set1:
    if i%2==0:
        print(i)
    

# even of set number
print("count the set number :- ")
count = 0
sum_of_set = 0
for i in set1:
    count+=1
    sum_of_set = sum_of_set + i
print("Total count : ",count)
print("Total sum of number : ",sum_of_set)
