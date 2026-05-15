# Write a python program that takes user input and prints the multiplication table of that number.

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} X {i} = {n*i}")
