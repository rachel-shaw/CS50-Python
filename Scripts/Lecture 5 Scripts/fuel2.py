"""
GOALS:
- implement a program that prompts the user for a fraction
- formatted as X/Y (both int)
- outputs as percent rounded to nearest integer
- If 1% or less remains, output E for empty
- if 99% or more remains, output F for full
- If x or y is not an int, x is greater than y, or y is 0, instead prompt user again
- be sure to catch any exceptions like ValueError or ZeroDivisionError
"""

def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            pass
    print(gauge(percentage))

def convert(fraction):
    x,y = fraction.split("/")
    x = int(x)
    y = int(y)
    if y == 0:
        raise ZeroDivisionError
    elif x > y:
        raise ValueError
    return round((x / y) * 100)


def gauge(percentage): 
    if 100 >= percentage >= 99:
        return("F")
    elif percentage <= 1:
        return("E")
    else:
        return(f"{int(percentage)}%")

    

if __name__ == "__main__":
    main()