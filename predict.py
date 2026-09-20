import math

f = False
t = True

nums = [34, 52, 3, 64, 32]

# print(7 // 2, 7 % 2, -7 // 2)
# output prediction : 3.5, 1, -3.5

print(7 // 2, 7 % 2, -7 // 2)
# Output : 3, 1, -4


# print(int(-5.9), math.floor(-5.9))
# ouput prediction : -5, -6
  # They are different because one is taking the decimal away
  # While the Other is rounding down no matter the circumstance

print(int(-5.9),math.floor(-5.9))
# Output : -5 -6


# print("5" * 3, "5" + "5")
# output prediction : 555 55

print("5" * 3, "5" + "5")
# Output : 555 55


# print(2 ** 4, math.pow(2, 4))
# output prediction : 16 16
  # The two values look different because one uses the pow function from an import
  # While the other uses the built in ** function

print(2**4,math.pow(2,4))
# Output : 16, 16.0


# print(True + True + True)
# output prediction : True

print(True + True + True)
# Output : 3


# print(0.1 + 0.2 == 0.3)
# out prediction : True

print(0.1 + 0.2 == 0.3)
# Output : False
# Suprised because I thought it was true
# It makes sense now because the errors add up making them slightly unequal

