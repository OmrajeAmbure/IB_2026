"""
Create:

shopping_cart(**products)

Example:

shopping_cart(
    Laptop=50000,
    Mouse=1000,
    Keyboard=2000,
    Headphones=3000
)

The function should calculate:

Total amount
Discount
Tax
Final amount

Use a default parameter for discount:

discount=10

Inside the main function, create nested functions for:

calculate_total()
calculate_discount()
calculate_tax()
calculate_final_amount()

Condition: Don't use built-in functions like sum() for calculating the total
"""
def shopping_cart(*, discount=10, tax_rate=18, **products):
    # 1. Calculate the initial subtotal without using sum()
    def calculate_total():
        total = 0
        for price in products.values():
            total += price
        return total
    
    # 2. Calculate the absolute discount amount
    def calculate_discount(total_amount):
        return total_amount * (discount / 100)
        
    # 3. Calculate tax based on the discounted amount
    def calculate_tax(discounted_amount):
        return discounted_amount * (tax_rate / 100)
        
    # 4. Combine everything for the final bill
    def calculate_final_amount():
        total = calculate_total()
        disc_amt = calculate_discount(total)
        discounted_subtotal = total - disc_amt
        tax_amt = calculate_tax(discounted_subtotal)
        final_bill = discounted_subtotal + tax_amt
        
        # Display the receipt summary
        print(f"--- Shopping Receipt ---")
        print(f"Items Total:  ₹{total:,.2f}")
        print(f"Discount ({discount}%): -₹{disc_amt:,.2f}")
        print(f"Tax ({tax_rate}%):      +₹{tax_amt:,.2f}")
        print(f"------------------------")
        print(f"Final Amount: ₹{final_bill:,.2f}")
        
        return final_bill

    return calculate_final_amount()

# Example Execution:
shopping_cart(
    Laptop=50000,
    Mouse=1000,
    Keyboard=2000,
    Headphones=3000
)
