#This is the program of basic calculator in Python

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Enter 1 for Addition \n Enter 2 for Substraction \n Enter 3 for Multiplcation \n Enter 4 for Division\n")
key = int(input("Enter: "))

match key:
    case 1:
        print("Addition is: ", num1 + num2)

    case 2:
        print("Substraction is: ", num1 - num2)
    
    case 3:
        print("Multiplcation is: ", num1 * num2)

    case 4:
        if (num2 != 0):
            print("Division is: ", num1 / num2)

        else:
            print("Division by 0 not possible")

    case _:
        print("Invalid!!")

"""There is one more way to make a calculator in Python it is in just one line"""


cal = eval(input("Enter the expression: "))
print(cal)