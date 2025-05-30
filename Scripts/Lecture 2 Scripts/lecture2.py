
"""
While Loop
"""
# i = 0
# while i < 3:
#     print("meow")
#     i = i + 1


"""
For Loop
"""
# for i in range(3):
#     print("meow")

## can also write it 
# print("meow\n" * 3, end="")



"""
Improving with User Input
"""
# while True:
#     n = int(input("What's n? "))
#     if n < 0:
#         continue
#     else:
#         break

### don't really need continue
# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for i in range(n):
#     print("meow")

## do better using function
# def main():
#     meow(get_number())

# def get_number():
#     while True:
#         n = int(input("What's n? "))
#         if n > 0:
#             return n
        
# def meow(n):
#     for i in range(n):
#         print("meow")

# main()




"""
More About Lists
"""
# students = ["Hermione", "Harry", "Ron"]

# for student in students:
#     print(student)




"""
Length
"""

# students = ["Hermione", "Harry", "Ron"]

# for i in range(len(students)):
#     print(i + 1, students[i])


"""
Dictionaries
"""

### create dictionary
# students = {
#     "Hermione": "Gryiffindor",
#     "Harry": "Gryiffindor",
#     "Ron": "Gryiffindor",
#     "Draco": "Slytherin",
# }

# for student in students:
#     print(student, students[student], sep=", ")


### add more data
# students = [
#     {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
#     {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
#     {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
#     {"name": "Draco", "house": "Slytherin", "patronus": None},
# ]

# for student in students:
#     print(student["name"], student["house"], student["patronus"], sep=", ")


"""
Mario
"""
## print one tower
# def main():
#     print_column(3)

# def print_column(height):
#     for i in range(height):
#         print("#")

# main()


### print four rows
# def main():
#     print_row(4)

# def print_row(width):
#     print("?" * width)

# main()


### now both rows and columns
# def main():
#     print_square(3)

# def print_square(size):

#     #for each row in square
#     for i in range(size):

#         #for each brick in row
#         for j in range(size):

#             #print brick
#             print("#", end="")
        
#         #print blank lane
#         print() ## otherwise will output #########%

# main()


### can further abstract our code
# def main():
#     print_square(3)

# def print_square(size):
#     for i in range(size):
#         print_row(size)

# def print_row(width):
#     print("#" * width)

# main()


"""""""""""""""""
Dictionaries (short)
"""""""""""""""""


# def main():
# 	spacecraft = {"name": "James Webb Space Telescope"}
# 	# spacecraft["distance"] = 0.01
# 	spacecraft.update({"distance": 0.01, "orbit": "Sun"})
# 	print(create_report(spacecraft))

# def create_report(spacecraft):
# 	return f"""
# 	========= REPORT ==========

# 	Name: {spacecraft.get("name", "Unknown")}
# 	Distance: {spacecraft.get("distance", "Unknown")} AU
# 	Orbit: {spacecraft.get("orbit", "Unknown")}

# 	===========================
# 	"""
	
# main()



# # DISTANCES
# distances = {
#     "Voyager I": 163, 
#     "Voyager II": 136,
#     "Pioneer 10": 80,
#     "New Horizons": 58,
#     "Pioneer II": 44
# }

# def main():
#     for name in distances.keys():
#         print(f"name is {distances[name]} AU from Earth")
    

# main()


## another ways for values
# distances = {
#     "Voyager I": 163, 
#     "Voyager II": 136,
#     "Pioneer 10": 80,
#     "New Horizons": 58,
#     "Pioneer II": 44
# }

# def main():
#     for distance in distances.values():
#         print(f"{distance} AU is {convert(distance)} m")
    
# def convert(au):
#     return au * 14959780700

# main()


"""""""""""""""""
Dictionary Methods
"""""""""""""""""

# WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

# def main():
# 	print("Welcome to Spelling Bee!")
# 	print("Your letters are: A I P C R H G")

# 	while len(WORDS) > 0:
# 		print(f"{len(WORDS)} words left!")
# 		guess = input("Guess a word: ")

# 		#TO DO: Check if guess in dictionary
# 		#TO DO: end game early if guess GRAPHIC
# 		if guess == "GRAPHIC":
# 			WORDS.clear()
# 			print("You've won!")
# 		if guess in WORDS.keys():
# 			points = WORDS.pop(guess) #to remove word from key
# 			print(f"Good job! You scored {points} points.")

	
# 	print("That's the game!")

# main()

# ##Next day, give user a list of possible words from previous day's game
# WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

# def main():
# 	print("Welcome to Spelling Bee!")
# 	for word, points in WORDS.items(): #can also use key, value
# 		print(f"{word} was worth {points} points.")


# main()


"""""""""""
FOR LOOPS
"""""""""""

# ## USING ITEMS in DICTIONARY
# invitees = {
#     "Mario":"Princess Peach", "Luigi":"Princess Peach", "Daisy":"Princess Peach", "Yoshi":"Princess Peach"
# }


# def main():
#     for receiver, sender in invitees.items():
#         print(write_letter(receiver, sender))
    
# def write_letter(receiver, sender):
#     return f"""
#     +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
#         Dear {receiver},

#         You are cordially invited to a ball at Peach's
#         Castle this evening, 7:00 PM. 

