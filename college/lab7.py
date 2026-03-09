"""To develop a Python program to implement the following using Functions:
a) Built-in Functions (e.g., math, number, operator)
b) User-Defined Functions"""


# a) Built-in Functions
import math
def calculate_circle_area(radius):
    """Calculate the area of a circle given its radius."""
    area = math.pi * (radius ** 2)
    return area

# b) User-Defined Functions
def greet(name):
    """Greet the user by name."""
    return f"Hello, {name}!"    

# Example usage
radius = 5
area = calculate_circle_area(radius)
print(f"The area of a circle with radius {radius} is: {area}")

name = "Swanand"
greeting = greet(name)
print(greeting)
