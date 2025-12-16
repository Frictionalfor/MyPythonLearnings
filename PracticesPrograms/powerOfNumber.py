import math

def power_of_number(base, exponent):
    """
    This function takes a base number and an exponent, and returns the base raised to the power of the exponent.
    
    Parameters:
    base (int/float): The base number.
    exponent (int/float): The exponent to which the base is raised.
    
    Returns:
    int/float: The result of base raised to the power of exponent.
    """
    return math.pow(base, exponent) 

num = float(input("Enter the base number: "))
exp = float(input("Enter the exponent: "))
result = power_of_number(num, exp)
print(f"{num} raised to the power of {exp} is: {result}")   

