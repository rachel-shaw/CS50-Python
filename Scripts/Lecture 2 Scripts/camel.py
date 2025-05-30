"""
GOALS:
- implement a program that prompts the user for the name of a variable in camel case
- outputs the same name in snake case
- assume the user's input will be in camel case
"""


def main():
    camel = input("camelCase: ")
    snake = ""

    for char in camel:
        if char.isupper():
            snake += "_" + char
        else:
            snake += char
    
    print(f"snake_case: {snake.lstrip('_').lower()}")



main()