name = "         my name name name name name Omraje Ambure            "

print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.count("Omraje"))
print("Replace : ",name.replace('name','OM',1))
print(name.find('O'))

# True False Method
print(name.startswith("my"))
print(name.endswith("my"))
print(name.isalpha()) 
print(name.isalnum())
print(name.isdigit())
print(name.isspace())
splite = name.split('@')
print(splite)
print('-'.join(splite))

print(len(name))
print(name.strip())
lstrip = name.lstrip()
print(lstrip)
print(len(lstrip))
rstrip = name.rstrip()
print(name.rstrip())
print(len(rstrip))

print(len(name.strip()))


name = "my name name name name Omraje Ambure"

data = name.find("name")
print(data)
mid = name.find('name',data+1)
print(mid)
name = name[:mid]+"Raj"+name[mid + len("name"):]
print(name)
print(len("name"))
print(name.find("a"))

string = " "
print(string.isspace())

name = "my@name@name@name@name@Omraje@Ambure"
splite = name.split("@")
print(splite)
print(' '.join(splite))


num = ['10','20','30','40','50']
print('-'.join(num))

