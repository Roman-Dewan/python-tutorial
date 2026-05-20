# Write a python function to print multiplication table of a given number.

def multiplication_table(number):
    for i in range(1, 11, 1):
        print(f"{number} x {i} = {number * i}")

number = int(input("Enter a number: "))
multiplication_table(number)