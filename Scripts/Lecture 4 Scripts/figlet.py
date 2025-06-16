"""
GOAL:
- implement a program that:
- expects zero or two command-line arguments
    - zero if the user would like to output text in a random font
    - two if the user would like to output text in a specific font
        - first argument = -f or --font
        - second arument = name of font
- prompts the user for a str of text
- outputs that text in a desired font
- if the user provides two command line arguments but the first is not -f or --font or the second isn't a font
    - program should exit via sys.exit with an error message
"""

import sys
import random
from pyfiglet import Figlet

#activate module
figlet = Figlet()

#get list of available fonts
# print(figlet.getFonts())
font_choices = figlet.getFonts()

#check arguments on command line
if 1 < len(sys.argv) < 3:
    sys.exit("Too few arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many arguments")

#set font and check for -f/--font
if len(sys.argv) == 1:
    font_name = random.choice(font_choices)
elif sys.argv[1] == "-f" or sys.argv[1] == "--font":
    font_name = sys.argv[2]
else:
    sys.exit("Incorrect argument. Please use -f or --font before font name")

    
#output
if font_name in figlet.getFonts():
    figlet.setFont(font=font_name)
    #user input text
    text = input("Input: ")
    #print font
    print(figlet.renderText(text))
else:
    sys.exit("Font not found")