#         Sincerely,
#         {sender}
#     +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
#     """

# main()





# ## FOR LOOP
# names = ["Mario", "Luigi", "Daisy", "Yoshi"]


# def main():
#     for i in range(len(names)):
#         print(write_letter(names[i], "Princess Peach"))
    
# def write_letter(receiver, sender):
#     return f"""
#     +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
#         Dear {receiver},

#         You are cordially invited to a ball at Peach's
#         Castle this evening, 7:00 PM. 

#         Sincerely,
#         {sender}
#     +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
#     """

# main()



# ## SIMPLFY FOR LOOP
# names = ["Mario", "Luigi", "Daisy", "Yoshi"]


# def main():
#     for name in names:
#         print(write_letter(name, "Princess Peach"))
    
# def write_letter(receiver, sender):
#     return f"""
#     +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
#         Dear {receiver},

#         You are cordially invited to a ball at Peach's
#         Castle this evening, 7:00 PM. 

#         Sincerely,
#         {sender}
#     +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
#     """

# main()




"""""""""
LISTS
"""""""""

# ## APPEND, REMOVE from List
# results = ["Mario", "Luigi"]

# #to add additional items to list
# results.append("Princess")

# results.append(["Bowser", "Donkey Kong Jr."]) #this adds entire list as grouped LIST
# results.remove(["Bowser", "Donkey Kong Jr."]) #let's remove and try another way

# results.extend(["Bowser", "Donkey Kong Jr."]) #this adds multiple items correctly

# print(results)


# ### INSERT and REVERSE in List
# results = ["Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa", "Toad", "Bowser", "Donkey Kong Jr."]

# results.remove("Bowser") #remove's first instance of bowser
# # results.append("Bowser") #adds to end of list - not what we want
# results.insert(0, "Bowser") #specify location to add him

# results.reverse() #to reverse list

# print(results)



"""""""""""
List and Dictionary Comprehensions
"""""""""""
# ### USE LIST COMPREHENSION
# from helpers import get_words, save_counts

# def main():
#     counts = {}
#     words = get_words("address.txt")
#     lowercase_words = [word.lower() for word in words] #list comprehension to turn all words to lower case

#     for word in lowercase_words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1

#     save_counts(counts)

# main()



# ### USE LIST COMPREHENSION with filter
# from helpers import get_words, save_counts

# def main():
#     counts = {}
#     words = get_words("address.txt")
#     lowercase_words = [word.lower() for word in words if len(word) > 4] #list comprehension to turn all words to lower case, keep words greater than 4 letters

#     for word in lowercase_words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1

#     save_counts(counts)

# main()


### USE DICTIONARY COMPREHENSION with filter
# from helpers import get_words, save_counts

# def main():
#     words = get_words("address.txt")
#     lowercase_words = [word.lower() for word in words if len(word) > 4] #list comprehension to turn all words to lower case, keep words greater than 4 letters

#     counts = {word: words.count(word) for word in lowercase_words}

#     save_counts(counts)

# main()


"""""""""""""""
List Methods
"""""""""""""""
# def main():
#     history = []

#     while True:
#         action = input("Action: ")

#         if action == "Undo":
#             undone = history.pop() #remove last action
#             print(f"Undone: {undone}") #print what we undid

#         elif action == "Restart":
#             history.clear()  #clear all actions
#             print(f"Game restarted!")
#         else:
#             history.append(action)
#         print(history)


# main()


"""""""""
String Slicing
"""""""""

# def main():
#     phone = "617-495-1000"
#     print(phone[0:3]) #can use indexes to find area code (3 b/c up to but not including last number)
#     print(phone[:3]) #also works if want first index
#     print(phone[8:]) #last four digits through last index
#     print(phone[-4:]) #last 4

# main()


"""""""""
Tuples
"""""""""

# using indexes to break apart tuple
# def main():
#     coordinates = (42.376, -71.115)
#     print(f"Latitude: {coordinates[0]}") #grab using index
#     print(f"Longitude: {coordinates[1]}") #grab using index


# main()



# ## Using Tuples (like list but not because can't change once written
# def main():
#     coordinates = (42.376, -71.115) #this is a tuple
#     latitude, longitude = coordinates 
#     print(f"Latitude: {latitude}") #grab using tuple
#     print(f"Longitude: {longitude}") #grab using tuple


# main()



#### Tuples vs list memory (tuple smaller in memory!)
### tuples are great when you know you wont be changing data (like lat/long)
# import sys

# def main():
#     coordinate_tuple = (42.376, -71.115) 
#     coordinate_list = [42.376, -71.115]
#     print(f"{sys.getsizeof(coordinate_tuple)} bytes")
#     print(f"{sys.getsizeof(coordinate_list)} bytes")


# main()


"""""""""""""""""""""
While Loops
"""""""""""""""""""""
# from soil import sample

# def main():
#     moisture = sample()
#     days = 0
#     print(f"Day {days}: Moisture is {moisture}%")

#     while moisture > 20:
#         moisture = sample()
#         days += 1 #add one day each time
#         print(f"Day {days}: Moisture is {moisture}%")
    
#     print("Time to water!") #exit loop when <= 20


# main()
