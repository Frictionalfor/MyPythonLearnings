#This is program for checking the prime number

num = int(input("Enter the number: "))

if num <= 1:
    print("The number is invaild")

else:
    is_prime = True #It is a varible flag for checking for the number
    for i in range(2, int(num **0.5) + 1):
        if num % i == 0:
            is_prime = False   #If the condition gets true we conclude that the number is not a prime number
            break #and break the loop
    

#Giving the proper output to the user
if is_prime == True:
    print(num, "is the prime number")  
else:
    print(num, "is not a prime number")

