I’m thinking of a number between 1 and 100…

What is it?

It’s 50! But what if it were more random?

In a file called `game.py`, implement a program that:

- Prompts the user for a level, n. If the user does not input a positive integer, the program should prompt again.
- Randomly generates an integer between 1 and n, inclusive, using the `random` module.
- Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
    - If the guess is smaller than that integer, the program should output `Too small!` and prompt the user again.
    - If the guess is larger than that integer, the program should output `Too large!` and prompt the user again.
    - If the guess is the same as that integer, the program should output `Just right!` and exit.

#### Hints
- Note that the `random` module comes with quite a few functions, per [docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html).

## Demo
```
$ python game.py
Level: 1
Guess: 1
Just right!
$ python game.py
Level: 10
Guess: 5
Too large!
Guess: 3
Just right!
$ python game.py
Level: cat
Level: 10
Guess: cat
Guess: dog
Guess: 5
Too large!
Guess: 2
Too small!
Guess: 3
Just right!
```

## Before You Begin

Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

```
$
```

Next execute

```
mkdir game
```

to make a folder called `game` in your codespace.

Then execute

```
cd game
```

to change directories into that folder. You should now see your terminal prompt as `game/ $`. You can now execute

```
code game.py
```

to make a file called `game.py` where you’ll write your program.

## How to Test

Here’s how to test your code manually:

- Run your program with `python game.py`. Type `cat` at a prompt that says `Level:` and press Enter. Your program should reprompt you:
    
    ```
    Level:   
    ```
    
- Run your program with `python game.py`. Type `-1` at a prompt that says `Level:` and press Enter. Your program should reprompt you:
    
    ```
    Level:   
    ```
    
- Run your program with `python game.py`. Type `10` at a prompt that says `Level:` and press Enter. Your program should now be ready to accept guesses:
    
    ```
    Guess:   
    ```
    
- Run your program with `python game.py`. Type `10` at a prompt that says `Level:` and press Enter. Then type `cat`. Your program should reprompt you:
    
    ```
    Guess:   
    ```
    
- Run your program with `python game.py`. Type `10` at a prompt that says `Level:` and press Enter. Then type `-1`. Your program should reprompt you:
    
    ```
    Guess:   
    ```
    
- Run your program with `python game.py`. Type `1` at a prompt that says `Level:` and press Enter. Then type `1`. Your program should output:
    
    ```
    Just right!  
    ```
    
    There’s only one possible number the answer could be!
    
- Run your program with `python game.py`. Type `10` at a prompt that says `Level:` and press Enter. Then type `100`. Your program should output:
    
    ```
    Too large!  
    ```
    
    Looks like you’re guessing outside the range you specified.
    
- Run your program with `python game.py`. Type `10000` at a prompt that says `Level:` and press Enter. Then type `1`. Your program should output:
    
    ```
    Too small!  
    ```
    
    Most likely, anyways: you might get lucky and see `Just right!`. But it would certainly be odd for you to see `Just right!` every time. And certainly you shouldn’t see `Too large!`.
    

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

```
check50 cs50/problems/2022/python/game
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

## How to Submit

In your terminal, execute the below to submit your work.

```
submit50 cs50/problems/2022/python/game
```


### ANSWER
```python
"""
GOALS:
- prompts the user for a level, n
- if the user does not input a positive int, the program should prompt again
- randomly generates an int between 1 and n, inclusive, using random module
- prompts the user to guess that int
- if the guess is not a positive int, program should prompt user again
- if the guess is smaller, program should output "Too small!"
- if the guess is larger, program should output "Too large!"
- if the guess is correct, program should output "Just right!" and exit
"""

import random

def main():
	level = get_positive_int("Level: ")
	random_num = random.randint(1, level) #get range instead of using range with random.choice
	while True:
		userguess = get_positive_int("Guess: ")
		if userguess < random_num:
			print("Too small!")
		elif userguess > random_num:
			print("Too large!")
		else:
			print("Just right!")
			break
		#don't need ValueError here for guess because already taken care of in get_positive_int function
  
#verify user entry is int larger than 0
def get_positive_int(prompt):
	while True:
		try:
			userinput = int(input(prompt)) #prompt instead of having input("Level: ") down here and now we can use it for guess too
			if userinput > 0:
				return userinput
		except ValueError:
			pass

main()
```