# Write a program to find the sum of first n natural numbers using while loop.

num = int(input("Enter a number: "))
i = 1
sum = 0

for i in range(0, num+1): 
    sum += i
    i += 1

print(f"The sum of first {num} natural numbers is {sum}")