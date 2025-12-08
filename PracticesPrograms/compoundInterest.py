#This is the program for Compound Interest

principal = int(input("Enter the principal: "))
time = float(input("Enter the time period (in years): "))
rate = float(input("Enter the rate: "))

#A = P(1 + R/100)^t 
amount = principal*(1 + rate/100) **time

print("The Compound Interest is: ", amount-principal) #CP = amount - principal
