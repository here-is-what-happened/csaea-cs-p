import math

# Challenge 1, Tip generator

bill = 50

tip = bill * 0.2
total = bill + tip

print(f"Your tip is ${tip} ")
print(f"Your total is ${total}")


# challenge 2, pizza order

students = 23
slices_per_student = 2
slices_per_pizza = 8

pies = math.ceil(slices_per_student * students / slices_per_pizza)
leftover = (pies * slices_per_pizza) / slices_per_pizza * students

print(f"\nOrder {pies} pizza pies \n{leftover} extra slices of pizza ")


# Challenge 3, temperature converter

fahrenheit = 212
celsius = (fahrenheit - 32) * 5/9
print(f"\n{fahrenheit} F is {celsius} C")


# challenge 4, report card
score = 84
print("\n")
if score >= 90:
    print("A")
elif score >= 80 and score < 90:
    print("B")
elif score >= 70 and score < 80:
    print("C")
elif score >= 60 and score < 70:
    print("D")
else:
    print("F")

# challenge 5, login screen
print("\n")
password = "csaea2026"
attempt = "CSAEA2026"

if attempt == password:
    print("Acess granted")
else:
    print("Acess denied")


# challenge 6, even/odd parking

plate = 4827
remainder = 4827 % 2
if remainder == 1:
    print("\nPark on the West side")
else:
    print("\nPark on the East side")

# challenge 7, roller coaster gate

height = 30
age = 9
has_adult = True

if height < 48:
    print("You can't ride the rolar coaster")
elif height >= 48 and age >= 10 or has_adult == True:
    print("\nYou may ride the rollar coaster")
else:
    print("\nYou can't ride the roller coaster")

# challenge 8, name tag generator
first = "Ada"
last = "Lovelace"
school = "CSAEA"



# challenge 11, rocket launch count down

print("\n")
for i in range(10, 1, -1):
    print(i)
print("The rocket has launched!")

# challenge 12, times table, helper

number = 7
total = 0
print("\n")
for i in range(1, 11, 1):
    total += 7
    print(f"{number} x {i} = {total}")

# challenge 14, high score calculator
scores = [340, 1250, 980, 1510, 720]

high_score = max(scores)
print(f"\nThe high score is {high_score}")

# challenge 15, class pass rate
grades = [88, 65, 72, 91, 54, 70]
passing = 70
passed = 0
total_students = 0

for grade in grades:
    if grade >= 70:
        passed += 1
        total_students += 1
    else:
        total_students += 1
print(f"\n{passed} out of {total_students} students passed the test")

# challenge 16, garden fence

area = 49
amount_of_fence = 4*(math.sqrt(area))
print(f"\nFence needed in ft : {amount_of_fence}")

# challenge 17, parking meter calculator

minutes_parked = 50
block_length = 15
cost_per_block = 1

final_cost = math.ceil(minutes_parked / block_length)
print(f"\nYou owe ${final_cost} for parking")

# challenge 18, playlist swap

playlist = ["Intro", "Song A", "Song B", "Finale"]

playlist[0], playlist[-1] = playlist[-1], playlist[0]

print(f"\n{playlist}")