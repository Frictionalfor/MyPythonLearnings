#This file consists of pass statement in Python
#The pass statement in Python is used as a placeholder for future code.
#When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.

#Pass Statement in Functions
"""s used when we define a function but don't want to implement its logic immediately. 
It allows the function to be syntactically valid, even though it doesn’t perform any actions yet."""

def fun():
    pass

fun() # Call the function

#Control Statements with Pass
"""The pass statement can also be used in control statements (like if, for, while) where no action is required."""
for i in range(5):
    pass  # Placeholder for future code 

if True:
    pass  # Placeholder for future code
else:
    pass  # Placeholder for future code     

while False:
    pass  # Placeholder for future code

#Class with Pass Statement
"""The pass statement can be used when defining a class without any methods or attributes."""
class MyClass:
    pass  # Placeholder for future code
obj = MyClass()  # Create an instance of the class
print(obj)  # Output the object
#This file consists of return statements, pass by reference/value and recursive functions in Python

