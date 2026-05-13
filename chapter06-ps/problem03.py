# A spam comment is defined as a text containing following keywords:
# "Make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.

spam = ["Make a lot of money", "buy now", "subscribe this", "click this"]

text = str(input("Enter text: "))

if(text in spam): 
    print("This is spam")
else: 
    print("This is not spam")