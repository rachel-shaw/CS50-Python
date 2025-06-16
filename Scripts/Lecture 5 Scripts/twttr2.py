""""
GOALS:
- shorten function expects a str as input
- returns that same str but with all vowels omitted
- account for uppercase and lowercase
"""

def main():
    userinput = input("")
    print(shorten(userinput))


# def shorten(word):
#     vowels = "aeiouAEIOU"
#     for i in vowels:
#         word = word.replace(i, "")
#     return word

def shorten(word):
    shortword = ""
    for char in word:
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            shortword += char
    return shortword


if __name__ == "__main__":
    main()