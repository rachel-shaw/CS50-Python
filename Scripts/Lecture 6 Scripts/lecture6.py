"""
Open
"""
# name = input("What's your name? ")

#write file
# file = open("names.txt", "w")
# file.write(name)
# file.close()

#append to write and add more
# file = open("names.txt", "a")
# file.write(f"{name}\n") 
# file.close()

"""
With (automate closing the file)
"""
# name = input("What's your name? ")

"""automate closing the file"""
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

"""read from file"""
# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip()) #rstrip removes additional line between rows

"""read and sort"""
# names = []

# with open("names.txt") as file: #don't need to specify r for read
#     for line in file:
#         names.append(line.rstrip()) #this appends list to remove extra line, not appending file

# for name in sorted(names):
#     print(f"hello, {name}")

"""faster way to read and sort"""
# with open("names.txt") as file:
#     for line in sorted(file):
#         print("hello,", line.rstrip())

"""
CSV
"""
"""write CSV"""
# name = input("Name / House? ")

# #automate closing the file
# with open("students.csv", "a") as file:
#     file.write(f"{name}\n")

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")

"""sort in csv using list"""
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")
    
# for student in sorted(students):
#     print(student)

"""dictionaries in csv"""
# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)

# for student in students:
#     print(f"{student['name']} is in {student['house']}")

"""dictionaries sorted"""
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)

# def get_name(student):
#     return student["name"]

# for student in sorted(students, key = get_name, reverse=False):
#     print(f"{student['name']} is in {student['house']}")

"""better way to do use dictionaries to sort"""
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append({"name": name, "house": house})

# for student in sorted(students, key=lambda student: student["name"]): #lambda is an anonymous function
#     print(f"{student['name']} is in {student['house']}")

"""update csv to home address instead of house"""
# students = []

# with open("students_home.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append({"name": name, "home": home})

# for student in sorted(students, key=lambda student: student["name"]): #lambda is an anonymous function
#     print(f"{student['name']} is in {student['home']}")

"""Above gives ValueError; must use reader to avoid extra commas"""
# import csv

# students = []

# with open("students_home.csv") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         students.append({"name": row[0], "home": row[1]})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

"""add column names into csv + use DictReader"""
# import csv

# students = []

# with open("students_home.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['home']}")

"""write using DictWriter"""
# import csv

# name = input("What's your name? ")
# home = input("What's your home? ")

# with open("students_home2.csv", "a") as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "home"])
#     writer.writerow({"name": name, "home": home})

"""
Binary Files & PIL
"""
# import sys

# from PIL import Image

# images = []

# for arg in sys.argv[1:]:
#     image = Image.open(arg)
#     images.append(image)

# images[0].save(
#     "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
# )

"""
Pillow Shorts
"""
# import sys
# from PIL import Image
# from PIL import ImageFilter

# def main():
#     with Image.open("in.jpeg") as img:
#         # print(img.size)
#         # print(img.format)
#         img = img.rotate(180)
#         img = img.filter(ImageFilter.FIND_EDGES)
#         img.save("out.jpeg")

# main()

"""
Reading and Writing CSVs Shorts
"""
"""read brightness from each file"""
# import csv
# import numpy as np
# from PIL import Image

# def main():
#     with open("src_readwritecsvs/views.csv", "r") as file:
#         reader = csv.DictReader(file)

#         for row in reader:
#             brightness = calculate_brightness(f"src_readwritecsvs/{row['id']}.jpeg")
#             # print(row["id"])
#             print(round(brightness, 2))

# def calculate_brightness(filename):
#     with Image.open(filename) as image:
#         brightness = np.mean(np.array(image.convert("L"))) / 255
#     return brightness


# main()

"""create new csv with brightness column (read + write two separate files at same time)"""
# import csv
# import numpy as np
# from PIL import Image

# def main():
#     with open("src_readwritecsvs/views.csv", "r") as views, open("analysis.csv", "w") as analysis:
#         reader = csv.DictReader(views)
#         writer = csv.DictWriter(analysis, fieldnames = reader.fieldnames + ["brightness"])
#         writer.writeheader()

#         for row in reader:
#             brightness = calculate_brightness(f"src_readwritecsvs/{row['id']}.jpeg")
#             writer.writerow(
#                 {
#                     "id": row["id"], 
#                     "english_title": row["english_title"], 
#                     "japanese_title": row["japanese_title"],
#                     "brightness": round(brightness, 2)
#                 }
#             )


# def calculate_brightness(filename):
#     with Image.open(filename) as image:
#         brightness = np.mean(np.array(image.convert("L"))) / 255
#     return brightness


# main()

"""write code more efficiently"""
# import csv
# import numpy as np
# from PIL import Image

# def main():
#     with open("src_readwritecsvs/views.csv", "r") as views, open("analysis.csv", "w") as analysis:
#         reader = csv.DictReader(views)
#         writer = csv.DictWriter(analysis, fieldnames = reader.fieldnames + ["brightness"])
#         writer.writeheader()

#         for row in reader:
#             row["brightness"] = round(calculate_brightness(f"src_readwritecsvs/{row['id']}.jpeg"),2)
#             writer.writerow(row)


# def calculate_brightness(filename):
#     with Image.open(filename) as image:
#         brightness = np.mean(np.array(image.convert("L"))) / 255
#     return brightness


# main()



"""
Reading and Writing Files
"""

def main():
    with open("src_readwritefiles/alice.txt", "r") as f:
        # contents = f.read() #read whole thing
        contents = f.readlines()

    # print(contents[0]) #read line 0

    chapter1 = contents[52:271]
    with open("chapter1.txt", "w") as f:
        f.writelines(chapter1)
    

main()