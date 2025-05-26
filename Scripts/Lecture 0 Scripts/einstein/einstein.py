"""
GOALS:
- formula E=mc2
- E = energy (joules)
- m = mass (kilograms)
- c = speed of light (300000000 meters per second)
- Implement a program that prompts the user for mass as an integer
- Outputs the equivalent number of Joules as integer
- Assume the user will input an integer
"""

def main():
    mass = int(input("Enter mass: "))
    E = mass * (300000000*300000000)
    print(E)

main()

