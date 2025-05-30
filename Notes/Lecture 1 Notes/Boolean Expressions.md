<iframe width="560" height="315" 
src="https://video.cs50.io/51BNn5Ojupw?start=4" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
### GOAL: clean code from Conditionals (short) video
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

```