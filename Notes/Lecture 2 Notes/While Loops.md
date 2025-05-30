
<iframe width="560" height="315" 
src="https://video.cs50.io/CYobbeiGgp8" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
from soil import sample

def main():
	moisture = sample()
	days = 0
	print(f"Day {days}: Moisture is {moisture}%")
	
	while moisture > 20:
		moisture = sample()
		days += 1 #add one day each time
		print(f"Day {days}: Moisture is {moisture}%")
		print("Time to water!") #exit loop when <= 20

main()

```