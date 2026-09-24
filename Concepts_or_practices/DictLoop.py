# name age city course

dictloop = {
    "name":"raj varma",
    "age":23,
    "city":"Pune",
    "course":"Python"
}
# default give only key
for i in dictloop:
    print(i)
    
print()
print(dictloop.values())
print()

# default give only value
for i in dictloop.values():
    print(i)
print()

if "city" in dictloop:
    print("Key Exist")
else:
    print("Key not Exist")

print()

if "city" not in dictloop:
    print("Key not Exist")
else:
    print("Key Exist")

data = {
    "name":"raj varma",
    "age":23,
    "city":"Pune",
    "course":["python","java","php"]
}


for i in data.get("course"):
    print(i)
print()
for i in data["course"]:
    print(i)

data.update({1:"om",2:"om"})
print(data)
