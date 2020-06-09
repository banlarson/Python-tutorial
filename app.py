"""
This is an example script.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""

import os
string = "Hello World its Brian"
for x in string:
    if x == "B":
        print(x)

fruits = ["apple", "banana", "cherry"]
for y in fruits:
    print(y)

print(os.getcwd())

f = open("demofile.txt", "r")
print(f.readline())
f.close()
