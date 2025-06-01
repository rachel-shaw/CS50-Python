
<iframe width="560" height="315" 
src="https://video.cs50.io/BltXeMM96DA" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
# use raise exception
def main():
	pace = get_pace(miles=26.2, minutes=0)
	print(f"You need to run each mile in {round(pace, 2)} minutes.")

def get_pace(miles, minutes):
	if not minutes > 0:
		raise Exception() #or use raise ValueError to specify in error message
		return minutes / miles  

main()


## specify error
def main():
	pace = get_pace(miles=26.2, minutes=0)
	print(f"You need to run each mile in {round(pace, 2)} minutes.")

def get_pace(miles, minutes):
	if not minutes > 0:
		raise ValueError("Minutes must be greater than 0")
	return minutes / miles

main()
```