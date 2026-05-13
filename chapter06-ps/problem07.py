post = "Hey buddy Whats'up? I'm fine, what about you? roman, ..?"

name = str(input("Enter name: "))

if(name.lower() in post.lower()):
    print("Name is present")
else: 
    print("Name is not present")