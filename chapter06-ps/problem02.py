marks = []
num1 = marks.append(int(input("Enter Number 1: ")))
num2 = marks.append(int(input("Enter Number 2: ")))
num3 = marks.append(int(input("Enter Number 3: ")))

percentage = (sum(marks) / 300) * 100
if(marks[0] < 33 or marks[1] < 33 or marks[2] < 33 or percentage < 40): 
    print("You are failed your, percentage is: ", percentage)
else: 
    print("You are passed your, percentage is: ", percentage)
