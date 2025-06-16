"""
Call Library (import)
"""

# import random

# coin = random.choice(["heads", "tails"])
# print(coin)

"""
Call Library + Function using From (this prevents from loading all functions within library)
"""
# from random import choice

# coin = choice(["heads", "tails"])
# print(coin)

"""
Statistics
"""
# import statistics

# print(statistics.mean([100, 90]))

"""
Command-line arguments
"""
# import sys

# print("hello, my name is", sys.argv[1]) #have to type python lecture4.py rachel

## adjust to clarify for potential errors if user doesn't type or types too many
# import sys

# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("hello, my name is", sys.argv[1])


## can also rewrite using sys.exit and print below
# import sys

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

# print("hello, my name is", sys.argv[1])

"""
Slice (subset of list)
"""
# import sys

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")

# for arg in sys.argv[1:]: #specify start and end of list (slice)
#     print("hello, my name is", arg) #add arg as variable, can be called anything


"""
Packages
"""
# cowsay is a well-known package that allows a cow to talk to the user
#pypi.org is a repo of all 3rd party packages

#install by typing pip install cowsay (pip is package manager)
# import cowsay
# import sys

# if len(sys.argv) == 2:
#     cowsay.cow("hello, " + sys.argv[1]) # cow image

# import cowsay
# import sys

# if len(sys.argv) == 2:
#     cowsay.trex("hello, " + sys.argv[1]) # dino image


"""
APIs
"""
# import json
# import requests
# import sys

# if len(sys.argv) != 2:
#     sys.exit() #enter name of band at command line

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]) #term = is what you are entering (band name)
# print(json.dumps(response.json(), indent=2)) #indents each field so little more readable

## output just the name of the track
# import json
# import requests
# import sys

# if len(sys.argv) != 2:
#     sys.exit()

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

# o = response.json() #stores json response to variable called o
# for result in o["results"]:
#     print(result["trackName"]) #print track name (within result dictionary)

## try to add number in front of track name to count how many tracks:
# import json
# import requests
# import sys

# if len(sys.argv) != 2:
#     sys.exit()

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

# o = response.json() #stores json response to variable called o

# i = 1
# for result in o["results"]:
#     print(f"{i}. {result["trackName"]}") #print track name (within result dictionary)
#     i += 1



"""
Make your own library
"""
#instead of running main() use:

# if __name__ == "__main__": 
#     main()

## otherwise will run main wihin library
## this way it will only run main if file name being called at command line (python lecture4.py), main will not get called





"""""""""""
Supplemental Videos
"""""""""""

"""
API Calls
"""
# import requests

# def main():
#     print("Search the Art Institute of Chicago!")
#     artist = input("Artist: ")
#     try:
#         response = requests.get(
#             "https://api.artic.edu/api/v1/artworks/search",
#             {"q": artist} #from museum documentation
#         )
#         # print(response) #200 means api connected correctly
#         response.raise_for_status()
#     except requests.HTTPError:
#         print("Couldn't complete API request")
#         return
    
#     content = response.json()
#     for artwork in content["data"]: #content[data] from museum documentation
#         print(f"- {artwork['title']}") #artwork[title] from museum documentation

# main()


"""
Creating Modules & Packages
"""
# ## ARTWORK
# from artwork_rs import get_artwork

# def main():
#     artwork = input("Artwork: ")
#     artworks = get_artwork(query=artwork, limit=3)

#     for artwork in artworks:
#         print(f"- {artwork}")


# main()  

## ARTIST
# from artists_rs import get_artists

# def main():
#     artist = input("Artist: ")
#     artists = get_artists(query=artist, limit=3)

#     for artist in artists:
#         print(f"- {artist}")


# main()  


## PACKAGE (collection of multiple modules) - create a folder to put all of the modules in
# create file called "__init__.py" which can be empty

# from museum_rs.artists_rs import get_artists
# from museum_rs.artwork_rs import get_artwork

# def main():
#     artist = input("Artist: ")
#     artwork = input("Artwork: ")
#     artists = get_artists(query=artist, limit = 3)
#     artworks = get_artwork(query=artwork, limit=3)
#     for artist in artists:
#         print(f"ARTIST: {artist}")
#         print(f"ARTWORK: {artworks}")

# main()






"""
Random
"""

## choice --> random sampling ONE item from list
# import random

# cards = ["jack", "queen", "king"]

# def main():
#     print(random.choice(cards))


# main()


# # choices --> sampling with replacement
# import random

# cards = ["jack", "queen", "king"]

# def main():
#     print(random.choices(cards, k=2)) # k = how many from list to output

# main()


# # sample --> sampling without replacement
# import random

# cards = ["jack", "queen", "king"]

# def main():
#     print(random.sample(cards, k=2)) # k = how many from list to output

# main()


# ## choices + weights -> sampling with replacement + weights
# import random

# cards = ["jack", "queen", "king"]

# def main():
#     print(random.choices(cards, weights = [75,20,5], k=2)) # weights = % of how often will get choosen

# main()

## seed
# import random

# cards = ["jack", "queen", "king"]

# def main():
#     random.seed() #random based on time of system
#     print(random.choices(cards, k=2)) 

# main()


## seed but use it to debug
# import random

# cards = ["jack", "queen", "king"]

# def main():
#     random.seed(0) #set to 0 or 1 to make it stay constant so can test
#     print(random.choices(cards, k=2)) 

# main()


"""
Style: PEP 8 (peps.python.org/pep-0008/)
"""
## SEE students_rs.py script

# pylint #style guide checker, but is a bit intense
# pycodestyle #auto reformats your style
#black # opinionated format style

#run black by typing "black students_rs.py"
    #reformats scripts (can undo but can't redo with control + z)

# students = {"Hermione": "Gryffindor", "Harry": "Gryffindor", "Ron": "Gryffindor", "Draco": "Slytherin"}
# for student in students:
#   print(student)


