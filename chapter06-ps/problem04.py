# Write a program to find whether a given username contains less than 10 characters or not.

username = str(input("Enter username: "))

if(len(username) < 10): 
    print("UserName is less than 10 characters")
else: 
    print("UserName is more than 10 characters")
