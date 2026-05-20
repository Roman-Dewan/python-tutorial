# Write a recursive function to calculate the sum of first n natural numbers.

def sum(number):
    if(number == 1):
        return 1
    else: 
        return number + sum(number - 1)

number = int(input("Enter a number: "))
print(f"The sum of first {number} natural numbers is {sum(number)}.")