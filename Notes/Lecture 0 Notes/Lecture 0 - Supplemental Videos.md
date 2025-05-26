## Visual Studio Code for CS50
<iframe width="560" height="315" 
src="https://video.cs50.io/Oi1lvJS4uS8?start=399" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>
### Command Line Interface

- Create new python script file (terminal): `code hello.py`
- run python script (terminal): `python hello.py`

- `ls`: list files in folder
- `cp`: copy 
	- `cp (file to copy) (new file name)
	- ex) `cp hello.py goodbye.py`
- `mv`: move
	- `mv (file to move) (change name to)`
		- ex) `mv goodbye.py farewell.py`
	- `mv farewell.py ..` to move file up one folder
	- 
- `rm`: remove
- `mkdir`: make folder
	- `mkdir foldername`
- `cd`: change directory
	- `cd ..` to go up one folder
	- `cd` or `cd ~ ` to default folder
- `rmdir`: remove directory
- `clear`: clear terminal window 






## Functions
<iframe width="560" height="315" 
src="https://video.cs50.io/lGS6O47debI" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

### Def main():
```
def main():
	print("Hello, world!")
	print("This is CS50P.")


main()
```




## Variables
<iframe width="560" height="315" 
src="https://video.cs50.io/MyWf3zyyvjc" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

### Variable types
- when using `input("Enter a guess: ")`, this grabs a string. Need int in front if you want an integer
```
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



## Return Values
<iframe width="560" height="315" 
src="https://video.cs50.io/Jt1p_qQYeUU" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```
def greet(input):
	if "hello" in input:
		return "hello, there"
	else:
		return "I'm not sure what you mean"

greeting = greet("hello, computer") #fill this out differently to test
print("Hm, " + greeting)
```



## Side Effects
<iframe width="560" height="315" 
src="https://video.cs50.io/a002hwAqLDw" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>
- *side effects* are not the return value, but anything that gets changed while function is running
	- ex) printing to terminal
	- ex) change emotional state as side effect by **modifying** using global
- *global variable*  = emoticon because at top
	- it is **accessible** but not **modifiable** unless call global in function
- *local variable* = phase because stuck in "say" function

```
emoticon = "v.v"


def main():
	global emoticon
	say("Is anyone there?")
	emoticon = ":D"
	say("Oh, hi!")
	
def say(phrase):
	print(phrase + " " + emoticon)


main()
```




## String Methods
<iframe width="560" height="315" 
src="https://video.cs50.io/f4_ZPwvKF5g" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```
SHOWS = [
	" Avatar: the last airbender",
	"Ben 10",
	"Arthur",
	" Spongebob Squarepants",
	"Phineas and ferb",
	"Kim possible",
	"Jimmy Neutron",
	"the Proud family"
]


def main():
	cleaned_shows = []    # create empty list
	for show in SHOWS:
		cleaned_shows.append(show.title().strip())    #put in new list
	
	print(', '.join(cleaned_shows)) #join list elements with comma between




main()
```