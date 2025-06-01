"""
GOALS:
- implement a program that prompts the user for items, one per line
- until the user inputs control + d to end input
- output the user's grocery list in all uppercase
- sorted alphabetically
- prefixing each line with the number of time the user inputted that item
- no need to pluralize the items
- treat the user's input case-insensitively
"""

def main():
    grocerylist = create_dict()

    for item in sorted(grocerylist):
        print(f"{grocerylist[item]} {item}")

def create_dict():
    grocerylist = {}

    while True:
        try:
            item = input().strip().upper()
            if item:
                if item in grocerylist:
                    grocerylist[item] += 1
                else:
                    grocerylist[item] = 1
        except EOFError:
            break

    return grocerylist

main() 