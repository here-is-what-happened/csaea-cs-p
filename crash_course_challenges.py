import math

# Challenge 1, Tip generator

bill = 50

tip = bill * 0.2
total = bill + tip

print(f"Your tip is ${tip} ")
print(f"Your total is ${total}")

# Challenge 3, temperature converter

fahrenheit = 212
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit} F is {celsius} C")

# challenge 6, even/odd parking

plate = 4827
remainder = 4827 % 2
if remainder == 1:
    print("Park on the West side")
else:
    print("Park on the East side")

# challenge 11, rocket launch count down

print("\n")
for i in range(10, 1, -1):
    print(i)
print("The rocket has launched!")

# challenge 12, times table, helper

number = 7
total = 0

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
print(f"Fence needed in ft : {amount_of_fence}")