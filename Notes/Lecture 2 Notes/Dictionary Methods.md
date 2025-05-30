
<iframe width="560" height="315" 
src="https://video.cs50.io/3zJoCpvKhx4" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
### USING KEYS and POP and CLEAR
WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

def main():
	print("Welcome to Spelling Bee!")
	print("Your letters are: A I P C R H G")

	while len(WORDS) > 0:
		print(f"{len(WORDS)} words left!")
		guess = input("Guess a word: ")

		#TO DO: Check if guess in dictionary
		#TO DO: end game early if guess GRAPHIC
		if guess == "GRAPHIC":
			WORDS.clear()
			print("You've won!")
		if guess in WORDS.keys():
			points = WORDS.pop(guess) #to remove word from key
			print(f"Good job! You scored {points} points.")


print("That's the game!")

main()

```

``` python
## USING ITEMS
WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

def main():
	print("Welcome to Spelling Bee!")
	for word, points in WORDS.items(): #can also use key, value
		print(f"{word} was worth {points} points.")

main()
```