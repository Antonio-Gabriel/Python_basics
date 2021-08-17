#!python3


elements = [1, 2, 2, 3, 4]

def even(x):
    return x % 2 == 0

for item in elements:
    if even(item):
        elements.remove(item)        

print(elements)