
students = [("om",21),("rohit",23),("mohit",20),("varun",29),("z",1)]
students.sort(key = lambda x : x[1])
print(students)

students = [("om",21),("rohit",23),("mohit",20),("varun",29),("z",1)]
students.sort(key = lambda x : x[0])
print(students)
print(students[0])


string1 = "infobens"
print(len(string1))
length = lambda i : len(i)
print(length(string1))

# lambda with sorted methods and string
l = ["om","rohit","mohit","varun","z"]
print()
len1 = list(map(lambda x : len(x),l))
print(len1)

l.sort(key = lambda x : len(x))
print(l)

l.sort(key = lambda x : len(x),reverse=True)
print(l)
