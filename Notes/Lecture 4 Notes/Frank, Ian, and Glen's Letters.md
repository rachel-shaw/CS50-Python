[FIGlet](https://en.wikipedia.org/wiki/FIGlet), named after [Frank, Ian, and Glen’s letters](http://www.figlet.org/faq.html), is a program from the early 1990s for making large letters out of ordinary text, a form of [ASCII art](https://en.wikipedia.org/wiki/ASCII_art):

```
 _ _ _          _   _     _
| (_) | _____  | |_| |__ (_)___
| | | |/ / _ \ | __| '_ \| / __|
| | |   <  __/ | |_| | | | \__ \
|_|_|_|\_\___|  \__|_| |_|_|___/
```

Among the fonts supported by FIGlet are those at [figlet.org/examples.html](http://www.figlet.org/examples.html).

FIGlet has since been ported to Python as a module called [pyfiglet](https://pypi.org/project/pyfiglet/).

In a file called `figlet.py`, implement a program that:

- Expects zero or two command-line arguments:
    - Zero if the user would like to output text in a random font.
    - Two if the user would like to output text in a specific font, in which case the first of the two should be `-f` or `--font`, and the second of the two should be the name of the font.
- Prompts the user for a `str` of text.
- Outputs that text in the desired font.

If the user provides two command-line arguments and the first is not `-f` or `--font` or the second is not the name of a font, the program should exit via `sys.exit` with an error message.

#### Hints
- You can install `pyfiglet` with:
    
    ```
    pip install pyfiglet
    ```
    
- The documentation for pyfiglet isn’t very clear, but you can use the module as follows:
    
    ```
    from pyfiglet import Figlet
    
    figlet = Figlet()
    ```
    
    You can then get a `list` of available fonts with code like this:
    
    ```
    figlet.getFonts()
    ```
    
    You can set the font with code like this, wherein `f` is the font’s name as a `str`:
    
    ```
    figlet.setFont(font=f)
    ```
    
    And you can output text in that font with code like this, wherein `s` is that text as a `str`:
    
    ```
    print(figlet.renderText(s))
    ```
    
- Note that the `random` module comes with quite a few functions, per [docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html).

## Demo
```
$ python figlet.py -f slant                                              Input: hello, world                                               
Output:
    __         ____                               __    __   / /_  ___  / / /___       _      ______  _____/ /___/ /                        / __ \/ _ \/ / / __ \     | | /| / / __ \/ ___/ / __  /                       / / / /  __/ / / /_/ /     | |/ |/ / /_/ / /  / / /_/ /                        /_/ /_/\___/_/_/\____( )    |__/|__/\____/_/  /_/\__,_/                                              |/
```
This demo’s first output used a random font. Your output may vary.

## Before You Begin

Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

```
$
```

Next execute

```
mkdir figlet
```

to make a folder called `figlet` in your codespace.

Then execute

```
cd figlet
```

to change directories into that folder. You should now see your terminal prompt as `figlet/ $`. You can now execute

```
code figlet.py
```

to make a file called `figlet.py` where you’ll write your program.

## How to Test

Here’s how to test your code manually:

- Run your program with `python figlet.py test`. Your program should exit via `sys.exit` and print an error message:
    
    ```
    Invalid usage
    ```
    
- Run your program with `python figlet.py -a slant`. Your program should exit via `sys.exit` and print an error message:
    
    ```
    Invalid usage
    ```
    
- Run your program with `python figlet.py -f invalid_font`. Your program should exit via `sys.exit` and print an error message:
    
    ```
    Invalid usage
    ```
    
- Run your program with `python figlet.py -f slant`. Type `CS50`. Your program should print the following:
    
    ```
       ___________ __________ 
      / ____/ ___// ____/ __ \
     / /    \__ \/___ \/ / / /
    / /___ ___/ /___/ / /_/ / 
    \____//____/_____/\____/  
    ```
    
- Run your program with `python figlet.py -f rectangles`. Type `Hello, world`. Your program should print the following:
    
    ```
     _____     _ _                        _   _ 
    |  |  |___| | |___      _ _ _ ___ ___| |_| |
    |     | -_| | | . |_   | | | | . |  _| | . |
    |__|__|___|_|_|___| |  |_____|___|_| |_|___|
                      |_|                       
    ```
    
- Run your program with `python figlet.py -f alphabet`. Type `Moo`. Your program should print the following:
    
    ```
    M   M         
    MM MM         
    M M M ooo ooo 
    M   M o o o o 
    M   M ooo ooo                     
    ```
    

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

```
check50 cs50/problems/2022/python/figlet
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

## How to Submit

In your terminal, execute the below to submit your work.

```
submit50 cs50/problems/2022/python/figlet
```


### ANSWER:
```python
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
```