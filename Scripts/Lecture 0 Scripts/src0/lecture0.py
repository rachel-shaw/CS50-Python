

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
# x = int(input("What's x? "))
# y = int(input("What's y? "))

# print(x + y)

"""
Float Basics
"""
## using floats
# x = float(input("What's x? ")) #floats allows decimals
# y = float(input("What's y? "))

# print(x + y)

##rounding (to whole number)
# x = float(input("What's x? ")) #floats allows decimals
# y = float(input("What's y? "))

# z = round(x + y)

# print(f"{z:,}") #includes commas in thousands place, etc

##rounding (to 2 numbers after decimal)
# x = float(input("What's x? ")) #floats allows decimals
# y = float(input("What's y? "))

# z = round(x * y, 2)

# print(f"{z:,}") #includes commas in thousands place, etc


"""
More on Floats
"""
#use fstring instead of round to round to 2 numbers after decimal 
# Get the user's input
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# # Calculate the result
# z = x * y

# # Print the result
# print(f"{z:,.2f}") #get two decimal places and include comma for large numbers

"""
Def
"""
    
# Create our own function
# def hello(to):
#     print("hello,", to) #add parameter "to"


# # Output using our own function
# name = input("What's your name? ")
# hello(name)

### add default answer if user doesn't fill out argument
# Create our own function
# def hello(to="world"):
#     print("hello,", to)

# # Output using our own function
# name = input("What's your name? ")
# hello(name)

# # Output without passing the expected arguments
# hello()


#### Setting up Main

# def main():

#     # Output using our own function
#     name = input("What's your name? ")
#     hello(name)

#     # Output without passing the expected arguments
#     hello()


# # Create our own function
# def hello(to="world"):
#     print("hello,", to)

# main()


"""
Returning Values
"""
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


main()