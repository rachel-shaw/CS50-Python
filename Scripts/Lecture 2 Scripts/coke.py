"""
GOAL:
- implement a program that prompts the user to insert a coin
- each time informing the user of the amount due
- once the user has inputted at least 50 cents, output how many cents in change the owner is owed
- assume the user can only enter integers
- ignore any integer that isn't as accepted denomination
- can only accept 25 cents, 10 cents, and 5 cents
"""

def main():
    cost = 50
    total_inserted = 0

    while total_inserted < cost:
        print(f"Amount Due: {cost - total_inserted}")
        coin = int(input("Insert Coin: "))

        if coin in [5, 10, 25]:
            total_inserted += coin
    
    change = total_inserted - cost
    print(f"Change Owed: {change}")



main()