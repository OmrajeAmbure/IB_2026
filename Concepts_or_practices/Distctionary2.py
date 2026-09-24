
# nested dictionary
info = {
  "FSD":{
      "srno":1,
      "name":"vijay",
      "address":"Pune"
  },
  "FSP":{
      "srno":2,
      "name":"rohit",
      "address":"Pune"
  }
}

print(info)
print(info["FSD"])
print(info["FSP"]["name"])
print(info["FSD"]["address"])


# dictionary inside list
student = [{"name":"om","age":21,"address":"Pune"},{"name":"raj","age":19,"address":"Pune"},{"name":"vinnay","age":26,"address":"Pune"}]
print(student)
print(student[0])
print(student[1]["name"])
print(student[1:2])
 
