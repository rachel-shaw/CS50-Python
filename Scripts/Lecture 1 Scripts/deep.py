"""
GOAL:
- implement a program that prompts the user for the answer of the Great Question of Life, the Universe and Everything
- Outputting Yes if the user inputs 42, forty-two, or forty tw0
- Otherwise output No
"""

def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    
    normalized = answer.strip().lower().replace("-", " ") #to account for hyphen and capitalizing

    if normalized == "42" or normalized == "forty two":
        print("Yes")
    else:
        print("No")



main()
