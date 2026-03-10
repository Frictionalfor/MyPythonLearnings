import math

def mathOperations():
    print("Math Operations:")
    print("Addition: a + b =", a + b)
    print("Subtraction: a - b =", a - b)
    print("Multiplication: a * b =", a * b)
    print("Division: a / b =", a / b)
    print("Power: a ** b =", math.pow(a, b))
    print("Square Root of a: ", math.sqrt(a))
    
def numberOperations():
    print("Number Operations:")
    print("Max : ", max(a, b))
    print("Min : ", min(a, b))
    print("Absolute: ", abs(a))

def main():
    global a, b
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    mathOperations()
    numberOperations()

main()