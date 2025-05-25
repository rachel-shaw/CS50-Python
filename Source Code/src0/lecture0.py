

#print("hello, world")
# name = input("What's your name? ")
# print("hello,", name)



"""
Strings and Parameters
"""
# Ask the user for their name
# name = input("What's your name? ")
# print("hello, ", end="") #print function includes end=`\n` but we can provide this argument ourselves to change it
# print(name)

# name = input("What's your name? ")
# print("hello, ", end="???") #shows example of what end would look like
# print(name)

# name = input("What's your name? ")
# print("hello, ", sep="???") #shows example of what seperator would look like
# print(name)

##sep and end are examples of parameters


""" 
A small problem with quotation marks 
"""
# print("hello, "friend"") #won't work for quotes
# print("hello, \"friend\"") #add backslash to tell interpreter keep quotes



""" 
Formatting Strings
"""
# Ask the user for their name
# name = input("What's your name? ")
# print(f"hello, {name}") #use format string (fstring)



"""
More on Strings - dont fully trust user
"""
# Ask the user for their name
# name = input("What's your name? ")

# Remove whitespace from the str
# name = name.strip()

# Capitalize the first letter of each word
# name = name.title() ## can also use name.Capitize() to only capitalize first word

# Print the output
# print(f"hello, {name}")

## more efficient way of writing
# Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
# name = input("What's your name? ").strip().title() #don't need name. anymore for strip and title since included at beginning

# Print the output
# print(f"hello, {name}")

### can also seperate into first and last name
# # Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
# name = input("What's your name? ").strip().title()

# #split the user's name into first name and last name
# first, last = name.split(" ")

# # Print the output
# print(f"hello, {first}")


"""
Integers or int
"""
# x = 1
# y = 2

# z = x + y

# print(z)


# x = input("What's x? ")
# y = input("What's y? ")

# z = x + y #concats x and y together, doesn't add

# print(z)

# x = input("What's x? ")
# y = input("What's y? ")

# z = int(x) + int(y)

# print(z)

## more efficient way to write
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)