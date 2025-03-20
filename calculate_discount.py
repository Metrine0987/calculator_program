def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount is 20% or higher, it is applied; otherwise, the original price is returned.
    """
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
    else:
        final_price = price
    return final_price

# Prompt user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(price, discount_percent)
    print(f"Final price after discount: {final_price:.2f}")
except ValueError:
    print("Invalid input! Please enter numeric values.")
