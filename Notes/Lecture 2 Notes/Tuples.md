
<iframe width="560" height="315" 
src="https://video.cs50.io/v9n6wYBq4HI" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>
```python
#using indexes to break apart tuple
def main():
	coordinates = (42.376, -71.115)
	print(f"Latitude: {coordinates[0]}") #grab using index
	print(f"Longitude: {coordinates[1]}") #grab using index

main()


## Using Tuples (like list but not because can't change once written
def main():
	coordinates = (42.376, -71.115) #this is a tuple
	latitude, longitude = coordinates
	print(f"Latitude: {latitude}") #grab using tuple
	print(f"Longitude: {longitude}") #grab using tuple

main()



# Tuples vs list memory (tuple smaller in memory!)
#tuples are great when you know you wont be changing data (like lat/long)
import sys

def main():
	coordinate_tuple = (42.376, -71.115)
	coordinate_list = [42.376, -71.115]
	print(f"{sys.getsizeof(coordinate_tuple)} bytes")
	print(f"{sys.getsizeof(coordinate_list)} bytes")

main()
```