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


#verify user entry is int larger than 0
def get_positive_int(prompt):
    while True:
        try:
            userinput = int(input(prompt))
            if userinput > 0:
                return userinput
        except ValueError:
            pass
        


main()