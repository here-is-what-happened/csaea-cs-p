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

print("            ")
print(not f)
print(f or t)
print(f or t and not f)
print(f and t)
print("                           ")


# CASTING ()

g = int(5.5)
print(g)
print("          ")


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