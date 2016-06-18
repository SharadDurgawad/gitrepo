import sys
import os
print("Current working directory", os.getcwd())

a = int(22)
original = a
visited = set()

while 1:
    if a == 1:
        print("Number",original,"is happy!")
        break
    a = sum(int(c) ** 2 for c in str(a))
    
    if a in visited:
        print("Number",original,"is not happy")
        break
    visited.add(a)
