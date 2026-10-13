"""
5>create the product class with products name and price add products dynamically user
input store each product object in a list disply all product and disply the total no
of prodect added
"""
class Product:
    count_of_product = 0
    def __init__(self,id,name,price):
        self.id = id
        self.name = name
        self.price = price
        Product.count_of_product += 1
    def display(self):
        print(f"""
P_ID : {self.id} 
Name : {self.name} 
Price : {self.price}
        """)

Products = []
while True:
    print(""" 
        1. Add Product
        2. Diaplay
        3. Stop
    """)
    print("Enter The Choice To Perform Opration : ")
    chocie = int(input())
    match chocie:
        case 1:
            print("Enter The Product ID : ")
            id = input()
            print("Enter The Name of Product : ")
            name = input()
            print("Enter The Price of Product : ")
            price = input()
            Products.append(Product(id,name,price))
        case 2:
            print("================== Products Details ==================")
            count_of_product = 0
            for emp in Products:
                if emp == None:
                    print("No Products Found...!")
                emp.display()
            print("Product Count : ",Product.count_of_product)
            print()
        case 3:
            break

