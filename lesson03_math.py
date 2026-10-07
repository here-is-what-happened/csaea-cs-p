

add = 7 + 24
print("Sum:", add)

subtract = 43 - 3
print("Difference:", subtract)

multiply = 7 * 2
print("Product:", multiply)

float_divide = 10/3
print("Float division:", float_divide)

integer_divide = 7//2
print("Integer division:", integer_divide)

mod = 7%2
print("Modulus:", mod)

exponent = 7 ** 2
print("Exponent:", exponent)

result1 = (2 + 3) * 4
print("Result 1:", result1)

result2 = 2 ** 3 * 4
print("Result 2:", result2)

result3 = 5 + 2 ** 3 * (4 - 1)

# Challenge 1: Rectangle Area  
# Calculate the area of a rectangle with a width of 8 and a height of 5.


w = 8
h = 5
area = w * h

print("Area:", area)

# Challenge 2: Circle Area  
# Use the formula πr² to calculate the area of a circle with radius 7. (Use 3.14 for π.)  

r = 7
pi = 3.14159265358
area = (r ** 2) * pi
print("Area:", area)

# Challenge 3: Shopping Total  
# A book costs $12.99 and a notebook costs $3.50.  
# Calculate the total cost for 3 books and 4 notebooks.

book = 12.99
notebook = 3.50
amount_b = 3
amount_n = 4

total = (amount_b * book) + (amount_n * notebook)

print(f"\nBook: ${book} \nNotebook: ${notebook} \nTotal: ${total}")

# Challenge 4: Even or Odd  
# Use the modulus operator to check if the number 57 is even or odd. 

a = 57

remainder = a % 2

if remainder == 0:
    print(f"\n{a} is even")
else:
    print(f"\n{a} is odd")

