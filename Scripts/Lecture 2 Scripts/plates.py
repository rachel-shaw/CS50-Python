"""
GOALS:
- implement a program that prompts the user for a vanity plate 
- then outputs Valid if meets requirements or Invalid if not
- any letters in input will be capitalized
- requirements:
    - all plates must start with at least two letters
    - max of 6 characters, min of 2
    - numbers cannot be in middle of plate, must come at end
    - first number used cannot be 0
    - no periods, spaces, or puncuation marks allowed
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check length and first two letters
    if not (2 <= len(s) <= 6 and s[:2].isalpha()):
        return False
    
     # Reject if any character is not a letter or number
    if not s.isalnum():
        return False

    found_digit = False
    for char in s:
        if char.isdigit():
            if not found_digit:
                # First digit found — check if it's 0
                if char == '0':
                    return False
                found_digit = True
        elif found_digit and char.isalpha():
            # Letter appears after digits — invalid
            return False

    return True




main()