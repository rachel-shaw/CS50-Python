
<iframe width="560" height="315" 
src="https://video.cs50.io/f4_ZPwvKF5g" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
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