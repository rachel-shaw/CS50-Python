"""
GOAL:
- implement a program that prompts the user for an arithmetic expression
- then calculates and outputs the result as a float with one decimal
- assume input will be formated as x y z
- x = int
- y is + - * or /
- z = int
"""

# def main():
#     expression = input("Expression: ")

#     x, y, z = expression.split(" ")

#     if y == "+":
#         print(int(x) + int(z))
#     if y == "-":
#         print(int(x) - int(z))
#     if y == "*":
#         print(int(x) * int(z))
#     if y == "/":
#         print(int(x) / int(z))



# main()


def main():
    expression = input("Expression: ")

    x, y, z = expression.split(" ")

    match y:
        case "+":
            print(round(float(int(x) + int(z)), 1))
        case "-":
            print(round(float(int(x) - int(z)), 1))
        case "*":
            print(round(float(int(x) * int(z)), 1))
        case "/":
            print(round(float(int(x) / int(z)), 1))



main()