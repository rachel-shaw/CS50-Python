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
    answer = get_answer()

    if 100 >= answer >= 99:
        print("F")
    elif answer <= 1:
        print("E")
    else:
        print(f"{int(answer)}%")
    

def get_answer():
    while True:
        try:
            userentry = input("Fraction: ")
            x,y = userentry.split("/")
            answer = int(x)/int(y)*100

            if answer > 100:
                continue
            return answer
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
    


main()