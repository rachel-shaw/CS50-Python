
<iframe width="560" height="315" 
src="https://video.cs50.io/wjWMOYLNK_E"
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
##add try/except
distances = {
"Voyager 1": "163",
"Voyager 2": "136",
"Pioneer 10": "80 AU",
"New Horizons": "58",
"Pioneer 11": "44 AU"
}

def main():
	spacecraft = input("Enter a spacecraft: ")
	try:
		au = float(distances[spacecraft])
	except ValueError:
		print("Can't convert '{distances[spacecraft]}' to a float")
		return

	m = convert(au)
	print(f"{m} m away")

def convert(au):
	return au * 14959780700

main()


#add second except
distances = {
"Voyager 1": "163",
"Voyager 2": "136",
"Pioneer 10": "80 AU",
"New Horizons": "58",
"Pioneer 11": "44 AU"
}

def main():
	spacecraft = input("Enter a spacecraft: ")
	try:
		au = float(distances[spacecraft])
	except KeyError:
		print(f"'{spacecraft}' is not in dictionary")
		return
	except ValueError:
		print(f"Can't convert '{distances[spacecraft]}' to a float")
		return

	m = convert(au)
	print(f"{m} m away")

def convert(au):
	return au * 14959780700

main()
```