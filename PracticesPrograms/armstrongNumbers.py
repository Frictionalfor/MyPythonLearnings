#Thi is the program for checking the armstrong number

num = int(input("Enter the number: ")) 
n = num
power = len(str(num))
check = 0

while n > 0:
    digit = n % 10
    check += digit **power
    n //= 10

if check == num:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")