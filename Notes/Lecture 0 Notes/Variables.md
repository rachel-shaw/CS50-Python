
<iframe width="560" height="315" 
src="https://video.cs50.io/MyWf3zyyvjc" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

### Variable types
- when using `input("Enter a guess: ")`, this grabs a string. Need int in front if you want an integer
```python
def get_guess():
	guess = int(input("Enter a guess: "))
	return guess

def main():
	guess = get_guess() # not referring to same guess as above
	if guess == 50:
		print("Correct!")
	else:
		print("Incorrect!")
	print(guess)

main()
	
```

