"""
If Statements
"""
# x = int(input("What's x? "))
# y = int(input("What's y? "))

# if x < y:
#     print("x is less than y")



"""
Control Flow, elif, and else
"""
### using if
# x = int(input("What's x? "))
# y = int(input("What's y? "))

# if x < y:
#     print("x is less than y")
# if x > y:
#     print("x is greater than y")
# if x == y:
#     print("x is equal to y")

### using elif
# x = int(input("What's x? "))
# y = int(input("What's y? "))

# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# elif x == y:
#     print("x is equal to y")

### if elif else
# x = int(input("What's x? "))
# y = int(input("What's y? "))

# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# else:
#     print("x is equal to y")

"""
OR
"""
### using or
# x = int(input("What's x? "))
# y = int(input("What's y? "))

# if x < y or x > y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")

### can also write another way
# x = int(input("What's x? "))
# y = int(input("What's y? "))

# if x != y: #not equal to
#     print("x is not equal to y")
# else:
#     print("x is equal to y")

### can write the opposite way as well
# x = int(input("What's x? "))
# y = int(input("What's y? "))

# if x == y:
#     print("x is equal to y")
# else:
#     print("x is not equal to y")

"""
AND
"""
### using AND
# score = int(input("Score: "))

# if score >= 90 and score <= 100:
#     print("Grade: A")
# elif score >=80 and score < 90:
#     print("Grade: B")
# elif score >=70 and score < 80:
#     print("Grade: C")
# elif score >=60 and score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")

### better way to write
# score = int(input("Score: "))

# if 90 <= score <= 100:
#     print("Grade: A")
# elif 80 <= score < 90:
#     print("Grade: B")
# elif 70 <= score < 80:
#     print("Grade: C")
# elif 60 <= score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")

### write clearer still
# score = int(input("Score: "))

# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")



"""
Modulo (to see if two numbers divide evenly or divide and have remainder)
"""

# x = int(input("What's x? "))

# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


"""
Creating Our Own Parity Function
"""
# def main():
#     x = int(input("What is x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
    

# main()

"""
Pythonic
"""
### traditional way to write in python
# def main():
#     x = int(input("What's x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")


# def is_even(n):
#     return True if n % 2 == 0 else False


# main()


### even clearer way to write
# def main():
#     x = int(input("What's x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")

# def is_even(n):
#     return n % 2 == 0

# main()


"""
Match
"""
# name = input("What's your name? ")

# if name == "Harry":
#     print("Gryffindor")
# elif name == "Hermione":
#     print("Gryffindor")
# elif name == "Ron": 
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

### write better using MATCH
# name = input("What's your name? ")

# match name: 
# case "Harry" | "Hermione" | "Ron":
#     print("Gryffindor")
# case "Draco":
#     print("Slytherin")
# case _:
#     print("Who?")



"""
Conditionals (short)
"""
### GOAL: recommend games based on difficulty and number of players

# def main():
# 	difficulty = input("Difficult or Causal? ") 
# 	players = input("Multiplayer or Single-player? ")
	
# 	if difficulty == "Difficult":
# 		if players == "Multiplayer":
# 			recommend("Poker")
# 		elif players == "Single-player":
# 			recommend("Klondike")
# 		else:
# 			print("Recommend a valid number of players")
# 	elif difficulty == "Casual": 
# 		if players == "Multiplayer":
# 			recommend("Hearts")
# 		elif players == "Single-player":
# 			recommend("Clock")
# 		else:
# 			print("Recommend a valid number of players")
# 	else:
# 		print("Enter a valid difficulty")

# def recommend(game):
# 	print("You might like", game)

# main()


"""
Boolean Expression
"""
### GOAL: clean code from Conditionals (short) video above and make more efficient

def main():
	difficulty = input("Difficult or Causal? ") 
	if not (difficulty == "Difficult" or difficulty == "Casual"):
		print("Enter a valid difficulty")
		return

	players = input("Multiplayer or Single-player? ")
	if not(players == "Multiplayer" or players == "Single-player"):
		print("Enter a valid number of players")
		return

	if difficulty == "Difficult" and players == "Multiplayer":
		recommend("Poker")
	elif difficulty == "Difficult" and players == "Single-player":
		recommend("Klondike")
	elif difficulty == "Casual" and players == "Multiplayer": 
		recommend("Hearts")
	else:
		recommend("Clock")


def recommend(game):
	print("You might like", game)
	
main()