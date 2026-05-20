# Write a python function which converts inches to cms.

def inches_to_cms(inches):
    cms = inches * 2.54
    return round(cms, 2)

inches = float(input("Enter a value in inches: "))
cms = inches_to_cms(inches)
print(cms)