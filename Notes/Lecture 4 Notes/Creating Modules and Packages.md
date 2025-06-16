
<iframe width="560" height="315" 
src="https://video.cs50.io/imrloYMePL0" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>
```python
## ARTWORK
from artwork_rs import get_artwork

def main():
	artwork = input("Artwork: ")
	artworks = get_artwork(query=artwork, limit=3)
	
	for artwork in artworks:
		print(f"- {artwork}")

main()

## ARTIST
from artists_rs import get_artists

def main():
	artist = input("Artist: ")
	artists = get_artists(query=artist, limit=3)

	for artist in artists:
		print(f"- {artist}")

main()


### PACKAGES (collection of multiple modules) - create a folder to put all of the modules in
# create file called "__init__.py" which can be empty

from museum_rs.artists_rs import get_artists
#from museum_rs.artwork_rs import get_artwork

def main():
	artist = input("Artist: ")
	#artwork = input("Artwork: ")
	artists = get_artists(query=artist, limit = 3)
	#artworks = get_artwork(query=artwork, limit=3)
	
	for artist in artists:
		print(f"ARTIST: {artist}")
		#print(f"ARTWORK: {artworks}")
  
main()



```