"""
GOALS"
- implement a program that prompts consumers users to input a fruit (case-insensitively)
- then outputs the number of calories in 1 portion
- assume users will type fruits exactly as written in the poster
- ignore any input that isn't a fruit
"""

fruit_dictionary = {
    "Apple": 130,
    "Avocado": 50,
    "Banana": 110,
    "Cantaloupe": 50,
    "Grapefruit": 60,
    "Grapes": 90,
    "Honeydew Melon": 50,
    "Kiwifruit": 90,
    "Lemon": 15,
    "Lime": 20,
    "Nectarine": 60,
    "Orange": 80,
    "Peach": 60,
    "Pear": 100,
    "Pineapple": 50,
    "Plums": 70,
    "Strawberries": 50,
    "Sweet Cherries": 100,
    "Tangerine": 50,
    "Watermelon": 80
}

def main():
    fruit = input("Item: ")

    if fruit in fruit_dictionary:
        print(f"Calories: {fruit_dictionary[fruit]}")


main()