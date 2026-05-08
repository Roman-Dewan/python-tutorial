# first you have to install the pyjokes library using pip:
# pip install pyjokes

import pyjokes

jokes = pyjokes.get_jokes()
print("jokes[-1:4]:\n", jokes[-1:4])