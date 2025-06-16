
<iframe width="560" height="315" 
src="https://video.cs50.io/cyURNr9LZdM" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>
```python
import requests

def main():
	print("Search the Art Institute of Chicago!")
	artist = input("Artist: ")
	try:
		response = requests.get(
			"https://api.artic.edu/api/v1/artworks/search",
			{"q": artist} #from museum documentation
		)
		# print(response) #200 means api connected correctly
		response.raise_for_status()
	except requests.HTTPError:
		print("Couldn't complete API request")
		return
		
	content = response.json()
	for artwork in content["data"]: #content[data] from museum documentation
		print(f"- {artwork['title']}") #artwork[title] from museum documentation

main()
```