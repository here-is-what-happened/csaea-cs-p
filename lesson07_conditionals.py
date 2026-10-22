# Boolean refresher

print(3 == 2)
print("Hello" == "Hi there")
print(7 != 4)
print(4 > 5)

num = 11
if num == 10:
    print("Your num is equal to 10")
else:
    print("Your number is less then or greater then 12")

###

temperature = 72
if temperature > 95:
    print("It's hot")
elif temperature >= 60:
    print('Nice')
else:
    print("its cold")



print()

x = 2
y = 20

if x == y:
    print("x is equal to y")
elif x > y:
    print("x is greater then y")
elif x < y:
    print("x is less then y")
else:
    print("error")


# logical operators

age = 16
has_permission = True

if age >= 16 and has_permission:
    print('you can drive')
else:
    print('you cant drive')


day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!") 
else:
    print("It's the weekday")


if day is not "Monday":
    print("It's not Monday, thankfully")


# Challenge 1: Movie Admission
# Ask the user for their age. 
# If under 13, “You can watch PG or G movies.”
# If 13–17, “You can watch PG-13 movies.”
# If 18+, “You can watch any movie.”
# Example output:
# Enter your age: 15
# You can watch PG-13 movies.
'''
age = int((input("Whats your age? ")))

if age >= 18:
    print("You can watch any movie.")
elif age >= 13 and age <= 17:
    print("You can watch PG-13 movies.")
elif age < 13:
    print("You can watch pg or g movies")
else:
    print('error')
'''
# Challenge 2: Leap Year
# Ask for a year. It's a leap year if divisible by 4, EXCEPT century
# years (divisible by 100), which must also be divisible by 400.
# Example output:
# Enter a year: 1900
# 1900 is not a leap year.
# (Test: 2024 -> leap, 1900 -> not, 2000 -> leap)

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")