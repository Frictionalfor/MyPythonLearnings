# This program is for printing the Fabonacci series of a number

num = int(input("Enter how many terms you want: "))

previousNumber, nextNumber = 0, 1

print("Fibonacci Series:")

for i in range(num):
    print(previousNumber, end=" ")
    previousNumber, nextNumber = nextNumber, previousNumber + nextNumber
