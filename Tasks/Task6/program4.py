# use lamnda to find number that are both even and grater than 20
data = [6,22,46,4,2,12,60,80]
even_and_gt20 = list(filter(lambda num: (num%2==0 and num>20),data))
print(even_and_gt20)
