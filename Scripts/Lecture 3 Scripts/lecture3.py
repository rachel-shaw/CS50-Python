"""Try and While True"""

# try:
#     x = int((input("What's x? ")))
# except ValueError:
#     print("x is not an integer")
# else: #if try part is correct and runs all the way, then else
#     print(f"x is {x}")


### don't stop program when user enter issue
# while True:
#     try:
#         x = int ((input("What's x? ")))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break

# print(f"x is {x}")


"""
Creating a function to get an integer
"""
# def main():
#     x = get_int()
#     print(f"x is in {x}")

# def get_int():
#     while True:
#         try:
#             x = int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             return x

# main()
                  

"""
pass - catch but ignore 
"""
# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             return int(input("What's x? "))
#         except ValueError:
#             pass

# main()

### Further refine
# def main():
#     x = get_int("What's x? ")
#     print(f"x is {x}")

# def get_int(prompt):
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             pass

# main()



"""""""""""""""""""""
Debugging
"""""""""""""""""""""
# ##use print to debug
# def main():
#     height = int(input("Height: "))
#     pyramid(height)

# def pyramid(n):
#     for i in range(n):
#         print(i, end="")
#         print("#" * (i+1))

# if __name__ == "__main__": #for larger files where you only want to run main?
#     main()


# ##use debugger
# def main():
#     height = int(input("Height: "))
#     pyramid(height)

# def pyramid(n):
#     for i in range(n):
#         print("#" * i)

# if __name__ == "__main__": #for larger files where you only want to run main?
#     main()



"""
Handling Exceptions
"""

# ##add try/except 
# distances = {
#     "Voyager 1": "163",
#     "Voyager 2": "136",
#     "Pioneer 10": "80 AU",
#     "New Horizons": "58",
#     "Pioneer 11": "44 AU"
# }

# def main():
#     spacecraft = input("Enter a spacecraft: ")
#     try:
#         au = float(distances[spacecraft]) 
#     except ValueError:
#         print("Can't convert '{distances[spacecraft]}' to a float")
#         return

#     m = convert(au)
#     print(f"{m} m away")

# def convert(au):
#     return au * 14959780700

# main()


# #add second except 
# distances = {
#     "Voyager 1": "163",
#     "Voyager 2": "136",
#     "Pioneer 10": "80 AU",
#     "New Horizons": "58",
#     "Pioneer 11": "44 AU"
# }

# def main():
#     spacecraft = input("Enter a spacecraft: ")
#     try:
#         au = float(distances[spacecraft]) 
#     except KeyError:
#         print(f"'{spacecraft}' is not in dictionary")
#         return
#     except ValueError:
#         print(f"Can't convert '{distances[spacecraft]}' to a float")
#         return

#     m = convert(au)
#     print(f"{m} m away")

# def convert(au):
#     return au * 14959780700

# main()


"""
Raising Exceptions
"""
# use raise exception
# def main():
#     pace = get_pace(miles=26.2, minutes=0)
#     print(f"You need to run each mile in {round(pace, 2)} minutes.")

# def get_pace(miles, minutes):
#     if not minutes > 0:
#         raise Exception() #or use raise ValueError to specify in error message

#     return minutes / miles

# main()


# ## specify error
# def main():
#     pace = get_pace(miles=26.2, minutes=0)
#     print(f"You need to run each mile in {round(pace, 2)} minutes.")

# def get_pace(miles, minutes):
#     if not minutes > 0:
#         raise ValueError("Minutes must be greater than 0") 
#     return minutes / miles

# main()

