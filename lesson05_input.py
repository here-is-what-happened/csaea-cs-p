import random

# USER INPUT IN PYTHON
#print("<prompt>")

"""
name = input("Enter your name : ")
print(f"Hello {name}")

age = input("Enter your age: ")
print(f"Your age is {age}")

print(type(name), type(age))

age_converted = int(age)
print(type(age_converted))

height = float(input("Enter your height: "))
print(f"You are {height} meters tall")
print(height + 1)

"""

# Challenge 1: Favorite Color
# Ask the user for their favorite color and print out a message using it.

fav_color = input("What is your favorite color? ")
print(f"Your favorite color is {fav_color}")

# Challenge 2: Adding Two Numbers
# Ask the user for two numbers, add them together, and print the result.



num1 = int(input("\nGive a random number. "))
num2 = int(input("Give another random number. "))

total = num1 + num2
print(f"The total is {total}")

# Challenge 3: Circle Area from User Input
# Ask the user for the diameter of a circle, then calculate and print the area.

diameter = int(input("\nEnter the diameter of a circle : "))
area = ((diameter/2) ** 2) * 3.14159265
print(f"The area is {area}")

# Challenge 4: Custom Die Roll
# Ask the user to enter how many sides the die should have.
# Then simulate rolling the die once and print the result.

sides_of_die = int(input("\nHow many sides should the die have? "))
roll_of_die = random.randint(1, sides_of_die)
print(f"You rolled a {roll_of_die}")