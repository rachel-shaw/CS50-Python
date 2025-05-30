
<iframe width="560" height="315" 
src= "https://video.cs50.io/sBaB1bcOgVE"
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

````python
### POP and CLEAR

def main():
	history = []
	
	while True:
		action = input("Action: ")
		if action == "Undo":
			undone = history.pop() #remove last action
			print(f"Undone: {undone}") #print what we undid
		elif action == "Restart":
			history.clear() #clear all actions
			print(f"Game restarted!")
		else:
			history.append(action)
		print(history)

main()

```