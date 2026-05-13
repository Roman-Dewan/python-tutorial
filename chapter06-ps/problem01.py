num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
num3 = int(input("Enter Number 3: "))
num4 = int(input("Enter Number 4: "))

if(num1 > num2 and num1 > num3 and num1 > num4):
    print("Num1 is gretter", num1)
elif(num2 > num1 and num2 > num3 and num2 > num4): 
    print("Num2 is gretter", num2)
elif(num3 > num1 and num3 > num2 and num3 > num4): 
    print("Num3 is gretter", num3)
else: 
    print("Num4 is gretter", num4)