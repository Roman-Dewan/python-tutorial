# Write a program using functions to find greatest of three numbers.

def average(a, b, c):
    avg = (a + b + c) / 3
    return avg

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

result = round(average(num1, num2, num3), 2)
print(result)