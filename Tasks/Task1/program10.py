# Shopping Cart Calculations
product_price = float(input("Enter Product Price : "))
product_quantity = int(input("Enter Product Quantity : "))
discount_percentage = float(input("Enter Discount Percentage (e.g., 10 for 10%) : "))

# Calculate total price before discount
total_before_discount = product_price * product_quantity

# Calculate discount amount using floating-point division for accuracy
discount_amount = (total_before_discount * discount_percentage) / 100

# Subtract discount from the total price
final_price = total_before_discount - discount_amount

print(f"Total Before Discount : {total_before_discount:,.2f}")
print(f"Discount Applied      : {discount_amount:,.2f}")
print(f"Final Payable Price   : {final_price:,.2f}")
