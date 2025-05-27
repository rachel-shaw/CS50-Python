"""
GOAL:
- implement a program that prompts the user for a greeting
- if the greeting starts with hello, output $0
- h but not hello, output $20
- otherwise, output $100
"""

def main():
    greeting = input("Greeting: ").strip().lower()

    if "hello" in greeting:
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")


main()
