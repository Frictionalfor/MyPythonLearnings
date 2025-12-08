#Loops

#for loop 
""" it is used to iterate over a sequence"""
print("For Loop: ")
n = 5
for i in range(0,n):  #range() is a function which checks the range of the given argument here it is 0 to n
    print(i)


#while loop
"""it is used to execute a block of statements repeatedly until a given condition is satisfied"""
print("While loop: ")
n = 0
while (n < 5):
    n = n + 1
    print("Happy Coding in Linux")

#Infinite While Loop
"""This is just a while loop which never ends it runs infinte number of times"""
"""
while (True):
    print("Frictional Happy Linux")  #Do  not run it!!

"""

#Nested Loop 
"""One loop is present inside another loop"""
print("Nested Loop (for + for): ")
# from __future__ import print_function    || Just imported print_function from future object

for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()


#Loop Control Statements

#Continue
"""returns the control to the beginning of the loop"""

print("Continue Statement: ")

for letter in 'HappyCodingLinux':   #here if you observe that we can also run loops on strings
    if letter == 'C' or letter == 'x':   #if statemnet with or logical operator
        continue          #the keyword for contunue looping statement
    print('Current Letter :', letter)  #for printing letters



#Break
"""It bring control out of loop"""

print("Break statement: ")

for letter in 'HappyCodingLinux':
    if letter == 'i' or letter == 'g':
        break

print('Current Letter :', letter)

#Pass
"""It is used to empty the loop"""

print("Pass Statement: ")
for letter in 'FrictionalLinux':
    pass
print('Last Letter :', letter)
