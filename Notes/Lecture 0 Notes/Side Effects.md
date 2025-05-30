
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

```python
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

