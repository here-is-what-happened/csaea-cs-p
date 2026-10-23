# LISTS IN PYTHON
# Lists store multiple values in one variable.
# They are ordered, mutable (changeable), and allow duplicates.

empty_list = []

# CREATE LIST
animals = ['donkey', 'pangolin', 'blobfish']
numbers = [2, 4, 6, 8, 10]
mixed = ['piffle', 42, True, 9.99]

print("Animals list:", animals)
print("Numbers list:", numbers)
print("Mixed data types list", mixed)  

# print the third element in animals.
# print the last element in numbers
#print the first element in the mixed list

print(f"animal : {animals[2]}\nnumber : {numbers[-1]}\nmixed : {mixed[0]}")

animals[-1] = 'babarusa'
print(animals)

# add elements to end of list
animals.append('glass frog')
print(animals)

# insert in specific spot
animals.insert(2, 'aye-aye')
print(animals)

# remove elements
animals.remove("aye-aye")
print(animals)

# remove (pop off) last element and save it into a variable
last_animal = animals.pop()
print(last_animal)
print(animals)

### **Challenge 1: Animal Swap**

# Store this list in a variable: [ 1, 2, 3, 4, 5, 6 ] 
# Ask the user to enter a new integer.
# Replace the **third integer** in the original list with the user’s input, and then print the updated list.
# *Hint: use indexing and assignment.*
'''
nums = [1, 2, 3, 4, 5, 6]
new_nums = int(input("\nEnter a new integer -- > "))
nums.remove(3)
nums.insert(2, new_nums)
print(nums)

'''

### **Challenge 2: Shopping List Manager**

# Initialize an empty list called `shopping`.
# Add three items of your choice using `.append()`.
# Then insert one extra item at the second position and remove one item of your choice.
# Finally, print the final shopping list.

shopping = []
shopping.append('milk')
shopping.append('salmon')
shopping.append('olive oil')
print("")
print(shopping)
shopping.insert(2, 'yogurt')
shopping.remove('milk')
print(shopping)


# length and len

nums = [6, 5, 7, 4, 8, 3, 9, 2, 0, 1]
print(f"\nNumbers : {nums}")
print(f"Length of list:", len(nums))
print("max :", max(nums))
print("min :", min(nums))
print("sum :", sum(nums))

nums.sort()
print(nums)

animals.sort()
print(animals)

nums.reverse()
print(nums)

if "cat" in animals:
    print("Cat is in the list")
else:
    print("Cat is not in the list")

### Challenge 3: Number Stats

# Create a list of five floats called measurements.
# Print the length, minimum, maximum, and sum of the list using built-in functions.

measurements = [1.4, 5.3, 2.9, 9.4, 7.1]
print('length of list :', len(measurements))
print('max of list :', max(measurements))
print('min of list :', min(measurements))
print('sum of list :', sum(measurements))