a = {1,2,3,4,5,6,10,11}
b = {5,6,7,8,9,10}

print(a.union(b))
print(b.union(a))
print(a|b)

print(a.intersection(b))
print(b.intersection(a))
print(a & b)

print(a.difference(b))
print(b.difference(a))
print(a-b)
print(b-a)

print(a^b)
print(b^a)


a = {1,2,3}
b = {1,2,3,5,6,7,8,9,10}
print(a.issubset(b))
print(b.issubset(a))

print(a.issuperset(b))
print(b.issuperset(a))

a = {11,12}
b = {1,2,3,5,6,7,8,9,10}

print(a.isdisjoint(b))
print(b.isdisjoint(a))

a = {1,2,3}
b = {1,2,3,5,6,7,8,9,10}
print(a in b)
print(b not in a)
