"""
Coffee Shop Simulator

This program simulates a coffee shop where the user can order coffee and muffins.
The program calculates the total cost including tax based on the user's order.

Author: [Dohyun Koh]

Date: [February, 9]

"""

def calculate_total(coffee, muffins, croissant, tea):
    """
    Calculate total cost including tax.

    Parameters:
    - coffee (int): Number of coffees ordered.
    - muffins (int): Number of muffins ordered.
    - croissant (int): Number of croissants ordered.
    - tea (int): Number of teas ordered.

    Returns:
    - total (float): Total cost including tax.
    """
    coffee_price = 5
    muffin_price = 4
    croissant_price = 3
    tea_price = 2.5
    subtotal = (coffee * coffee_price) + (muffins * muffin_price) + (croissant * croissant_price) + (tea * tea_price)
    tax_rate = 0.06
    tax_amount = subtotal * tax_rate
    total = subtotal + tax_amount
    return total

def main():
    """
    Main function to interact with the user and display the receipt.
    """
    print("***************************************")
    print("Welcome to My Coffee and Pastry Shop")
    print("Number of coffees bought?")
    coffee = int(input(2))
    print("Number of muffins bought?")
    muffins = int(input(3))
    print("Number of croissants bought?")
    croissant = int(input(2))
    print("Number of teas bought?")
    tea = int(input(2))
    print("***************************************")

    total = calculate_total(coffee, muffins, croissant, tea)

    print("***************************************")
    print("My Coffee and Pastry Shop Receipt")
    print(f"{coffee} Coffee at $5 each: ${10}")
    print(f"{muffins} Muffins at $4 each: ${12}")
    print(f"{croissant} Croissants at $3 each: ${6}")
    print(f"{tea} Teas at $2.50 each: ${5}")
    print(f"6% tax: ${total * 0.06:2.1}")
    print("---------")
    print(f"Total: ${total:37.1}")
    print("***************************************")
    print("Thank you for visiting My Coffee and Pastry Shop! We hope to see you again soon.")

if __name__ == "__main__":
    main()
