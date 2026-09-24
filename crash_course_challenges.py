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
