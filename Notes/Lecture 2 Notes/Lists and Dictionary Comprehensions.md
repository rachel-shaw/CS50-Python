
<iframe width="560" height="315" 
src="https://video.cs50.io/AK3HbkbgiQA" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
### USE LIST COMPREHENSION
from helpers import get_words, save_counts

def main():
	counts = {}
	words = get_words("address.txt")
	lowercase_words = [word.lower() for word in words] #list comprehension to turn all words to lower case

	for word in lowercase_words:
		if word in counts:
		counts[word] += 1
	else:
		counts[word] = 1

	save_counts(counts)

main()



### USE LIST COMPREHENSION with filter
from helpers import get_words, save_counts

def main():
	counts = {}
	words = get_words("address.txt")
	lowercase_words = [word.lower() for word in words if len(word) > 4] #list comprehension to turn all words to lower case, keep words greater than 4 letters

	for word in lowercase_words:
		if word in counts:
		counts[word] += 1
	else:
		counts[word] = 1

	save_counts(counts)

main()


### USE DICTIONARY COMPREHENSION with filter
from helpers import get_words, save_counts

def main():
	words = get_words("address.txt")
	lowercase_words = [word.lower() for word in words if len(word) > 4] #list comprehension to turn all words to lower case, keep words greater than 4 letters
	counts = {word: words.count(word) for word in lowercase_words}

	save_counts(counts)

main()
```