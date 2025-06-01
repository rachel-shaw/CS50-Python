"""
GOALS:
- using menu, implement a program that enables the user to place an order
- prompting them for items, one per line
- until the user inputs control-d (common way to end input)
- after each inputted item, display total cost of bill thus far
- prefixed with $
- formatted to two decimals
- ignore any output that isn't an item.
- assume every item on the menu will be titlecased
"""

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    totalprice = 0.0
    while True:
        try:
            order = input("Item: ").title()
            if order in menu:
                totalprice += menu[order]
                print(f"Total: ${totalprice:.2f}")
        except EOFError: #lets control + D end input
            print()
            break



main()