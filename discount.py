def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If the discount is 20% or higher, apply the discount;
    otherwise, return the original price.
    
    Parameters:
    - price (float): The original price of the item.
    - discount_percent (float): The discount percentage.
    
    Returns:
    - float: The final price after applying the discount or the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price

# Prompt the user for inputs
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price using the function
    final_price = calculate_discount(original_price, discount_percentage)

    # Output the result
    if final_price != original_price:
        print(f"After a {discount_percentage}% discount, the final price is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: ${original_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")
