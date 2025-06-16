"""
GOALS:
- prompt the user for a level, v
    - if the user doesn't enter 1, 2, or 3, prompt again
- randomly generate 10 math problems formatted as `X + Y =`
    - X and Y are non-negative integers with n digits. 
    - no need to support operations other than addition
- prompt the user to solve each problem
- if answer is not correct, output EEE and prompt user again
    - user has 3 tries to get it right
    - after 3 tries, the program should output the correct answer
- ultimately output the user's score
    - number of correct answers out of 10
"""


import random

def main():
	level = get_level()
	score = 0
	
	for i in range(10):
		x = generate_integer(level)
		y = generate_integer(level)
		attempts = 0
		while attempts < 3:
			try:
				response = input(f"{x} + {y} = ")
				if x + y == int(response):
					score +=1
					break
				else:
					print("EEE")
			except ValueError:
				print("EEE")
			attempts += 1

		if attempts == 3:
			print(f"{x} + {y} = {x + y}")

	print(f"Score: {score}")


# get 1, 2, or 3 as int
def get_level():
	while True:
		try:
			userinput = int(input("Level: ")) 
			if 0 < userinput < 4:
				return userinput
		except ValueError:
			pass

#return a randomly generated int >= 0 with level as digits
def generate_integer(level):
	while True:
		try:
			num_digits = level
			if 0 <= num_digits < 4:
				lowerbound = 10**(num_digits-1)
				upperbound = 10**num_digits-1
				random_num = random.randint(lowerbound, upperbound)
				return random_num
		except ValueError:
			pass
		

if __name__ == "__main__":
    main()