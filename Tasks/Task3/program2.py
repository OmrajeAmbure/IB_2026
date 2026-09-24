cars = {
    "barnd": "Toytoa",
    "model":"enova",
    "Year":2025
}

# print model,add color,update year, delete model print final dict
print("Car Model : ",cars["model"])

cars.update({"color":"red"})

cars["Year"] = 2026

print(cars)

val = cars.pop("model")

print(cars)

# display all key values of items
print()
for i,j in cars.items():
    print(f"{i} = {j}")
