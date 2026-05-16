# Write a program to calculate the factorial of a given number using for loop.

num = int(input("Enter a number: "))
i = 1
multiplication = 1

for i in range(1, num+1): 
    multiplication *= i
    i += 1

print(f"The factorial of {num} is {multiplication}")