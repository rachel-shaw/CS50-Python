"""
GOALS:
- implement a program that prompts the user for names, one per line
    - until the user inputs control + d
- assume the user will input at least one name
- the bid adieu to those names
- separating 2 names with one "and"
- 3 names with two commas and one "and"
- and n names with n-1 commas and one "and"
"""

import inflect

def main():
    namelist = create_dict()

    p = inflect.engine()
    formatted_names = p.join(namelist)
    print(f"Adieu, adieu, to {formatted_names}")

def create_dict():
    names = []
    while True:
        try:
            name = input("Name: ").strip()
            if name:
                names.append(name)
        except EOFError:
            break
    
    return names


main()