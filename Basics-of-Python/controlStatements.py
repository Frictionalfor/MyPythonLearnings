#Control Statements manges the flow of program

#if statement

age = 18

if age >= 18:
    print("Your are adult") #This statement will only execute when the condition is true

#When the condition is false then the if block code won't be executed

#if-else statement
"""This statement has 2 ways in it First on is when the condition is true and other is false"""
age = 10

if age >= 18:
    print("Your are adult")  #When condition is true it executes the if block

else:
    print("You are a teenager")     #When condition is false it executes the else block


#if-elif-else statements

"""This statement is used when there are mutiple conditions in it"""
# elif = else if

age = 60

if age <= 17:
    print("You are teen")    #if condition is true this will be executed

elif age <= 40:
    print("You are young")  #if the first condition is false then this condition will get checked and excuted as it is

elif age <= 50:
    print("You are getting older")      #if the above condition is false then this condition will get checked and excuted as it is

else:
    print("You are old")        #if all the condtions are false this will be executed

#Nested if-else conditions

"""an if-else statement inside another if statement we can use nested if statements to check conditions within conditions"""

age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")


#Ternary Conditional Statement

"""It is just a compact way to write if-else statement"""

# Assign a value based on a condition
age = 20
s = "Adult" if age >= 18 else "Minor" 
print(s)

#Match Case statement
"""it is Python's version of a switch-case found in other languages"""

number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")