# Chapter 1 - Exercise 1.9.2

#round(41.5)
#round(42.5)
#round(43.5)
#round(44.5)

# It seems like Python rounds down if the number is even
# And if the number is odd, it rounds up.
# I double checked this with a virtual assistant which verified this by saying:
# "Python uses a rounding method called "round half to even," which means that if a number ends in 0.5, it will round to the nearest even integer."

# Reflection: When comparing this with the instructor's, it looks like we had the same results.


# Exercise 1.9.3

#n = +2
#n = 2++2
#n= 4 2
#n = round42.5
#print (n)

# Putting a + in front of a number just makes the number positive
# "2++2" acts like 2+2 and makes the variable "4"
# If you have two values with no operator, like "4 2", you get a SyntaxError
# If you call a function like "round()" and you forget one or both parenthesis then you get a syntax error

# Reflection: When comparing this with the instructor's, it looks like we had the same results.


# Exercise 1.9.4

# My best guess for the type of each expressions are:
# 765 - int
# 2.718 - float
# '2 pi' - string
# abs(-7) - function? Or, if we're guessing the type of the thing produced, then int
# abs(-7.0) - function? Or, if we're guessing the type of the thing produced, then float
# abs - class
# int - class
# type - function

print(type(765))
print(type(2.718))
print(type('2 pi'))
print(type(abs(-7)))
print(type(abs(-7.0)))
print(type(abs))
print(type(int))
print(type(type))

# Reflection: When comparing this with the instructor's, it looks like we had the same results.


# Exercise 1.9.4

# How many seconds are there in 42 minutes 42 seconds?
seconds_in_minutes = 42 * 60
total_seconds = seconds_in_minutes + 42
print(f"\n\nExercise 1.9.4 - 1. There are {total_seconds} in 42 minutes 42 seconds.\n")

# How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
miles = 10 / 1.61
print(f"2. There are {miles:.1f} miles in 10 kilometers.\n")

# If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace in seconds per mile?
avg_pace = total_seconds / miles
print(f"3. Average pace would be {avg_pace:.1f} seconds per mile.\n")

# What is your average pace in minutes and seconds per mile?
total_minutes = total_seconds / 60
remaining_seconds = total_minutes % 60
avg_pace_min = total_minutes / miles
print(f"4. Average pace would be {avg_pace_min:.1f} minutes and {remaining_seconds:.1f} seconds per mile.\n")

# What is your average speed in miles per hour?
total_hours = total_minutes / 60
avg_pace_hr = total_hours / miles
print(f"5. Average pace would be {avg_pace_hr:.2f} hours per mile.\n")

# Reflection: When comparing this with the instructor's, it looks like we had the similar results.


# Chapter 2 - Exercise 2.11.2

# 17 = n
# x = y = 1
# n = 7;
# n = 7.
# import maath

# None of the above statements are legal. 
# "17 = n" causes a syntax error, 
# "x = y = 1" just doesn't run (it causes an error but doesn't say what the error is so I imagine it's just not running)
# Adding a semi-colon at the end of a statement causes the same effect as "x = y = 1"
# Adding a period at the end of a statement causes the same effect as the semi-colon 
# Finally, trying to import "maath" causes a "ModuleNotFoundError" error

# Reflection: When comparing this with the instructor's, it looks like we had the same results.
# Though I wasn't sure what to do with "x = y = 1" and I just figured it didn't run, so it was interesting
# to see that this is a valid way of assigning a value to two different variables at the same time.

# Exercise 2.11.3

# Part 1
import math

pi = math.pi
# radius is in centimeters
radius = 5 
# volume is in cubic centimeters
volume = (4/3)*pi*(radius**3)

print(f"Exercise 2.11.3")
print(f"1. The volume of a sphere with a radius of {radius} is {volume:.1f} cubic centimeters\n")

# Reflection: When comparing this with the instructor's, it looks like we had the same results.


# Part 2
x = 42
cos_x = math.cos(x)
sin_x = math.sin(x)
sum = (cos_x**2)+(sin_x**2)
print(f"2. The result is {sum:.1f}.\n")

# Reflection: When comparing this with the instructor's, it looks like the instructor's
# results are more efficient and check to see if the pythagorean identity is true
# So rather than having a "yes/no" answer hard coded in, it'll check for you
# and then pick the appropriate answer. I like this much better than my own because if there is a value
# that isn't true, the program is already designed to react to that and nothing would need to be changed.


# Part 3
print(f"3a. Exponentiation operator: {math.e**2}")
print(f"3b. math.pow: {math.pow(math.e,2)}")
print(f"3c. math.exp: {math.exp(2)}")

# Reflection: When comparing this with the instructor's, it looks like we had the same results.