import os

# Get and print the current working directory
print("Current working directory:", os.getcwd())

# List all files and directories in the current working directory
print("List of files in the current directory:", os.listdir())

# Check if 'module.py' exists and is a file in the current directory
print("Is 'module.py' a file?", os.path.isfile('module.py'))

# Get the device encoding for file descriptor 0 (standard input)
print("Get execution path", os.device_encoding(0))

directory = "/"
print("List of files in the directory:", os.listdir(directory))


