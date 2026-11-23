"""Week 03 Graded Challenge: Functions — Think Python, Chapter 3.

Complete the three functions below. Replace pass with your code.
Use the supplied parameters and return the answer instead of printing it.
Do not use input(). No imports, loops, or conditions are needed.
Keep the function names and parameters unchanged so the tests can call them.
"""


# Challenge 1: Personal Greeting
# Return a greeting using the supplied name.
# Examples: greet("Ada") returns "Hello, Ada!"
#           greet("Deniz") returns "Hello, Deniz!"
def greet(name):
    greeting = f"Hello, {name}!"
    return greeting

name = "link"
greeting_message = greet(name)

print(greeting_message)
# Challenge 2: Square a Number
# Return the given number multiplied by itself.
# Examples: square(4) returns 16; square(7) returns 49.


def square(number):
    squared= number*number
    return squared
#f"doubled value {number} is {doubled}"

x = 2437
squared_value = square(x)
print(f"Squared value of {x} is {squared_value}")

# Challenge 3: Minutes to Seconds
# Return the number of seconds in the supplied number of minutes.
# There are 60 seconds in one minute.
# Examples: minutes_to_seconds(2) returns 120.
#           minutes_to_seconds(5) returns 300.
def minutes_to_seconds(minutes):
    converte_to_seconds = minutes*60
    return converte_to_seconds
y=9876
converted_to_seconds = minutes_to_seconds(y)
print(f"Converted value of {y} is {converted_to_seconds}")
