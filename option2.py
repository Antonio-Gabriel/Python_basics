#!python3


elements = [1, 2, 2, 3, 4]


def even(x):
    return x % 2 == 0


elements = [x for x in elements if not even(x)]

elements[:] = [x for x in elements if not even(x)]

print(elements)