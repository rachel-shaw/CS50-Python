"""
GOALS:
- implement a program that prompts the user for a str of text 
- then outputs the same text but with all of the vowels removed
- vowels = A, E, I, O , U
- vowels omitted regardless of case
"""

# def main():
#     word = input("Input: ").strip()
#     shortword = ""

#     for char in word:
#         if char in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
#             letter = word.replace(char, "").strip().lower()
#             letter += char
#         else:
#             shortword += char
            
#     print(shortword)
        


# main()


def main():
    word = input("Input: ").strip()
    shortword = ""

    for char in word:
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            shortword += char
            
    print(shortword)
        


main()