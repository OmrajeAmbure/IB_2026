dict1 = {}
dict2 = dict()
details = {
        "id":1,
        "name":"omraje",
        "address":"Pune",
        "address":"dharashive" # value are changes 
}
print(id(details))
print(type(details))
print(type(dict2))
print(type(dict1))
print(details)
print(details["name"])

# print(details[1]) # it show the error Key Error
print(details.get("id")) # it not show key error , return -> None

#  Add New Values
details["city"] = "Hadpsar"
print(details)

#  if key not find then return Not Avilable
print(details.get("concat","Not Avliable"))
print(details)

# updating value
details["address"] = "Pune"
print(details)

# create new dict
details = {
        "id":2,
        "name":"om",
        "address":"darashiv",
}
print(details)
print(id(details))

# length
# it use to count key values paris
print(len(details))

# reomving methods
print(details.pop("address")) # it delete specific key and return the value
print(details)

print(details.popitem()) # last element from dict and return the the {key : value} pairs
print(details)
details = {
        "id":2,
        "name":"om",
        "address":"darashiv",
}
del details["name"]
print(details)
details = {
        "id":2,
        "name":"om",
        "address":"darashiv",
}
details.clear()
print(details.)
