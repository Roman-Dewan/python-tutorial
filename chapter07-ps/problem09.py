"""
    ***
    * *
    ***
"""

# n = int(input("Enter a number: "))

# for i in range(1, n+1):
#     if(i==1 or i==n):
#         print("*" * n)
#     else:
#         print("*" + " " * (n-2) + "*")



n = int(input("Enter a number: "))
i = 1

while (i<=n):
    if(i==1 or i==n):
        print("*" * n)
    else:
        print("*" + " " * (n-2) + "*")
    i += 1
