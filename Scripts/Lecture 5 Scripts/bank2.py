"""
GOALS:
- value expects str as input
- value returns an int of:
    - 0 if starts with "hello"
    - 20 if starts with "h" but not "hello"
    - 100 otherwise
- treat str as case-insensitively
"""

def main():
    userinput = input("")
    print(f"${value(userinput)}")

def value(greeting):
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()