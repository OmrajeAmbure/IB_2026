"""
Q7. Shopping Cart Analyzer – Hard
Write a Python program to create a simple shopping cart.
Store the products and their prices in a dictionary:
products = {
"laptop": 50000,
"mobile": 25000,
"headphones": 2000,
"keyboard": 1500,
"mouse": 800
}
Ask the user to enter products one by one.
The program should:
1. Continue accepting products until the user enters "done".
2. Check whether the entered product exists in the dictionary.
3. If the product does not exist, display "Product not available" and
continue accepting the next product.
4. Store selected products in a list.
5. Calculate the total bill.
6. If the total bill is:
○ >= 50000 → 15% discount
○ >= 30000 → 10% discount
○ >= 15000 → 5% discount
○ Below 15000 → No discount
7. Display:
○ Selected products
○ Original bill
○ Discount amount
○ Final bill
8. If the user enters "exit" at any point, stop the program immediately
using break.
Additional condition:
The program should not allow the same product to be added more than once.
If the user enters the same product again, display:
Product already added.
Concepts expected:
Dictionary, List, while, if-elif-else, break, continue, operators and membership
operators (in).
"""
print("==========Shopping Cart Analyzer==============")
products = {
"laptop": 50000,
"mobile": 25000,
"headphones": 2000,
"keyboard": 1500,
"mouse": 800
}
list_product = []
discounted_bill = 0
total_bill=0
discount_price = 0
list_product_quentity = []
while True:  
    print("\nEnter The Product Name : ")
    prodact_name = input();
    if prodact_name not in products.keys():
        print("Product not available...!")
        continue
    print("\nEnter The Product Quantity : ")
    quentity = int(input())
    if prodact_name in list_product:
        print("Product already added.")
        continue
    else:
        list_product.append(prodact_name)
        list_product_quentity.append(quentity)
        for i in list_product:
            total_bill += products[i] * quentity
        if total_bill >= 50000:
            # Original Price × (Discount Percentage / 100)
            discount_price = total_bill * 15 // 100
            discounted_bill = total_bill - discount_price
        elif total_bill >= 30000:
            discount_price = total_bill * 10 // 100
            discounted_bill = total_bill - discount_price
        elif total_bill >= 15000:
            discount_price = total_bill * 5 // 100
            discounted_bill = total_bill - discount_price
        else:
            discount_price = 0
            discounted_bill = total_bill
    print("-------------------------------------")
    print("Selected Products : ",list_product)
    print("Quentity : ",list_product_quentity)
    print("Original Bill   : ",total_bill)
    print("Discount Amount : ",discount_price)
    print("-------------------------------------")
    print("Final bill      : ",discounted_bill)

