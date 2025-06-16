"""
GOALS:
- implement a program that prompts the user for a str in English
- outputs the emojized version of the str
- converting any codes or aliases therein to their corresponding emoji
"""

import emoji

userinput = input("Input: ")

print(emoji.emojize(f"Output: {userinput}", language = 'alias'))



