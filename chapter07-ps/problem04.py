# Write a program to find whether a given number is prime or not.

num = int(input("Enter a number: "))

for i in range (2, num):
    if(num % 2 == 0):
        print("This is not Prime")
        break
else:
    print("This is Prime")