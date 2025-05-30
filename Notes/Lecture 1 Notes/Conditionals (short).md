<iframe width="560" height="315" 
src="https://video.cs50.io/vGr1tvjqWs0" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>


```python
### GOAL: recommend games based on difficulty and number of players

def main():
	difficulty = input("Difficult or Causal? ") 
	players = input("Multiplayer or Single-player? ")
	
	if difficulty == "Difficult":
		if players == "Multiplayer":
			recommend("Poker")
		elif players == "Single-player":
			recommend("Klondike")
		else:
			print("Recommend a valid number of players")
	elif difficulty == "Casual": 
		if players == "Multiplayer":
			recommend("Hearts")
		elif players == "Single-player:
			recommend("Clock")
		else:
			print("Recommend a valid number of players")
	else:
		print("Enter a valid difficulty")




def recommend(game):
	print("You might like", game)

main()
```