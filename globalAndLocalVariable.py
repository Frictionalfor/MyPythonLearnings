#This file consists of examples of global and local variables in Python

# Global variable
x = "Happy"

def Happy():
    print(x)  # Accessing global variable inside a function 

Happy()  # Output: Happy
print(x)  # Accessing global variable outside the function  

# Local variable
def coding():
    y = "coding"
    print(y)  # Accessing local variable inside the function

coding()  # Output: coding
# print(y)  # Uncommenting this line will raise an error as y is not defined
# Accessing local variable outside the function
# NameError: name 'y' is not defined



#Global and Local Variable with same name

a = 1  # Global variable

def f():
    print("f():", a)  # Uses global a

def g():
    a = 2  # Local shadows global
    print("g():", a)

def h():
    global a
    a = 3  # Modifies global a
    print("h():", a)

print("global:", a)
f()
print("global:", a)
g()
print("global:", a)
h()
print("global:", a)

