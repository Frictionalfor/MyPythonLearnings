#This is about taking input and giving output in Python

# Taking input from the user
name = input("Enter your name: ") # input() function to take user input
age = input("Enter your age: ")
print("Hello, " + name + "! You are " + age + " years old.") # Printing a greeting with user input

# Demonstrating type conversion
age = int(age) # Converting age from string to integer
next_year_age = age + 1
print("Next year, you will be " + str(next_year_age) + " years old.") # Converting integer back to string for concatenation
print() # Printing a blank line for better readability

# Taking multiple inputs in one line
num1, num2 = input("Enter two numbers separated by space: ").split()
num1 = float(num1) # Converting input strings to float
num2 = float(num2)
sum_result = num1 + num2
print("The sum of", num1, "and", num2, "is", sum_result) # Printing the sum of the two numbers
print() # Printing a blank line for better readability

# Demonstrating formatted string literals (f-strings)
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height ** 2)
print(f"{name}, your BMI is {bmi:.2f}") # Printing BMI with two decimal places using f-string
print() # Printing a blank line for better readability

# End of the InputAndOutput.py script