# shopping bill

print("Enter Product : ")
product = str(input())
print("Enter price : ")
price = int(input())
print("Enter Quentity : ")
quentity = int(input())
total = price*quentity
print(f"""
Product Bill Calculator
--------------------------
Product Name : {product}
Price = {price}
Quentity = {quentity}
--------------------------
Total : {total}
""")
