"""
GOALS:
- vanity plates form problem set 2
- is_valid expects a str
- returns True if str meets all requirements
- returns False if not

Requirements:
- start with 2 letters
- max of 6 characters, min of 2
- numbers cannot be in middle of plate
- first number used cannot be 0
- no periods, spaces or punctuation marks
"""


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check length 
    if len(s) < 2 or len(s) > 6:
        return False
    
    # Must start with at least two letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    
     # Only letters and numbers, no punctuation
    if not s.isalnum():
        return False

    number_started = False
    for i, char in enumerate(s):
        if char.isdigit():
            if not number_started:
                number_started = True
                # First number cannot be zero
                if char == '0':
                    return False
            else:
                continue
        else:
            # Numbers cannot appear in the middle of letters
            if number_started:
                return False

    return True

if __name__ == "__main__":
    main()