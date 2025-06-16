
<iframe width="560" height="315" 
src="https://video.cs50.io/yec-UUauUV8" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>
```python

## choice --> random sampling ONE item from list
import random
cards = ["jack", "queen", "king"]

def main():
	print(random.choice(cards))

main()



# choices --> sampling with replacement
import random
cards = ["jack", "queen", "king"]

def main():
	print(random.choices(cards, k=2)) # k = how many from list to output

main()


  

# sample --> sampling without replacement
import random
cards = ["jack", "queen", "king"]

def main():
	print(random.sample(cards, k=2)) # k = how many from list to output

main()



## choices + weights -> sampling with replacement + weights
import random
cards = ["jack", "queen", "king"]

def main():
	print(random.choices(cards, weights=[75,20,5], k=2)) # weights = % of how often will get choosen

main()



## seed (random using computer time)
import random
cards = ["jack", "queen", "king"]

def main():
	random.seed() #random based on time of system
	print(random.choices(cards, k=2))

main()



## seed - using it as debugger
import random
cards = ["jack", "queen", "king"]

def main():
	random.seed(0) #set to 0 or 1 to make it stay constant so can test
	print(random.choices(cards, k=2))

main()
```