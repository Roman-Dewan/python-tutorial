name = "Roman Dewan"

print(name)  # Roman

print(f"name.startswith('R'): {name.lower().startswith('R')}")  # True
print(f"name.startswith('r'): {name.startswith('r')}")  # False
print(f"name.startswith('Ro'): {name.startswith('Ro')}")  # True

print(f"name.endswith('n'): {name.endswith('n')}")  # True
print(f"name.endswith('Ro'): {name.endswith('Ro')}")  # False

print(f"name.isalpha(): {name.isalpha()}")  # True
print(f"name.isdigit(): {name.isdigit()}")  # False
print(f"name.isalnum(): {name.isalnum()}")  # True

print(f"name.upper(): {name.upper()}")  # ROMAN
print(f"name.lower(): {name.lower()}")  # roman

print(f"name.capitalize(): {name.capitalize()}")  # Roman
print(f"name.title(): {name.title()}")  # Roman Dewan

print(f"name.count('a'): {name.count('a')}")  # 2
print(f"name.count('R'): {name.count('R')}")  # 1
print(f"name.count('r'): {name.count('r')}")  # 0

# find index
print(f"name.find('D'): {name.find('D')}")  # 6

result = name.replace("Dewan", "Smith")
print(f"name.replace('Dewan', 'Smith'): {result}")  # Roman Smith
print(f"name: {name}")  # Roman Dewan