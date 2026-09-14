import math


#comment

print("Hello World!")


# VARIABLE DECLARATION AND DATA TYPES:

a = 4        #integer
b = 5.5      #floats
c = "CSAEA"  #strings
d = True     #boolean


print(a, b, c, d)


# OPERATORS:
# +, -, /, *, %, **, //

e = 7+8
print(e)

e += 7
print(e)


# f-string

print(f"e is equal to {e}")

print(4 == 5)
print(4 != 7)

isEqual = "yes" == "yesss"
print(isEqual)

# LOGICAL OPERATORS
# ORDER OF PRECEDENCE   - not, and, or

f = False
t = True

print("")
print(not f)
print(f or t)
print(f or t and not f)
print(f and t)
print("")


# CASTING ()

g = int(5.5)
print(g)
print("")


# STRINGS

s1 = "Goodnight"
s2 = " and "
s3 = "Goodbye"
end = s1 + s2 + s3 #concetanation with +

end += ", Cowboy."

print(end + "\n")

# MATH LIBRARY

print(math.sqrt(14))
print(math.floor(3.65))
print(math.pow(2, 4))
print('      ')

# CONDITIONAL

t = True
f = False

if f:
    print("Reached the first condition")
elif t:
    print("Reached second condition")
else:
    print("Reached else")

if 1 > 1 and 1 + 1 == 2:
    print("Reached the first condition")
elif 45 + 2 < 4 or 1234567890 == 987654321:
    print("Reached second condition")
elif 9 == 9:
    print("Reached the third condition")
else:
    print("Reached else")

print("")
# LISTS

# INDEX: 0  1   2  3   4
nums = [34, 52, 3, 64, 32]
print(nums[2])
print(nums[3])



print("")


words = []

words.append("Word 1")
words.append("Word 2")
words.append("Word 3")

print(words)

words.remove("Word 1")
words.insert(0, "Word 4")
words[1] = "Word 5"
length = len(words)
print(words)
print(length)
print(" ")

# Iteration

# For Loop
# A for loop will iterate over a range
# range(stop), range(start, stop) ...

for i in range(5):
    print(i)

animals = ["sheep", "deer", "moose"]
print(f"List: {animals}")

for animal in animals:
    print(f"We saw a {animal}")


nums = [5.1, 2.2, 5.3, 3.4, 8.5]
# for num in nums:
#     print(num)

for i in range(len(nums)):
    print(nums[i])

# Debugging
# print(len(nums))
# print(range(5))
# for i in range(0, 5):
#     print(i)

# While loop

# iterates while a condition is true
# when the condition becomes false, it stops

x = 5
while x < 10:
    print(x)
    x += 1

t = True
f = False

while t or f:
    print("hi")