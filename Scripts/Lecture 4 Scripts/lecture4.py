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
