#This file consists about function and types of functions in Python

def fun():  #defining a functions def is used to define a function
    #func() is the name of the declared function
    print("Happy Frictional Coding with Linux")  #code inside the function
    
fun() # Driver code to call a function

#Function's Argument
def evenOdd(x):  #here you can see x is the Parameter passed to the function evenOdd()
    if (x % 2 == 0):   #Basic even odd program
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: ")) #Taking the input from user
print(evenOdd(num)) #Printing the output and calling the function with argument num


#Types or Arguments

#Default Argument
"""a parameter that assumes a default value if a value is not provided in the function call for that argument"""

def myFun(x, y = 50):
    print("x: ", x)
    print("y: ", y)

myFun(10)

#Keywords Argument
"""values are passed by explicitly specifying the parameter names, so the order doesn’t matter"""

def student(fname, lname):
    print(fname, lname)

student(fname='Frictional', lname='Linux')
student(lname='Linux', fname='Frictional')

#Positional Argument
"""values are assigned to parameters based on their order in the function call"""

def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Frictional", 17)

print("\nCase-2:")
nameAge(17, "Frictional")

#Arbitrary Arguments
"""an pass a variable number of arguments to a function using special symbols"""

#   *args in Python (Non-Keyword Arguments)
#   **kwargs in Python (Keyword Arguments)

def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")  #with *args (Non-Keyword argument in Python)
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")  #with **kwargs (Keyword argument in Python)
    for key, value in kwargs.items():
        print(f"{key} == {value}")

# Function call with both types of arguments
myFun('Hey', 'Welcome', first='Frctional', mid='Happy', last='Coding')

#Function within Function
"""A function defined inside another function is called an inner function (or nested function). 
It can access variables from the enclosing function’s scope and is often used to keep logic protected and organized"""

def f1():#First function
    string = 'Frctional Happy Coding in Linux'
    def f2():  #function f2() in function f1()
        print(string)
        
    f2()
f1()

#Anonymous Function
"""that a function is without a name. 
As we already know the def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions"""

def cube(x): return x*x*x   # without lambda
cube_l = lambda x : x*x*x  # with lambda

num = int(input("Enter a number: "))
print(cube(num))
print(cube_l(num))

#Return Statements in Functions
"""The return statement ends a function and sends a value back to the caller.
It can return any data type, multiple values (packed into a tuple), or None if no value is given."""

def square_value(num):
    """This function returns the square
    value of the entered number"""
    return num**2

num = int(input("Enter the number: "))
print(square_value(num))
print(square_value(num))

#Pass by Reference and Pass by Value
"""When we pass them to a function, the behavior depends on 
whether the object is mutable (like lists, dictionaries) or immutable (like integers, strings, tuples)"""

# Mutable objects: Changes inside the function affect the original object
# Immutable objects: The original value remains unchanged

# Function modifies the first element of list
def myFun(x):
    x[0] = 20

lst = [10, 11, 12, 13]
myFun(lst)
print(lst)   # list is modified

# Function tries to modify an integer
def myFun2(x):
    x = 20

a = 10
myFun2(a)
print(a)     # integer is not modified

#Recursive Function
"""a function that calls itself to solve a problem, it is mostly used in solving maths problems and divide and conquer
type of problems"""

def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 
      
num = int(input("Enter a number: "))
print(factorial(num))

#Here we completed the Functions part in Python