#This file consists of recursive functions in Python

#Working of Recursion

"""A recursive function is just like any other Python function except that it calls itself in its body.
Let's see basic structure of recursive function:"""
"""
def recursive_function(parameters):
    if base_case_condition:
        return base_result
    else:
        return recursive_function(modified_parameters)
"""

#Base Case: The stopping condition that prevents infinite recursion.
#Recursive Case: The part of the function where it calls itself with modified parameters.

#Example 1: Factorial of a number using recursion
num = int(input("Enter a number to find its factorial: "))
def factorial(num):
    # Base case
    if num == 0 or num == 1:
        return 1
    else:
        # Recursive case
        return num * factorial(num - 1)
    
print(f"The factorial of {num} is {factorial(num)}")

#Example 2: Fibonacci series using recursion
n = int(input("Enter the number of terms in Fibonacci series: "))

def fibonacci(n):
    # Base case
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        # Recursive case
        fib_series = fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series   
    
print(f"The first {n} terms of Fibonacci series are: {fibonacci(n)}")


#Types of Recursions

#Tail Recursion: When the recursive call is the last operation in the function.
def tail_recursive_factorial(n, accumulator=1):
    if n == 0 or n == 1:
        return accumulator
    else:
        return tail_recursive_factorial(n - 1, n * accumulator)
    
print(f"Tail Recursive Factorial of {num} is {tail_recursive_factorial(num)}")

#Non-Tail Recursion: When there are operations after the recursive call.
def non_tail_recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = non_tail_recursive_factorial(n - 1)
        return n * result  # Operation after the recursive call
    
print(f"Non-Tail Recursive Factorial of {num} is {non_tail_recursive_factorial(num)}")

#Recursion Vs Iteration

# Recursion can be more elegant and easier to implement for problems that have a natural recursive structure (like tree traversals).
# However, recursion can lead to higher memory usage due to function call stack, and Python has a recursion limit (default is 1000).
# Iteration is generally more memory efficient and can be faster for simple loops, but may require more code for complex problems.  

# Example of Iterative Factorial
def iterative_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(f"Iterative Factorial of {num} is {iterative_factorial(num)}")
