"""
GOALS:
- Implement two functions:
    - dollars_to_float, which should accept a str as input (formatted as $##.##); $50.00 as input should return 50.0
    - percent_to_float, which should accept a str as input (formatted as ##%); 15% as input should return as 0.15
- Assume the user will input values in the expected formulas
"""

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.replace("$", "") #to remove $
    return float(d)

def percent_to_float(p):
    p = float(p.replace("%", "")) #to remove $
    perc = p /100
    return perc


main()