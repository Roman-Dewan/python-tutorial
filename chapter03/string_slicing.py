name = "Roman"

# positive index string slicing
print("string slicing:")
print(f"name[0:5]: {name[0:5]}")  # Roman
print(f"name[0:3]: {name[0:3]}")  # Rom
print(f"name[2:5]: {name[2:5]}")  # man
print(f"name[:3]: {name[:3]}")  # Rom

# negative index string slicing
print(f"name[-5:-1]: {name[-5:-1]}")  # Roma
print(f"name[:-1]: {name[:-1]}")  # Roma
print(f"name[-5:3]: {name[-5:3]}")  # Rom
print(f"name[-5:]: {name[-5:]}")  # Roman
print(f"name[-1:]: {name[-1:]}")  # n

# name[start:end:step]
# string slicing with step

# start → where to begin
# end → where to stop (not included)
# step → how many positions to skip each time

print("string slicing with step:")
print(f"name[0:5:2]: {name[0:5:2]}")  # Rmn
print(f"name[0:5:1]: {name[0:5:1]}")  # Roman
print(f"name[0:5:3]: {name[0:5:3]}")  # Ra
print(f"name[0:5:4]: {name[0:5:4]}")  # Rn
print(f"name[0:5:5]: {name[0:5:5]}")  # R
print(f"name[0:5:6]: {name[0:5:6]}")  # R
print(f"name[0:3:1]: {name[0:3:1]}")  # Rom
print(f"name[0:4:2]: {name[0:4:2]}")  # Rm