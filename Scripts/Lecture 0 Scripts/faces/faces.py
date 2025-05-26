"""
GOALS:
- Implement a function called convert that accepts a str as inputs
- Returns that same input with any :) converted to 🙂 and :( converted to 🙁
- All other text should remain the same
- In the same file, implement a function called main that prompts the user for input
- Calls convert on that input
- Prints the result
- Prompt the user expicitly by passing a str as an argument to input
- Be sure to call main at the bottom of your file
"""







def convert(feeling):
        feeling = feeling.replace(":)", "🙂")
        feeling = feeling.replace(":(", "🙁")
        return feeling
        

def main():
    userinput = input("")
    print(convert(userinput))

main()
    


