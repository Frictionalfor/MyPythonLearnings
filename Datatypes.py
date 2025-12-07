#This file consist of all the datatypes which Python has

#Numeric
integer = 67 #This is an int datatype it stores a whole integer number 
integer2 = -12 #A negative integer
print("Positive integer: ", integer)
print("Negative integer: ", integer2)

float_var = 2.4 #This is a float datatype it stores decimal values in it
float_var2 = -243 #This stores a negative float value
print("Positive float number: ", float_var)
print("Negative float number: ", float_var2)

#Complex number = real number + imaginary number
z = 3 + 4j
print(z.real)  # Output: 3.0
#real represents the real part of the complex number
print(z.imag)  # Output: 4.0
#imag represents the imaginary part of complex number

#Dictionary
"""It is used to store values like map in it
It holds data in key: value pair
Key value is provided to make it optimized"""

d = {} #Empty dictionary

d = {1: 'happy', 2: 'Frictional', 3: 'Linux'} #initializing dictionary d
# : is used for paring key and value
# , is used to seprate a key and value pair

#There is a constructor for dictionary for creating it
#dict()
d1 = dict()

#Accessing values in Dictionary
print(d[3]) #Accessing using key
print(d.get(2)) #Accessing using get()

"""We can also put a string as a key value in dictionary"""

#Boolean
"""This datatype has only 2 values True and False
1 = True and 0 = False"""
#This is case sensetive True and False can only be use

if 1:
    print("1 is truthy")

if not 0:
    print("0 is falsy")

#Sequence 

"""This datatype has 3 types"""
#First one is String Datatype
"""This datatype consists of alphabetical words in them
It has single quotes in it"""

string = 'Happy Linux Coding with Frictional'
print(string)

# check data type 
print(type(string))

# access string with index
print(string[1])
print(string[2])
print(string[-1])

#Second is List
"""It is similar to the array we used in other programming languages"""
#It also consists of int, float, string types in it.

# Empty list
a = []

# list with int values
listOfInt = [1, 2, 3]
print(listOfInt)

# list with mixed values int and String
listOfMix = ["Linux", "Frictional", "Coding", 4, 5]
print(listOfMix)

