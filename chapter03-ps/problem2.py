# Write a program to fill in a letter template given below with name and date.

letter = """
        Dear <|Name|>,
        You are selected!
        Date: <|Date|>
    """
name = str(input("Enter your name: "))
date = str(input("Enter the date: "))

letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)

print(letter)