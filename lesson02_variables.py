# Variables store any kind of information .
# Make sure to use descriptive variables names. 
# Note that variables can be overwritten

age = 73
print(age)
age = 74 
print(age)

password = "G00seberryPie5"
email = "abc@def.com"

print("Password: ", password, "\nEmail:", email)

# Variable naming convention for booleans

isComplete = False
isEnabled = False
isAwake = True

# Math conventions

x = 3.14
y = 8

print(x + y)
count = 10
print(count)
countdown = 10-1
print(countdown)
count=countdown
print(count)

# Challenge 1: Rename Variables  
# Change the variable names x, y, z below to more descriptive names. 

x = "Radia Perlman"
y = 34
z = "Networking Engineer"

x = "Guy Person"
y = 40
z = "network engineer at cisco"
print(f"My name is {x}, and I am {y} of age. I work at {z}")

# Challenge 2: Update Variables  
# Create a variable called 'count' with a value of 10.  
# Use another variable to increase 'count' by 5
# Print the result


count = 10
increase_count = 5
count = count + increase_count
print("")
print(count)


# Challenge 3: Swap Variables  
# Given variables num = 4 and y = "hello".  
# Swap the values so that x = "hello" and y = 4. 
# Use a temporary variable.  
# Hint: You will need to create one new variable. 


num = 4
y = "hello"

temp_variable = y
y = num
num = temp_variable

print(f"\ny = {y} \nnum = {num}")
