# String formatting, string concatination
first_name = "Ada"
last_name = "Lovelace"


print("Hello,", first_name, last_name, "!")
print("Hello " + first_name + " " + last_name + "!")
print(f"Hello {first_name} {last_name}!")

"""
greeting = "hello"
first_name = "ada"
print(greeting, first_name)

second_letter = greeting[1]
print(second_letter)

# String indexing and slicing

word = "super-cali-fragil-expi-ali-docious"

print(f"\nThe word is: {word}")
print("First letter is:,", word[0])
print("The last letter is,", word[-1])
print("Range of letter (noninclusive)", word[3:7])
print("First five letters:", word[0:5])
print("Everything after first five letters:", word[5:])
print("Last seven letters:", word[-7:])
print("Step through every second character:", word[::2])
print("String in reverse", word[::-1])

last_name = "lovelace"
length = len(last_name)
print("Length of string:", length)
"""

# Challenge 1: Favorite Quote
# Ask the user for their favorite quote and display its length.
# EXAMPLE OUTPUT:
# Enter your favorite quote: Those who believe in telekinetics, raise my hand.
# Your quote is 48 characters long.

length = len(input("What is your favorite quote? "))
print(f"Your quote is {length} charcters long.")

# Challenge 2:
# Ask the user to enter a word that is at least 7 characters long. 
# Print the 2nd through 6th characters.
# Use string slicing.

q = input("Enter a charcter atleast 7 letters long --> ")
print("The 2 through 6 charcters are", q[1:6])

# Challenge 3: Name Formatter
# Ask the user for their first and last name, then format it as "Last, First".
# Use concatenation or f-strings.
# Example output:
# Enter your first name: Ada
# Enter your last name: Lovelace
# Formatted name: Lovelace, Ada

first = input("Enter your first name --> ")
last = input("Enter your last name --> ")
print(f"{last}, {first}")

