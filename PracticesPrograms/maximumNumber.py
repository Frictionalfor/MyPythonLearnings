#This is just a maximum number find program


num1, num2 = map(int, input("Enter the 2 numbers and separate them with space: ").split())

if num1 > num2:
    print(num1, "is greater than the other one")

elif num1 == num2:
    print("Both are equal")

else:
    print(num2, "is greater")
