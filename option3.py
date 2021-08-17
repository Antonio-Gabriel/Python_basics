#!python3

from itertools import filterfalse

elements = [1, 2, 2, 3, 4]

def even(x):
    return x % 2 == 0

elements[:] = filterfalse(even, elements)

print(elements)