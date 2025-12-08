import math   #for way 2


"""Way 1 without any Libary"""
#This program is to find factorial of a number

num = int(input("Enter a number: "))
fac = 1
for i in range(1, num +1):
    fac *= i

print("Factorial of the entered number is:", fac)


"""There is an another way also to find factorial of a number in Python"""

numX = int(input("Enter the number: "))
print("The factorial is: ", math.factorial(numX))
